<script setup>
import {onMounted, ref} from "vue";
import {getBusinesses, changeBusiness} from "../module/Map/Business.js";

const input = ref('')

const BS_data = ref()
const data = ref()

function searchFun(){
  if (input.value !== "")
    BS_data.value = BS_data.value.filter(item => item.name.search(input.value) !== -1)
  else
    BS_data.value = data.value
}

onMounted(async () => {
  data.value = await getBusinesses()
  BS_data.value = data.value
})

</script>

<template>
  <div class="box-content w100 h100 flex f-d-c">
    <div>
      <div class="search-container">
        <el-input v-model="input" size="large" placeholder="请输入企业名称"></el-input>
        <el-button
            size="large"
            type="primary"
            @click="searchFun"
            color="#0088ff">搜索</el-button>
      </div>
    </div>
    <div class="data-content-list">
      <div
          class="data-content-item"
          v-for="(item, index) in BS_data"
          :key="index"
      >
        <div>{{item['name']}}</div>
        <router-link to="/map/sub">
          <el-button
              type="primary"
              size="small"
              color="#1a4ed7"
              @click="changeBusiness(item['name'])"
          >
            进入企业
          </el-button>
        </router-link>

      </div>

    </div>
  </div>
</template>

<style scoped>
.box-content{
  color: #fff;
  padding: 0 10px;
}
.h100{
  height: 100%;
}
.w100{
  width: 100%;
}
.f-d-c {
  flex-direction: column;
}
.flex {
  display: flex;
}
.search-container{
  margin: 10px 0;
  display: flex;
  align-items: center;
  justify-content: center;
}
:deep(.search-container .el-input .el-input__wrapper) {
  font-size: 16px;
  font-weight: 400;
  border-radius: 0;
  background: #879ec74d;
  box-shadow: inset 0 3px 7px #2a8aecf2;
}
:deep(.search-container .el-input input){
  color: #d4e8f8;
}
.search-container .el-button {
  border-radius: 0;
}

.data-content-list{
  flex: 1;
  overflow-y: auto;
  scrollbar-width: none;
}

.data-content-list .data-content-item:first-child {
  margin-top: 0;
}
.data-content-list .data-content-item{
  margin-top: 10px;
  padding: 0 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 32px;
  background: linear-gradient(#2d2dff1a, #2d5effb3);
  border-radius: 2px;
}
</style>