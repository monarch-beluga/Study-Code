<script setup>

import {inject, onMounted, provide, ref, toRefs} from "vue";
import axios from "axios";
import PanContainer from "../PanContainer.vue";

const props = defineProps({
  info: String
})
const {info} = toRefs(props)

const staticData = inject("staticData");

let key = ref(true)
let tableData = []
const showQyYjwzLayer = inject("showQyYjwzLayer")
const yjwzPan = ref()

function getYjwzData(index) {
  let url = staticData.api + staticData.yjwzJson + `?firmName=${index}`
  axios.get(url).then((response) => {
    tableData = []
    let data = response.data
    data.forEach(record => {
      if (record.firmName === index) {
        tableData.push({
          "materialName": record.materialName,
          "materialAddress": record.materialAddress,
          "quantity": record.quantity,
        })
      }
    })
    key.value = !key.value
  })
}

onMounted(()=>{
  getYjwzData(info.value)
  showQyYjwzLayer(info.value, yjwzPan.value)
})


</script>

<template>
  <div class="right-container">
    <div class="data box h0 flex-1">
      <div class="title-box">
        <div class="title">应急物资</div>
      </div>
      <div class="context-box">
        <div class="w100 h0 flex-1 flex f-d-c">
          <div class="h0 flex-1 table-content">
            <el-table
                :data="tableData"
                border
                :key="key"
                show-overflow-tooltip
                style="width: 100%;height: calc(100vh - 210px)">
              <el-table-column prop="materialName" label="物资名称"/>
              <el-table-column prop="materialAddress" label="物资地址"/>
              <el-table-column prop="quantity" label="数量"/>
            </el-table>
          </div>
          <PanContainer ref="yjwzPan"></PanContainer>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.right-container {
  right: 0;
}
.right-container {
  display: flex;
  flex-direction: column;
  position: absolute;
  top: 0;
  width: 408px;
  height: 100%;
  pointer-events: auto;
  background: #1c73c333;
}
.page-container .right-container>div {
  display: flex;
  flex-direction: column;
}
.right-container>div .title-box {
  position: relative;
  height: 38px;
  line-height: 38px;
  background: url("/images/title-box.png") no-repeat center / 100% 100%;
}
.title-box .title {
  margin-left: 30px;
  text-align: left;
  font-size: 18px;
  font-family: Alibaba PuHuiTi;
  font-weight: 700;
  font-style: italic;
  color: transparent;
  text-shadow: 0px 2px 8px rgba(5, 28, 55, .42);
  background-image: linear-gradient(180deg, #0ec5ec5c 5%, #31beff5c 20%, #fff 40%);
  -webkit-background-clip: text;
}
</style>