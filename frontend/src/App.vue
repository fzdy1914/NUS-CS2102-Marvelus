<template>
  <div id="app">
    <div class="container">
      <h2>Welcome to Event Center!</h2>
      <ul class="nav nav-pills">
        <li><a @click="goChannel(null)">All</a></li>
        <li v-for="channel in channels"><a @click="goChannel(channel.id)">{{ channel.name }}</a></li>
      </ul>
      <router-view/>
      <nav>
        <ul class="pagination">
          <li><a href="#"><span>&laquo;</span></a></li>
          <li><a href="#">1</a></li>
          <li><a href="#">2</a></li>
          <li><a href="#">3</a></li>
          <li><a href="#">4</a></li>
          <li><a href="#">5</a></li>
          <li><a href="#"><span>&raquo;</span></a></li>
        </ul>
      </nav>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  data () {
    return {
      msg: 'Hello World',
      channels: null
    }
  },
  mounted () {
    this.$axios.request({
      url: this.$url + 'channels/',
      method: 'GET',
      params: {
        'offset': this.$route.query.offset,
        'limit': this.$route.query.limit,
      }
    }).then(response => {
      let data = response.data
      if (data.state === true) {
        this.state = true
        this.channels = data.channels
      } else {
        this.state = false
        this.msg = data.error
      }
    })
  },
  methods: {
    goChannel: function(channelId) {
      this.$router.push({
        name: 'EventList',
        query: {
          channelId: channelId
        }
      })
    }
  }
}
</script>

<style>
  nav {
    text-align: center;
  }
</style>
