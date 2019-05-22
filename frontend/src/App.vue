<template>
  <div id="app">
    <h1>Welcome to Event Center!</h1>
    <router-link to="/">Index</router-link>
    <router-link to="/hello">Go to HelloWorld</router-link>
    <input v-model="channelId">
    <a @click="goChannel()">Go Channel</a>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
  data () {
    return {
      msg: 'Hello World',
      channels: null,
      channelId: null
    }
  },
  methods: {
    goChannel: function() {
      this.$router.push({
        name: 'EventList',
        query: {
          channelId: this.channelId
        }
      })
    }
  }
}
</script>

<style>
  a {
    color:#0000FF;
    text-decoration:none;
  }
  a:hover {
    color:#CC3300;
    text-decoration:underline;
    cursor:pointer;
  }
</style>
