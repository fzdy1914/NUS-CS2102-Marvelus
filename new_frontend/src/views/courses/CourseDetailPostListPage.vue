<template>
  <div>
    <div style="font-size: 20px; text-align: left;margin-left: 15px; font-weight: bold;">This is all Posts in Forum {{$route.params.fid}}</div>
    <BasicPostList style="font-size: 20px; text-align: left;margin-left: 15px;margin-right: 15px;" :posts="posts"/>
  </div>
</template>

<script>
import BasicPostList from "../../components/lists/BasicPostList";

export default {
  name: "CourseDetailPostListPage",
  components: {
    BasicPostList
  },
  data() {
    return {
      state: false,
      msg: 'Network Error',
      posts: null,
    }
  },
  mounted() {
    this.getPosts()
  },
  methods: {
    getPosts: function () {
      this.$axios.request({
        url: this.$url + 'posts/' + this.$route.params.code + '/' + this.$route.params.fid + '/',
        method: 'GET'
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.state = true
          this.posts = data.data.posts
        } else {
          this.state = false
          this.msg = data.error
        }
      })
    }
  }
}
</script>

<style scoped>

</style>