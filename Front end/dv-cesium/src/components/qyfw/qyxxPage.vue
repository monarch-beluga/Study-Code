<script setup>

import {onMounted, ref, toRefs} from "vue";
import axios from "axios";

const props = defineProps({
  info: String
})
const {info} = toRefs(props)

const data = ref()
function getQyfbData(name){
  axios.get("api/jsonData/anyi_qyfb.json").then((response) => {
    for (const item of response.data) {
      if (item.name === name){
        data.value = {
          "单位所在地": item['地址'],
          "中心经度": item.lng,
          "中心纬度": item.lat,
          "企业面积": item.area + "（公顷）",
          "行业类别": item["行业类别"],
          "负责人": item["应急联络人"],
          "联系电话": item["应急联络人电话"]
        }
      }
    }
  })
}
getQyfbData(info.value)

</script>

<template>
  <div class="right-container">
    <div class="box">
      <div class="title-box">
        <div class="title">企业简介</div>
      </div>
      <div class="content-box">
        <div class="box-content-box">
          <div class="box-content">
            <div class="box-content-img">
              <el-image style="width: 100px; height: 100px;">
                <template #error>
                  <div class="image-slot">
                    <el-icon style="height: 16px;width: 16px"><Picture color="#ffffff"/></el-icon>
                  </div>
                </template>
              </el-image>
              <span></span>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="box h0 flex-1">
      <div class="title-box">
        <div class="title">基本信息</div>
      </div>
      <div class="content-box">
        <div class="data-content w100 h100">
          <div class="company-info">
            <div class="company-info-item"
                 v-for="(item,index) in data"
            >
              <el-row style="box-sizing: border-box;display: flex;flex-wrap: wrap;position: relative;">
                <el-col :span="20" style="flex: 0 0 25%;max-width: 40%;">
                  <div class="company-info-title">{{index}}</div>
                </el-col>
                <el-col :span="18">
                  <div class="company-info-content">{{data[index]}}</div>
                </el-col>
              </el-row>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.el-row {
  box-sizing: border-box;
  display: flex;
  flex-wrap: wrap;
  position: relative;
}
.company-info-title, .company-info-content{
  margin: 4px 0;
}
.h0 {
  height: 0;
}
.flex-1{
  flex:1
}
.data-content {
  padding: 10px;
  color: #fff;
}
.company-info{
  margin-top: 10px;
}
.h100 {
  height: 100%;
}
.w100 {
  width: 100%;
}
.right-container{
  display: flex;
  flex-direction: column;
  position: absolute;
  top: 0;
  right: 0;
  width: 440px;
  height: 100%;
  pointer-events: auto;
  background: #1c73c333;
}
.h100 {
  height: 100%;
}
.right-container .title-box{
  position: relative;
  height: 38px;
  line-height: 38px;
  background: url("/images/title-box.png") no-repeat center / 100% 100%;
}
.title{
  margin-left: 30px;
  text-align: left;
  font-size: 18px;
  font-family: Alibaba PuHuiTi;
  font-weight: 700;
  font-style: italic;
  color: transparent;
  text-shadow: 0px 2px 8px rgba(5, 28, 55, .42);
  background-image: linear-gradient(180deg, #0ec5ec5c 5%, #31beff5c 20%, #fff 40%);
  -webkit-background-clip: text;
}
.content-box{
  display: flex;
  flex-direction: column;
  height: calc(100% - 38px);
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
.box-content-img span {
  line-height: 25px;
  letter-spacing: 1px;
}
</style>