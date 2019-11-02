<template>
  <div>
    <table class="table table-bordered table-hover">
      <thead>
        <tr>
          <th>ID</th>
          <th>Title</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="forum in forums" :key="forum.fid" @click="clickAction(forum.fid)">
          <td class="group">{{ forum.fid }}</td>
          <td>{{ forum.title }}</td>
          <td class="operation" v-if="canDelete">
            <button class="btn btn-primary delete">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'BasicForumList',
  props: {
    forums: Array,
    canDelete: Boolean
  },
  methods: {
    clickAction: function (fid) {
      this.$emit('goPostList', fid)
    }
  }
}
</script>

<style scoped>
  .group{
    width: 150px;
  }
  .operation {
    width: 200px
  }
  .delete {
    background-color: #D94600;
    border-color: #BB3D00;
  }
  .btn {
    padding: 3px 8px;
  }
</style>
