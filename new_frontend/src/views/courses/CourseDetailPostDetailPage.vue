<template>
  <div>
    <Button label = "Add" @click="display = true" class="p-button-success"/>
    <Button label = "Back" @click="goBack()"/>
    <div>
      <div style="font-size: 20px; text-align: left;margin-left: 15px; font-weight: bold;">This is the post</div>
      <div>{{ post.title }}</div>
      <div>{{ post.content }}</div>
      <div>{{ post.name }}</div>
    </div>

    <div v-if="this.replies.length > 0">
      <div style="font-size: 20px; text-align: left;margin-left: 15px; font-weight: bold;">This is the replies</div>
      <div v-for="reply in replies" :key="reply.pid">
        <div>{{ reply.title }}</div>
        <div>{{ reply.content }}</div>
        <div>{{ reply.name }}</div>
      </div>
    </div>

    <Dialog header="Add New Reply" :visible.sync="display" :style="{width: '800px'}" :modal="true">
      <div class="title-group">
        <div class="post-label">Title:</div>
        <InputText v-model="reply_title" type="text" class="input"/>
      </div>
      <div class="post-label">Content:</div>
      <Textarea v-model="reply_content" :autoResize="true" rows="5" cols="100" class="input"/>
      <template #footer>
        <Button label="Yes" icon="pi pi-check" @click="addReply()" />
        <Button label="No" icon="pi pi-times" @click="display = false" class="p-button-secondary"/>
      </template>
    </Dialog>
  </div>
</template>

<script>
import Button from 'primevue/button';
import Dialog from 'primevue/dialog'
import InputText from 'primevue/inputtext';
import Textarea from 'primevue/textarea';

export default {
  name: "CourseDetailPostListPage",
  components:{
    Button,
    InputText,
    Textarea,
    Dialog
  },
  data() {
    return {
      state: false,
      msg: 'Network Error',
      post: {title: '', content: ''},
      replies: [],
      display: false,

      reply_title: '',
      reply_content:''
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
    },
    addReply: function () {
      this.$axios.request({
        url: this.$url + 'reply/add/',
        method: 'POST',
        data: {
          title: this.reply_title,
          content: this.reply_content,
          code: this.$route.params.code,
          fid: this.$route.params.fid,
          pid: this.$route.params.pid
        }
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.error = null
          this.reply_title = ''
          this.reply_content = ''
          this.display = false
          this.replies.push(data.data.reply)
        } else {
          this.error = data.error
        }
      })
    }
  }
}
</script>

<style scoped>
.input {
  width: 600px;
}
.post-label {
  width: 70px;
  float: left;
}
.title-group {
  margin-bottom: 10px;
}
</style>