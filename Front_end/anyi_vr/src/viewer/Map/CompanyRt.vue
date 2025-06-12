<script setup>

import RightContainer from "../../common/RightContainer.vue";
import ContainerBox from "../../common/ContainerBox.vue";
import {onMounted, ref} from "vue";
import {getCurrBusiness} from "../../module/Map/Business.js";
import {getRtData, getRtDataByFirmName} from "../../module/Table/RtTable.js";

const tableData = ref([])

onMounted(async ()=>{
  const data = await getRtData("企业救援队伍")
  tableData.value = getRtDataByFirmName(data, getCurrBusiness())
})
</script>

<template>
  <RightContainer>
    <template #content>
      <ContainerBox>
        <template #title>
          救援队伍
        </template>
        <template #content>
          <el-table
              :data="tableData"
              border
              show-overflow-tooltip
              style="width: 100%;height: calc(100vh - 210px);">
            <el-table-column type="index" label="ID" width="42"/>
            <el-table-column prop="firmName" label="企业名称"/>
            <el-table-column prop="responsiblePersonName" label="责任人姓名"/>
            <el-table-column prop="contactNumber" label="联系电话"/>
          </el-table>
        </template>
      </ContainerBox>
    </template>
  </RightContainer>
</template>

<style scoped>
.el-table{
  background-color: transparent;
}
</style>