<script setup>

import ContainerBox from "../common/ContainerBox.vue";
import {Picture} from "@element-plus/icons-vue"

const data = {
  image: "./images/logo.png",
  introductions: [
    "江西省、中国科学院庐山植物园由老一辈著名的植物学家胡先骕、秦仁昌、陈封怀（尊称“三老”）于1934年创建，为我国第一座科学植物园，占地面积5000余亩，分为庐山本部、鄱阳湖分园、山南分园和南昌科研中心四个园区（一园四区）。经过几代科学家和科技工作者的不懈努力，现已建成杜鹃园、松柏区、蕨苑、树木园、温室区、岩石园、猕猴桃园等17个专类园区，迁地保育植物9000余种，其中珍稀濒危植物600余种，是我国植物多样性保护的重要基地，特别是在杜鹃花属植物、松柏纲植物、蕨类植物和水生植物的引种保育方面取得了丰硕成果，形成了国内植物园中独树一帜的四大特色。",
    "庐山植物园秉承“科学内涵、美丽外貌、文化底蕴”的办园理念，与国际国内众多的植物研究机构建立了友好关系，是国际植物园保护联盟（BGCI）和中国植物园联合保护计划（ICCBG）成员之一。庐山植物园将依托名山大湖，围绕国家生物资源多样性保护与生态文明建设，聚焦亚热带山地及鄱阳湖湿地植物资源，重点开展物种保护、科学研究、资源利用和环境教育等工作，为打造美丽中国“江西样板”提供精品工程。",
    "庐山植物园现有在职职工191人，其中博士63人，硕士53人。庐山植物园正在全面推进人才队伍引进与学科建设、科研支撑平台建设、园林及基础设施建设等，已初步建成5个研究中心24个研究团队。建有江西省植物迁地保护与利用重点实验室，依托南昌大学招收并培养硕士和博士研究生。",
    "庐山植物园每年接待中外游客80余万人次。1999年以来，被授予“全国科普教育基地”、“全国青少年科技教育基地”、“全国青少年走进科学世界科技活动示范基地”、“全国野生植物科普教育基地”、“全国研学旅行基地”、江西省首家“科普教育基地”，也是庐山“世界文化景观”和“世界地质公园”的重要组成部分。"
  ]
}

</script>

<template>
 <div class="right-container">
   <ContainerBox>
     <template #title>
       植物园简介
     </template>
     <template #content>
       <div class="box-content-box">
         <div class="box-content">
           <div class="box-content-img">
             <el-image style="width: 100px; height: 100px;" :src="data.image">
               <template #error>
                 <div class="image-slot">
                   <el-icon><Picture color="#ffffff"/></el-icon>
                 </div>
               </template>
             </el-image>
             <span v-for="item in data.introductions">
               {{item}}
             </span>
           </div>
         </div>
       </div>
     </template>
   </ContainerBox>
 </div>
</template>

<style scoped>
.right-container {
  right: 0;
  display: flex;
  flex-direction: column;
  position: absolute;
  top: 0;
  width: 408px;
  height: 100%;
  pointer-events: auto;
  background: #1c73c333;
}
.box-content{
  display: flex;
  justify-content: space-between;
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
  line-height: 28px;
  scrollbar-width: none;
  overflow-x: hidden;
  overflow-y: auto;
}
.box-content-img .el-image {
  float: left;
  margin: 5px 15px 5px 5px;
}
.box-content-img span {
  line-height: 25px;
  letter-spacing: 1px;
  display: block;
  text-indent: 2em;
}
</style>