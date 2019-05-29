<template>
  <div id="app">
    <div class="container">
      <div v-show="$store.state.username">
        <div class="page-header">
          <h1>{{ welcomeText }}</h1>
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
  data () {
    return {
      isAdminPage: false
    }
  },
  mounted () {
    if (this.$route.name && this.$route.name.indexOf('Admin') !== -1) {
      this.isAdminPage = true
    } else {
      this.isAdminPage = false
    }
  },
  computed: {
    username: function () {
      return this.$store.state.username || 'Anonymous User'
    },
    welcomeText: function () {
      if (this.isAdminPage) {
        return 'Event Center Management'
      } else {
        return 'Welcome to Event Center !'
      }
    }
  },
  methods: {
    logout () {
      this.$store.commit('setUsername', null)
      this.$store.commit('isAdmin', false)
      this.$axios({
        method: 'get',
        url: this.$url + 'logout/'
      })
      this.$router.push({name: 'Login'})
    }
  },
  watch: {
    '$route' (to, from) {
      if (to.name.indexOf('Admin') !== -1) {
        this.isAdminPage = true
      } else {
        this.isAdminPage = false
      }
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
  .table > tbody > tr > td {
    vertical-align: middle;
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
