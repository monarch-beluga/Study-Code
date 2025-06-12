<script setup>
import {inject, ref} from "vue";

const input = ref('')

let initData = [{'id': 1, 'name': '江西晶安高科技股份有限公司'},
  {'id': 2, 'name': '江西亚龙美氟科技有限公司'},
  {'id': 3, 'name': '江西中迅农化有限公司'},
  {'id': 4, 'name': '江西华晟化工有限公司'},
  {'id': 5, 'name': '江西安德力高新科技有限公司'},
  {'id': 6, 'name': '江西金德锂新能源科技有限公司'},
  {'id': 7, 'name': '江西信达航科新材料科技有限公司'},
  {'id': 8, 'name': '江西江远材料科技有限公司'},
  {'id': 9, 'name': '江西万华环保材料有限公司'},
  {'id': 11, 'name': '南昌广荣新材料有限公司'},
  {'id': 12, 'name': '江西省亚染科技有限公司'},
  {'id': 13, 'name': '江西众荣环保有限公司'},
  {'id': 14, 'name': '江西洪安化工有限公司'},
  {'id': 15, 'name': '江西汉江药业有限公司'},
  {'id': 16, 'name': '南方印务有限公司'}]

const qyEnter = inject("qyEnter")

let data = ref(initData)

function searchFun(){
  if (input.value !== "")
    data.value = data.value.filter(item => item.name.search(input.value) !== -1)
  else
    data.value = initData
}

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
          v-for="item in data"
          :key="item['id']"
      >
        <div>{{item['name']}}</div>
        <el-button
            type="primary"
            size="small"
            color="#1a4ed7"
            @click="qyEnter(item['name'])"
            >
          进入企业
        </el-button>
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