<script setup>

</script>

<template>
  <div class="search-bar">
    <div class="search-cont" style="flex: 1 1 0;min-width: 28%;">
      <span class="search-cont-label" style="display: none;">:</span>
      <slot name="input"></slot>
    </div>
    <div class="search-cont search-cont-btn">
      <slot name="btn"></slot>
    </div>
  </div>
</template>

<style scoped>
.search-bar {
  padding-left: 10px;
  margin-bottom: 10px;
  display: flex;
  flex-wrap: wrap;
}
.search-bar .search-cont {
  margin-right: 10px;
  margin-top: 10px;
  display: flex;
  align-items: center;
}
.search-bar .search-cont-label{
  display: flex
;
  align-items: center;
  white-space: nowrap;
  font-size: 14px;
  color: #fff;
}
.search-bar .search-cont-btn{
  margin-top: 10px;
}
.search-bar .search-cont{
  margin-right: 10px;
  margin-top: 10px;
  display: flex;
  align-items: center;
}
</style>