<script setup>
import {inject, ref} from "vue";
import axios from "axios";

const staticData = inject("staticData");
const tabs = [
    "园区救援队伍",
    "企业救援队伍"
]

let key = ref(true)
const currentTab = ref("园区救援队伍")
let tableData = []

function getJydwData(index) {
  let url = staticData.api + staticData.jydwJson[index]
  axios.get(url).then((response) => {
    tableData = []
    let data = response.data
    data.forEach(record => {
      if (index === "园区救援队伍"){
        tableData.push({
          "rescueTeamName": record.rescueTeamName,
          "rescueTeamDuties": record.rescueTeamDuties,
          "responsiblePersonName": record.responsiblePersonName,
          "parkPositions": record.parkPositions,
          "contactNumber": record.contactNumber,
        })
      }
      else{
        tableData.push({
          "firmName": record.firmName,
          "responsiblePersonName": record.responsiblePersonName,
          "contactNumber": record.contactNumber,
          "responsiblePersonName2": record.responsiblePersonName2,
          "contactNumber2": record.contactNumber2,
        })
      }

    })
    key.value = !key.value
  })

}
getJydwData(currentTab.value)

</script>

<template>
  <div class="content_box">
    <div class="list_box">
      <el-scrollbar ref="scroll">
        <div class="scrollbar-flex-content">
          <p
              v-for="tab in tabs"
              :key="tab"
              :class="{active: currentTab === tab}"
              @click="currentTab=tab;getJydwData(tab)"
              class="scrollbar-demo-item"
          >
            {{tab}}
          </p>
        </div>
      </el-scrollbar>
    </div>
    <div class="page_box">
      <el-table
          v-if="currentTab==='园区救援队伍'"
          :data="tableData"
          border
          :key="key"
          show-overflow-tooltip
          style="width: 100%">
        <el-table-column prop="rescueTeamName" label="救援队伍组名称"/>
        <el-table-column prop="rescueTeamDuties" label="救援队伍组职务"/>
        <el-table-column prop="responsiblePersonName" label="责任人姓名"/>
        <el-table-column prop="parkPositions" label="园区职务"/>
        <el-table-column prop="contactNumber" label="联系电话"/>
      </el-table>
      <el-table
          v-if="currentTab==='企业救援队伍'"
          :data="tableData"
          border
          :key="key"
          show-overflow-tooltip
          style="width: 100%">
        <el-table-column prop="firmName" label="企业名称"/>
        <el-table-column prop="responsiblePersonName" label="责任人姓名"/>
        <el-table-column prop="contactNumber" label="联系电话"/>
        <el-table-column prop="responsiblePersonName2" label="责任人姓名"/>
        <el-table-column prop="contactNumber2" label="联系电话"/>
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