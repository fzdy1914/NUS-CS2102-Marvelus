<template>
  <div>
    <ul class="nav nav-tabs">
      <li :class="{ active: currentPanel === 'Channels' }"><a @click="goChannels">Channels</a></li>
      <li :class="{ active: currentPanel === 'Events' }"><a @click="goEvents">Events</a></li>
      <li><a href="#">Comments</a></li>
      <li class="navbar-right"><button type="button" class="btn btn-primary new" @click="newItem">New</button></li>
    </ul>
      <div class="modal-content" v-if="isEdit">
        <div class="modal-header">
          <button type="button" class="close" @click="isEdit = false">&times;</button>
          <h4 class="modal-title">New channel</h4>
        </div>
        <div class="modal-body">
          <form>
            <div v-show="error" class="form-group error">
              <label>Error: {{ error }}</label>
            </div>
            <div class="form-group">
              <label>Name</label>
              <input type="text" class="form-control" placeholder="Channel Name" v-model="channelName"/>
            </div>
          </form>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-default" @click="isEdit = false">Close</button>
          <button type="button" class="btn btn-primary submit" @click="submit">Submit</button>
        </div>
      </div>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'AdminItemList',
  data () {
    return {
      currentPanel: 'Events',
      isEdit: false,
      channelName: '',
      error: null
    }
  },
  mounted () {
    if (this.$route.name === 'AdminEventList') {
      this.currentPanel = 'Events'
    } else if (this.$route.name === 'AdminChannelList') {
      this.currentPanel = 'Channels'
    }
  },
  methods: {
    goChannels: function () {
      this.currentPanel = 'Channels'
      this.$router.push({
        name: 'AdminChannelList'
      })
    },
    goEvents: function () {
      this.currentPanel = 'Events'
      this.$router.push({
        name: 'AdminEventList'
      })
    },
    goNewEvent: function () {
      this.$router.push({
        name: 'AdminEventList',
        query: {
          isEdit: true
        }
      })
    },
    newItem: function () {
      if (this.currentPanel === 'Events') {
        this.goNewEvent()
      } else if (this.currentPanel === 'Channels') {
        this.newChannel()
      }
    },
    newChannel: function () {
      this.isEdit = true
    },
    submit: function () {
      this.$axios.request({
        url: this.$url + 'channels/',
        method: 'POST',
        data: {
          name: this.channelName
        }
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.$router.push({
            name: 'AdminChannelList',
            query: {
              startPage: 1,
              currentPage: 1
            }
          })
          this.channelName = ''
          this.isEdit = false
          this.error = null
        } else {
          this.error = data.error
        }
      })
    }
  },
  watch: {
    '$route' (to, from) {
      if (to.name === 'AdminEventList') {
        this.currentPanel = 'Events'
      } else if (to.name === 'AdminChannelList') {
        this.currentPanel = 'Channels'
      }
    }
  }
}
</script>

<style scoped>
  .nav{
    font-size: 18px;
    background: #FCFCFC
  }
  li {
    vertical-align: middle;
  }
  .new {
    font-size: 18px;
    background-color: #009100;
    border-color: #007500;
    margin-top: 3px;
  }
  .submit {
    background-color: #009100;
    border-color: #007500;
  }
  .navbar-right {
    margin-right: 0px;
  }
  .modal-content {
    margin-top: 20px;
  }
  .error {
    color: #D94600;
  }
</style>
