<template>
  <div>
    <div v-if="isEdit">
      <AdminEvent :eventId="eventId" v-on:cancelEdit="cancelEdit" v-on:replaceEvent="replaceEvent"/>
    </div>
    <div v-else>
      <div v-if="state">

        <ChannelBar :isAdmin="true"/>

        <EventList :events="events" :isAdmin="true" v-on:editEvent="editEvent" v-on:loadEvent="loadEvent"/>

        <NavigationBar :isAdmin="true" :count="count"/>

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
import AdminEvent from './AdminEvent'
import EventList from '../EventList'
import ChannelBar from '../ChannelBar'
import NavigationBar from '../NavigationBar'
export default {
  name: 'AdminEventListPage',
  components: {
    NavigationBar,
    ChannelBar,
    EventList,
    AdminEvent
  },
  data () {
    return {
      isEdit: false,
      msg: 'Network Error',
      events: null,
      count: null,
      state: false,

      offset: 0,
      limit: 15,
      channelId: null,
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
    let parse = this.$util.parse
    this.channelId = parse(this.$route.query.channelId)
    this.offset = parse(this.$route.query.offset)
    this.sinceDate = parse(this.$route.query.sinceDate)
    this.untilDate = parse(this.$route.query.untilDate)
    this.isEdit = this.$route.query.isEdit === true || this.$route.query.isEdit === 'true'
    this.eventId = parse(this.$route.query.eventId)
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
    },

    loadEvent: function (event) {
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
    editEvent: function (eventId) {
      let query = this.$route.query
      this.$router.push({
        name: 'AdminEventList',
        query: {
          offset: query.offset,
          channelId: query.channelId,
          limit: query.limit,
          currentPage: query.currentPage,
          startPage: query.startPage,
          sinceDate: query.sinceDate,
          untilDate: query.untilDate,
          isEdit: true,
          eventId: eventId
        }
      })
    },
    cancelEdit: function () {
      let query = this.$route.query
      this.$router.push({
        name: 'AdminEventList',
        query: {
          offset: query.offset,
          channelId: query.channelId,
          limit: query.limit,
          currentPage: query.currentPage,
          startPage: query.startPage,
          sinceDate: query.sinceDate,
          untilDate: query.untilDate,
          isEdit: false,
          eventId: null
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
      this.isEdit = to.query.isEdit === true || to.query.isEdit === 'true'
      this.eventId = parse(to.query.eventId)
      if (to.query.limit) {
        this.limit = parse(to.query.limit)
      }
      this.updateEventList()
    }
  }
}
</script>

<style scoped>
  .delete {
    background-color: #D94600;
    border-color: #BB3D00;
  }
  .btn {
    padding: 3px 8px;
  }
</style>
