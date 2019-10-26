<template>
  <div>
    <table class="table table-bordered table-hover">
      <thead>
        <tr>
          <th>Group</th>
          <th v-if="isProf">Operation</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="tutorial in tutorials" :key="tutorial.group_num">
          <td class="group">{{ tutorial.group_num }}</td>
          <td class="operation" v-if="isProf">
            <button class="btn btn-primary approve">Approve</button>
            <button class="btn btn-primary reject">Reject</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'BasicTutorialList',
  props: {
    tutorials: Array,
    isProf: Boolean
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
  .reject {
    background-color: #D94600;
    border-color: #BB3D00;
  }
  .btn {
    padding: 3px 8px;
  }
</style>
