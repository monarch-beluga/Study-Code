<script setup>
import {ref, onMounted} from "vue"
import * as DC from '@dvgis/dc-sdk'
import {getBusinessDetail} from "../../module/Map/Business.js";
import ContainerBox from "../../common/ContainerBox.vue";
import RightContainer from "../../common/RightContainer.vue";
import {Picture} from "@element-plus/icons-vue";

const data = ref({})

onMounted(async ()=>{
  const detail = await getBusinessDetail()
  data.value = {
    "单位所在地": detail['地址'],
    "中心经度": detail["lng"],
    "中心纬度": detail["lat"],
    "企业面积": detail.area + "（公顷）",
    "行业类别": detail["行业类别"],
    "负责人": detail["应急联络人"],
    "联系电话": detail["应急联络人电话"]
  }
})
</script>

<template>
  <RightContainer>
    <template #content>
      <ContainerBox>
        <template #title>
          企业简介
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
          </div>
        </template>
      </ContainerBox>
      <ContainerBox class="h0 flex-1">
        <template #title>
          基本信息
        </template>
        <template #content>
          <div class="data-content">
            <div class="company-info">
              <div class="company-info-item"
                   v-for="(item,index) in data"
              >
                <el-row style="box-sizing: border-box;display: flex;flex-wrap: wrap;position: relative;">
                  <el-col :span="20" style="flex: 0 0 25%;max-width: 40%;">
                    <div class="company-info-title">{{index}}</div>
                  </el-col>
                  <el-col :span="18">
                    <div class="company-info-content">{{item}}</div>
                  </el-col>
                </el-row>
              </div>
            </div>
          </div>
        </template>
      </ContainerBox>
    </template>
  </RightContainer>
</template>

<style scoped>
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

.company-info-title, .company-info-content{
  margin: 4px 0;
}
.data-content {
  padding: 10px;
  color: #fff;
}
.company-info{
  margin-top: 10px;
}
</style>