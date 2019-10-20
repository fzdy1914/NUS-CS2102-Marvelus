<template>
  <div>
    This is Course Info:
    <div>Code: {{ $route.params.code }}</div>
  </div>
</template>

<script>
export default {
  name: "CourseDetailInfoPage",
  data() {
    return {
      state: false,
      msg: 'Network Error',
      course: null,
      profs: null,
      TAs: null
    }
  },
  mounted() {
    this.getCourse()
    this.getProfs()
    this.getTAs()
  },
  methods: {
    getCourse: function () {
      this.$axios.request({
        url: this.$url + 'course/code/' + this.$route.params.code + '/',
        method: 'GET'
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.state = true
          this.course = data.data.course
        } else {
          this.state = false
          this.msg = data.error
        }
      })
    },
    getProfs: function () {
      this.$axios.request({
        url: this.$url + 'profs/code/' + this.$route.params.code + '/',
        method: 'GET'
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.state = true
          this.profs = data.data.profs
        } else {
          this.state = false
          this.msg = data.error
        }
      })
    },
    getTAs: function () {
      this.$axios.request({
        url: this.$url + 'TAs/code/' + this.$route.params.code + '/',
        method: 'GET'
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.state = true
          this.TAs = data.data.TAs
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