import * as DC from '@dvgis/dc-sdk'

const path = "./api/3dtiles/tileset.json"
const layerName = "TileLayer"

function getTilesetLayer() {
    let tile3dLayer = new DC.TilesetLayer(layerName)
    $viewer.addLayer(tile3dLayer)
    new DC.Tileset(path).addTo(tile3dLayer)
}

function showTilesetLayer(checked) {
    let tile3dLayer = $viewer.getLayer(layerName)
    tile3dLayer.show = checked
}

export {getTilesetLayer, showTilesetLayer}
