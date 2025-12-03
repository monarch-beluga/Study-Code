<script setup>

</script>

<template>
  <div class="content">
    <div class="img-box">
      <el-image
          :preview-src-list="['zzt.jpg']"
          :initial-index="0"
          style="width: 100%; height: 100%"
          fit="contain"
          :src="'zzt.jpg'">
      </el-image>
    </div>
  </div>
</template>

<style scoped>
.content{
  padding: 20px 0;
  background: #1c73c333;
  position: absolute;
  width: 100%;
  height: 100%;
}
.img-box{
  width: 100%;
  height: calc(100% - 30px);
}
</style>