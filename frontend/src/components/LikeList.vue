<template>
  <div>
    <div v-if="state">
      <h3>{{ count }} Likes:
        <button v-if="!hasLiked" class="btn btn-primary like" @click="like">Like</button>
        <button v-else class="btn btn-primary unlike" @click="unlike">Unlike</button>
      </h3>
      <ul class="list-inline">
        <li v-for="like in displayLikes" :key="like.user_id">{{ like.username }},</li>
        <li><a @click="showMore = !showMore">{{ showMore ? 'show less' : 'show more' }}</a></li>
      </ul>
    </div>
    <div v-else>
      <h3>{{ msg }}</h3>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LikeList',
  props: {
    eventId: Number
  },
  data () {
    return {
      msg: 'Network Error',
      likes: null,
      state: false,

      showMore: false
    }
  },
  mounted () {
    this.updateList()
  },
  methods: {
    updateList: function () {
      this.$axios.request({
        url: this.$url + 'likes/' + this.eventId + '/',
        method: 'GET',
        params: {
          'limit': 50
        }
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.state = true
          this.likes = data.data.likes
          this.count = data.data.count
        } else {
          this.state = false
          this.msg = data.error
        }
      })
    },
    like: function () {
      this.$axios.request({
        url: this.$url + 'likes/' + this.eventId + '/',
        method: 'POST'
      }).then(response => {
        let data = response.data
        if (data.state === true && data.data.like.username === this.$store.state.username) {
          this.state = true
          this.likes.unshift(data.data.like)
          this.count++
        } else {
          this.state = false
        }
      })
    },
    unlike: function () {
      this.$axios.request({
        url: this.$url + 'likes/' + this.eventId + '/',
        method: 'DELETE'
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          if (this.hasLiked) {
            for (let i = 0; i < this.likes.length; i++) {
              if (this.likes[i].username === this.$store.state.username) {
                this.likes.splice(i, 1)
              }
            }
            this.count--
          }
        } else {
          this.state = false
        }
      })
    }
  },
  computed: {
    displayLikes: function () {
      return this.showMore ? this.likes : this.likes.slice(0, 10)
    },
    hasLiked: function () {
      for (let i = 0; i < this.likes.length; i++) {
        if (this.likes[i].username === this.$store.state.username) {
          return true
        }
      }
      return false
    }
  }
}
</script>

<style scoped>
  h3 {
    height: 26px;
  }
  .btn {
    padding: 3px 8px;
    margin-bottom: 4px;
  }
  .like {
    background-color: #009100;
    border-color: #007500;
  }
  .unlike {
    background-color: #D94600;
    border-color: #BB3D00;
  }
</style>
