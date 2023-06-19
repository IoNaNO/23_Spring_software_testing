<template>
    <el-container>
      <el-header>
        <h1>系统测试报告</h1>
      </el-header>
      <el-main>
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <span>1. 导航测试结果</span>
          </div>
          <el-image
            :src="imageUrl1"
            fit="cover"></el-image>
        </el-card>
        
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <span>2. 图形测试结果</span>
          </div>
          <el-image
            :src="imageUrl2"
            fit="cover"></el-image>
        </el-card>
        
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <span>3. 基于系统功能的测试结果</span>
          </div>
          
          <h3>3.1 用户信息子系统</h3>
          <el-image
            :src="imageUrl3"
            fit="cover"></el-image>
  
          <h3>3.2 分享子系统</h3>
          <el-image
            :src="imageUrl4"
            fit="cover"></el-image>
  
          <h3>3.3 演出信息子系统</h3>
          <el-image
            :src="imageUrl5"
            fit="cover"></el-image>
  
          <h3>3.4 订单子系统</h3>
          <el-image
            :src="imageUrl6"
            fit="cover"></el-image>
  
          <h3>3.5 转卖子系统</h3>
          <el-image
            :src="imageUrl7"
            fit="cover"></el-image>
        </el-card>
        
      </el-main>
    </el-container>
  </template>
  
  <script>
  export default {
    data() {
      return {
        imageUrl1: 'https://example.com/test-image-1.png',
        imageUrl2: 'https://example.com/test-image-2.png',
        imageUrl3: 'https://example.com/test-image-3.png',
        imageUrl4: 'https://example.com/test-image-4.png',
        imageUrl5: 'https://example.com/test-image-5.png',
        imageUrl6: 'https://example.com/test-image-6.png',
        imageUrl7: 'https://example.com/test-image-7.png',
      }
    },
  }
  </script>
  
  <style scoped>
  .el-header {
    background-color: #B3C0D1;
    color: #333;
    line-height: 60px;
  }
  </style>
  