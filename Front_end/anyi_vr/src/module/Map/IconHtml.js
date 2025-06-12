
function getDivIconPopupHtml(class_name, map_name, img_src){
    return `
        <div class='${class_name}'>
          <div class="map-name">${map_name}</div>
          <div class="map-icon">
            <img src='${img_src}'>
          </div>
        </div>
        `
}

function getDivPopupHtml(name, mainFuncName, facilityImg, capacity) {

    if (capacity !== "\\")
        return `
          <div class="public-map-popup-two">
            <div class="marsBlueGradientPnl">
              <div>所属单位：${name}</div>
              <div>作用：${mainFuncName}</div>
              <div>容量：${capacity}立方米</div>
              <img class="popup-img" src='${facilityImg}'/>
            </div>
          </div>
        `
    else
        return `
          <div class="public-map-popup-two">
            <div class="marsBlueGradientPnl">
              <div>所属单位：${name}</div>
              <div>作用：${mainFuncName}</div>
              <img class="popup-img" src='${facilityImg}'/>
            </div>
          </div>
        `
}

function getRsDivPopupHtml(materialName, riskSourcesName, riskLevel){
    return `
          <div class="public-map-popup-three">
            <div></div>
            <div class="marsBlueGradientPnl">
              <li>行业类别：${materialName}</li>
              <li>风险等级: ${riskLevel}</li>
              <li>风险物质：${riskSourcesName}</div>
            </div>
          </div>
        `
}

function getPdDivPopupHtml(content){
    return `
      <div class="dynamic-map-popup">
        <div class="content-wrap">
          <div class="content">
            <p>${content}</p>
          </div>
        </div>
        <div class="arrow"></div>
      </div>
        `
}

export {getDivIconPopupHtml, getDivPopupHtml, getRsDivPopupHtml, getPdDivPopupHtml}
