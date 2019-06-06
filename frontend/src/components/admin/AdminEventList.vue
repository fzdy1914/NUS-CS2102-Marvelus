<template>
  <div>
    <div v-if="isEdit">
      <AdminEvent :eventId="eventId" v-on:cancelEdit="cancelEdit" v-on:replaceEvent="replaceEvent"/>
    </div>
    <div v-else>
      <div v-if="state">
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
        <table class="table table-bordered table-hover">
          <thead>
            <tr>
              <th>ID</th>
              <th>Title</th>
              <th>Date</th>
              <th>Channel</th>
              <th>Likes</th>
              <th>Operation</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="event in events" :key="event.id">
              <td class="id">{{ event.id }}</td>
              <td class="title"><a @click="goEvent(event.id)">{{ event.title }}</a></td>
              <td class="date">{{ $util.getDate(event.timestamp) }}</td>
              <td class="channel">{{ event.channel }}</td>
              <td class="likes">{{ event.likes }}</td>
              <td class="operation">
                <button class="btn btn-primary edit" @click="editEvent(event)">Edit</button>
                <button class="btn btn-primary delete" data-toggle="modal" data-target="#deleteEvent" @click="loadEvent(event)">Delete</button>
              </td>
            </tr>
          </tbody>
        </table>
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
        <div class="modal fade" id="deleteEvent" tabindex="-1" role="dialog" aria-hidden="true">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal">&times;</button>
                <h4 class="modal-title">Delete Event</h4>
              </div>
              <div class="modal-body">
                <form>
                  <div class="form-group">
                    <label>Id: {{ eventId }}</label>
                  </div>
                  <div v-show="error" class="form-group error">
                    <label>Error: {{ error }}</label>
                  </div>
                  <div class="form-group">
                    <label>Title: {{ eventTitle }}</label>
                  </div>
                  <div class="form-group">
                    <label>Channel: {{ eventChannel }}</label>
                  </div>
                  <div class="form-group">
                    <label>Date: {{ eventDate }}</label>
                  </div>
                </form>
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-default" data-dismiss="modal" id="close">Close</button>
                <button type="button" class="btn btn-primary delete" @click="deleteEvent">Delete</button>
              </div>
              </div>
          </div>
        </div>
      </div>
      <div v-else>
        <h3>{{ msg }}</h3>
      </div>
    </div>
  </div>
</template>

<script>
import DatePicker from '../DoubleDatePicker'
import AdminEvent from './AdminEvent'
export default {
  name: 'AdminEventList',
  components: {
    DatePicker,
    AdminEvent
  },
  data () {
    return {
      isEdit: false,
      msg: 'Network Error',
      events: null,
      channels: null,
      count: null,
      state: false,

      offset: 0,
      limit: 15,
      channelId: null,
      startPage: 1,
      currentPage: 1,
      sinceDate: null,
      untilDate: null,

      eventId: null,
      eventTitle: '',
      eventDate: '',
      eventChannel: '',
      error: null
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
    this.channelId = parse(this.$route.query.channelId)
    this.startPage = parse(this.$route.query.startPage) || 1
    this.currentPage = parse(this.$route.query.currentPage) || 1
    this.offset = parse(this.$route.query.offset)
    this.sinceDate = parse(this.$route.query.sinceDate)
    this.untilDate = parse(this.$route.query.untilDate)
    this.isEdit = this.$route.query.isEdit === true || this.$route.query.isEdit === 'true'
    this.eventId = parse(this.$route.query.eventId)
    this.updateEventList()
  },
  methods: {
    goPage: function (index) {
      this.$router.push({
        name: 'AdminEventList',
        query: {
          offset: (index - 1) * this.limit,
          channelId: this.channelId,
          limit: this.limit,
          currentPage: index,
          startPage: this.startPage,
          sinceDate: this.sinceDate,
          untilDate: this.untilDate,
          isEdit: false
        }
      })
    },
    goChannel: function (channelId) {
      this.$router.push({
        name: 'AdminEventList',
        query: {
          channelId: channelId,
          startPage: 1,
          currentPage: 1,
          sinceDate: this.sinceDate,
          untilDate: this.untilDate,
          isEdit: false
        }
      })
    },
    goDate: function () {
      this.$router.push({
        name: 'AdminEventList',
        query: {
          channelId: this.channelId,
          startPage: 1,
          currentPage: 1,
          sinceDate: this.sinceDate,
          untilDate: this.untilDate,
          isEdit: false
        }
      })
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
    },
    updateSinceDate: function (sinceDate) {
      this.sinceDate = sinceDate === '' ? null : Date.parse(sinceDate)
      this.goDate()
    },
    updateUntilDate: function (untilDate) {
      this.untilDate = untilDate === '' ? null : Date.parse(untilDate) + 86400000
      this.goDate()
    },

    loadEvent: function (event) {
      console.log('a')
      this.eventId = event.id
      this.eventTitle = event.title
      this.eventDate = this.$util.getDate(event.timestamp)
      this.eventChannel = event.channel
    },
    deleteEvent: function () {
      this.$axios.request({
        url: this.$url + 'event/' + this.eventId + '/',
        method: 'DELETE'
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.removeEvent()
          this.eventId = null
          this.eventTitle = ''
          this.eventDate = ''
          this.eventChannel = ''
          this.error = null
          document.getElementById('close').click()
        } else {
          this.error = data.error
        }
      })
    },
    removeEvent: function () {
      for (let i = 0; i < this.events.length; i++) {
        if (this.events[i].id === this.eventId) {
          this.events.splice(i, 1)
        }
      }
    },
    replaceEvent: function (event) {
      for (let i = 0; i < this.events.length; i++) {
        if (this.events[i].id === event.id) {
          this.events.splice(i, 1, event)
        }
      }
    },
    editEvent: function (event) {
      this.$router.push({
        name: 'AdminEventList',
        query: {
          offset: this.offset,
          channelId: this.channelId,
          limit: this.limit,
          currentPage: this.index,
          startPage: this.startPage,
          sinceDate: this.sinceDate,
          untilDate: this.untilDate,
          isEdit: true,
          eventId: event.id
        }
      })
    },
    cancelEdit: function () {
      this.$router.push({
        name: 'AdminEventList',
        query: {
          offset: this.offset,
          channelId: this.channelId,
          limit: this.limit,
          currentPage: this.index,
          startPage: this.startPage,
          sinceDate: this.sinceDate,
          untilDate: this.untilDate,
          isEdit: false
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
      this.startDate = parse(to.query.startDate)
      this.untilDate = parse(to.query.untilDate)
      this.isEdit = to.query.isEdit === true || to.query.isEdit === 'true'
      this.eventId = parse(to.query.eventId)
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
    },
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
  .id {
    width: 150px;
  }
  .title {
    width: 550px;
  }
  .date, .channel {
    width: 150px;
  }
  .likes {
    width: 100px;
  }
  .operation {
    width: 200px
  }
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
  .delete {
    background-color: #D94600;
    border-color: #BB3D00;
  }
  .btn {
    padding: 3px 8px;
  }
</style>
