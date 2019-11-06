<template>
  <div>
    <div>
      <div class="title-font" style="margin-bottom: 10px">
        Post:
      </div>
      <div class="post-card">
        <div class="title"><b>{{ post.title }}</b></div>
        <div class="name">Posted by: {{ post.name }}</div>
        <hr/>
        <div class="content">{{ post.content }}</div>
      </div>
    </div>

    <div>
      <div class="title-font" style="margin-top: 20px; margin-bottom: 20px">
        Replies:
        <Button style="float: right; margin-right: 15px" label = "Add" @click="display = true" class="p-button-success"/>
        <Button v-if="selectedPid && displayDelete" class="p-button-danger" style="float: right; margin-right: 5px" label="Delete" @click="deletePost(selectedPid)"/>
      </div>
      <div v-if="replies.length > 0">
        <div v-for="reply in replies" :key="reply.pid">
          <div class="post-card" style="margin-bottom: 15px" :class="{active: displayDelete && selectedPid == reply.pid, reply: displayDelete}" @click="selectedPid = reply.pid">
            <div class="title"><b>{{ reply.title }}</b></div>
            <div class="name">Posted by: {{ reply.name }}</div>
            <hr/>
            <div class="content">{{ reply.content }}</div>
          </div>
        </div>
      </div>
      <div v-else class="text-font">No Reply Now :(</div>
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
      reply_content:'',
      selectedPid: null,
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
    },
    deletePost: function (pid) {
      this.$axios.request({
        url: this.$url + 'post/delete/' + this.$route.params.code + '/' + this.$route.params.fid + '/' + pid + '/',
        method: 'GET'
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.state = true
          this.getPostAndReplies()
        } else {
          this.state = false
          this.msg = data.error
        }
      })
    }
  },
  computed: {
    displayDelete: function () {
      return this.$route.name.startsWith('Teach') || this.$route.name.startsWith('Assist') || true;
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
.post-card {
  border: #b6b6b6 1px solid;
  margin: 0px 15px;
  padding: 10px;
  text-align:left;
}
.active {
  border: #696969 2px solid;
}
.reply:hover {
  border: #696969 2px solid;
  cursor: pointer;
}
.title {
  font-size: 17px;
}
hr {
  margin: 5px 0px;
  border-color: #b6b6b6;
}
</style>