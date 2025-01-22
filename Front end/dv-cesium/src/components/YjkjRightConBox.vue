<script setup>
import {inject, provide, ref} from "vue";
import axios from "axios";
import SearchBar from "./SearchBar.vue";

const staticData = inject("staticData");
let tableData = []

let key = ref(true)
let curr = ref(6)

function getYjkjData(type){
  let param = staticData.htmlLayerParam[type]
  let url = staticData.api + param.jsonPath + `?type=${param.type}`
  axios.get(url).then((response) => {
    tableData = []
    let data = response.data
    let id = 0;
    data.forEach(record => {
      if (record.type === param.type) {
        id += 1
        let position = [record.lng, record.lat, 1000, 360, -90, 0]
        tableData.push({
          "id": id,
          "position": position,
          "facilityImg": record.facilityImg,
          "firmName": record.firmName,
          "name": record.name,
          "mainFuncName": record.mainFuncName,
        })
      }
    })
    key.value = !key.value
    curr.value = type
  })
}
defineExpose({getYjkjData})
const viewFlyToPoint = inject("viewFlyToPoint");

function getYjkjDataByName(name){
  let param = staticData.htmlLayerParam[curr.value]
  let url = staticData.api + param.jsonPath + `?type=${param.type}&name=${name}`
  axios.get(url).then((response) => {
    tableData = []
    let data = response.data
    let id = 0;
    data.forEach(record => {
      if (record.type === param.type && record.name.search(name) !== -1) {
        id += 1
        let position = [record.lng, record.lat, 1000, 360, -90, 0]
        tableData.push({
          "id": id,
          "position": position,
          "firmName": record.firmName,
          "name": record.name,
          "mainFuncName": record.mainFuncName,
        })
      }
    })
    key.value = !key.value
  })
}
provide("getYjkjDataByName", getYjkjDataByName)

function getCurrData(){
  getYjkjData(curr.value)
}
provide("getCurrData", getCurrData)

getYjkjData(curr.value)

</script>

<template>
<div class="w100 h0 flex-1 flex f-d-c">
  <SearchBar></SearchBar>
  <div class="h0 flex-1 table-content">
    <el-table
        :data="tableData"
        border
        :key="key"
        @row-click="viewFlyToPoint"
        show-overflow-tooltip
        style="width: 100%;height: calc(100vh - 210px)">
      <el-table-column prop="id" label="ID" width="42"/>
      <el-table-column prop="firmName" label="企业名称" width="155"/>
      <el-table-column prop="name" label="名称" width="155"/>
      <el-table-column prop="mainFuncName" label="作用" width="55"/>
    </el-table>
  </div>
</div>
</template>

<style scoped>


</style>