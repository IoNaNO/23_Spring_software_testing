<template>
  <div class="single-case">
    <el-form
      class="single-form"
      :label-position="labelPosition"
      label-width="400px"
      :model="formLabelAlign"
    >
      <el-form-item label="本月的通话分钟数X（分钟）">
        <el-input v-model="formLabelAlign.X"></el-input>
      </el-form-item>
      <el-form-item label="本年度至本月的累计未按时缴费的次数Y（次）">
        <el-input v-model="formLabelAlign.Y"></el-input>
      </el-form-item>
      <el-form-item label="月份">
        <el-date-picker v-model="date" type="month" placeholder="选择月"
        value-format="yyyy-MM" >
        </el-date-picker>
      </el-form-item>
      <el-form-item label="每月的电话总费用预期输出">
        <el-input v-model="formLabelAlign.expectation"></el-input>
      </el-form-item>
    </el-form>
          <el-button
        class="main-button"
        type="success"
        plain
        @click="doTest"
        :loading="loading"
        >进行测试<i class="el-icon-upload el-icon--right"></i
      ></el-button>
        <div>
    <span>实际输出：{{actual}}</span>
    <el-divider direction="vertical"></el-divider>
    <span>运行信息：{{info}}</span>
    <el-divider direction="vertical"></el-divider>
  </div>
  </div>
</template>

<script>
import { testcash } from "@/api/cashtest.js";
export default {
  name: "SingleCase",
  components: {},
  props: {},
  data() {
    return {
      actual:"",
      info:"",
      labelPosition: 'right',
        formLabelAlign: {
          X: 0,
          Y: 0,
          expectation: 0
        }, 
        date:"",
        loading:false,

    };
  },
  computed: {},
  watch: {},
  created() {},
  mounted() {},
  methods: {
    doTest(){
      let formdata = {
        id:"TS1",
        year:this.date.split("-")[0],
        month:this.date.split("-")[1],
        X:this.formLabelAlign.X,
        Y:this.formLabelAlign.Y,
        expectation:this.formLabelAlign.expectation,
      }
      let data = {
        cash_test_list:[formdata],
      }
      testcash(data).then((res)=>{
        this.actual = res.data.test_result[0].actual;
        this.info = res.data.test_result[0].info;

      }).catch((err)=>{
        this.$message.err("Server Error");
      })

    }
  },
};
</script>

<style scoped>
.main-button {
  width:100%;
}
.single-form{
  width:600px;
  top:50%;
  left:50%;
}
</style>
