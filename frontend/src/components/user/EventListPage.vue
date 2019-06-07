<template>
  <div>
    <div v-if="state">
      <ChannelBar :isAdmin="false"/>

      <EventList :events="events" :isAdmin="false"/>

      <NavigationBar :isAdmin="false" :count="count"/>
    </div>
    <div v-else>
      <h3>{{ msg }}</h3>
    </div>
  </div>
</template>

<script>
import EventList from '../EventList'
import ChannelBar from '../ChannelBar'
import NavigationBar from '../NavigationBar'
export default {
  name: 'EventListPage',
  components: {
    NavigationBar,
    ChannelBar,
    EventList
  },
  data () {
    return {
      msg: 'Network Error',
      events: null,
      count: null,
      state: false,

      offset: 0,
      limit: 15,
      channelId: null,
      sinceDate: null,
      untilDate: null
    }
  },
  mounted () {
    let parse = this.$util.parse
    this.channelId = parse(this.$route.query.channelId)
    this.offset = parse(this.$route.query.offset)
    this.sinceDate = parse(this.$route.query.sinceDate)
    this.untilDate = parse(this.$route.query.untilDate)
    if (this.$route.query.limit) {
      this.limit = parse(this.$route.query.limit)
    }
    this.updateEventList()
  },
  methods: {
    updateEventList: function () {
      this.$axios.request({
        url: this.$url + 'events/',
        method: 'GET',
        params: {
          'offset': this.offset,
          'limit': this.limit,
          'channel_id': this.channelId,
          'since': this.sinceDate,
          'until': this.untilDate
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
      let parse = this.$util.parse
      this.offset = parse(to.query.offset)
      this.channelId = parse(to.query.channelId)
      this.sinceDate = parse(to.query.sinceDate)
      this.untilDate = parse(to.query.untilDate)
      if (to.query.limit) {
        this.limit = parse(to.query.limit)
      }
      this.updateEventList()
    }
  }
}
</script>
