
<template>
  <el-menu
    class="el-menu-vertical-demo"
    @open="handleOpen"
    @close="handleClose"
    background-color="#3498db"
    text-color="#ecf0f1"
    active-text-color="#a9c0d3"
    :collapse="isCollapse"
    :default-openeds="openeds"
    router
    >
    <el-submenu index="1">
      <template slot="title">
        <i class="el-icon-location"></i>
        <span>课程练习</span>
      </template>
      <el-menu-item-group>
    
        <el-menu-item index="/cash">电信收费问题</el-menu-item>
        <el-menu-item index="/calendar">万年历问题</el-menu-item>
        <el-menu-item index="/triangle">判断三角形</el-menu-item>
        <el-menu-item index="/sales">电脑销售系统</el-menu-item>
        <el-menu-item index="/two">第2题：销售管理系统</el-menu-item>
        <el-menu-item index="/four">第4题：讨论</el-menu-item>
        <el-menu-item index="/seven">第7题：实时系统</el-menu-item>
        <el-menu-item index="/nine">第9题：ATM机</el-menu-item>
        <el-menu-item index="/ten">第10题：ERP系统</el-menu-item>
        <el-menu-item index="/eleven">第11题：实时Web系统</el-menu-item>
        <el-menu-item index="/twelve">第12题：构建程序图</el-menu-item>
        <el-menu-item index="/thirteen">第13题：销售系统</el-menu-item>
      </el-menu-item-group>
   
    </el-submenu>

    <el-submenu index="2">
      <template slot="title">
        <i class="el-icon-notebook-2"></i>
        <span>单元测试</span>
      </template>
    </el-submenu>

    <el-submenu index="3">
      <template slot="title">
        <i class="el-icon-data-line"></i>
        <span>集成测试</span>
      </template>
    </el-submenu>

    <el-submenu index="4">
      <template slot="title">
        <i class="el-icon-cpu"></i>
        <span>系统测试</span>
      </template>
    </el-submenu>
    <el-submenu index="5">
      <template slot="title">
        <i class="el-icon-cpu"></i>
        <span><router-link to="/press">性能测试</router-link></span>
      </template>
    </el-submenu>
    <el-submenu index="6">
      <template slot="title">
        <i class="el-icon-cpu"></i>
        <span><router-link to="/security">安全测试</router-link></span>
      </template>
    </el-submenu>

  </el-menu>
</template>

<script>

export default {
name: "AsideBar",
components: {},
props: ['is-collapse'],
data() {
  return {
    openeds: ['1'],
  }
},
computed: {},
watch: {},
created() {},
mounted() {},
methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    }
},
};
</script>

<style scoped lang="less">
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
  min-height: 400px;
}

</style>
