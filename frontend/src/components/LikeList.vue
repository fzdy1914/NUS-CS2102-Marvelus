<template>
  <div>
    <div v-if="state">
      <h3>{{ count }} Likes:</h3>
      <ul class="list-inline">
        <li v-for="like in displayLikes" :key="like.user_id">{{ like.username }}</li>
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
    }
  },
  computed: {
    displayLikes: function () {
      return this.showMore ? this.likes : this.likes.slice(0, 10)
    }
  }
}
</script>
