<template>
  <div>
    <ul class="nav nav-tabs">
      <li :class="{ active: currentPanel === 'Channels' }"><a @click="goChannels">Channels</a></li>
      <li :class="{ active: currentPanel === 'Events' }"><a @click="goEvents">Events</a></li>
      <li><a href="#">Comments</a></li>
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
  .navbar-collapse {
    padding-left: 0px;
  }
</style>
