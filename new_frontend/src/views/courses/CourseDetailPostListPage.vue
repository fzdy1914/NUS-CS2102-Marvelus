<template>
  <div>
    <div style="font-size: 20px; text-align: left;margin-left: 15px; font-weight: bold;">This is all Posts in Forum {{$route.params.fid}}</div>\
    <Button label = "Add" @click="display = true" class="p-button-success"/>
    <Button label = "Back" @click="goBack()"/>
    <BasicPostList style="font-size: 20px; text-align: left;margin-left: 15px;margin-right: 15px;" :posts="posts" v-on:goPost="goPost"/>
    <Dialog header="Add New Post" :visible.sync="display" :style="{width: '800px'}" :modal="true">
      <div class="title-group">
        <div class="post-label">Title:</div>
        <InputText v-model="new_title" type="text" class="input"/>
      </div>
      <div class="post-label">Content:</div>
      <Textarea v-model="new_content" :autoResize="true" rows="5" cols="100" class="input"/>
      <template #footer>
        <Button label="Yes" icon="pi pi-check" @click="addPost()" />
        <Button label="No" icon="pi pi-times" @click="display = false" class="p-button-secondary"/>
      </template>
    </Dialog>
  </div>
</template>

<script>
import BasicPostList from "../../components/lists/BasicPostList";
import Button from 'primevue/button';
import Dialog from 'primevue/dialog'
import InputText from 'primevue/inputtext';
import Textarea from 'primevue/textarea';

export default {
  name: "CourseDetailPostListPage",
  components: {
    BasicPostList,
    Button,
    Dialog,
    InputText,
    Textarea
  },
  data() {
    return {
      state: false,
      msg: 'Network Error',
      posts: null,
      display: false,
      new_title: '',
      new_content:''
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
      this.$axios.request({
        url: this.$url + 'post/add/',
        method: 'POST',
        data: {
          title: this.new_title,
          content: this.new_content,
          code: this.$route.params.code,
          fid: this.$route.params.fid
        }
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.error = null
          this.new_title = ''
          this.new_content = ''
          this.display = false
          this.posts.push(data.data.post)
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