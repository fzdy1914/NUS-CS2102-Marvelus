<template>
  <div v-if="channels && state">
    <nav class="navbar navbar-default">
      <!-- Collect the nav links, forms, and other content for toggling -->
      <div class="collapse navbar-collapse">
        <ul class="nav navbar-nav navbar-left">
          <li :class="{ active: !channelId }"><a @click="goChannel(null)">All</a></li>
          <li v-for="channel in channels.slice(0, 4)" :key="channel.id" :class="{ active: channelId === channel.id }">
            <a @click="goChannel(channel.id)">{{ channel.name }}</a>
          </li>
          <li class="dropdown" :class="{ active: activeDropdown }">
            <a class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">
              {{ dropdownText }}<span class="caret"/>
            </a>
            <ul class="dropdown-menu">
              <li v-for="channel in channels.slice(4)" :key="channel.id" :class="{ active: channelId === channel.id }">
                <a @click="goChannel(channel.id)">{{ channel.name }}</a>
              </li>
            </ul>
          </li>
        </ul>
        <form class="navbar-right">
          <DatePicker v-on:updateSinceDate="updateSinceDate" v-on:updateUntilDate="updateUntilDate"/>
        </form>
      </div><!-- /.navbar-collapse -->
    </nav>
  </div>
  <div v-else>
    <h3>{{ msg }}</h3>
  </div>
</template>

<script>
import DatePicker from './DoubleDatePicker'
export default {
  name: 'ChannelBar',
  components: {
    DatePicker
  },
  props: {
    isAdmin: Boolean
  },
  data () {
    return {
      msg: 'Network Error',
      channels: null,
      count: null,
      channelId: null,
      sinceDate: null,
      untilDate: null
    }
  },
  mounted () {
    this.$axios.request({
      url: this.$url + 'channels/',
      method: 'GET',
      params: {
        'limit': 100
      }
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
    let parse = this.$util.parse
    this.sinceDate = parse(this.$route.query.sinceDate)
    this.untilDate = parse(this.$route.query.untilDate)
    this.channelId = parse(this.$route.query.channelId)
  },
  methods: {
    goChannel: function (channelId) {
      this.$router.push({
        name: this.isAdmin ? 'AdminEventList' : 'EventList',
        query: {
          channelId: channelId,
          startPage: 1,
          currentPage: 1,
          sinceDate: this.sinceDate,
          untilDate: this.untilDate
        }
      })
    },
    goDate: function () {
      this.$router.push({
        name: this.isAdmin ? 'AdminEventList' : 'EventList',
        query: {
          channelId: this.channelId,
          startPage: 1,
          currentPage: 1,
          sinceDate: this.sinceDate,
          untilDate: this.untilDate
        }
      })
    },
    updateSinceDate: function (sinceDate) {
      this.sinceDate = sinceDate === '' ? null : Date.parse(sinceDate)
      this.goDate()
    },
    updateUntilDate: function (untilDate) {
      this.untilDate = untilDate === '' ? null : Date.parse(untilDate) + 86400000
      this.goDate()
    }
  },
  watch: {
    '$route' (to, from) {
      let parse = this.$util.parse
      this.channelId = parse(to.query.channelId)
      this.sinceDate = parse(to.query.sinceDate)
      this.untilDate = parse(to.query.untilDate)
    }
  },
  computed: {
    dropdownText: function () {
      if (this.channelId) {
        for (let channel of this.channels.slice(4)) {
          if (this.channelId === channel.id) {
            return channel.name
          }
        }
      }
      return 'More Channels'
    },
    activeDropdown: function () {
      if (this.channelId) {
        for (let channel of this.channels.slice(4)) {
          if (this.channelId === channel.id) {
            return true
          }
        }
      }
      return false
    }
  }
}
</script>

<style scoped>
  .nav{
    font-size: 18px;
    background: #FCFCFC
  }
  .navbar-right {
    vertical-align: center;
  }
  .navbar-collapse {
    padding-left: 0px;
  }
</style>
