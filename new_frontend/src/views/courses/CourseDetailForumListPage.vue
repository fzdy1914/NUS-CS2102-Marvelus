<template>
  <div>
    <div style="font-size: 20px; text-align: left;margin-left: 15px; font-weight: bold;">This is all Forums</div>
    <BasicForumList style="font-size: 20px; text-align: left;margin-left: 15px;margin-right: 15px;" :forums="forums" v-on:goPostList="goPostList"/>
  </div>
</template>

<script>
import BasicForumList from "../../components/lists/BasicForumList";

export default {
  name: "CourseDetailForumListPage",
  components: {
    BasicForumList
  },
  props: {
    forums: Array
  },
  methods: {
    goPostList: function (fid) {
      this.$router.push({name: 'CourseDetailPostList', params: {code: this.$route.params.code, fid: fid}})
    }
  }
}
</script>

<style scoped>

</style>