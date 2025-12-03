import axios from "axios";
import * as DC from '@dvgis/dc-sdk'

const path = "./api/jsonData/yqfw.json"
const layerName = "areaLayer"

function getParkScopeLayer() {
    const layer = new DC.VectorLayer(layerName).addTo($viewer)
    axios.get(path).then((res) => {
        const data = res.data
        data.forEach(item => {
            let wall = new DC.Wall(item.feature)
            wall.setStyle({
                material: new DC.WallTrailMaterialProperty({
                    color: DC.Color.fromCssColorString("#00ff3b"),
                    speed: 10
                }),
                classificationType: 2
            })
            layer.addOverlay(wall)
        })
    })
}

function showParkScopeLayer(checked){
    $viewer.getLayer(layerName).show = checked
}

export {getParkScopeLayer, showParkScopeLayer}
