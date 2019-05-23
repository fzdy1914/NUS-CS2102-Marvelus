<template>
  <div id="app">
    <div class="container">
      <h2>Welcome to Event Center!</h2>
      <ul class="nav nav-pills">
        <li :class="{ active: currentChannel === 0 }"><a @click="goChannel(null)">All</a></li>
        <li v-for="channel in channels" :key="channel.id" :class="{ active: currentChannel === channel.id }">
          <a @click="goChannel(channel.id)">{{ channel.name }}</a>
        </li>
      </ul>
      <router-view/>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  data () {
    return {
      msg: 'Hello World',
      channels: null,
      currentChannel: 0
    }
  },
  mounted () {
    this.$axios.request({
      url: this.$url + 'channels/',
      method: 'GET'
    }).then(response => {
      let data = response.data
      if (data.state === true) {
        this.state = true
        this.channels = data.data.channels
      } else {
        this.state = false
        this.msg = data.error
      }
    })
  },
  methods: {
    goChannel: function (channelId) {
      this.$router.push({
        name: 'EventList',
        query: {
          channelId: channelId,
          startPage: 1,
          currentPage: 1
        }
      })
      this.currentChannel = channelId || 0
    }
  }
}
</script>

<style>
  a:hover{
    cursor:pointer;
  }
</style>
