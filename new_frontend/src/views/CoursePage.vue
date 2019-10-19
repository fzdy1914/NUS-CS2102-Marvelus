<template>
  <div class="module-page">
    <NavBar :showAssists="assists" :whichActive="'courses'"/>
    <div v-for="course in courses">{{ course.code }}</div>
  </div>
</template>

<script>
import NavBar from "../components/NavBar";

export default {
  name: 'CoursePage',
  components: {
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
