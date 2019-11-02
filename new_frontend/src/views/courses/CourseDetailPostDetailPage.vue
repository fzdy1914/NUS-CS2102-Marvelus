<template>
  <div>
    <Button label = "Back" @click="goBack()"/>
    <div>
      <div style="font-size: 20px; text-align: left;margin-left: 15px; font-weight: bold;">This is the post</div>
      <div>{{ post.title }}</div>
      <div>{{ post.content }}</div>
    </div>

    <div style="font-size: 20px; text-align: left;margin-left: 15px; font-weight: bold;">This is the replies</div>
    <div v-for="reply in replies" :key="reply.pid">
      <div>{{ reply.title }}</div>
      <div>{{ reply.content }}</div>
    </div>

  </div>
</template>

<script>
import Button from 'primevue/button';
export default {
  name: "CourseDetailPostListPage",
  components:{
    Button
  },
  data() {
    return {
      state: false,
      msg: 'Network Error',
      post: null,
      replies: null
    }
  },
  mounted() {
    this.getPostAndReplies()
  },
  methods: {
    getPostAndReplies: function () {
      this.$axios.request({
        url: this.$url + 'posts/' +
          this.$route.params.code + '/' + this.$route.params.fid + '/' + this.$route.params.pid + '/',
        method: 'GET'
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.state = true
          this.post = data.data.post
          this.replies = data.data.replies
        } else {
          this.state = false
          this.msg = data.error
        }
      })
    },
    goBack: function () {
      this.$router.push({
        name: 'CourseDetailPostList', params: {code: this.$route.params.code, fid: this.$route.params.fid}})
    }
  }
}
</script>

<style scoped>

</style>