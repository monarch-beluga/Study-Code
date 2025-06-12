<script setup>
import {inject, ref} from "vue";
import axios from "axios";

const staticData = inject("staticData");
const firmNames = [
  "安义工业园区化工集中区",
  "南昌市安义生态环境局",
  "江西省晶磊工程新技术开发有限公司",
  "江西金德锂新能源科技有限公司",
  "江西江远材料科技有限公司",
  "江西安德力高新科技有限公司",
  "江西信达航科新材料科技有限公司",
  "江西中迅农化有限公司",
  "江西亚龙美氟科技有限公司",
  "江西华晟化工有限公司",
  "江西洪安化工有限公司",
  "江西晶安高科技股份有限公司"
]

const scroll = ref(null)

function button(i){
  let l = scroll.value.$refs.wrapRef.scrollLeft
  l += i
  scroll.value.setScrollLeft(l)
}

let key = ref(true)
const currentTab = ref("安义工业园区化工集中区")
let tableData = []

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
getYjwzData(currentTab.value)

</script>

<template>
<div class="content_box">
  <div class="list_box">
    <span class="content_span" @click="button(-50)">
      <img src="/images/left-button.png" alt/>
    </span>
    <el-scrollbar ref="scroll">
      <div class="scrollbar-flex-content">
        <p
          v-for="firmName in firmNames"
          :key="firmName"
          :class="{active: currentTab === firmName}"
          @click="currentTab=firmName;getYjwzData(firmName)"
          class="scrollbar-demo-item"
        >
          {{firmName}}
        </p>
      </div>
    </el-scrollbar>
    <span class="content_span" @click="button(50)">
      <img src="/images/right-button.png" alt/>
    </span>
  </div>
  <div class="page_box">
    <el-table
        :data="tableData"
        border
        :key="key"
        show-overflow-tooltip
        style="width: 100%;height: calc(100vh - 320px)">
      <el-table-column prop="materialName" label="物资名称"/>
      <el-table-column prop="materialAddress" label="物资地址"/>
      <el-table-column prop="quantity" label="数量"/>
    </el-table>
  </div>
</div>
</template>

<style scoped>
.page_box .el-table{
  width: 100%;
  height: 680px;
}
.content_box{
  color: #ffffff;
}
.content_box .list_box{
  display: flex;
  text-align: center;
}
.content_box .content_span{
  line-height: 70px;
  margin: 0 15px;
  cursor: pointer;
}
.content_box .content_span img{
  vertical-align: middle;
  width: 30px;
  height: 30px;
}

.scrollbar-flex-content{
  display: flex;
}
.scrollbar-demo-item{
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 50px;
  margin: 10px;
  padding: 0 5px;
  text-align: center;
  border-radius: 10px;
  box-shadow: inset 0 0 40px #409eff;
  cursor: pointer;
}
.active{
  box-shadow: inset 0 0 100px #2a8ef1;
}
</style>