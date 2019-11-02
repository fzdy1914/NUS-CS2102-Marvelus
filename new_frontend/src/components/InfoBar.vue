<template>
  <div class="info-bar">
    <img class="logo-img" src="../assets/logo-transparent-bg.png">
    <div class="user">Welcome, {{ $store.state.username }} <Button class="p-button-danger" icon="pi pi-sign-out" @click="logout()"/></div>
  </div>
</template>


<script>
import Button from 'primevue/button';

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
    }
  },
  components:{
    Button
  }
}
</script>

<style scoped>
  .info-bar {
    height: 60px;
    background-color: #1565c0;
  }
  .user {
    color: white;
    padding-top: 10px;
    padding-right: 25px;
    float:right;
    font-size: 14pt;
  }
  .logo-img {
    float:left;
    width: auto;
    margin-top: 5px;
    margin-left: 10px;
    height: 50px;
  }
</style>