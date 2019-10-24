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
        <tr v-for="student in students" :key="student.uname">
          <td class="name">{{ student.name }}</td>
          <td class="major">{{ student.major }}</td>
          <td class="email">{{ student.email }}</td>
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
  name: 'BasicStudentList',
  props: {
    students: Array,
    isProf: Boolean,
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
