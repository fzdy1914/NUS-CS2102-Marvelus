<template>
  <div class="module-page">
    <NavBar :whichActive="'assists'"/>
    <router-view :courses="assists"/>
  </div>
</template>

<script>
import NavBar from '../components/NavBar'

export default {
  name: 'AssistPage',
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
    this.getAssists()
  },
  methods: {
    getAssists: function () {
      this.$axios.request({
        url: this.$url + 'assists/',
        method: 'GET'
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.state = true
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

</style>
