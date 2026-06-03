/**
 * Nexlamp Webhook Receiver
 * Serverless-ready function for receiving content updates
 * 
 * Supports:
 * - Express.js (traditional server)
 * - AWS Lambda (serverless)
 * - Vercel Serverless Functions
 * - Netlify Functions
 * 
 * Usage:
 *   Express: node webhook-receiver.js
 *   Serverless: Export handler function
 */

const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

// ========================================
// Configuration
// ========================================
const CONFIG = {
    // Security: Use environment variable in production
    secret: process.env.WEBHOOK_SECRET,
    
    // Content directory
    postsDir: process.env.POSTS_DIR || path.join(__dirname, 'posts'),
    
    // Allowed origins (CORS)
    allowedOrigins: process.env.ALLOWED_ORIGINS 
        ? process.env.ALLOWED_ORIGINS.split(',') 
        : ['https://www.nexlamp.com', 'http://localhost:3000'],
    
    // Rate limiting
    maxRequestsPerMinute: parseInt(process.env.RATE_LIMIT) || 10,
    
    // Company info (for logging)
    company: 'Nexlamp Technology Co., Ltd.',
    phone: '13825496855'
};

// ========================================
// Rate Limiting (in-memory store)
// ========================================
const requestLog = new Map();

function checkRateLimit(clientId) {
    const now = Date.now();
    const windowStart = now - 60000; // 1 minute window
    
    const requests = requestLog.get(clientId) || [];
    const recentRequests = requests.filter(time => time > windowStart);
    
    if (recentRequests.length >= CONFIG.maxRequestsPerMinute) {
        return false;
    }
    
    recentRequests.push(now);
    requestLog.set(clientId, recentRequests);
    return true;
}

// ========================================
// Security Helpers
// ========================================

/**
 * Validate webhook signature
 * Supports HMAC-SHA256 signature verification
 */
function verifySignature(payload, signature, secret) {
    if (!signature) return false;
    
    const expected = crypto
        .createHmac('sha256', secret)
        .update(payload, 'utf8')
        .digest('hex');
    
    // Timing-safe comparison
    try {
        return crypto.timingSafeEqual(
            Buffer.from(signature, 'hex'),
            Buffer.from(expected, 'hex')
        );
    } catch {
        return false;
    }
}

/**
 * Validate request origin
 */
function validateOrigin(origin) {
    if (!origin) return false; // 拒绝无 Origin 头的请求
    return CONFIG.allowedOrigins.includes(origin);
}

// ========================================
// Content Processing
// ========================================

/**
 * Sanitize filename to prevent directory traversal
 */
function sanitizeFilename(title) {
    return title
        .toLowerCase()
        .replace(/[^\w\s-]/g, '')
        .replace(/\s+/g, '-')
        .substring(0, 100);
}

/**
 * Generate Markdown content from payload
 */
function generateMarkdown(data) {
    const {
        title,
        body,
        excerpt,
        category = 'General',
        tags = [],
        author = 'Nexlamp Tech Team',
        date = new Date().toISOString().split('T')[0]
    } = data;
    
    // Validate required fields
    if (!title || !body) {
        throw new Error('Missing required fields: title and body are required');
    }
    
    // Build frontmatter
    const frontmatter = [
        '---',
        `title: ${title}`,
        `date: ${date}`,
        `category: ${category}`,
        `tags: [${Array.isArray(tags) ? tags.map(t => `"${t}"`).join(', ') : `"${tags}""`}]`,
        excerpt ? `excerpt: ${excerpt}` : `excerpt: ${body.substring(0, 150).replace(/\n/g, ' ')}...`,
        `author: ${author}`,
        '---',
        ''
    ].join('\n');
    
    return frontmatter + body;
}

/**
 * Save Markdown file
 */
