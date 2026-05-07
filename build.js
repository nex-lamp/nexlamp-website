#!/usr/bin/env node

/**
 * Nexlamp Static Site Builder
 * Scans /posts/*.md and generates HTML blog pages
 * ZERO external dependencies - uses built-in Markdown parser
 *
 * Usage:
 *   node build.js                # Build all posts
 *   node build.js --watch        # Watch for changes and rebuild
 *
 * Markdown front matter format:
 *   ---
 *   title: Article Title
 *   date: 2025-04-15
 *   category: 协议解析
 *   description: Short description for SEO
 *   keywords: keyword1, keyword2
 *   ---
 *   Article content in Markdown...
 */

const fs = require('fs');
const path = require('path');

// --- Configuration ---
const POSTS_DIR = path.join(__dirname, 'posts');
const OUTPUT_DIR = path.join(__dirname, 'dist', 'blog');
const TEMPLATE_FILE = path.join(__dirname, 'post.html');
const BLOG_PAGE = path.join(__dirname, 'blog.html');

// --- Simple Markdown Parser (no external deps) ---
function parseMarkdown(md) {
  let html = md.replace(/\r\n/g, '\n').replace(/\r/g, '\n');

  // Code blocks (```lang ... ```)
  html = html.replace(/```(\w*)\n([\s\S]*?)```/g, function (_, lang, code) {
    const escaped = code.replace(/</g, '&lt;').replace(/>/g, '&gt;');
    return '<pre><code class="language-' + lang + '">' + escaped.trim() + '</code></pre>';
  });

  // Inline code
  html = html.replace(/`([^`]+)`/g, '<code>$1</code>');

  // Headings
  html = html.replace(/^#### (.+)$/gm, '<h4>$1</h4>');
  html = html.replace(/^### (.+)$/gm, '<h3>$1</h3>');
  html = html.replace(/^## (.+)$/gm, '<h2>$1</h2>');
  html = html.replace(/^# (.+)$/gm, '<h1>$1</h1>');

  // Bold and italic
  html = html.replace(/\*\*\*(.+?)\*\*\*/g, '<strong><em>$1</em></strong>');
  html = html.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
  html = html.replace(/\*(.+?)\*/g, '<em>$1</em>');

  // Links
  html = html.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2">$1</a>');

  // Images
  html = html.replace(/!\[([^\]]*)\]\(([^)]+)\)/g, '<img src="$2" alt="$1" loading="lazy">');

  // Blockquotes
  html = html.replace(/^> (.+)$/gm, '<blockquote><p>$1</p></blockquote>');

  // Unordered lists
  html = html.replace(/^[\-\*] (.+)$/gm, '<li>$1</li>');
  html = html.replace(/((?:<li>.*<\/li>\n?)+)/g, '<ul>$1</ul>');

  // Ordered lists
  html = html.replace(/^\d+\. (.+)$/gm, '<li>$1</li>');

  // Horizontal rules
  html = html.replace(/^---$/gm, '<hr>');

  // Tables (improved)
  const lines = html.split('\n');
  const processedLines = [];
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    const rowMatch = line.match(/^\|(.+)\|$/);
    if (!rowMatch) {
      processedLines.push(line);
      continue;
    }
    const content = rowMatch[1];
    // Check if next line is a separator (|---|---|)
    const isHeader = (i + 1 < lines.length && lines[i + 1].match(/^\|[\s\-\|:]+\|$/));
    // Check if current line IS a separator
    if (content.match(/^[\s\-\|:]+$/)) {
      // Skip separator rows entirely
      continue;
    }
    const cells = content.split('|').map(function (c) { return c.trim(); });
    const tag = isHeader ? 'th' : 'td';
    processedLines.push('<tr>' + cells.map(function (c) { return '<' + tag + '>' + c + '</' + tag + '>'; }).join('') + '</tr>');
  }
  html = processedLines.join('\n');
  // Pass 2: wrap consecutive <tr> rows into <table>
  html = html.replace(/((?:<tr>.*<\/tr>\n?)+)/g, '<table>$1</table>');

  // Paragraphs (lines that aren't already wrapped)
  html = html.split('\n\n').map(function (block) {
    block = block.trim();
    if (!block) return '';
    if (block.match(/^<(h[1-6]|ul|ol|li|pre|blockquote|table|tr|td|th|hr|img)/)) return block;
    return '<p>' + block + '</p>';
  }).join('\n');

  // Clean up empty paragraphs
  html = html.replace(/<p>\s*<\/p>/g, '');

  return html;
}

// --- Parse Front Matter ---
function parseFrontMatter(content) {
  const meta = {
    title: '未命名文章',
    date: new Date().toISOString().split('T')[0],
    category: '技术文章',
    description: '耐利普科技技术文章',
    keywords: '智能照明,LED驱动电源',
    slug: '',
    cover: '',
    tags: '',
    excerpt: ''
  };

  const fmMatch = content.match(/^---\r?\n([\s\S]*?)\r?\n---/);
  if (fmMatch) {
    const fm = fmMatch[1];
    fm.split('\n').forEach(function (line) {
      const colonIndex = line.indexOf(':');
      if (colonIndex === -1) return;
      const key = line.substring(0, colonIndex).trim();
      const value = line.substring(colonIndex + 1).trim();
      if (key && value) {
        meta[key] = value;
      }
    });
  }

  // Extract body (remove front matter)
  const body = fmMatch ? content.slice(fmMatch[0].length).trim() : content;

  // Generate slug from title
  if (!meta.slug) {
    meta.slug = meta.title
      .toLowerCase()
      .replace(/[^\w\s\u4e00-\u9fff-]/g, '')
      .replace(/\s+/g, '-')
      .replace(/-+/g, '-')
      .substring(0, 80);
  }

  return { meta: meta, body: body };
}

// --- Build Single Post ---
function buildPost(filePath, template) {
  const raw = fs.readFileSync(filePath, 'utf-8');
  const { meta, body } = parseFrontMatter(raw);
  const htmlContent = parseMarkdown(body);

  // Format date for display
  const dateObj = new Date(meta.date);
  const dateDisplay = dateObj.getFullYear() + '\u5E74' + (dateObj.getMonth() + 1) + '\u6708' + dateObj.getDate() + '\u65E5';

  // Build related posts list (placeholder)
  const relatedHtml = '<li><a href="../../blog.html">\u6D4F\u89C8\u6240\u6709\u6587\u7AE0</a></li>';

  // Replace template placeholders
  let output = template
    .replace(/\{\{title\}\}/g, meta.title)
    .replace(/\{\{description\}\}/g, meta.description)
    .replace(/\{\{keywords\}\}/g, meta.keywords)
    .replace(/\{\{slug\}\}/g, meta.slug)
    .replace(/\{\{dateISO\}\}/g, meta.date)
    .replace(/\{\{date\}\}/g, dateDisplay)
    .replace(/\{\{category\}\}/g, meta.category)
    .replace(/\{\{cover\}\}/g, meta.cover || 'images/blog-default.jpg')
    .replace(/\{\{content\}\}/g, htmlContent)
    .replace(/\{\{relatedPosts\}\}/g, relatedHtml);

  // Write output
  const outputPath = path.join(OUTPUT_DIR, meta.slug + '.html');
  fs.writeFileSync(outputPath, output, 'utf-8');
  console.log('  \u2713 Built: ' + meta.slug + '.html (' + meta.title + ')');

  return meta;
}

// --- Main Build ---
function build() {
  console.log('\n\uD83D\uDD28 Nexlamp Static Site Builder');
  console.log('================================\n');

  // Ensure output directory exists
  if (!fs.existsSync(OUTPUT_DIR)) {
    fs.mkdirSync(OUTPUT_DIR, { recursive: true });
  }

  // Read template
  if (!fs.existsSync(TEMPLATE_FILE)) {
    console.error('\u274C Template not found: ' + TEMPLATE_FILE);
    process.exit(1);
  }
  const template = fs.readFileSync(TEMPLATE_FILE, 'utf-8');

  // Scan posts directory
  if (!fs.existsSync(POSTS_DIR)) {
    console.error('\u274C Posts directory not found: ' + POSTS_DIR);
    process.exit(1);
  }

  const mdFiles = fs.readdirSync(POSTS_DIR).filter(function (f) {
    return f.endsWith('.md') && f !== 'TEMPLATE.md';
  });

  if (mdFiles.length === 0) {
    console.log('\u26A0\uFE0F  No markdown files found in /posts/');
    return;
  }

  console.log('Found ' + mdFiles.length + ' post(s) to build:\n');

  const posts = [];
  mdFiles.forEach(function (file) {
    const filePath = path.join(POSTS_DIR, file);
    const meta = buildPost(filePath, template);
    meta.fileName = file;
    posts.push(meta);
  });

  // Sort by date descending
  posts.sort(function (a, b) { return new Date(b.date) - new Date(a.date); });

  console.log('\n\u2705 Build complete! ' + posts.length + ' article(s) generated in dist/blog/\n');

  // Generate blog index data (JSON for dynamic loading)
  const indexData = posts.map(function (p) {
    return {
      title: p.title,
      slug: p.slug,
      date: p.date,
      category: p.category,
      description: p.description,
      cover: p.cover || '',
      excerpt: p.excerpt || p.description || ''
    };
  });

  fs.writeFileSync(
    path.join(OUTPUT_DIR, 'index.json'),
    JSON.stringify(indexData, null, 2),
    'utf-8'
  );
  console.log('  \u2713 Generated: index.json (blog index data)\n');

  // --- Auto-generate sitemap.xml ---
  generateSitemap(posts);
}

// --- Generate sitemap.xml ---
function generateSitemap(posts) {
  const SITE_URL = 'https://www.nexlamp.com';
  const today = new Date().toISOString().split('T')[0];

  let xml = '<?xml version="1.0" encoding="UTF-8"?>\n';
  xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n\n';

  // Static pages
  const staticPages = [
    { loc: '/', changefreq: 'weekly', priority: '1.0' },
    { loc: '/products.html', changefreq: 'monthly', priority: '0.9' },
    { loc: '/blog.html', changefreq: 'daily', priority: '0.8' },
    { loc: '/blog-archive.html', changefreq: 'weekly', priority: '0.7' }
  ];

  staticPages.forEach(function (page) {
    xml += '  <url>\n';
    xml += '    <loc>' + SITE_URL + page.loc + '</loc>\n';
    xml += '    <changefreq>' + page.changefreq + '</changefreq>\n';
    xml += '    <priority>' + page.priority + '</priority>\n';
    xml += '  </url>\n\n';
  });

  // Blog posts
  posts.forEach(function (post) {
    xml += '  <url>\n';
    xml += '    <loc>' + SITE_URL + '/dist/blog/' + post.slug + '.html</loc>\n';
    xml += '    <lastmod>' + post.date + '</lastmod>\n';
    xml += '    <changefreq>monthly</changefreq>\n';
    xml += '    <priority>0.7</priority>\n';
    xml += '  </url>\n\n';
  });

  xml += '</urlset>';

  const sitemapPath = path.join(__dirname, 'sitemap.xml');
  fs.writeFileSync(sitemapPath, xml, 'utf-8');
  console.log('  \u2713 Generated: sitemap.xml (' + (staticPages.length + posts.length) + ' URLs)\n');
}

// --- Watch Mode ---
function watch() {
  console.log('\n\uD83D\uDC40 Watching /posts/ for changes... (Ctrl+C to stop)\n');
  build();

  let debounceTimer = null;
  fs.watch(POSTS_DIR, { recursive: true }, function (eventType, filename) {
    if (filename && filename.endsWith('.md')) {
      clearTimeout(debounceTimer);
      debounceTimer = setTimeout(function () {
        console.log('\n\uD83D\uDD04 Change detected: ' + filename);
        build();
      }, 300);
    }
  });
}

// --- CLI ---
const args = process.argv.slice(2);
if (args.includes('--watch') || args.includes('-w')) {
  watch();
} else if (args.includes('--help') || args.includes('-h')) {
  console.log('\nNexlamp Static Site Builder\n');
  console.log('Usage: node build.js [options]\n');
  console.log('Options:');
  console.log('  --watch, -w    Watch for changes and rebuild');
  console.log('  --help, -h     Show this help\n');
  console.log('No external dependencies required.\n');
} else {
  build();
}
