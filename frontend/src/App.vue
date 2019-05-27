<template>
  <div id="app">
    <div class="container">
      <div v-show="$store.state.username">
        <div class="page-header">
          <h1>Welcome to Event Center !</h1>
          <span>Current user:  <strong><em>{{ username }}</em></strong>,&nbsp;</span>
          <a @click="logout">Logout</a>
        </div>
      </div>
      <router-view/>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  computed: {
    username: function () {
      return this.$store.state.username || 'Anonymous User'
    }
  },
  methods: {
    logout () {
      this.$store.commit('setUsername', null)
      this.$axios({
        method: 'get',
        url: this.$url + 'logout/'
      })
      this.$router.push({name: 'Login'})
    }
  }
}
</script>

<style>
  table {
    margin-top: 25px;
    font-size: 15px;
  }
  th, td {
    text-align: center;
  }
  a:hover{
    cursor: pointer;
  }
  nav {
    text-align: center;
  }
  .page-header {
    margin-top: 0px;
    font-size: 16px;
  }
</style>
