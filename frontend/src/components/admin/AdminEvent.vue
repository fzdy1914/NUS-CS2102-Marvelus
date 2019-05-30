<template>
  <div>
    <form>
      <div class="form-group">
        <h3>Event title:</h3>
        <input type="text" class="form-control" placeholder="Event title" v-model="event.title"/>
      </div>
      <div class="form-group">
        <h3>Event location:</h3>
        <input type="text" class="form-control" placeholder="Event location" v-model="event.location"/>
      </div>
      <div class="form-group">
        <h3>Event date:</h3>
        <input type="text" class="form-control" placeholder="Event date" v-model="event.timestamp"/>
      </div>
      <div class="form-group">
        <h3>Event description:</h3>
        <textarea rows="6" type="text" class="form-control" placeholder="Event description" v-model="event.description"/>
      </div>
      <div class="form-group">
        <h3>Event image:</h3>
        <input type="text" class="form-control" placeholder="Event image url" v-model="event.image_url"/>
        <h3>Preview:</h3>
        <img :src="event.image_url">
      </div>
      <div v-show="error" class="form-group error">
        <h3>Error: {{ error }}</h3>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-default" id="close" @click="cancel">Close</button>
        <button type="button" class="btn btn-primary" @click="submit">Submit</button>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: 'AdminEvent',
  props: {
    eventId: Number
  },
  data () {
    return {
      event: {
        title: '',
        location: '',
        timestamp: '',
        description: '',
        image_url: ''
      },
      error: null
    }
  },
  mounted () {
    if (this.eventId) {
      this.updateEvent(this.eventId)
    }
  },
  methods: {
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
    },
    cancel: function () {
      this.$emit('cancelEdit')
    },
    submit: function () {
      this.$axios.request({
        url: this.$url + 'event/' + this.eventId + '/',
        method: 'PUT',
        data: {
          title: this.event.title,
          description: this.event.description,
          timestamp: this.event.timestamp,
          location: this.event.location,
          image_url: this.event.image_url
        }
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.error = null
          this.$emit('replaceEvent', data.data.event)
          document.getElementById('close').click()
        } else {
          this.error = data.error
        }
      })
    }
  },
  watch: {
    '$route' (to, from) {
      this.updateEvent(to.params.eventId)
    },
    'eventId' (to, from) {
      this.updateEvent(to)
    }
  }
}
</script>

<style scoped>
  .form-control {
    font-size: 16px;
    padding: 10px 10px
  }
  .error {
    color: #D94600;
  }
  img {
    width: 600px;
  }
</style>
