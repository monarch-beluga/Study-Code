
import axios from "axios";

const path = "./api/jsonData/anyi_yjwz.json"

async function getSuppliesData(){
    const res = await axios.get(path);
    return res.data
}

function getSuppliesDataByFirmName(data, firmName){
    return data.filter(item => item.firmName === firmName)
}

export {getSuppliesData, getSuppliesDataByFirmName}
