const https = require('https');
const fs = require('fs');
const path = require('path');

const files = [
  { url: 'https://cdnjs.cloudflare.com/ajax/libs/mqtt/4.3.7/mqtt.min.js', out: 'mqtt.min.js' },
  { url: 'https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js', out: 'three.min.js' },
  { url: 'https://cdn.jsdelivr.net/npm/topojson-client@3/dist/topojson-client.min.js', out: 'topojson-client.min.js' },
  { url: 'https://cdn.jsdelivr.net/npm/world-atlas@2/land-110m.json', out: 'land-110m.json' }
];

const libDir = path.join(__dirname, 'lib');

function download(url, dest) {
  return new Promise((resolve, reject) => {
    const file = fs.createWriteStream(dest);
    https.get(url, (res) => {
      if (res.statusCode >= 300 && res.statusCode < 400 && res.headers.location) {
        file.close();
        fs.unlinkSync(dest);
        return download(res.headers.location, dest).then(resolve).catch(reject);
      }
      res.pipe(file);
      file.on('finish', () => { file.close(); resolve(); });
    }).on('error', reject);
  });
}

(async () => {
  for (const f of files) {
    const dest = path.join(libDir, f.out);
    console.log('Downloading ' + f.out + '...');
    await download(f.url, dest);
    const stat = fs.statSync(dest);
    console.log('  -> ' + stat.size + ' bytes');
  }
  console.log('Done!');
})();
