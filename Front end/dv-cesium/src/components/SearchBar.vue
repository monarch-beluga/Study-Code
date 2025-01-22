<script setup>
import { Search, Refresh } from '@element-plus/icons-vue'
import {inject, ref} from "vue";

const getYjkjDataByName = inject("getYjkjDataByName");
const getCurrData = inject("getCurrData");

const input = ref('')
function searchFun() {
  getYjkjDataByName(input.value)
}

function refreshFun() {
  input.value = ""
  getCurrData()
}

</script>

<template>
  <div class="search-bar">
    <div class="search-cont" style="flex: 1 1 0;min-width: 28%;">
      <span class="search-cont-label" style="display: none;">:</span>
      <el-input v-model="input" style="flex: 1 1 0" placeholder="请输入名称"></el-input>
    </div>
    <div class="search-cont search-cont-btn">
      <el-button
          type="primary"
          :icon="Search"
          @click="searchFun"
          class="search-btn">查询</el-button>
      <el-button :icon="Refresh" class="reset-btn" @click="refreshFun">重置</el-button>
    </div>
  </div>
</template>

<style scoped>
.search-bar {
  padding-left: 10px;
  margin-bottom: 10px;
  display: flex;
  flex-wrap: wrap;
}
.search-bar .search-cont {
  margin-right: 10px;
  margin-top: 10px;
  display: flex;
  align-items: center;
}
.search-bar .search-cont-label{
  display: flex
;
  align-items: center;
  white-space: nowrap;
  font-size: 14px;
  color: #fff;
}
.search-bar .search-cont-btn{
  margin-top: 10px;
}
.search-bar .search-cont{
  margin-right: 10px;
  margin-top: 10px;
  display: flex;
  align-items: center;
}
.search-bar .search-cont-btn .search-btn{
  background: #277dff;
  border-color: #277dff;
}
.search-bar .search-cont-btn .reset-btn{
  color: #d4e8f8;
  background: #43779b;
  border-color: #43779b;
}
.search-bar .search-cont-btn el-button{
  margin-left: 12px;
  padding: 8px 15px;
}

</style>