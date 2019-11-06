<template>
  <div class="sidebar-menu">
    <div class="nav-code">{{course.code}}</div>
    <div class="nav-title">{{course.title}}</div>
    <div class="nav-info">{{course.info}}</div>
    <div class="nav-row">Role: <b>Student</b></div>
    <div class="p-menu p-component">
      <ul class="p-menu-list p-reset">
        <li class="p-menuitem" :class="{ active: isInfoActive }" @click="goInfo()">
          <a class="p-menuitem-link">Course Info</a>
        </li>
        <li class="p-menuitem" :class="{ active: isTutActive }" @click="goTut()">
          <a class="p-menuitem-link">Tutorial</a>
        </li>
        <li class="p-menuitem" :class="{ active: isForumActive }" @click="goForum()">
          <a class="p-menuitem-link">Forum</a>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: "CourseSideBarMenu",
  data(){
    return{
      course: {},
    }
  },
  mounted(){
    this.getCourse();
  },
  computed: {
    isInfoActive: function () {
      return this.$route.name == 'CourseDetail' || this.$route.name == 'CourseDetailInfo'
    },
    isTutActive: function () {
      return this.$route.name == 'CourseDetailTut'
    },
    isForumActive: function () {
      return this.$route.name.indexOf('Forum') >= 0 || this.$route.name.indexOf('Post') >= 0
    },
  },
  methods: {
    goInfo: function () {
      if (this.$route.name != 'CourseDetailInfo') {
        this.$router.push({name: 'CourseDetailInfo', params: {code: this.$route.params.code}})
      }
    },
    goTut: function () {
      if (this.$route.name != 'CourseDetailTut') {
        this.$router.push({name: 'CourseDetailTut', params: {code: this.$route.params.code}})
      }
    },
    goForum: function () {
      if (this.$route.name != 'CourseDetailForumList') {
        this.$router.push({name: 'CourseDetailForumList', params: {code: this.$route.params.code}})
      }
    },
    getCourse: function () {
      this.$axios.request({
        url: this.$url + 'course/code/' + this.$route.params.code + '/',
        method: 'GET'
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.course = data.data.course
        } else {
          this.state = false
          this.msg = data.error
        }
      })
    },
  }
}
</script>

<style scoped>
.sidebar-menu {
  display: inline-block;
  float: left;
}
.active {
  background-color: #dedede;
}
.nav-code{
  color: #1976d2;
  max-width: 150px;
  margin-bottom: 15px;
  font-weight: bold;
  font-size: 17px;
  margin-left: 12.5px;
}
.nav-title{
  max-width: 150px;
  font-weight: Bold ;
  font-size: 20px;
  margin-bottom: 15px;
  margin-left: 12.5px;
}
.nav-info{
  max-width: 150px;
  margin-bottom: 15px;
  margin-left: 12.5px;
}
.nav-row {
  font-size: 16px;
  max-width: 150px;
  margin-bottom: 15px;
  margin-left: 12.5px;
  color: #5e5e5e;
}
</style>