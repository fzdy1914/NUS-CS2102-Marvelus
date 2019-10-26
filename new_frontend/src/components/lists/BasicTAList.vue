<template>
  <div>
    <table class="table table-bordered table-hover">
      <thead>
        <tr>
          <th>Name</th>
          <th>Major</th>
          <th>Email</th>
          <th v-if="isProf">Operation</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="TA in TAs" :key="TA.uname">
          <td class="name">{{ TA.name }}</td>
          <td class="major">{{ TA.major }}</td>
          <td class="email">{{ TA.email }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'BasicTAList',
  props: {
    TAs: Array,
    isProf: Boolean
  },
  methods: {
  }
}
</script>

<style scoped>
  .name, .major {
    width: 150px;
  }
  .email {
    width: 350px;
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
