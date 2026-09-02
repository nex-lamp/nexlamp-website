const https = require('https');
const fs = require('fs');

const API_KEY = 'cKj98BLMNRcfsJSGGZXN5xaU';

function readArticle(filename) {
  const content = fs.readFileSync(filename, 'utf-8');
  // Strip YAML front matter for Dev.to (avoids "Date" class conflict)
  const stripped = content.replace(/^---[\s\S]*?---\s*/m, '').trim();
  // Extract title from H1
  const m = stripped.match(/^# (.+)$/m);
  const title = m ? m[1].trim() : 'Untitled';
  return { title, body: stripped };
}

async function postToDevTo() {
  const { title, body } = readArticle('d:/AI共享文件夹/nexlamp-website/posts/devto-2026-08-24-matter-over-thread-bulb-test.md');
  const payload = JSON.stringify({
    article: {
      title: title,
      body_markdown: body,
      published: true,
      canonical_url: 'https://www.nexlamp.com/blog/matter-over-thread-bulb-2026-review.html',
      tags: ['matter', 'thread', 'lighting'],  // Max 4 tags
      cover_image: 'https://www.nexlamp.com/blog/images/2026-08-24-matter-over-thread-bulb-test-cover.png',
      description: 'After testing 5 Matter-over-Thread bulbs side by side for 30 days, here is what actually matters and where Thread falls short of marketing.'
    }
  });
  console.log('Title:', title);
  console.log('Body length:', body.length);

  return new Promise((resolve) => {
    const req = https.request({
      hostname: 'dev.to',
      port: 443,
      path: '/api/articles',
      method: 'POST',
      headers: {
        'api-key': API_KEY,
        'User-Agent': 'nexlamp-publisher',
        'Accept': 'application/vnd.forem.api+json',
        'Content-Type': 'application/json',
        'Content-Length': Buffer.byteLength(payload)
      }
    }, (res) => {
      let respBody = '';
      res.on('data', chunk => respBody += chunk);
      res.on('end', () => {
        console.log('Status:', res.statusCode);
        try {
          const data = JSON.parse(respBody);
          if (res.statusCode === 201) {
            console.log('✅ Dev.to published:', data.url);
            resolve(true);
          } else {
            console.error('❌ Dev.to error:', JSON.stringify(data).substring(0, 500));
            resolve(false);
          }
        } catch (e) {
          console.error('❌ Parse error:', respBody.substring(0, 500));
          resolve(false);
        }
      });
    });
    req.on('error', e => { console.error('❌ Request error:', e.message); resolve(false); });
    req.write(payload);
    req.end();
  });
}

postToDevTo();
