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
  name: "ForumDetailPage",
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
    },
    status: function () {
      if (this.$route.name.startsWith('Teach')) {
        return 'Prof'
      } else if (this.$route.name.startsWith('Assist')) {
        return 'TA'
      }
      return 'Student'
    }
  },
  methods: {
    goBack: function () {
      let address
      if (this.status == 'Prof') {
        address = "Teach"
      } else if (this.status == 'TA') {
        address = "Assist"
      } else {
        address = "Course"
      }
      if (this.$route.name.indexOf('PostDetail') >= 0) {
        this.$router.push({
        name: address + 'DetailPostList', params: {code: this.$route.params.code, fid: this.$route.params.fid}})
      } else {
        this.$router.push({name: address + 'DetailForumList', params: {code: this.$route.params.code}})
      }
    },
  }
}
</script>

<style scoped>

</style>