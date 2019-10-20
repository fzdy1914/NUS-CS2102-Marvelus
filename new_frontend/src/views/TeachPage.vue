<template>
  <div class="module-page">
    <NavBar :whichActive="'courses'"/>
    <router-view :courses="courses"/>
  </div>
</template>

<script>
import NavBar from '../components/NavBar'

export default {
  name: 'TeachPage',
  components: {
    NavBar
  },
  data () {
    return {
      msg: 'Network Error',
      courses: null,
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

</style>
