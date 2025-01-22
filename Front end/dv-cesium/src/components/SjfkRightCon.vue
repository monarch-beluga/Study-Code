<script setup>

import {ref} from "vue";

let curr = ref("1")
let contents = {
  "1": {
    "img_src": "one-SJFK.png",
    "text": [
        " 第一级应急防控体系，即事故废水不出企业，事故发生时，首先启动一级防控。关闭所有可能外溢事故污水的外排口，利用企业自身的围堰、应急池等环境应急防控设施，将污水控制在企业厂区内部。园区内所有企业均设置相应的事故应急池，企业雨水（清下水）排口设有监管部门控制的阀门。一旦发生物料泄漏及火灾等安全生产事故，相关企业快速断开雨水排口，联动打开事故应急池，将事故废水和消防尾水导入事故应急池。事故结束后，应急事故池中的废水进入厂区自身污水处理站处理，无污水处理站的企业按照监测结果进入园区污水处理厂处理。 "
    ]
  },
  "2": {
    "img_src": "two-SJFK.png",
    "text": [
        " 一级防控能力不足时，启动二级防控。通过专用管道或临时转输措施，与相邻企业应急池、园区公共应急池等互联互通，拦截处置事故污水。第二级应急防控体系，即事故废水不出园区，事故废水储存在园区公共应急池及园区内雨水管网公共空间内。 ",
        " （1）公共应急池的选址。建设园区公共应急池或利用园区内干枯河道、低洼地带等进行改造，并设置独立管网进行事故废水的收集和输送，保证每家企业内部应急池与公共应急池有效连通；在事故废水超过设计标准的情况下，也可有效利用雨水管网分段建设闸门井进行废水容纳。一旦园区内企业发生事故，且消防尾水过量超出企业自身防控能力时，开启园区公共应急池阀门，企业内部无法收纳的消防事故水将通过应急管网流入公共应急池，将事故废水控制在园区应急池内，不进入区内河道。事故结束后，对公共应急池内收纳的事故废水进行监测，若达标，则就近排入河道；若不达标，则分批次用槽车送入园区污水处理厂处理。 ",
        " （2）公共应急池容量设计。根据《化工园区事故应急设施（池）建设标准》（T/CPCIF 0049—2020）进行公共应急池设置，以化工集中区产生事故废水外排量最大的一个企业计算。 ",
    ]
  },
  "3": {
    "img_src": "three-SJFK.png",
    "text": [
        " 事态进一步扩大，污水进入园区内水体，启动三级防控。利用化工集中区内的坑塘、河道、沟渠以及周边水系等，构建环境应急防控空间，对进出园区的水体实施封闭或分段管控。结合化工集中区区实际，确定事故废水通过雨污管网在进入赣江前有效拦截，当发生重大企业突发环境事故或危化品运输车辆侧翻等事故时，事故废水流入化工集中区内水体，立即关闭应急闸坝，污染河道使用移动闸截断污染团（带）；同时根据污染团（带）所在位置，就近闸断园区内部河道形成临时应急池，防止污染团从园区内水系进一步扩散至外环境。事故结束后，对临时应急空间内水质进行监测，若达标，则开启河道应急闸坝；若不达标，则将临时应急空间内污水由水泵将河水分批次送入公共应急池，进一步送园区污水处理厂处理。 "
    ]
  }
}

function changeData(level){
  curr.value = level
}
defineExpose({changeData})

</script>

<template>
  <div class="right-container">
    <div class="fire-source box">
      <div class="title-box">
        <div class="title"></div>
      </div>
      <div class="content">
        <div class="content-box">
          <template v-for="(item, index) in contents">
            <div v-if="curr === index">
              <div>
                <el-image
                    :key="curr"
                    :preview-src-list="[item.img_src]"
                    :initial-index="0"
                    :src="item.img_src">
                </el-image>
              </div>
              <div class="content_text_box">
                <div
                    v-for="(text) in item.text"
                    class="content_text">
                    {{text}}
                </div>
              </div>
            </div>
          </template>
        </div>
      </div>

    </div>
  </div>
</template>

<style scoped>
.page-container .left-container>div, .page-container .right-container>div {
  display: flex;
  flex-direction: column;
}
.right-container{
  display: flex;
  flex-direction: column;
  padding: 20px;
  position: absolute;
  top: 0;
  right: 0;
  background: #1c73c333;
  width: 440px;
  height: 100%;
  pointer-events: auto;
}
.right-container .box:first-child {
  margin-top: 0;
}
.right-container .fire-source{
  display: flex;
  flex-direction: column;
  flex: 1;
  height: 0;
}
.page-container .left-container>div .title-box, .page-container .right-container>div .title-box {
  position: relative;
  height: 38px;
  line-height: 38px;
  background: url("/images/title-box.png") no-repeat center / 100% 100%;
}
.content{
  padding: 20px 0;
  display: flex;
  flex-direction: column;
  height: calc(100% - 40px);
}
.content-box{
  color: #fff;
  height: 100%;
  flex: 1;
  display: flex;
  flex-direction: column;
}
.content-box>div{
  display: flex;
  flex-direction: column;
  height: 100%;
}
.content_text{
  text-indent: 2em;
  width: 100%;
  line-height: 25px;
  letter-spacing: 2px;
  font-size: 16px;
}
.content_text_box{
  overflow: hidden;
  overflow-y: auto;
}
</style>