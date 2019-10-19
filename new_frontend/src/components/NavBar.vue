<template>
  <div>
    <nav class="navbar navbar-default">
      <!-- Collect the nav links, forms, and other content for toggling -->
      <ul class="nav navbar-nav navbar-left">
        <!--<li :class="{ active: !channelId }"><a @click="goChannel(null)">All</a></li>-->
        <li :class="{ active: whichActive === 'courses' }"><a>My Modules</a></li>
        <li v-if="!$store.state.isProf" :class="{ active: whichActive === 'search' }"><a>Module Search</a></li>
        <li v-if="showAssists" :class="{ active: whichActive === 'assists' }"><a>My Assisting Modules</a></li>
      </ul>
    </nav>
  </div>
</template>

<script>
export default {
  name: 'NavBar',
  props: {
    showAssists: Array,
    whichActive:String
  },
  data () {
    return {
    }
  },
  methods: {
    // goChannel: function (channelId) {
    //   this.$router.push({
    //     name: this.isAdmin ? 'AdminEventList' : 'EventList',
    //     query: {
    //       channelId: channelId,
    //       startPage: 1,
    //       currentPage: 1,
    //       sinceDate: this.sinceDate,
    //       untilDate: this.untilDate
    //     }
    //   })
    // }
  }
}
</script>

<style scoped>
  .nav{
    font-size: 18px;
    background: #FCFCFC
  }
</style>
