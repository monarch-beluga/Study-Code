<script setup>

import axios from "axios";
import {onMounted, ref} from "vue";
import ContainerBox from "../common/ContainerBox.vue";
import drawBarChart from "../module/echarts/DrawBarChart.js";
import drawPieChart from "../module/echarts/DrawPieChart.js";
import LeftContainer from "../common/LeftContainer.vue";

const chartContainer1 = ref()
async function getChart1() {
  const res = await axios.get("./api/jsonData/anyi_yqjy_StatisticData.json")
  const data = res.data
  let colors = ["#9370db", "#ff6b6b", "#66bb6a", "#42a5f5", "#ab47bc", "#ffd54f", "#ff85c0", "#9ccc65", "#ffa726", "#78909c", "#5470c6"]
  let x_data = []
  let y_data = []
  data.forEach((item, index) => {
    x_data.push(item.name)
    y_data.push({
      value: item.value,
      itemStyle: {color: colors[index]}
    })
  })
  drawBarChart(chartContainer1, x_data, y_data)
}

const chartContainer2 = ref()
async function getChart2() {
  const res = await axios.get("./api/jsonData/anyi_yjkj_StatisticData.json")
  const data = res.data
  let colors = ["#9370db", "#ff6b6b", "#66bb6a", "#42a5f5", "#ab47bc", "#ffd54f", "#ff85c0", "#9ccc65", "#ffa726", "#78909c"]
  let chartData = []
  let count = 0
  data.forEach((item, index) => {
    count += item.value
    chartData.push({
      name: item.name,
      value: item.value,
      itemStyle: {color: colors[index]}
    })
  })
  drawPieChart(chartContainer2, chartData, count)
}

const chartContainer3 = ref()
async function getChart3() {
  const res = await axios.get("./api/jsonData/anyi_rs_StatisticData.json")
  const data = res.data
  let colors = ["#ffff00", "#ffa500"]
  let chartData = []
  let count = 0
  data.forEach((item, index) => {
    count += item.value
    chartData.push({
      name: item.name,
      value: item.value,
      itemStyle: {color: colors[index]}
    })
  })
  drawPieChart(chartContainer3, chartData, count)
}

onMounted(async ()=>{
  await getChart1()
  await getChart2()
  await getChart3()
})

</script>

<template>
  <LeftContainer>
    <template #content>
      <ContainerBox class="h0 flex-1">
        <template #title>
          救援队伍统计
        </template>
        <template #content>
          <div class="w100 h100" ref="chartContainer1" style="position: relative; left: 0px; top: 0px; height: 100%">

          </div>
        </template>
      </ContainerBox>
      <ContainerBox class="h0 flex-1">
        <template #title>
          应急空间统计
        </template>
        <template #content>
          <div class="w100 h100" ref="chartContainer2" style="position: relative; left: 0px; top: 0px; height: 100%">

          </div>
        </template>
      </ContainerBox>
      <ContainerBox class="h0 flex-1">
        <template #title>
          风险源统计
        </template>
        <template #content>
          <div class="w100 h100" ref="chartContainer3" style="position: relative; left: 0px; top: 0px; height: 100%">

          </div>
        </template>
      </ContainerBox>
    </template>
  </LeftContainer>
</template>

<style scoped>
.h0{
  height: 0;
}
.flex-1{
  flex: 1;
}
</style>