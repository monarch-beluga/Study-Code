import axios from "axios";
import * as DC from '@dvgis/dc-sdk'

const path = "./api/jsonData/anyi_whlx.json"
const layerName = "whlx-yq"

async function getHCRLayer(){
    let layer = new DC.VectorLayer(layerName).addTo($viewer)
    const res = await axios.get(path)
    const data = res.data
    data.forEach(item => {
        let polyline = new DC.Polyline(item.feature)
        polyline.setStyle({
            width: 5,
            material: new DC.PolylineTrailMaterialProperty({
                color: DC.Color.fromCssColorString("#ff0000"),
                speed:Math.floor(4000/polyline.distance) + 1,
            }),
            clampToGround: true
        })
        layer.addOverlay(polyline)
    })
}

async function showHCRLayer(checked){
    if (checked){
        await getHCRLayer()
    }else{
        $viewer.getLayer(layerName).remove()
    }
}

export {showHCRLayer}
