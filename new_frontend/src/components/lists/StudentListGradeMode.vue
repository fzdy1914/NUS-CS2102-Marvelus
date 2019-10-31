<template>
  <div style="font-size: 20px; text-align: left;margin-left: 15px;margin-right: 15px;">
    <table class="table table-bordered table-hover" :sticky-header=true>
      <thead>
        <tr>
          <th>Name</th>
          <template v-if="isGradeMode">
            <th>Attendance Grade</th>
            <th>Test Grade</th>
            <th>Final Grade</th>
          </template>
          <template v-else>
            <th>Major</th>
            <th>Year</th>
            <th>Email</th>
          </template>
          <th v-if="isSelectTutor">Group Number</th>
          <th v-if="isProf">Operation</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="student in students" :key="student.uname">
          <td class="name">{{ student.name }}</td>
          <template v-if="isGradeMode">
            <td class="attendance_grade" v-if="student.attendance_grade">{{student.attendance_grade}}</td>
            <td class="attendance_grade" v-else>NA</td>
            <td class="test_grade" v-if="student.test_grade">{{student.test_grade}}</td>
            <td class="test_grade" v-else>NA</td>
            <td class="final_grade" v-if="student.final_grade">{{student.final_grade}}</td>
            <td class="final_grade" v-else>NA</td>
          </template>
          <template v-else>
            <td class="major">{{ student.major }}</td>
            <td class="year">{{ student.year }}</td>
            <td class="email">{{ student.email }}</td>
          </template>
          <td class="grpNum" v-if="isSelectTutor">{{ student.group_num }}</td>
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
  name: 'StudentListGradeMode',
  props: {
    students: Array,
    isProf: Boolean,
    isSelectTutor: Boolean,
    isGradeMode: Boolean
  },
  methods: {

  }
}
</script>

<style scoped>
  .name, .major, .year {
    width: 150px;
  }
  .email {
    width: 350px;
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
