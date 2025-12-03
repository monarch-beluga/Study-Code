<script setup>

</script>

<template>
 <div class="box">
   <div class="title-box">
     <div class="title">
       <slot name="title"></slot>
     </div>
   </div>
   <div class="content-box">
     <slot name="content"></slot>
   </div>
 </div>
</template>

<style scoped>
.title-box{
  position: relative;
  height: 38px;
  line-height: 38px;
  background: url("/images/title-box.png") no-repeat center / 100% 100%;
}
.title-box .title {
  margin-left: 30px;
  text-align: left;
  font-size: 18px;
  font-family: Alibaba PuHuiTi;
  font-weight: 700;
  font-style: italic;
  color: transparent;
  -webkit-background-clip: text;
  text-shadow: 0px 2px 8px rgba(5, 28, 55, .42);
  background-image: linear-gradient(180deg, #0ec5ec5c 5%, #31beff5c 20%, #fff 40%);
}
.content-box{
  display: flex;
  flex-direction: column;
  height: calc(100% - 38px)
}
</style>