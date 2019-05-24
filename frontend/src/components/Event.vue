<template>
  <div>
    <div v-if="state">
      <table class="table table-bordered table-hover">
        <thead>
          <tr>
            <th>ID</th>
            <th>Title</th>
            <th>Date</th>
            <th>Channel</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="event in events" :key="event.id">
            <td class="id">{{ event.id }}</td>
            <td class="title">{{ event.title }}</td>
            <td class="date">{{ getDate(event.timestamp) }}</td>
            <td class="channel">{{ event.channel }}</td>
          </tr>
        </tbody>
      </table>
      <nav>
        <ul class="pagination">
          <li v-bind:class="{ disabled: startPage === 1 }">
            <a @click="startPage=prevPage"><span>&laquo;</span></a>
          </li>
          <li v-for="index in generateArray(startPage, endPage)" :key="index" :class="{ active: index === currentPage}">
            <a @click="goPage(index)">{{ index }}</a>
          </li>
          <li v-bind:class="{ disabled: endPage === maxPage }">
            <a @click="startPage=nextPage"><span>&raquo;</span></a>
          </li>
        </ul>
      </nav>
    </div>
    <div v-else>
      <h3>{{ msg }}</h3>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Event',
  data () {
    return {
      msg: 'Network Error',
      events: null,
      count: null,
      state: false,
      offset: 0,
      limit: 25,
      channelId: null,
      startPage: 1,
      currentPage: 1
    }
  },
  mounted () {
    this.$axios.request({
      url: this.$url + 'events/',
      method: 'GET',
      params: {
        'offset': this.$route.query.offset,
        'limit': this.limit,
        'channel_id': this.$route.query.channelId
      }
    }).then(response => {
      let data = response.data
      if (data.state === true) {
        this.state = true
        this.events = data.data.events
        this.count = data.data.count
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
    generateArray: function (start, end) {
      return Array.from(new Array(end + 1).keys()).slice(start)
    },
    goPage: function (index) {
      this.$router.push({
        name: 'EventList',
        query: {
          offset: (index - 1) * this.limit,
          channelId: this.channelId,
          limit: this.limit
        }
      })
      this.currentPage = index
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
          this.events = data.data.events
          this.count = data.data.count
        } else {
          this.state = false
          this.msg = data.error
        }
      })
    }
  },
  watch: {
    '$route' (to, from) {
      this.offset = to.query.offset
      this.channelId = to.query.channelId
      if (to.query.startPage) {
        this.startPage = to.query.startPage
      }
      if (to.query.currentPage) {
        this.currentPage = to.query.currentPage
      }
    },
    'offset' (to, from) {
      this.updateList(to, this.limit, this.channelId)
    },
    'channelId' (to, from) {
      this.updateList(this.offset, this.limit, to)
    }
  },
  computed: {
    maxPage: function () {
      return Math.ceil(this.count / this.limit)
    },
    endPage: function () {
      return this.startPage + 9 < this.maxPage ? this.startPage + 9 : this.maxPage
    },
    prevPage: function () {
      return this.startPage - 10 < 1 ? 1 : this.startPage - 10
    },
    nextPage: function () {
      return this.endPage === this.maxPage ? this.startPage : this.endPage + 1
    }
  }
}
</script>
