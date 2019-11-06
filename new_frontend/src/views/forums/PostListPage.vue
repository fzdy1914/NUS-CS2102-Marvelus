<template>
  <div>
    <div class="title-font" style="margin-top: 20px; margin-bottom: 20px">
      This is all Posts:
      <Button class="p-button-success" style="float: right; margin-right: 15px" label="Post" icon="pi pi-plus" @click="display = true"/>
      <Button v-if="selectedPost" style="float: right; margin-right: 5px" label="View" @click="goPost(selectedPost.pid)"/>
      <Button v-if="selectedPost && status!='Student'" class="p-button-danger" style="float: right; margin-right: 5px" label="Delete" @click="deletePost(selectedPost.pid)"/>
    </div>

    <DataTable :value="posts" sortMode="multiple" :selection.sync="selectedPost" dataKey="pid" style="margin-top: 12px">
      <Column selectionMode="single" headerStyle="width: 3em"></Column>
      <Column field="title" header="Post Title"></Column>
      <Column field="name" header="Author"></Column>
    </DataTable>

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
import Button from 'primevue/button';
import Dialog from 'primevue/dialog'
import InputText from 'primevue/inputtext';
import Textarea from 'primevue/textarea';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';

export default {
  name: "PostListPage",
  components: {
    Button,
    Dialog,
    InputText,
    Textarea,
    DataTable,
    Column,
  },
  data() {
    return {
      state: false,
      msg: 'Network Error',
      posts: null,
      display: false,
      new_title: '',
      new_content:'',
      selectedPost: null,
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
      if (this.status == 'Prof') {
        this.$router.push({name: 'TeachDetailPostDetail', params: {code: this.$route.params.code, fid: this.$route.params.fid, pid: pid}})
      } else if (this.status == 'TA') {
        this.$router.push({name: 'AssistDetailPostDetail', params: {code: this.$route.params.code, fid: this.$route.params.fid, pid: pid}})
      } else {
        this.$router.push({name: 'CourseDetailPostDetail', params: {code: this.$route.params.code, fid: this.$route.params.fid, pid: pid}})
      }
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
    },
    deletePost: function (pid) {
      this.$axios.request({
        url: this.$url + 'post/delete/' + this.$route.params.code + '/' + this.$route.params.fid + '/' + pid + '/',
        method: 'GET'
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.state = true
          this.getPosts()
        } else {
          this.state = false
          this.msg = data.error
        }
      })
    }
  },
  computed: {
    status: function () {
      if (this.$route.name.startsWith('Teach')) {
        return 'Prof'
      } else if (this.$route.name.startsWith('Assist')) {
        return 'TA'
      }
      return 'Student'
    },
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