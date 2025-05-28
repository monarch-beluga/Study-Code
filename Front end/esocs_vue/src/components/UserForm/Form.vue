<script setup>

</script>

<template>
  <el-container>
    <el-header >
      江西省化学品生产使用环境信息管理系统--线路板行业新污染物治理试点
      <div class="quit">
        <router-link to="/login">
          <el-button type="primary">退出</el-button>
        </router-link>
      </div>
    </el-header>
    <el-container>
      <el-aside width="200px">
        <el-row claa="asid">
          <el-col :span="24">
            <el-menu
                default-active="1"
                class="el-menu-vertical-demo"
            >
              <router-link to="/form/user/esocs">
                <el-menu-item index="2">
                  <span>化学品统计信息</span>
                </el-menu-item>
              </router-link>
            </el-menu>
          </el-col>
        </el-row>
      </el-aside>
      <el-main>
        <router-view></router-view>
      </el-main>
    </el-container>
  </el-container>
</template>

<style scoped>
.el-header{
  width: 100%;
  height: 56px;
  background-color: rgb(197.7, 225.9, 255);
  display: flex;
  line-height: 56px;
  font-size: 24px;
  flex: auto;
  padding-left: 8px;
}
.el-aside{
  width: 200px;
  height: calc(100vh - 56px);
  background-color: rgb(197.7, 225.9, 255);
}
.el-header .quit{
  margin-left: auto;
  align-items: center;
}
.el-main{
  display: block;
}
</style>