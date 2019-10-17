<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <div v-for="course in courses">{{ course.code }}</div>>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'home',
  components: {
    HelloWorld
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
