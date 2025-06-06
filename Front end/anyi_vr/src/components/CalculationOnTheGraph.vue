<script setup>
import * as DC from '@dvgis/dc-sdk'
import MapLayersChangeBox from "../common/MapLayersChangeBox.vue";
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";
import {faCalculator} from "@fortawesome/free-solid-svg-icons";

const measure = new DC.Measure($viewer)
const calcTools = [
  "空间距离",
  "贴地距离",
  "水平面积",
  "贴地面积",
  "角度",
  "高度差",
  "三角测量",
  "贴物高度",
]

function measureTool(name){
  switch (name){
    case "空间距离":
      measure.distance()
      break
    case "贴地距离":
      measure.distanceSurface()
      break
    case "水平面积":
      measure.area()
      break
    case "贴地面积":
      measure.areaSurface();
      break
    case "角度":
      measure.angle();
      break
    case "高度差":
      measure.angle({
        clampToModel:true
      });
      break
    case "三角测量":
      measure.triangleHeight();
      break
    case "贴物高度":
      measure.height({
        clampToModel:true
      });
      break
    default:
      measure.deactivate();
      break
  }
}

</script>

<template>
  <MapLayersChangeBox>
    <template #title>
      <div class="name"><span><font-awesome-icon :icon="faCalculator"/>测量工具</span></div>
    </template>
    <template #content>
      <div class="container-box">
        <div
            v-for="name in calcTools"
            @click="measureTool(name)"
            class="item">
          <img class="icon_img" src="/calcTool.png" alt srcset/>
          <div class="text">{{name}}</div>
        </div>
      </div>
      <div class="button-clear">
        <el-button style="border: none;" @click="measureTool()" >清空测量数据</el-button>
      </div>
    </template>
  </MapLayersChangeBox>
</template>

<style scoped>
.container-box {
  width: 230px;
  display: flex;
  flex-wrap: wrap;
  font-size: 12px;
}
.icon_img {
  width: 40px;
  height: 40px;
}
.item:hover{
  background-color: #2a8ef1;
  border-radius: 20%;
}
.item {
  width: 60px;
  margin: 8px;
  text-align: center;
  padding: 3px;
  cursor: pointer;
}
.button-clear {
  display: flex;
  justify-content: center;
  margin: 10px 0;
}
.el-button:hover{
  background-color: #2a8ef1;
  color: #fff;
}
:deep(.svg-inline--fa){
  margin-right: 5px;
}
</style>