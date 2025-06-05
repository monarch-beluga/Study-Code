import * as DC from '@dvgis/dc-sdk'

const url = "https://data.mars3d.cn/terrain"

function setTer(checked){
    if (checked){
        let ter =  DC.TerrainFactory.createUrlTerrain({
            url: url
        })
        $viewer.setTerrain(ter)
    }
    else{
        $viewer.setTerrain(null)
    }

}

export default setTer
