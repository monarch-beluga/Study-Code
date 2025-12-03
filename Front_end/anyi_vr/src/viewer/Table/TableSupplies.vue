<script setup>
import {ref, onMounted} from "vue"
import {getSuppliesData, getSuppliesDataByFirmName} from "../../module/Table/SuppliesTable.js";

const currTab = ref("安义工业园区化工集中区")
const firmNames = [
  '安义工业园区化工集中区',
  '南昌市安义生态环境局',
  '江西万华环保材料有限公司',
  '江西金德锂新能源科技有限公司',
  '江西江远材料科技有限公司',
  '江西安德力高新科技有限公司',
  '江西信达航科新材料科技有限公司',
  '江西中迅农化有限公司',
  '江西亚龙美氟科技有限公司',
  '江西华晟化工有限公司',
  '江西晶安高科技股份有限公司'
]
const data = ref([])
const tableData = ref([])
const scroll = ref("")

function scrollChange(distance){
  let scrollLeft = scroll.value.wrapRef.scrollLeft += distance
  scroll.value.setScrollLeft(scrollLeft)
}

function changeData(tab){
  currTab.value = tab
  tableData.value = getSuppliesDataByFirmName(data.value, currTab.value)
}

onMounted(async ()=>{
  data.value = await getSuppliesData()
  tableData.value = getSuppliesDataByFirmName(data.value, currTab.value)
})

</script>

<template>
  <div class="content">
    <div class="content_box">
      <div class="list_box">
        <span class="content_span" @click="scrollChange(-200)">
          <img src="/images/left-button.png" alt/>
        </span>
        <el-scrollbar ref="scroll">
          <div class="scrollbar-flex-content">
            <p
                v-for="firmName in firmNames"
                @click="changeData(firmName)"
                :class="{active: currTab === firmName}"
                class="scrollbar-demo-item"
            >
              {{firmName}}
            </p>
          </div>
        </el-scrollbar>
        <span class="content_span" @click="scrollChange(200)">
          <img src="/images/right-button.png" alt/>
        </span>
      </div>
      <div class="page_box">
        <el-table
            :data="tableData"
            border
            show-overflow-tooltip
            style="width: 100%;height: calc(100vh - 320px)">
          <el-table-column type="index" label="序号" width="60"></el-table-column>/
          <el-table-column prop="materialName" label="物资名称"/>
          <el-table-column prop="materialAddress" label="物资地址"/>
          <el-table-column prop="quantity" label="数量"/>
        </el-table>
      </div>
    </div>
  </div>
</template>

<style scoped>
.content{
  padding: 20px 0;
  background: #1c73c333;
  position: absolute;
  width: 100%;
  height: 100%;
}
.page_box .el-table{
  width: 100%;
  height: 680px;
}
.content_box{
  color: #ffffff;
  pointer-events: auto;
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

.content_box .content_span img:hover{
  background-color: #BFBFBF;
  border-radius: 10px;
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
.el-table{
  background: transparent;
}
</style>