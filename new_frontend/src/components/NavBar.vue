<template>
  <div class="navbar-h">
    <nav class="navbar navbar-inverse">
      <!-- Collect the nav links, forms, and other content for toggling -->
      <ul class="nav navbar-nav navbar-left ">
        <li class="tab" v-if="$store.state.isProf" :class="{ active: whichActive === 'courses' }" @click="goTeach()">
          <a >My Teaching Modules</a>
        </li>
        <li class="tab" v-else :class="{ active: whichActive === 'courses' }" @click="goCourses()"><a>My Modules</a></li>
        <li class="tab" :class="{ active: whichActive === 'search' }" @click="goSearch()"><a>Module Search</a></li>
        <li class="tab" v-if="$store.state.isTA" :class="{ active: whichActive === 'assists' }" @click="goAssists()">
          <a>My Assisting Modules</a>
        </li>
      </ul>
    </nav>
  </div>

</template>

<script>
  import TabView from 'primevue/tabview';
import TabPanel from 'primevue/tabpanel';
export default {
  name: 'NavBar',
  props: {
    whichActive:String
  },components:{
    TabView,
    TabPanel,
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
  .tab{
    border-radius: 10px;
  }
  .navbar-h{
    background-color: #1976d2;
  }
  .navbar-left{
    font-size: 18px;
    font-weight: bold;
    background:  #1e88e5;
  }
  .navbar-inverse {
    border: #1565c0;
    background-color:#1565c0;

  }
  .navbar-inverse .navbar-nav > .active > a,
  .navbar-inverse .navbar-nav > .active > a:hover,
  .navbar-inverse .navbar-nav > .active > a:focus {
    color: #1976d2;
    background-color: white;
  }
  .navbar-inverse .navbar-nav > li > a {
    color: white;
  }
  .navbar-inverse .navbar-nav > li > a:hover {
    color: lightblue;
  }
</style>
