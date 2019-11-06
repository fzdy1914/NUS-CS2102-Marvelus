<template>
  <div>
    <div v-if="forums.length > 0">
      <div class="title-font" style="margin-bottom: 20px">
        This is all Forums:
        <Button v-if="selectedForum" style="float: right; margin-right: 15px" label="View" @click="goPostList(selectedForum.fid)"/>
        <Button v-if="selectedForum && status=='Prof'" class="p-button-danger" style="float: right; margin-right: 5px" label="Delete" @click="deleteForum(selectedForum.fid)"/>
      </div>
      <DataTable :value="forums" sortMode="multiple" :selection.sync="selectedForum" dataKey="fid" style="margin-top: 12px">
        <Column selectionMode="single" headerStyle="width: 3em"></Column>
        <Column field="fid" header="Forum Number"></Column>
        <Column field="title" header="Forum Title"></Column>
      </DataTable>
    </div>
    <div v-else>
      <div class="title-font">You cannot view any forums :(</div>
    </div>
  </div>
</template>

<script>
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import Button from 'primevue/button';

export default {
  name: "ForumListPage",
  components: {
    DataTable,
    Column,
    Button,
  },
  props: {
    forums: Array
  },
  data() {
    return {
      selectedForum: null,
    }
  },
  methods: {
    goPostList: function (fid) {
      if (this.status == 'Prof') {
        this.$router.push({name: 'TeachDetailPostList', params: {code: this.$route.params.code, fid: fid}})
      } else if (this.status == 'TA') {
        this.$router.push({name: 'AssistDetailPostList', params: {code: this.$route.params.code, fid: fid}})
      } else {
        this.$router.push({name: 'CourseDetailPostList', params: {code: this.$route.params.code, fid: fid}})
      }
    },
    deleteForum: function (fid) {
      this.$axios.request({
        url: this.$url + 'forum/delete/' + this.$route.params.code + '/' + fid + '/',
        method: 'GET'
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.state = true
          this.$emit('update')
        } else {
          this.state = false
          this.msg = data.error
        }
      })
    }
  },
  computed: {
    status: function () {
      if (this.$route.name.startsWith('Teach')) {
        return 'Prof'
      } else if (this.$route.name.startsWith('Assist')) {
        return 'TA'
      }
      return 'Student'
    }
  }
}
</script>

<style scoped>

</style>