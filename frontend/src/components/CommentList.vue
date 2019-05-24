<template>
  <div>
    <div v-if="state">
      <h3>Comment List:</h3>
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
      currentPage: 1
    }
  },
  mounted () {
    let parse = this.$util.parse
    this.startPage = parse(this.$route.query.startPage) || 1
    this.currentPage = parse(this.$route.query.currentPage) || 1
    this.offset = parse(this.$route.query.offset)
    this.updateList(this.offset, this.limit)
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
    updateList: function (offset, limit) {
      this.$axios.request({
        url: this.$url + 'comments/' + this.eventId + '/',
        method: 'GET',
        params: {
          'offset': offset,
          'limit': limit
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
    },
    'offset' (to, from) {
      this.updateList(to, this.limit)
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

<style>
  .title {
    width: 300px;
  }
  .content{
    width: 700px;
  }
  .username {
    width: 100px;
  }
</style>
