<template>
  <div>
    <div v-if="state">
      <div class="page-header">
        <h1>Welcome to Event Center !</h1>
      </div>
      <ul class="nav nav-pills">
        <li :class="{ active: !channelId }"><a @click="goChannel(null)">All</a></li>
        <li v-for="channel in channels" :key="channel.id" :class="{ active: channelId === channel.id }">
          <a @click="goChannel(channel.id)">{{ channel.name }}</a>
        </li>
      </ul>
      <table class="table table-bordered table-hover">
        <thead>
          <tr>
            <th>ID</th>
            <th>Title</th>
            <th>Date</th>
            <th>Channel</th>
            <th>Likes</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="event in events" :key="event.id">
            <td class="id">{{ event.id }}</td>
            <td class="title"><a @click="goEvent(event.id)">{{ event.title }}</a></td>
            <td class="date">{{ getDate(event.timestamp) }}</td>
            <td class="channel">{{ event.channel }}</td>
            <td class="likes">{{ event.likes }}</td>
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
  name: 'EventList',
  data () {
    return {
      msg: 'Network Error',
      events: null,
      channels: null,
      count: null,
      state: false,

      offset: 0,
      limit: 15,
      channelId: null,
      startPage: 1,
      currentPage: 1
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
    this.channelId = this.parse(this.$route.query.channelId)
    this.startPage = this.parse(this.$route.query.startPage) || 1
    this.currentPage = this.parse(this.$route.query.currentPage) || 1
    this.offset = this.parse(this.$route.query.offset)
    this.updateList(this.offset, this.limit, this.channelId)
  },
  methods: {
    parse: function (candidate) {
      if (candidate && typeof (candidate) === 'string') {
        return parseInt(candidate)
      }
      return candidate
    },
    getDate: function (timestamp) {
      return new Date(timestamp * 1000).toLocaleDateString()
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
          limit: this.limit,
          currentPage: index,
          startPage: this.startPage
        }
      })
      this.currentPage = index
    },
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
    },
    goEvent: function (eventId) {
      this.$router.push({
        name: 'Event',
        params: {
          eventId: eventId
        },
        query: {
          startPage: 1,
          currentPage: 1
        }
      })
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
      this.offset = this.parse(to.query.offset)
      this.channelId = this.parse(to.query.channelId)
      if (to.query.startPage) {
        this.startPage = this.parse(to.query.startPage)
      }
      if (to.query.currentPage) {
        this.currentPage = this.parse(to.query.currentPage)
      }
      if (to.query.startPage) {
        this.startPage = this.parse(to.query.startPage)
      }
    },
    'offset' (to, from) {
      this.updateList(this.parse(to), this.limit, this.channelId)
    },
    'channelId' (to, from) {
      this.updateList(this.offset, this.limit, this.parse(to))
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

<style>
  table {
    margin-top: 25px;
    font-size: 15px;
  }
  th, td {
    text-align: center;
  }
  nav {
    text-align: center;
  }
  .id {
    width: 150px;
  }
  .title {
    width: 700px;
  }
  .date, .channel {
    width: 200px;
  }
  .likes {
    width: 150px;
  }
  a:hover{
    cursor: pointer;
  }
  .nav{
    font-size: 18px;
    background: #FCFCFC
  }
</style>
