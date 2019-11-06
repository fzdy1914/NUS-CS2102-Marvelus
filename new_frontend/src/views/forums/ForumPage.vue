<template>
  <div>
    <router-view :forums="forums" v-on:update="getForums"/>
  </div>
</template>

<script>
export default {
  name: "ForumPage",
  data() {
    return {
      state: false,
      msg: 'Network Error',
      forums: null,
    }
  },
  mounted() {
    this.getForums()
  },
  methods: {
    getForums: function () {
      let keyword
      if (this.status == 'Student') {
        keyword = 'view'
      } else {
        keyword = 'code'
      }
      this.$axios.request({
        url: this.$url + 'forums/' + keyword + '/' + this.$route.params.code + '/',
        method: 'GET'
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.state = true
          this.forums = data.data.forums
        } else {
          this.state = false
          this.msg = data.error
        }
      })
    }
  },
  computed: {
    status: function () {
      if (this.$route.name.startsWith('Teach')) {
        return 'Prof'
      } else if (this.$route.name.startsWith('Assist')) {
        return 'TA'
      }
      return 'Student'
    }
  }
}
</script>

<style scoped>

</style>