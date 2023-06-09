<template>
  <el-header class="header">
    <div>
        <i class="el-icon-s-fold" @click="changeCollapse"></i>
        <span class="title">2023陈元哲组软件测试平台</span>
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
}
.avatar-bar {
  display: flex;
  justify-content: center;
  align-items: center;
  .avatar {
    margin-right: 10px;
  }
  div .title {
    font-size: 60px !important;
}



}
</style>