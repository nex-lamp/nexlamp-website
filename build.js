#!/usr/bin/env node

/**
 * Nexlamp Static Site Builder
 * Scans /posts/*.md and generates HTML blog pages
 * Uses `marked` for safe Markdown parsing (XSS protection)
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
const { marked } = require('marked');

// --- Configuration ---
const POSTS_DIR = path.join(__dirname, 'posts');
const OUTPUT_DIR = path.join(__dirname, 'dist', 'blog');
const TEMPLATE_FILE = path.join(__dirname, 'post.html');
const BLOG_PAGE = path.join(__dirname, 'blog.html');

// --- Markdown Parser (using marked, with XSS protection) ---
function parseMarkdown(md) {
  let content = md.replace(/\r\n/g, '\n').replace(/\r/g, '\n');

  // Fix relative image paths: Markdown uses "images/xxx" but blog HTML is in dist/blog/,
  // so "images/" must become "../../images/" to resolve correctly
  content = content.replace(/!\[([^\]]*)\]\(images\//g, '![$1](../../images/');

  // Use marked for safe HTML generation (auto-escapes HTML in markdown)
  const html = marked.parse(content);
  return html;
}


// --- HTML escape helper (SEC #4 hardening) ---
function escapeHtml(str) {
  if (str == null) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
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
      let value = line.substring(colonIndex + 1).trim();
      // Strip surrounding quotes from scalar values
      if ((value.startsWith('"') && value.endsWith('"')) ||
          (value.startsWith("'") && value.endsWith("'"))) {
        value = value.slice(1, -1);
      }
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

  // Build cover image HTML (visible in article body)
  let coverHtml = '';
  if (meta.cover) {
    let coverSrc = meta.cover;
    if (coverSrc.startsWith('images/')) {
      coverSrc = '../../' + coverSrc;
    }
    coverHtml = '<div class="post-cover"><img src="' + escapeHtml(coverSrc) + '" alt="' + escapeHtml(meta.title) + '"></div>';
  }

  // Build related posts list (placeholder)
  const relatedHtml = '<li><a href="../../blog.html">\u6D4F\u89C8\u6240\u6709\u6587\u7AE0</a></li>';

  // Remove first h1 to avoid duplicate with template {{title}}
  let finalContent = htmlContent.replace(/<h1>.*?<\/h1>\n*/, '');

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
    .replace(/\{\{coverImage\}\}/g, coverHtml)
    .replace(/\{\{content\}\}/g, finalContent)
    .replace(/\{\{relatedPosts\}\}/g, relatedHtml);

  // Write output
  const outputPath = path.join(OUTPUT_DIR, meta.slug + '.html');
  fs.writeFileSync(outputPath, output, 'utf-8');
  console.log('  \u2713 Built: ' + meta.slug + '.html (' + meta.title + ')');

  return meta;
}

// --- Main Build ---
function build() {
  console.log('\uD83D\uDD28 Nexlamp Static Site Builder');
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
  console.log('\uD83D\uDC40 Watching /posts/ for changes... (Ctrl+C to stop)\n');
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
  console.log('Uses marked for safe Markdown parsing.\n');
} else {
  build();
}
