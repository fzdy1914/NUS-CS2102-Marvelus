<template>
  <div>
    <div v-if="state">
      <ul class="breadcrumb">
        <li>
          <a @click="goChannel(null)">EventCenter</a>
        </li>
        <li>
          <a @click="goChannel(event.channel_id)">{{ event.channel }}</a>
        </li>
        <li class="active">{{ event.title }}</li>
      </ul>
      <h1 class="event-title">
        {{ event.title }}
      </h1>
      <h3 class="event-location">
        Location: {{ event.location }}
      </h3>
      <h3 class="event-date">
        Date: {{ $util.getDate(event.timestamp) }}
      </h3>
      <h3>
        Description:
      </h3>
      <p class="event-description">
        {{ event.description }}
      </p>
      <LikeList :eventId="event.id"></LikeList>
      <CommentList :eventId="event.id"></CommentList>
    </div>
    <div v-else>
      <h3>{{ msg }}</h3>
    </div>
  </div>
</template>

<script>
import CommentList from './CommentList'
import LikeList from './LikeList'

export default {
  name: 'Event',
  components: {
    CommentList,
    LikeList
  },
  data () {
    return {
      msg: 'Network Error',
      event: null,
      count: null,
      state: false
    }
  },
  mounted () {
    this.updateEvent(this.$route.params.eventId)
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
    },
    updateEvent: function (eventId) {
      this.$axios.request({
        url: this.$url + 'event/' + eventId + '/',
        method: 'GET'
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.state = true
          this.event = data.data.event
        } else {
          this.state = false
          this.msg = data.error
        }
      })
    }
  },
  watch: {
    '$route' (to, from) {
      this.updateEvent(to.params.eventId)
    }
  }
}
</script>

<style scoped>
  .breadcrumb > li + li:before {
    color: #000000;
  }
  .breadcrumb {
    font-size: 20px;
    background: #FCFCFC;
  }
  .event-title {
    font-size: 50px;
  }
  .event-description {
    font-size: 20px;
  }
</style>
