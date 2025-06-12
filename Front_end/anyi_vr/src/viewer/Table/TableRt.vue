<script setup>
import {ref, onMounted} from "vue"
import {getRtData} from "../../module/Table/RtTable.js";

const tabs = [
  "园区救援队伍",
  "企业救援队伍"
]
const currentTab = ref("园区救援队伍")
const tableData = ref([])

async function changeData(tab){
  currentTab.value = tab
  tableData.value = await getRtData(currentTab.value)
}

onMounted(async ()=>{
  tableData.value = await getRtData(currentTab.value)
})

</script>

<template>
  <div class="content">
    <div class="content_box">
      <div class="list_box">
        <el-scrollbar ref="scroll">
          <div class="scrollbar-flex-content">
            <p
                v-for="tab in tabs"
                :class="{active: currentTab === tab}"
                @click="changeData(tab)"
                class="scrollbar-demo-item"
            >
              {{tab}}
            </p>
          </div>
        </el-scrollbar>
      </div>
      <div class="page_box">
        <el-table
            :data="tableData"
            border
            show-overflow-tooltip
            style="width: 100%;height: calc(100vh - 320px)">
          <el-table-column type="index" label="序号" width="60"></el-table-column>
          <template v-if="currentTab==='园区救援队伍'">
            <el-table-column prop="rescueTeamName" label="救援队伍组名称"/>
            <el-table-column prop="rescueTeamDuties" label="救援队伍组职务"/>
            <el-table-column prop="responsiblePersonName" label="责任人姓名"/>
            <el-table-column prop="parkPositions" label="园区职务"/>
            <el-table-column prop="contactNumber" label="联系电话"/>
          </template>
          <template v-if="currentTab==='企业救援队伍'">
            <el-table-column prop="firmName" label="企业名称"/>
            <el-table-column prop="responsiblePersonName" label="责任人姓名"/>
            <el-table-column prop="contactNumber" label="联系电话"/>
            <el-table-column prop="responsiblePersonName2" label="责任人姓名"/>
            <el-table-column prop="contactNumber2" label="联系电话"/>
          </template>
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
.el-table{
  background: transparent;
}
</style>