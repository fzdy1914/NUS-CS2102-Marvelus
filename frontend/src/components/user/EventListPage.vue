<template>
  <div>
    <div v-if="state">
      <ChannelBar :isAdmin="false"/>

      <EventList :events="events" :isAdmin="false"/>

      <nav>
        <ul class="pagination">
          <li v-bind:class="{ disabled: startPage === 1 }">
            <a @click="startPage=prevPage"><span>&laquo;</span></a>
          </li>
          <li v-for="index in indexArray" :key="index" :class="{ active: index === currentPage}">
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
import EventList from '../EventList'
import ChannelBar from '../ChannelBar'
export default {
  name: 'EventListPage',
  components: {
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
      startPage: 1,
      currentPage: 1,
      sinceDate: null,
      untilDate: null
    }
  },
  mounted () {
    let parse = this.$util.parse
    this.channelId = parse(this.$route.query.channelId)
    this.startPage = parse(this.$route.query.startPage) || 1
    this.currentPage = parse(this.$route.query.currentPage) || 1
    this.offset = parse(this.$route.query.offset)
    this.sinceDate = parse(this.$route.query.sinceDate)
    this.untilDate = parse(this.$route.query.untilDate)
    this.updateEventList()
  },
  methods: {
    goPage: function (index) {
      this.$router.push({
        name: 'EventList',
        query: {
          offset: (index - 1) * this.limit,
          channelId: this.channelId,
          limit: this.limit,
          currentPage: index,
          startPage: this.startPage,
          sinceDate: this.sinceDate,
          untilDate: this.untilDate
        }
      })
    },
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
      if (to.query.startPage) {
        this.startPage = parse(to.query.startPage)
      }
      if (to.query.currentPage) {
        this.currentPage = parse(to.query.currentPage)
      }
      this.sinceDate = parse(to.query.sinceDate)
      this.untilDate = parse(to.query.untilDate)
      this.updateEventList()
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
    },
    indexArray: function () {
      return this.$util.generateArray(this.startPage, this.endPage)
    }
  }
}
</script>
