<script setup>

import QymlBox from "./QymlBox.vue";

const yqjj_data = [
  {
    title: "2.83",
    text: "(平方公里)",
    content: "园区规划面积",
    img: "./img/yqmj.png"
  },
  {
    title: "21",
    text: "(人)",
    content: "救援人员数量",
    img: "./img/jyrs.png"
  },
  {
    title: "118",
    text: "",
    content: "应急空间数量",
    img: "./img/yjkj.png"
  },
  {
    title: "15",
    text: "",
    content: "企业数量",
    img: "./img/qysl.png"
  }
]

</script>

<template>
  <div class="right-container">
    <div class="box">
      <div class="title-box">
        <div class="title">园区简介</div>
      </div>
      <div class="content-box">
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
                v-for="item in yqjj_data"
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


      </div>
    </div>
    <div class="h0 flex-1 box">
      <div class="title-box">
        <div class="title">企业名录</div>
      </div>
      <div class="content-box">
        <QymlBox></QymlBox>
      </div>
    </div>
  </div>
</template>

<style scoped>
.h0 {
  height: 0;
}
.flex-1{
  flex:1
}
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
.right-container>div .title-box {
  position: relative;
  height: 38px;
  line-height: 38px;
  background: url("/images/title-box.png") no-repeat center / 100% 100%;
}
.page-container .left-container>div .title-box .title, .page-container .right-container>div .title-box .title {
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