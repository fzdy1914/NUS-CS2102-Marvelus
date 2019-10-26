<template>
  <div>
    <table class="table table-bordered table-hover">
      <thead>
        <tr>
          <th>Title</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="post in posts" :key="post.pid">
          <td>{{ post.title }}</td>
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
  name: 'BasicPostList',
  props: {
    posts: Array,
    canDelete: Boolean
  },
  methods: {
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
