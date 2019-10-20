<template>
  <div class="module-page">
    <NavBar :showAssists="assists" :whichActive="'courses'"/>
    <SidebarMenu/>
    <div class="placeholder"><router-view :courses="courses" :assists="assists"/></div>
  </div>
</template>

<script>
import NavBar from '../components/NavBar'
import SidebarMenu from '../components/SidebarMenu'

export default {
  name: 'CoursePage',
  components: {
    SidebarMenu,
    NavBar
  },
  data () {
    return {
      msg: 'Network Error',
      courses: null,
      assists: null,
      state: false,
    }
  },
  mounted () {
    this.getCourses()
  },
  methods: {
    getCourses: function () {
      this.$axios.request({
        url: this.$url + 'courses/',
        method: 'GET'
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.state = true
          this.courses = data.data.courses
          this.assists = data.data.assists
        } else {
          this.state = false
          this.msg = data.error
        }
      })
    }
  }
}
</script>

<style scoped>
.placeholder {
  width: calc(100% - 175px);
  float:right;
}
</style>
