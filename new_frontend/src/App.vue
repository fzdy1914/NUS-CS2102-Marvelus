<template>
  <div id="app">
    <InfoBar v-if="$store.state.username"/>
    <router-view/>
  </div>
</template>

<script>
import InfoBar from "./components/InfoBar";

export default {
  components: {InfoBar}
}

</script>
<style lang="scss">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  padding: 30px;
  a {
    font-weight: bold;
    color: #2c3e50;
    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
html {
  background-color: #fff;
}
</style>
