<template>
  <div>
    <div class="course-card" v-for="course in courses" @click="goCourse(course.code)" @mousemover.native="hover = true" @mouseleave.native="hover = false">
      <div class="course-code"> {{course.code}} </div>
      <div class="course-title"> {{course.title}} </div>
      <div class="course-detailed-info"> {{course.title}} </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "TeachListPage",
  props:{
    courses:Array
  },
  methods: {
    goCourse: function (code) {
      this.$router.push({name: 'TeachDetail', params: {code: code}})
    }
  },
  data(){
    return {
      hover:false,
    };
  }
}
</script>

<style scoped>
  .teach-list-page{
    padding-left: 30px;
    padding-right: 30px;
    width: 100%;
    height: 100%;
    background-color: grey;
  }
  .course-card {
    display: inline-block;
    background:#FFFFFF;
    box-shadow: 7px 7px 10px #EEEEEE;
    float: left;
    padding: 20px;
    margin: 10px;
    max-width: 280px;
    max-height: 240px;
    min-width: 210px;
    min-height: 180px;
    width: 28%;
    height: 28%;
  }
  .course-card:hover{
    background: #DDDDDD;
  }
  .course-code{
    font-size: 14px;
    color: grey;
    text-align: left;
  }
  .course-title{
    margin-top: 5px;
    font-size: 20px;
    text-align: left;
    height: 100px;
  }
  .course-detailed-info{
    font-size: 12px;
    color: grey;
    text-align: left;
    height: 50px;
  }
</style>