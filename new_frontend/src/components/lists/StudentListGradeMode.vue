<template>
  <div>
    <div style="font-size: 20px; text-align: left;margin-left: 15px; margin-right: 15px; font-weight: bold;">
      Students completed this module:
      <Button v-if="isViewingGrades" style="float: right" label="View Basic Info" @click="toggleGradeView()"/>
      <Button v-else style="float: right" label="View Grades" @click="toggleGradeView()"/>
      <Button v-if="selectedStu" icon="pi pi-plus" style="float: right; margin-right: 5px" label="Edit Test Grade" @click="editTestGrade()"/>
    </div>
    <DataTable :value="students" :paginator="true" :rows="20" sortMode="multiple" :selection.sync="selectedStu" dataKey="uname">
      <Column selectionMode="single" headerStyle="width: 3em"></Column>
      <Column field="name" header="Student Name"></Column>
      <template v-if="isViewingGrades">
        <Column field="attendance_grade" header="Attendance grade"></Column>
        <Column field="test_grade" header="Test grade"></Column>
        <Column field="final_grade" header="Final grade"></Column>
        <Column field="enroll_year" header="Enroll Year"></Column>
      </template>
      <template v-else>
        <Column field="matriculation_num" header="Matriculation number"></Column>
        <Column field="major" header="Major"></Column>
        <Column field="year" header="Year"></Column>
        <Column field="enroll_year" header="Enroll Year"></Column>
        <Column field="email" header="Email"></Column>
      </template>
    </DataTable>
  </div>
</template>

<script>
import Button from 'primevue/button';
import GradeEditBox from "../GradeEditBox";
import DataTable from "primevue/datatable";
import Column from 'primevue/column';
import ColumnGroup from 'primevue/columngroup';
export default {
  name: 'StudentListGradeMode',
  components:{
    Button,
    GradeEditBox,
    DataTable,
    Column,
    ColumnGroup,
  },
  data() {
    return {
      display: true,
      selectedStu: null,
      isViewingGrades: true
    }
  },
  props: {
    students: Array,
    isProf: Boolean,
    isSelectTutor: Boolean,
    isSelectCandidate: Boolean
  },
  methods: {
    generateFinalGrade: function () {

    },
    toggleGradeView: function () {
      this.isViewingGrades = !this.isViewingGrades
    },
    editTestGrade: function () {
      this.$axios.request({
        url: this.$url + 'student/uname/code/grade/' + this.selectedStu.uname + '/' + this.$route.params.code + '/' + "3.3" + "/" ,
        method: 'GET'
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.state = true
          this.$toast.add({severity:'success', summary: 'Success ', detail:'Attendance added in!', life: 3000});
          this.getStudentsCompleted();
        } else {
          this.state = false
          this.msg = data.error
        }
      })
    },
    getStudentsCompleted: function () {
      this.$axios.request({
        url: this.$url + 'students/code/status/' + this.$route.params.code + '/completed/',
        method: 'GET'
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.state = true
          this.studentsCompleted = data.data.students
        } else {
          this.state = false
          this.msg = data.error
        }
      })
    },
  }
}
</script>

<style scoped>

</style>