function saveMarkdown(filename, content) {
    // Ensure directory exists
    if (!fs.existsSync(CONFIG.postsDir)) {
        fs.mkdirSync(CONFIG.postsDir, { recursive: true });
    }
    
    const filePath = path.join(CONFIG.postsDir, `${filename}.md`);
    
    // Check if file already exists
    if (fs.existsSync(filePath)) {
        // Backup existing file
        const backupPath = `${filePath}.backup-${Date.now()}`;
        fs.copyFileSync(filePath, backupPath);
    }
    
    fs.writeFileSync(filePath, content, 'utf8');
    return filePath;
}

// ========================================
// Main Handler
// ========================================

async function handleWebhook(req, res) {
    const startTime = Date.now();
    const clientId = req.headers['x-forwarded-for'] || req.connection?.remoteAddress || 'unknown';
    
    // Set CORS headers
    const origin = req.headers.origin;
    if (validateOrigin(origin)) {
        res.setHeader('Access-Control-Allow-Origin', origin || '*');
        res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
        res.setHeader('Access-Control-Allow-Headers', 'Content-Type, X-Webhook-Signature, Authorization');
    }
    
    // Handle preflight
    if (req.method === 'OPTIONS') {
        res.statusCode = 204;
        res.end();
        return;
    }
    
    // Only accept POST
    if (req.method !== 'POST') {
        res.statusCode = 405;
        res.setHeader('Content-Type', 'application/json');
        res.end(JSON.stringify({
            success: false,
            error: 'Method not allowed. Use POST.'
        }));
        return;
    }
    
    try {
        // Rate limiting
        if (!checkRateLimit(clientId)) {
            res.statusCode = 429;
            res.setHeader('Content-Type', 'application/json');
            res.setHeader('Retry-After', '60');
            res.end(JSON.stringify({
                success: false,
                error: 'Rate limit exceeded. Maximum 10 requests per minute.'
            }));
            return;
        }
        
        // Parse body
        const body = await parseBody(req);
        
        // Verify signature (if provided)
        const signature = req.headers['x-webhook-signature'];
        const payload = JSON.stringify(body);
        
        if (signature && !verifySignature(payload, signature, CONFIG.secret)) {
            res.statusCode = 403;
            res.setHeader('Content-Type', 'application/json');
            res.end(JSON.stringify({
                success: false,
                error: 'Invalid signature'
            }));
            return;
        }
        
        // 必须通过环境变量设置 WEBHOOK_SECRET
        if (!CONFIG.secret) {
            res.statusCode = 500;
            res.setHeader('Content-Type', 'application/json');
            res.end(JSON.stringify({
                success: false,
                error: 'Webhook not configured: WEBHOOK_SECRET not set'
            }));
            return;
        }
        
        // Generate and save content
        const filename = sanitizeFilename(body.title);
        const markdown = generateMarkdown(body);
        const filePath = saveMarkdown(filename, markdown);
        
        // Trigger rebuild (if build script exists)
        let rebuildTriggered = false;
        const buildScript = path.join(__dirname, 'build.js');
        if (fs.existsSync(buildScript)) {
            // In production, this should trigger CI/CD pipeline
            // For now, just log it
            rebuildTriggered = true;
        }
        
        const duration = Date.now() - startTime;
        
        // Success response
        res.statusCode = 200;
        res.setHeader('Content-Type', 'application/json');
        res.end(JSON.stringify({
            success: true,
            message: 'Content received and saved',
            data: {
                filename: `${filename}.md`,
                path: filePath,
                title: body.title,
                category: body.category || 'General',
                date: body.date || new Date().toISOString().split('T')[0]
            },
            rebuild: {
                triggered: rebuildTriggered,
                note: rebuildTriggered 
                    ? 'Build script detected. Run `node build.js` to generate HTML.'
                    : 'No build script found. Manual rebuild required.'
            },
            meta: {
                duration: `${duration}ms`,
                timestamp: new Date().toISOString()
            }
        }, null, 2));
        
        console.log(`[${new Date().toISOString()}] Webhook received: ${body.title} (${duration}ms)`);
        
    } catch (error) {
        console.error(`[${new Date().toISOString()}] Webhook error:`, error.message);
        
        res.statusCode = 500;
        res.setHeader('Content-Type', 'application/json');
        res.end(JSON.stringify({
            success: false,
            error: error.message,
            timestamp: new Date().toISOString()
        }));
    }
}

