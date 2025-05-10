<script setup>
import {inject, provide, ref} from "vue";
import axios from "axios";
import RsSearchBar from "./RsSearchBar.vue";

const staticData = inject("staticData");
let tableData = []
let key = ref(true)

function getRsData(){
  let param = staticData.htmlLayerParam[15]
  let url = staticData.api + param.jsonPath
  axios.get(url).then((response) => {
    tableData = []
    let data = response.data
    let id = 0;
    data.forEach(record => {
      id += 1
      let position = [record.lon, record.lat, 1000, 360, -90, 0]
      tableData.push({
        "id": id,
        "position": position,
        "riskSourcesName": record.riskSourcesName,
        "name": record.name,
        "riskLevel": record.riskLevel,
      })
    })
    key.value = !key.value
  })
}

function getRsDataByName(name){
  let param = staticData.htmlLayerParam[15]
  let url = staticData.api + param.jsonPath
  axios.get(url).then((response) => {
    tableData = []
    let data = response.data
    let id = 0;
    data.forEach(record => {
      if (record.riskSourcesName.search(name) !== -1) {
        id += 1
        let position = [record.lon, record.lat, 1000, 360, -90, 0]
        tableData.push({
          "id": id,
          "position": position,
          "riskSourcesName": record.riskSourcesName,
          "name": record.name,
          "riskLevel": record.riskLevel,
        })
      }
    })
    key.value = !key.value
  })
}
provide("getRsDataByName", getRsDataByName)

const viewFlyRsToPoint = inject("viewFlyRsToPoint");

getRsData()

</script>

<template>
  <div class="w100 h0 flex-1 flex f-d-c">
    <RsSearchBar></RsSearchBar>
    <div class="h0 flex-1 table-content">
      <el-table
          :data="tableData"
          border
          :key="key"
          @row-click="viewFlyRsToPoint"
          show-overflow-tooltip
          style="width: 100%;height: calc(100vh - 210px)">
        <el-table-column prop="id" label="ID" width="42"/>
        <el-table-column prop="name" label="企业名称" width="155"/>
        <el-table-column prop="riskSourcesName" label="名称" width="155"/>
        <el-table-column prop="riskLevel" label="级别" width="55"/>
      </el-table>
    </div>
  </div>
</template>

<style scoped>

</style>