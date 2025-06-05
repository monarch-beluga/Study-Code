<script setup>
import * as DC from '@dvgis/dc-sdk'
import {Refresh, Search} from "@element-plus/icons-vue";
import RightContainer from "../common/RightContainer.vue";
import ContainerBox from "../common/ContainerBox.vue";
import SearchBar from "../common/SearchBar.vue";
import {ref, onMounted, inject, provide} from "vue";
import {getSpaceData, getSpaceDataByType} from "../module/Map/SpaceLayer.js";
import {getDivPopupHtml, getRsDivPopupHtml} from "../module/Map/IconHtml.js";

const input = ref("")
const dataInit = ref()
const data = ref()
const currIndex = ref(6)

function initData(type){
  currIndex.value = type
  data.value = getSpaceDataByType(dataInit.value, currIndex.value)
}
defineExpose({initData})

function searchFun(){
  if(input.value === ""){
    data.value =  getSpaceDataByType(dataInit.value, currIndex.value)
  }else{
    data.value = data.value.filter(item => item.name.search(input.value) !== -1)
  }
}

function refreshFun(){
  input.value = ""
  data.value = getSpaceDataByType(dataInit.value, currIndex.value)
}

function viewFlyPoint(e){
  let flyP = DC.Position.fromArray([e.lng, e.lat, 1000, 360, -90, 0])
  let position = new DC.Position(e.lng, e.lat)
  let popupLayer = new DC.HtmlLayer("popup").addTo($viewer)
  let popupDivHtml = getDivPopupHtml(e.firmName, e.mainFuncName, "./api/"+e.facilityImg, e.capacity)
  let popupDivIcon = new DC.DivIcon(position, popupDivHtml)
  popupDivIcon.on(DC.MouseEventType.CLICK, e=>{
    popupLayer.remove()
  })
  popupDivIcon.addTo(popupLayer)
  $viewer.flyToPosition(flyP)
}

onMounted(async ()=>{
  dataInit.value = await getSpaceData()
  initData(6)
})


</script>

<template>
  <RightContainer>
    <template #content>
      <ContainerBox class="h0 flex-1">
        <template #title>
          应急空间信息
        </template>
        <template #content>
          <SearchBar>
            <template #input>
              <el-input v-model="input" style="flex: 1 1 0" placeholder="请输入名称"></el-input>
            </template>
            <template #btn>
              <el-button
                  type="primary"
                  :icon="Search"
                  @click="searchFun"
                  class="search-btn">查询</el-button>
              <el-button
                  :icon="Refresh"
                  @click="refreshFun"
                  class="reset-btn">重置</el-button>
            </template>
          </SearchBar>
          <el-table
              :data="data"
              @row-click="viewFlyPoint"
              border
              show-overflow-tooltip
              style="width: 100%;height: calc(100vh - 210px)">
            <el-table-column type="index" label="ID" width="42"/>
            <el-table-column prop="firmName" label="所属单位" width="155"/>
            <el-table-column prop="name" label="名称" width="155"/>
            <el-table-column prop="mainFuncName" label="作用" width="55"/>
          </el-table>
        </template>
      </ContainerBox>
    </template>
  </RightContainer>
</template>

<style scoped>
.h0 {
  height: 0;
}
.flex-1{
  flex:1
}
:deep(.el-input .el-input__wrapper) {
  background: #879ec733;
  box-shadow: inset 0 3px 7px #2a8aecf2;
  border-radius: 4px;
  border: 1px solid #4081CB;
}
:deep(.el-input input) {
  color: #d4e8f8;
}
el-button{
  margin-left: 12px;
  padding: 8px 15px;
}
.search-btn{
  background: #277dff;
  border-color: #277dff;
}
.reset-btn{
  color: #d4e8f8;
  background: #43779b;
  border-color: #43779b;
}
.el-table{
  background-color: transparent;
}
</style>