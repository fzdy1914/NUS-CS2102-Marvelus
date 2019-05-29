<template>
  <div>
    <nav class="navbar navbar-default">
      <!-- Collect the nav links, forms, and other content for toggling -->
      <div class="collapse navbar-collapse">
        <ul class="nav navbar-nav navbar-left">
          <li :class="{ active: true }"><a>Events</a></li>
        </ul>
      </div><!-- /.navbar-collapse -->
    </nav>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'AdminItemList',
  data () {
    return {
    }
  },
  mounted () {
  },
  methods: {
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
