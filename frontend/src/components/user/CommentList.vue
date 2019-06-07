<template>
  <div>
    <div v-if="state">
      <h3>Comment List:
        <button class="btn btn-primary comment" data-toggle="modal" data-target="#addComment">Add Comment</button>
      </h3>

      <div class="modal fade" id="addComment" tabindex="-1" role="dialog" aria-hidden="true">
        <div class="modal-dialog">
          <div class="modal-content">
              <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal">&times;</button>
                <h4 class="modal-title">Add your comment</h4>
              </div>
              <div class="modal-body">
                <form>
                  <div class="form-group">
                    <label>Title</label>
                    <input type="text" class="form-control" placeholder="Comment title" v-model="commentTitle"/>
                  </div>
                  <div class="form-group">
                    <label>Content</label>
                    <textarea rows="4" type="text" class="form-control" placeholder="Comment content" v-model="commentContent"/>
                  </div>
                  <div v-show="error" class="form-group error">
                    <label>Error: {{ error }}</label>
                  </div>
                </form>
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-default" data-dismiss="modal" id="close">Close</button>
                <button type="button" class="btn btn-primary" @click="submit">Submit</button>
              </div>
            </div>
          </div>
      </div>

      <table class="table table-bordered table-hover">
        <thead>
          <tr>
            <th>Title</th>
            <th>Content</th>
            <th>User</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="comment in comments" :key="comment.id">
            <td class="title">{{ comment.title }}</td>
            <td class="content">{{ comment.content }}</td>
            <td class="username">{{ comment.username }}</td>
          </tr>
        </tbody>
      </table>

      <NavigationBar ref="navBar" :isComment="true" :count="count" :eventId="eventId"/>

    </div>
    <div v-else>
      <h3>{{ msg }}</h3>
    </div>
  </div>
</template>

<script>
import NavigationBar from '../NavigationBar'
export default {
  name: 'CommentList',
  components: {
    NavigationBar
  },
  props: {
    eventId: Number
  },
  data () {
    return {
      msg: 'Network Error',
      count: null,
      comments: null,
      state: false,

      offset: 0,
      limit: 5,

      commentTitle: '',
      commentContent: '',
      error: null
    }
  },
  mounted () {
    let parse = this.$util.parse
    this.offset = parse(this.$route.query.offset)
    if (this.$route.query.limit) {
      this.limit = parse(this.$route.query.limit)
    }
    this.updateCommentList()
  },
  methods: {
    updateCommentList: function () {
      this.$axios.request({
        url: this.$url + 'comments/' + this.eventId + '/',
        method: 'GET',
        params: {
          'offset': this.offset,
          'limit': this.limit
        }
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.state = true
          this.comments = data.data.comments
          this.count = data.data.count
        } else {
          this.state = false
          this.msg = data.error
        }
      })
    },
    submit: function () {
      if (this.commentTitle === '') {
        this.error = 'Empty comment title'
      } else if (this.commentContent === '') {
        this.error = 'Empty comment content'
      } else {
        this.$axios.request({
          url: this.$url + 'comments/' + this.eventId + '/',
          method: 'POST',
          data: {
            title: this.commentTitle,
            content: this.commentContent
          }
        }).then(response => {
          let data = response.data
          if (data.state === true) {
            this.commentTitle = ''
            this.commentContent = ''
            this.error = null
            this.$refs.navBar.goCommentPage(1, 1)
            document.getElementById('close').click()
          } else {
            this.error = data.error
          }
        })
      }
    }
  },
  watch: {
    '$route' (to, from) {
      let parse = this.$util.parse
      this.offset = parse(to.query.offset)
      if (to.query.limit) {
        this.limit = parse(to.query.limit)
      }
      this.updateCommentList()
    }
  }
}
</script>

<style scoped>
  .title {
    width: 300px;
  }
  .content{
    width: 700px;
  }
  .username {
    width: 100px;
  }
  h3 {
    height: 26px;
  }
  .comment {
    margin-bottom: 4px;
  }
  .btn {
    padding: 3px 8px;
  }
</style>
