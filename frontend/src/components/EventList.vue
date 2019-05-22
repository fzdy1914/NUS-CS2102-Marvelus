<template>
  <div>
    <div v-if="state">
      <table>
        <tr>
          <th>ID</th>
          <th>Title</th>
          <th>Date</th>
          <th>Channel</th>
        </tr>
        <tr v-for="event in events">
          <td class="id">id: {{ event.id }}</td>
          <td class="title">title: {{ event.title }}</td>
          <td class="date">date: {{ getDate(event.timestamp) }}</td>
          <td class="channel">channel: {{ event.channel_id }}</td>
        </tr>
      </table>
    </div>
    <div v-else>
      {{ msg }}
    </div>
  </div>
</template>

<script>
export default {
  name: 'EventList',
  data () {
    return {
      msg: 'Hello World',
      fruitList: [],
      events: null,
      state: null
    }
  },
  mounted () {
    this.$axios.request({
      url: this.$url + 'events/',
      method: 'GET',
      params: {
        'offset': this.$route.query.offset,
        'limit': this.$route.query.limit,
        'channel_id': this.$route.query.channelId
      }
    }).then(response => {
      let data = response.data
      if (data.state === true) {
        this.state = true
        this.events = data.events
      } else {
        this.state = false
        this.msg = data.error
      }
    })
  },
  methods: {
    getDate: function (timestamp) {
      return new Date(timestamp * 1000).toLocaleString()
    },
    updateList: function (offset, limit, channelId) {
      this.$axios.request({
        url: this.$url + 'events/',
        method: 'GET',
        params: {
          'offset': offset,
          'limit': limit,
          'channel_id': channelId
        }
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.state = true
          this.events = data.events
        } else {
          this.state = false
          this.msg = data.error
        }
      })
    }
  },
  watch: {
    '$route' (to, from) {
      console.log(to)
      let params = to.query
      this.updateList(params.offset, params.limit, params.channelId)
    }
  }

}
</script>

<style>

</style>
