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
                <h4 class="modal-title">
                  Add your comment
                </h4>
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
      <nav>
        <ul class="pagination">
          <li v-bind:class="{ disabled: startPage === 1 }">
            <a @click="startPage=prevPage"><span>&laquo;</span></a>
          </li>
          <li v-for="index in indexArray" :key="index" :class="{ active: index === currentPage}">
            <a @click="goPage(index)">{{ index }}</a>
          </li>
          <li v-bind:class="{ disabled: endPage === maxPage }">
            <a @click="startPage=nextPage"><span>&raquo;</span></a>
          </li>
        </ul>
      </nav>
    </div>
    <div v-else>
      <h3>{{ msg }}</h3>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CommentList',
  props: {
    eventId: Number
  },
  data () {
    return {
      msg: 'Network Error',
      comments: null,
      state: false,

      offset: 0,
      limit: 5,
      startPage: 1,
      currentPage: 1,

      commentTitle: '',
      commentContent: ''
    }
  },
  mounted () {
    let parse = this.$util.parse
    this.startPage = parse(this.$route.query.startPage) || 1
    this.currentPage = parse(this.$route.query.currentPage) || 1
    this.offset = parse(this.$route.query.offset)
    this.updateCommentList()
  },
  methods: {
    goPage: function (index) {
      this.$router.push({
        name: 'Event',
        params: {
          eventId: this.eventId
        },
        query: {
          offset: (index - 1) * this.limit,
          limit: this.limit,
          currentPage: index,
          startPage: this.startPage
        }
      })
      this.currentPage = index
    },
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
          this.state = true
          this.startPage = 1
          this.goPage(1)
          this.comments.unshift(data.data.comment)
          this.comments.splice(this.limit, 1)
          this.commentTitle = ''
          this.commentContent = ''
          document.getElementById('close').click()
        } else {
          this.state = false
        }
      })
    }
  },
  watch: {
    '$route' (to, from) {
      let parse = this.$util.parse
      this.offset = parse(to.query.offset)
      if (to.query.startPage) {
        this.startPage = parse(to.query.startPage)
      }
      if (to.query.currentPage) {
        this.currentPage = parse(to.query.currentPage)
      }
      this.updateCommentList()
    }
  },
  computed: {
    maxPage: function () {
      return Math.ceil(this.count / this.limit)
    },
    endPage: function () {
      return this.startPage + 9 < this.maxPage ? this.startPage + 9 : this.maxPage
    },
    prevPage: function () {
      return this.startPage - 10 < 1 ? 1 : this.startPage - 10
    },
    nextPage: function () {
      return this.endPage === this.maxPage ? this.startPage : this.endPage + 1
    },
    indexArray: function () {
      return this.$util.generateArray(this.startPage, this.endPage)
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
