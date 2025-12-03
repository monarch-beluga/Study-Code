import * as DC from '@dvgis/dc-sdk'

const path = "./api/3dtiles/tileset.json"
const layerName = "TileLayer"

function getTilesetLayer() {
    let tile3dLayer = new DC.TilesetLayer(layerName, {'cacheBytes': 5368709120*2, 'maximumCacheOverflowBytes': 536870912*2})
    $viewer.addLayer(tile3dLayer)
    new DC.Tileset(path, {maximumMemoryUsage: 10000}).addTo(tile3dLayer)
}

function showTilesetLayer(checked) {
    let tile3dLayer = $viewer.getLayer(layerName)
    tile3dLayer.show = checked
}

export {getTilesetLayer, showTilesetLayer}
