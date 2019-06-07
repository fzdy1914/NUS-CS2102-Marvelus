<template>
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
</template>

<script>
export default {
  name: 'NavigationBar',
  props: {
    isAdmin: Boolean,
    count: Number
  },
  data () {
    return {
      limit: 15,
      startPage: 1,
      currentPage: 1
    }
  },
  mounted () {
    let parse = this.$util.parse
    this.startPage = parse(this.$route.query.startPage) || 1
    this.currentPage = parse(this.$route.query.currentPage) || 1
    if (this.$route.query.limit) {
      this.limit = parse(this.$route.query.limit)
    }
  },
  methods: {
    goPage: function (index) {
      let query = this.$route.query
      this.$router.push({
        name: this.isAdmin ? 'AdminEventList' : 'EventList',
        query: {
          offset: (index - 1) * this.limit,
          channelId: query.channelId,
          limit: this.limit,
          currentPage: index,
          startPage: this.startPage,
          sinceDate: query.sinceDate,
          untilDate: query.untilDate
        }
      })
    }
  },
  watch: {
    '$route' (to, from) {
      let parse = this.$util.parse
      this.channelId = parse(to.query.channelId)
      if (to.query.startPage) {
        this.startPage = parse(to.query.startPage)
      }
      if (to.query.currentPage) {
        this.currentPage = parse(to.query.currentPage)
      }
      if (to.query.limit) {
        this.limit = parse(to.query.limit)
      }
      this.sinceDate = parse(to.query.sinceDate)
      this.untilDate = parse(to.query.untilDate)
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
