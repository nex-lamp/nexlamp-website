const https = require('https');
const fs = require('fs');
const path = require('path');

const TOKEN = process.argv[2];
const FILE_PATH = process.argv[3]; // relative to posts/ or dist/blog/
const REPO = 'nex-lamp/nexlamp-website';
const BRANCH = 'main';

async function getSha(targetPath) {
  const url = `https://api.github.com/repos/${REPO}/contents/${encodeURI(targetPath)}?ref=${BRANCH}`;
  return new Promise((resolve, reject) => {
    https.get(url, { headers: { 'Authorization': `Bearer ${TOKEN}`, 'User-Agent': 'nexlamp-publisher', 'Accept': 'application/vnd.github+json' } }, (res) => {
      let body = '';
      res.on('data', chunk => body += chunk);
      res.on('end', () => {
        try {
          const data = JSON.parse(body);
          resolve(data.sha || null);
        } catch (e) { resolve(null); }
      });
    }).on('error', reject);
  });
}

async function uploadFile(relPath) {
  // Check whether it's in posts/ or dist/blog/
  let localPath, apiPath;
  if (relPath.startsWith('dist/')) {
    localPath = path.join('d:/AI共享文件夹/nexlamp-website', relPath);
    apiPath = relPath;
  } else if (relPath.startsWith('posts/')) {
    localPath = path.join('d:/AI共享文件夹/nexlamp-website', relPath);
    apiPath = relPath;
  } else {
    console.error('Unknown path:', relPath);
    return false;
  }

  if (!fs.existsSync(localPath)) {
    console.error(`❌ File not found: ${localPath}`);
    return false;
  }
  const content = fs.readFileSync(localPath);
  const contentBase64 = content.toString('base64');

  // Try posts/ first if not dist/
  let finalApiPath = relPath;
  let sha = await getSha(finalApiPath);

  const url = `https://api.github.com/repos/${REPO}/contents/${encodeURI(finalApiPath)}`;
  const payload = JSON.stringify({
    message: `publish: ${path.basename(relPath)}`,
    content: contentBase64,
    branch: BRANCH,
    sha: sha || undefined
  });

  return new Promise((resolve) => {
    const req = https.request(url, {
      method: 'PUT',
      headers: {
        'Authorization': `Bearer ${TOKEN}`,
        'User-Agent': 'nexlamp-publisher',
        'Accept': 'application/vnd.github+json',
        'Content-Type': 'application/json',
        'Content-Length': Buffer.byteLength(payload)
      }
    }, (res) => {
      let body = '';
      res.on('data', chunk => body += chunk);
      res.on('end', () => {
        if (res.statusCode === 200 || res.statusCode === 201) {
          console.log(`✅ ${relPath}`);
          resolve(true);
        } else {
          console.error(`❌ ${relPath} (HTTP ${res.statusCode}): ${body.substring(0, 200)}`);
          resolve(false);
        }
      });
    });
    req.on('error', e => { console.error(`❌ ${relPath}: ${e.message}`); resolve(false); });
    req.write(payload);
    req.end();
  });
}

(async () => {
  const files = [
    'posts/2026-08-24-matter-over-thread-bulb-test.md',
    'posts/images/2026-08-24-thread-latency-comparison.svg',
    'posts/images/2026-08-24-thread-bulb-price-tier.svg',
    'posts/images/2026-08-24-thread-border-router-deployment.svg',
    'posts/images/2026-08-24-matter-over-thread-bulb-test-cover.png',
    'dist/blog/matter-over-thread-bulb-2026-review.html'
  ];
  for (const f of files) {
    await uploadFile(f);
  }
  console.log('\nAll uploads done.');
})();
