<script setup >
import {faMap, faCubes, faTasks, faClose, faCalculator, faMapPin, faDownload} from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import BaseMapLayersChange from './BaseMapLayersChange.vue'
import MapLayersChange from './MapLayersChange.vue'
import {inject, provide, ref} from "vue";
import ToolListBox from "./ToolListBox.vue";

let currTool = ref("")

const tools = {
  "底图": faMap,
  "图层": faCubes,
  "工具": faTasks
}

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
const measureTool = inject("measureTool")

let coordLng = ref(0)
let coordLat =  ref(0)
let coordEle = ref(0)
const coordTools = {
  "经度": coordLng,
  "纬度": coordLat,
  "高度": coordEle
}
const viewFlyToPoint = inject("viewFlyToPoint")


function toolClose(){
  currTool.value = ""
}
function changeBarTool(tool){
  currTool.value = tool
}
provide("changeBarTool", changeBarTool)

const mChange = ref()
function mapTreeChange(index, check){
  mChange.value.mapTreeChange(index, check)
}
defineExpose({mapTreeChange})
</script>

<template>
  <div class="toolBarRight">
    <el-button v-for="(img, name) in tools"
               class="toolBarRight-btn"
               type="primary"
               @click="currTool=currTool===name?'':name"
    >
      <font-awesome-icon :icon="img" />{{name}}
    </el-button>
  </div>
  <div v-show="currTool==='底图'" class="map-layers-change-box">
    <div class="title">
      <div class="name"><span><font-awesome-icon :icon="faMap"/>底图</span></div>
      <div class="close cursor-p" @click="toolClose">
        <font-awesome-icon :icon="faClose" />
      </div>
    </div>
    <div class="content">
      <BaseMapLayersChange></BaseMapLayersChange>
    </div>
  </div>
  <div v-show="currTool==='图层'" class="map-layers-change-box">
    <div class="title">
      <div class="name"><span><font-awesome-icon :icon="faTasks" />图层</span></div>
      <div class="close cursor-p" @click="toolClose">
        <font-awesome-icon :icon="faClose" />
      </div>
    </div>
    <div class="content">
      <MapLayersChange ref="mChange"></MapLayersChange>
    </div>
  </div>
  <div v-if="currTool==='图上量算'" class="map-layers-change-box">
    <div class="title">
      <div class="name"><span><font-awesome-icon :icon="faCalculator"/>测量工具</span></div>
      <div class="close cursor-p" @click="toolClose">
        <font-awesome-icon :icon="faClose" />
      </div>
    </div>
    <div class="content">
      <div>
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
          <el-button @click="measureTool()" >清空测量数据</el-button>
        </div>
      </div>
    </div>
  </div>
  <div v-if="currTool==='坐标定位'" class="map-layers-change-box">
    <div class="title">
      <div class="name"><span><font-awesome-icon :icon="faMapPin"/>坐标定位</span></div>
      <div class="close cursor-p" @click="toolClose">
        <font-awesome-icon :icon="faClose" />
      </div>
    </div>
    <div class="content">
      <div class="cur-content">
        <div v-for="(item, index) in coordTools">
          <span>{{index}}:</span>
          <el-input
              v-model="coordTools[index].value"
              size="small">
          </el-input>
        </div>
      </div>
      <div class="cur-btn">
        <el-button
            type="primary"
            style="--el-button-bg-color: rgba(13,100,167,.8); --el-button-text-color: var(--el-color-white); --el-button-border-color: rgba(13,100,167,.8); --el-button-hover-bg-color: rgba(86, 147, 193, 0.86); --el-button-hover-text-color: var(--el-color-white); --el-button-hover-border-color: rgba(86, 147, 193, 0.86); --el-button-active-bg-color: rgba(14, 84, 138, 0.84); --el-button-active-border-color: rgba(14, 84, 138, 0.84);"
            @click="viewFlyToPoint(coordLng, coordLat, coordEle)"
            size="small">
          坐标定位
        </el-button>
      </div>
    </div>

  </div>
  <ToolListBox v-show="currTool==='工具'"></ToolListBox>
</template>

<style scoped>
.cur-content>div span{
  width: 54px;
}
.cur-btn{
  margin: 10px 0;
  display: flex
;
  justify-content: center;
  align-items: center;
}
.cur-content>div{
  margin-top: 10px;
  padding: 0 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
:deep(.el-input__wrapper) {
  background: #3f4854b3 !important;
  border: none !important;
  border-radius: 5px;
  box-shadow: none;
}
:deep(.el-input__wrapper input){
  color: #fff
}
.button-clear {
  display: flex;
  justify-content: center;
  margin: 10px 0;
}
.toolBarRight{
  display: flex;
  flex-wrap: nowrap;
  position: absolute;
  right: 540px;
  z-index: 99;
  top: 110px;
  border: 1px solid #4081CB;
  border-radius: 4px;
  background: #879ec74d;
  box-shadow: inset 0 3px 7px #2a8aecf2;
  pointer-events: auto;
}
.item {
  width: 60px;
  margin: 8px;
  text-align: center;
  padding: 3px;
  cursor: pointer;
}
.icon_img {
  width: 40px;
  height: 40px;
}
.item:hover{
  background-color: #2a8ef1;
  border-radius: 20%;
}
.container-box {
  width: 230px;
  display: flex;
  flex-wrap: wrap;
  font-size: 12px;
}
.svg-inline--fa{
  margin-top: 0;
  margin-right: 0.2em;
}
.el-button.toolBarRight-btn {
  list-style-type: none;
  border-right: solid 1px #2b2c2f;
  color: #edffff;
  font-weight: 400;
  text-decoration: none;
  padding: 4px 12px;
  font-size: 14px;
  border-radius:0;
  line-height: 1.6;
  margin-left: 0;
  background: transparent;
  transition: border .2s linear, color .2s linear, width .2s linear, background-color .2s linear;
}
.toolBarRight .el-button:first-child {
  border-radius: 4px 0 0 4px;
}
.toolBarRight .el-button:last-child {
  border-right: none;
  border-radius: 0 4px 4px 0;
}

.map-layers-change-box{
  position: absolute;
  right: 540px;
  z-index: 99;
  top: 152px;
  border: 1px solid #4081CB;
  border-radius: 4px;
  background: #1e243299;
  box-shadow: inset 0 3px 7px #2a8aecf2;
  pointer-events: auto;
  color: #fff;
}
.map-layers-change-box .title{
  display: flex;
  justify-content: space-between;
  padding: 0 10px;
  border-bottom: 1px solid;
  border-color: #20a0ff4d;
  height: 40px;
  line-height: 40px;
  color: #fff;
  font-size: 16px;
}

</style>