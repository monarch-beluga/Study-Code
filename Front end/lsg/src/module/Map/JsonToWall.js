import axios from "axios";
import * as DC from '@dvgis/dc-sdk'

function JsonToWall(layer, path) {
    axios.get(path).then((res) => {
        res.data.forEach(item => {
            let wall = new DC.Wall(item.feature)
            wall.setStyle({
                material: new DC.WallTrailMaterialProperty({
                    color: DC.Color.fromCssColorString("#1449ff"),
                    speed: 10
                }),
                classificationType: 2
            })
            layer.addOverlay(wall)
        })
    })
}

export default JsonToWall
