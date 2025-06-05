<script setup>

import RightContainer from "../../common/RightContainer.vue";
import ContainerBox from "../../common/ContainerBox.vue";
import {onMounted, ref, onUnmounted} from "vue";
import {getSuppliesData, getSuppliesDataByFirmName} from "../../module/Table/SuppliesTable.js";
import {getCurrBusiness} from "../../module/Map/Business.js";
import {getSuppliesLayer, removeSuppliesLayer} from "../../module/Map/SuppliesLayer.js";

const tableData = ref([])

onMounted(async ()=>{
  const data = await getSuppliesData()
  tableData.value = getSuppliesDataByFirmName(data, getCurrBusiness())
  await getSuppliesLayer()
})

onUnmounted(()=>{
  removeSuppliesLayer()
})

</script>

<template>
  <RightContainer>
    <template #content>
      <ContainerBox>
        <template #title>
          应急物资
        </template>
        <template #content>
          <el-table
              :data="tableData"
              border
              show-overflow-tooltip
              style="width: 100%;height: calc(100vh - 210px);">
            <el-table-column type="index" label="ID" width="42"/>
            <el-table-column prop="materialName" label="物资名称"/>
            <el-table-column prop="materialAddress" label="物资地址"/>
            <el-table-column prop="quantity" label="数量"/>
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