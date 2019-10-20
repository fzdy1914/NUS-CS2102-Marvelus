<template>
  <div>
    <div class="course-card" v-for="course in courses" @click="goCourse(course.code)">{{ course.code }}</div>
  </div>
</template>

<script>
  export default {
    name: "CourseListPage",
    props:{
      courses:Array
    },
    methods: {
      goCourse: function (code) {
        this.$router.push({name: 'CourseDetail', params: {code: code}})
      }
    }
  }
</script>

<style scoped>
  .course-card {
    display: inline-block;
    float: left;
    padding: 20px;
    margin: 10px;
    border: #1b6d85 solid 1px;
  }
</style>