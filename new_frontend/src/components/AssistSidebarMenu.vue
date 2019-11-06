<template>
  <div class="sidebar-menu">
    <div class="nav-code">{{course.code}}</div>
    <div class="nav-title">{{course.title}}</div>
    <div class="nav-info">{{course.info}}</div>
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
  name: "AssistSideBarMenu",
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
      return this.$route.name == 'AssistDetail' || this.$route.name == 'AssistDetailInfo'
    },
    isTutActive: function () {
      return this.$route.name == 'AssistDetailTut'
    },
    isForumActive: function () {
      return this.$route.name.indexOf('Forum') >= 0 || this.$route.name.indexOf('Post') >= 0
    },
  },
  methods: {
    goInfo: function () {
      if (this.$route.name != 'AssistDetailInfo') {
        this.$router.push({name: 'AssistDetailInfo', params: {code: this.$route.params.code}})
      }
    },
    goTut: function () {
      if (this.$route.name != 'AssistDetailTutList') {
        this.$router.push({name: 'AssistDetailTutList', params: {code: this.$route.params.code}})
      }
    },
    goForum: function () {
      if (this.$route.name != 'AssistDetailForumList') {
        this.$router.push({name: 'AssistDetailForumList', params: {code: this.$route.params.code}})
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
  margin-left: 7px;
}
.nav-title{
  max-width: 150px;
  font-weight: Bold ;
  font-size: 20px;
  margin-bottom: 15px;
  margin-left: 7px;
}
.nav-info{
  max-width: 150px;
  margin-bottom: 15px;
  margin-left: 7px;
}
</style>