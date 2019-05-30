<template>
  <div>
    <ul class="nav nav-tabs">
      <li :class="{ active: currentPanel === 'Channels' }"><a @click="goChannels">Channels</a></li>
      <li :class="{ active: currentPanel === 'Events' }"><a @click="goEvents">Events</a></li>
      <li><a href="#">Comments</a></li>
      <li class="navbar-right"><button type="button" class="btn btn-primary" @click="newItem">New</button></li>
    </ul>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'AdminItemList',
  data () {
    return {
      currentPanel: 'Events'
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
      }
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
  .btn-primary {
    font-size: 18px;
    background-color: #009100;
    border-color: #007500;
    margin-top: 3px;
  }
  .navbar-right {
    margin-right: 0px;
  }
</style>
