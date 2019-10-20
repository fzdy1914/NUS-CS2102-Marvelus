<template>
  <div>
    <nav class="navbar navbar-default">
      <!-- Collect the nav links, forms, and other content for toggling -->
      <ul class="nav navbar-nav navbar-left">
        <li v-if="$store.state.isProf" :class="{ active: whichActive === 'courses' }" @click="goTeach()">
          <a>My Teaching Modules</a>
        </li>
        <li v-else :class="{ active: whichActive === 'courses' }" @click="goCourses()"><a>My Modules</a></li>
        <li :class="{ active: whichActive === 'search' }" @click="goSearch()"><a>Module Search</a></li>
        <li v-if="$store.state.isTA" :class="{ active: whichActive === 'assists' }" @click="goAssists()">
          <a>My Assisting Modules</a>
        </li>
      </ul>
    </nav>
  </div>
</template>

<script>
export default {
  name: 'NavBar',
  props: {
    whichActive:String
  },
  data () {
    return {
    }
  },
  methods: {
    goTeach: function () {
      if (this.$route.name != 'TeachList') {
        this.$router.push({name: 'TeachList'})
      }
    },
    goCourses: function () {
      if (this.$route.name != 'CourseList') {
        this.$router.push({name: 'CourseList'})
      }
    },
    goSearch: function () {
      if (this.$route.name != 'CourseSearch') {
        this.$router.push({name: 'CourseSearch'})
      }
    },
    goAssists: function () {
      if (this.$route.name != 'AssistList') {
        this.$router.push({name: 'AssistList'})
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
</style>
