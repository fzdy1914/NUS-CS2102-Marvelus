<template>
  <div style="font-size: 20px; text-align: left;margin-left: 15px;margin-right: 15px;">
    <table class="table table-bordered table-hover" :sticky-header=true>
      <thead>
        <tr v-if="isGradeMode">
          <th colspan="4">
            <template v-if="isEditMode">
              Editing grades
              <Button style="margin-left: 5px; margin-right: 5px;" class="p-button-warning" label="Generate Attendance Grade" @click="generateAttendanceGrade()"/>
              <Button style="margin-left: 5px; margin-right: 5px;" class="p-button-warning" label="Generate Final Grade" @click="generateFinalGrade()"/>
              <Button style="float: right;" class="p-button-warning" label="Finish" @click="toggleEditMode()"/>
            </template>
            <template v-else>
              Viewing grades
              <Button style="float: right;" class="p-button-warning" label="Edit" @click="toggleEditMode()"/>
            </template>
          </th>
        </tr>
        <tr v-else>
          <th colspan="4">
              Viewing basic info
          </th>
        </tr>
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
            <template v-if="isEditMode">
              <td class="attendance_grade" v-if="student.attendance_grade">{{student.attendance_grade}}</td>
              <td class="attendance_grade" v-else>NA</td>
              <td class="test_grade"><GradeEditBox :student=student /></td>
              <td class="final_grade" v-if="student.final_grade">{{student.final_grade}}</td>
              <td class="final_grade" v-else>NA</td>
            </template>
            <template v-else>
              <td class="attendance_grade" v-if="student.attendance_grade">{{student.attendance_grade}}</td>
              <td class="attendance_grade" v-else>NA</td>
              <td class="test_grade" v-if="student.test_grade">{{student.test_grade}}</td>
              <td class="test_grade" v-else>NA</td>
              <td class="final_grade" v-if="student.final_grade">{{student.final_grade}}</td>
              <td class="final_grade" v-else>NA</td>
            </template>
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
import Button from 'primevue/button';
import GradeEditBox from "../GradeEditBox";
export default {
  name: 'StudentListGradeMode',
  components:{
    Button,
    GradeEditBox
  },
  data() {
    return {
      isEditMode: false,
      display: true
    }
  },
  props: {
    students: Array,
    isProf: Boolean,
    isSelectTutor: Boolean,
    isGradeMode: Boolean
  },
  methods: {
    toggleEditMode: function () {
      this.isEditMode = !this.isEditMode
    },
    generateAttendanceGrade: function () {

    },
    generateFinalGrade: function () {

    }
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
