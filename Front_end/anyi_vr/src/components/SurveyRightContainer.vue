<script setup>

import ContainerBox from "../common/ContainerBox.vue";
import {onMounted, ref} from "vue";
import {Picture} from "@element-plus/icons-vue"
import axios from "axios";
import BusinessDirectoryBox from "./BusinessDirectoryBox.vue";
import RightContainer from "../common/RightContainer.vue";

const data = ref()

onMounted(async () => {
  const res = await axios.get("./api/jsonData/anyi_yqjj.json")
  data.value = res.data
})

</script>

<template>
 <RightContainer>
   <template #content>
     <ContainerBox>
       <template #title>
         园区简介
       </template>
       <template #content>
         <div class="box-content-box">
           <div class="box-content">
             <div class="box-content-img">
               <el-image style="width: 100px; height: 100px;">
                 <template #error>
                   <div class="image-slot">
                     <el-icon><Picture color="#ffffff"/></el-icon>
                   </div>
                 </template>
               </el-image>
             </div>
           </div>
           <div class="container">
             <div
                 v-for="item in data"
                 class="box-content-sj">
               <img :src=item.img alt>
               <div class="r">
                 <div class="box-content-text-title">
                   {{item.title}}
                   <text>{{item.text}}</text>
                 </div>
                 <div class="box-content-text-content">
                   {{item.content}}
                 </div>
               </div>

             </div>
           </div>
         </div>
       </template>
     </ContainerBox>
     <ContainerBox class="h0 flex-1">
       <template #title>
         企业名录
       </template>
       <template #content>
         <BusinessDirectoryBox></BusinessDirectoryBox>
       </template>
     </ContainerBox>
   </template>
 </RightContainer>
</template>

<style scoped>
.h0 {
  height: 0;
}
.flex-1{
  flex:1
}
.box-content{
  display: flex;
  justify-content: space-between;
}
.container{
  margin-top: 10px;
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
  gap: 5px;
}
.box-content-box{
  padding: 10px;
  color: #fff;
  font-size: 15px;
}
.box-content{
  display: flex;
  justify-content: space-between;
}
.box-content-img{
  height: 280px;
  line-height: 28px;
  scrollbar-width: none;
  overflow-x: hidden;
  overflow-y: auto;
}
.box-content-sj{
  min-width: 40%;
  box-sizing: border-box;
  display: flex
;
  align-items: center;
  justify-content: space-between;
}
.box-content-sj img{
  width: 36px;
  height: 36px;
  vertical-align: middle;
}
.box-content-sj .r{
  margin-left: 1px;
  flex: 1;
  display: flex
;
  flex-direction: column;
  justify-content: space-around;
}
.box-content-sj .r .box-content-text-title{
  font-size: 16px;
  font-weight: 700;
  margin-top: 5px;
  text-align: center;
}
.box-content-sj .r .box-content-text-title text {
  margin-top: 5px;
  font-size: 10px;
  text-align: center;
}
.box-content-sj .r .box-content-text-content{
  margin-top: 5px;
  font-size: 13px;
  text-align: center;
}
</style>