/**
 * Parse request body
 */
function parseBody(req) {
    return new Promise((resolve, reject) => {
        let data = '';
        
        req.on('data', chunk => {
            data += chunk;
            // Prevent large payloads
            if (data.length > 10 * 1024 * 1024) { // 10MB limit
                reject(new Error('Payload too large'));
            }
        });
        
        req.on('end', () => {
            try {
                const parsed = JSON.parse(data);
                resolve(parsed);
            } catch {
                reject(new Error('Invalid JSON payload'));
            }
        });
        
        req.on('error', reject);
    });
}

// ========================================
// Server Adapters
// ========================================

/**
 * Express.js adapter
 */
function createExpressApp() {
    const express = require('express');
    const app = express();
    
    app.use(express.json({ limit: '10mb' }));
    
    app.post('/webhook/new-content', (req, res) => {
        handleWebhook(req, res);
    });
    
    // Health check
    app.get('/health', (req, res) => {
        res.json({
            status: 'ok',
            service: 'Nexlamp Webhook Receiver',
            company: CONFIG.company,
            timestamp: new Date().toISOString()
        });
    });
    
    return app;
}

// ========================================
// Exports
// ========================================

// For Express.js
module.exports = { app: createExpressApp, handleWebhook };

// For AWS Lambda / Vercel / Netlify
module.exports.handler = async (event, context) => {
    // Convert Lambda event to Node.js req/res
    const req = {
        method: event.httpMethod,
        headers: event.headers,
        body: event.body,
        connection: { remoteAddress: event.requestContext?.identity?.sourceIp }
    };
    
    let responseBody = '';
    let statusCode = 200;
    const headers = {};
    
    const res = {
        statusCode: 200,
        setHeader: (key, value) => { headers[key] = value; },
        end: (body) => { responseBody = body; }
    };
    
    Object.defineProperty(res, 'statusCode', {
        get: () => statusCode,
        set: (val) => { statusCode = val; }
    });
    
    await handleWebhook(req, res);
    
    return {
        statusCode,
        headers,
        body: responseBody
    };
};

// ========================================
// CLI (Direct execution)
// ========================================

if (require.main === module) {
    const args = process.argv.slice(2);
    const port = parseInt(args.find(a => !a.startsWith('-')) || '3000');
    
    console.log(`
鈺斺晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晽
鈺?   Nexlamp Webhook Receiver            鈺?
鈺?   ${CONFIG.company}      鈺?
鈺氣晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨暆
`);
    
    try {
        const app = createExpressApp();
        app.listen(port, () => {
            console.log(`馃殌 Server running on port ${port}`);
            console.log(`馃摗 Webhook endpoint: http://localhost:${port}/webhook/new-content`);
            console.log(`馃彞 Health check: http://localhost:${port}/health`);
            console.log(`\n馃搧 Posts directory: ${CONFIG.postsDir}`);
            console.log(`馃敀 Secret: ${CONFIG.secret.substring(0, 8)}...`);
            console.log(`\nExample curl command:`);
            console.log(`curl -X POST http://localhost:${port}/webhook/new-content \\
  -H "Content-Type: application/json" \\
  -d '{
    "secret": "${CONFIG.secret}",
    "title": "New Article Title",
    "body": "Article content in Markdown...",
    "category": "Technical",
    "tags": ["LED", "Smart Lighting"]
  }'\n`);
        });
    } catch (error) {
        console.error('鉂?Failed to start server:', error.message);
        console.log('\n馃挕 Tip: Install Express first: npm install express\n');
        process.exit(1);
    }
}
