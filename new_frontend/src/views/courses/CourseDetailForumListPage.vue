<template>
  <div>
    <div class="title-font" style="margin-top: 20px; margin-bottom: 20px">
      This is all Forums:
      <Button v-if="selectedForum" style="float: right; margin-right: 15px" label="View" @click="goPostList(selectedForum.fid)"/>
      <Button v-if="selectedForum && displayDelete" class="p-button-danger" style="float: right; margin-right: 5px" label="Delete" @click="deleteForum(selectedForum.fid)"/>
    </div>
    <DataTable :value="forums" sortMode="multiple" :selection.sync="selectedForum" dataKey="fid" style="margin-top: 12px">
      <Column selectionMode="single" headerStyle="width: 3em"></Column>
      <Column field="fid" header="ID"></Column>
      <Column field="title" header="Title"></Column>
    </DataTable>
  </div>
</template>

<script>
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import Button from 'primevue/button';

export default {
  name: "CourseDetailForumListPage",
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
      this.$router.push({name: 'CourseDetailPostList', params: {code: this.$route.params.code, fid: fid}})
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
    displayDelete: function () {
      return this.$route.name.startsWith('Teach') || this.$route.name.startsWith('Assist') || true;
    }
  }
}
</script>

<style scoped>

</style>