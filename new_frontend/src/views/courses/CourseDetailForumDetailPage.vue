<template>
  <div>
    <div style="font-size: 20px; text-align: left;margin-left: 15px; font-weight: bold;">Forum Title: {{displayForum.title}}</div>
    <router-view/>
  </div>
</template>

<script>
import BasicForumList from "../../components/lists/BasicForumList";

export default {
  name: "CourseDetailForumDetailPage",
  components: {
    BasicForumList
  },
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