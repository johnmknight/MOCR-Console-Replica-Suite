const fs = require('fs');
const path = require('path');

const htmlPath = path.join(__dirname, 'hardscifi-fdo-console.html');
const ringsPath = 'C:\\Users\\john_\\dev\\KSA-Bridge\\examples\\hard-scifi\\lib\\land-110m.json';

// Parse topojson to get rings
const topo = require('topojson-client');
const world = JSON.parse(fs.readFileSync(ringsPath, 'utf8'));
const land = topo.feature(world, world.objects.land);
const rings = [];
const geoms = land.type === 'FeatureCollection' ? land.features : [land];
geoms.forEach(feature => {
  const coords = feature.geometry.type === 'Polygon' ? [feature.geometry.coordinates] : feature.geometry.coordinates;
  coords.forEach(polygon => {
    polygon.forEach(ring => {
      rings.push(ring.map(c => [Math.round(c[0]*10)/10, Math.round(c[1]*10)/10]));
    });
  });
});

const ringsJson = JSON.stringify(rings);
console.log('Coastline data:', rings.length, 'rings,', ringsJson.length, 'chars');

let html = fs.readFileSync(htmlPath, 'utf8');

// Replace the fetch block with inline data
const oldBlock = `fetch('lib/land-110m.json')
  .then(r => r.json())
  .then(world => {
    const land = topojson.feature(world, world.objects.land);
    const geoms = land.type === 'FeatureCollection' ? land.features : [land];
    geoms.forEach(feature => {
      const coords = feature.geometry.type === 'Polygon'
        ? [feature.geometry.coordinates]
        : feature.geometry.coordinates; // MultiPolygon
      coords.forEach(polygon => {
        polygon.forEach(ring => {
          const pts = ring.map(c => latLonToVec3(c[1], c[0], EARTH_R * 1.001));
          const geo = new THREE.BufferGeometry().setFromPoints(pts);
          earthGroup.add(new THREE.Line(geo, coastlineMat));
        });
      });
    });
  })
  .catch(e => console.warn('[FDO] Could not load coastlines:', e));`;

const newBlock = `// Coastline data: Natural Earth 110m land boundaries (public domain)
// Pre-extracted as [lon, lat] coordinate rings — no fetch or topojson needed
const COASTLINE_RINGS = ${ringsJson};
COASTLINE_RINGS.forEach(ring => {
  const pts = ring.map(c => latLonToVec3(c[1], c[0], EARTH_R * 1.001));
  const geo = new THREE.BufferGeometry().setFromPoints(pts);
  earthGroup.add(new THREE.Line(geo, coastlineMat));
});`;

if (html.includes(oldBlock)) {
  html = html.replace(oldBlock, newBlock);
  // Also remove the topojson-client script tag since we no longer need it
  html = html.replace(`  <script src="lib/topojson-client.min.js"></script>\n`, '');
  fs.writeFileSync(htmlPath, html, 'utf8');
  console.log('Done! Coastlines embedded, topojson-client removed.');
} else {
  console.log('ERROR: Could not find the fetch block to replace.');
  console.log('Looking for:', oldBlock.substring(0, 80));
}
