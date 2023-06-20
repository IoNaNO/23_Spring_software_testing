<template>
  <el-container>
    <el-header>
      <h1>系统测试报告</h1>
    </el-header>
    <el-main>
      <el-row :gutter="20">
        <el-col :span="12">
          <el-card class="box-card">
            <div slot="header" class="clearfix">
              <span>1. 导航测试结果</span>
            </div>
            <el-image
              :src="imageUrl1"
              fit="contain"
              :preview-src-list="[imageUrl1]">
            </el-image>
          </el-card>
        </el-col>
        <el-col :span="12">
          <el-card class="box-card">
            <div slot="header" class="clearfix">
              <span>2. 图形测试结果</span>
            </div>
            <el-image
              :src="imageUrl2"
              fit="contain"
              :preview-src-list="[imageUrl2]">
            </el-image>
          </el-card>
        </el-col>
      </el-row>
      
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <span>3. 基于系统功能的测试结果</span>
        </div>

        <el-row :gutter="20">
          <el-col :span="12">
            <h3>3.1 用户信息子系统</h3>
            <el-image
              :src="imageUrl3"
              fit="contain"
              :preview-src-list="[imageUrl3]">
            </el-image>
          </el-col>

          <el-col :span="12">
            <h3>3.2 分享子系统</h3>
            <el-image
              :src="imageUrl4"
              fit="contain"
              :preview-src-list="[imageUrl4]">
            </el-image>
          </el-col>

          <el-col :span="12">
            <h3>3.3 演出信息子系统</h3>
            <el-image
              :src="imageUrl5"
              fit="contain"
              :preview-src-list="[imageUrl5]">
            </el-image>
          </el-col>

          <el-col :span="12">
            <h3>3.4 订单子系统</h3>
            <el-image
              :src="imageUrl6"
              fit="contain"
              :preview-src-list="[imageUrl6]">
            </el-image>
          </el-col>

          <el-col :span="12">
            <h3>3.5 转卖子系统</h3>
            <el-image
              :src="imageUrl7"
              fit="contain"
              :preview-src-list="[imageUrl7]">
            </el-image>
          </el-col>
        </el-row>
      </el-card>
    </el-main>
  </el-container>
</template>

<script>
export default {
  data() {
    return {
      imageUrl1: 'https://pic.imgdb.cn/item/6491e0ce1ddac507ccc4f578.jpg',
      imageUrl2: 'https://pic.imgdb.cn/item/6491e1021ddac507ccc53353.jpg',
      imageUrl3: 'https://pic.imgdb.cn/item/6491e2251ddac507ccc67a26.jpg',
      imageUrl4: 'https://pic.imgdb.cn/item/6491e24d1ddac507ccc6b321.jpg',
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

.box-card .el-image {
  width: 100%;
  height: auto;
}
</style>
