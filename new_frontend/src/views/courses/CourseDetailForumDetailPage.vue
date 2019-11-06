<template>
  <div>
    <div style="text-align: left; margin-bottom: 15px;">
      <Button class="p-button-raised" icon="pi pi-arrow-left" label ="Back"  @click="goBack()" style="margin-left: 15px;"/>
    </div>
    <div class="title-font">Forum Title: </div>
    <div class="text-font">{{displayForum.title}}</div>
    <router-view/>
  </div>
</template>

<script>
import Button from 'primevue/button'

export default {
  name: "CourseDetailForumDetailPage",
  props: {
    forums: Array
  },
  components: {
    Button
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
  },
  methods: {
    goBack: function () {
      if (this.$route.name.indexOf('PostDetail') >= 0) {
        this.$router.push({
        name: 'CourseDetailPostList', params: {code: this.$route.params.code, fid: this.$route.params.fid}})
      } else {
        this.$router.push({name: 'CourseDetailForumList', params: {code: this.$route.params.code}})
      }
    },
  }
}
</script>

<style scoped>

</style>