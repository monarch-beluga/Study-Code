
import axios from "axios";

const paths = {
    "园区救援队伍": "./api/jsonData/anyi_yqjy.json",
    "企业救援队伍": "./api/jsonData/anyi_qyjy.json",
}

async function getRtData(lab){
    const path = paths[lab]
    const res = await axios.get(path);
    return res.data
}

function getRtDataByFirmName(data, firmName){
    return data.filter(item => item.firmName === firmName)
}

export {getRtData, getRtDataByFirmName}
