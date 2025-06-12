<script setup>
import {faMap, faCubes, faTasks} from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import {ref, provide, watch} from "vue";
import BaseLayerChange from "./BaseLayerChange.vue";
import { useRoute } from 'vue-router'
import MapLayersTree from "./MapLayersTree.vue";
import ToolListBox from "./ToolListBox.vue";
import CalculationOnTheGraph from "./CalculationOnTheGraph.vue";
import CoordinatePosition from "./CoordinatePosition.vue";
const route = useRoute()


const currTool = ref("")
const mapLayerTree = ref("")
function MapLayerTreeChange(index, check){
  mapLayerTree.value.MapLayerTreeChange(index, check)
}
defineExpose({MapLayerTreeChange})

function changeBarTool(tool){
  currTool.value = tool
}
provide("changeBarTool", changeBarTool)
watch(
    () => route.path, // 监听特定属性，如 path, query, params 等
    (newPath, oldPath) => {
      changeBarTool("")
    }
)
const tools = {
  "底图": faMap,
  "图层": faCubes,
  "工具": faTasks
}

</script>

<template>
  <div class="toolBarRight">
    <el-button v-for="(icon, name) in tools"
              class="toolBarRight-btn"
              type="primary"
              @click="currTool=currTool===name?'':name"
              >
      <font-awesome-icon :icon="icon"/>
      {{name}}
    </el-button>
  </div>
  <BaseLayerChange v-show="currTool==='底图'"></BaseLayerChange>
  <MapLayersTree v-show="currTool==='图层'" ref="mapLayerTree"></MapLayersTree>
  <ToolListBox v-show="currTool==='工具'"></ToolListBox>
  <CalculationOnTheGraph v-if="currTool==='图上量算'"></CalculationOnTheGraph>
  <CoordinatePosition v-if="currTool==='坐标定位'"></CoordinatePosition>
</template>

<style scoped>
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
.toolBarRight-btn {
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
.toolBarRight .toolBarRight-btn:first-child {
  border-radius: 4px 0 0 4px;
}
.toolBarRight .toolBarRight-btn:last-child {
  border-right: none;
  border-radius: 0 4px 4px 0;
}
:deep(.svg-inline--fa){
  margin-right: 3px;
}
</style>