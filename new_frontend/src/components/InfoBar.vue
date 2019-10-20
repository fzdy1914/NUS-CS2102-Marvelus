<template>
  <div class="info-bar">
    <div>Welcome: {{ $store.state.username }}, <a @click="logout()">Logout</a></div>
  </div>
</template>

<script>
  export default {
    name: "InfoBar",
    methods: {
      logout: function() {
        this.$store.commit('setUsername', null)
        this.$store.commit('isAdmin', false)
        this.$store.commit('isProf', false)
        this.$store.commit('isTA', false)
        this.$axios({
          method: 'get',
          url: this.$url + 'logout/'
        })
        this.$router.push({name: 'Login'})
      },
    }
  }
</script>

<style scoped>
  .info-bar {
    height: 100px;
  }
</style>