<template>
  <div>
    <div style="font-size: 20px; text-align: left;margin-left: 15px; font-weight: bold;">This is all Posts in Forum {{$route.params.fid}}</div>\
    <Button label = "Add" @click="addPost()"/>
    <Button label = "Back" @click="goBack()"/>
    <BasicPostList style="font-size: 20px; text-align: left;margin-left: 15px;margin-right: 15px;" :posts="posts" v-on:goPost="goPost"/>
  </div>
</template>

<script>
import BasicPostList from "../../components/lists/BasicPostList";
import Button from 'primevue/button';

export default {
  name: "CourseDetailPostListPage",
  components: {
    BasicPostList,
    Button
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
    },
    goPost: function (pid) {
      this.$router.push({
        name: 'CourseDetailPostDetail',
        params: {code: this.$route.params.code, fid: this.$route.params.fid, pid: pid}})
    },
    goBack: function () {
      this.$router.push({
        name: 'CourseDetailForumList', params: {code: this.$route.params.code}})
    },
    addPost: function () {
      this.$router.push({
        name: 'CourseDetailForumList', params: {code: this.$route.params.code}})
    }

  }
}
</script>

<style scoped>

</style>