<template>
  <el-header class="header">
    <div class="title-bar">
        <i class="el-icon-s-fold" @click="changeCollapse"></i>
        <h1 class="title">2023"一排一座"软件测试平台</h1>
    </div>

    <el-dropdown>
      <div class="avatar-bar">
      
      </div>
      <el-dropdown-menu slot="dropdown">
       
      </el-dropdown-menu>
    </el-dropdown>
  </el-header>
</template>


<script>
export default {
  name: "HeadBar",
  components: {},
  props: {},
  data() {
    return {};
  },
  computed: {},
  watch: {},
  created() {},
  mounted() {},
  methods: {
    changeCollapse() {
      this.$emit("changeCollapse", 0);
    },
    onLogout() {
      this.$confirm("是否确认退出？", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      })
        .then(() => {
          window.localStorage.removeItem("user");
          this.$router.push("/login");
          this.$message({
            type: "success",
            message: "退出登录成功",
          });
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: "已取消删除",
          });
        });
    },
  },
};
</script>

<style scoped lang="less">
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #002766; // 你可以选择不同的颜色
  padding: 10px 20px; // 为头部添加一些内边距，使其看起来更宽敞
}

.avatar-bar {
  display: flex;
  justify-content: center;
  align-items: center;
  .avatar {
    margin-right: 10px;
  }
}

.title {
  color: #ffffff; // 设置标题为白色，与背景颜色形成对比
  font-size: 30px !important;
  font-weight: bold; // 增加字体粗细
  margin-left: 10px; // 增加左边距，与图标之间留出一些空间
}

</style>