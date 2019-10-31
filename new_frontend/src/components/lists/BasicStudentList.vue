<template>
  <div>
    <Table class="table table-bordered table-hover" :sticky-header=true>
      <thead>
        <tr>
          <th>Name</th>
          <th>Matriculation number</th>
          <th>Major</th>
          <th>Year</th>
          <th>Email</th>
          <th v-if="isSelectCandidate">Course Final Grade</th>
          <th v-if="isSelectTutor">Group Number</th>
          <th v-if="isProf">Operation</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="student in students" :key="student.uname">
          <td class="name">{{ student.name }}</td>
          <td class="matnum">{{ student.matriculation_num }}</td>
          <td class="major">{{ student.major }}</td>
          <td class="year">{{ student.year }}</td>
          <td class="email">{{ student.email }}</td>
          <td class="email" v-if="isSelectCandidate">{{ student.final_grade }}</td>
          <td class="grpNum" v-if="isSelectTutor">{{ student.group_num }}</td>
          <td class="operation" v-if="isProf">
            <button class="btn btn-primary approve">Approve</button>
            <button class="btn btn-primary reject">Reject</button>
          </td>
        </tr>
      </tbody>
    </Table>
  </div>
</template>

<script>
export default {
  name: 'BasicStudentList',
  props: {
    students: Array,
    isProf: Boolean,
    isSelectTutor: Boolean,
    isSelectCandidate: Boolean
  },
  methods: {

  }
}
</script>

<style scoped>
  .name, .major, .year {
    width: 150px;
  }
  .email,.matnum {
    width: 300px;
  }
  .operation {
    width: 200px;
  }
  .grpNum {
    width: 150px;
  }
  .reject {
    background-color: #D94600;
    border-color: #BB3D00;
  }
  .btn {
    padding: 3px 8px;
  }
</style>
