<template>
  <el-container>
    <el-header>
      系统测试报告
    </el-header>
    <el-main>
      <iframe src="./系统测试报告.pdf" width="100%" height="600"></iframe>
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
