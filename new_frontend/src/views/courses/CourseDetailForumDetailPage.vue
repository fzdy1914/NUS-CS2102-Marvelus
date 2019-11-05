<template>
  <div>
    <div class="title-font">Forum Title: </div>
    <div class="text-font">{{displayForum.title}}</div>
    <router-view/>
  </div>
</template>

<script>

export default {
  name: "CourseDetailForumDetailPage",
  props: {
    forums: Array
  },
  computed: {
    displayForum() {
      for (let i in this.forums) {
        if (this.forums[i].fid == this.$route.params.fid) {
          return this.forums[i]
        }
      }
      return {'fid': 0, 'title': 'Not Exist'}
    }
  }
}
</script>

<style scoped>

</style>