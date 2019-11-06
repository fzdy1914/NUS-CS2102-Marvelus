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
      this.$axios.request({
        url: this.$url + 'forums/view/' + this.$route.params.code + '/',
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
  }
}
</script>

<style scoped>

</style>