<template>
  <div>
    <TabView class="p-tabview">
      <TabPanel header="Enrolled students">
        <div style="font-size: 20px; text-align: left;margin-left: 15px; font-weight: bold;">Students enrolled in this module:</div>
        <StudentListDataTable :peoples="studentsEnrolled" :is-showing-student="true" />
      </TabPanel>
      <TabPanel header="Completed students">
        <div style="font-size: 20px; text-align: left;margin-left: 15px; margin-right: 15px; font-weight: bold;">
          Students completed this module:
          <Button v-if="isViewingGrades" style="float: right" label="Info" @click="toggleGradeView()"/>
          <Button v-else style="float: right" label="Grades" @click="toggleGradeView()"/>
          <Button style="float: right; margin-right: 4px" label="GenerateFinalGrades" @click="generateFinalGrades()"/>
          <Button v-if="selectedStu" icon="pi pi-plus" style="float: right; margin-right: 4px" label="Edit Test Grade" @click="openEdit()"/>
          <Dialog header="Test Grade" :visible.sync="displayEdit" :modal="true">
             <InputText v-model="testGradeEntered" type="number" style="margin-right: 5px"/>
             <Button icon="pi pi-plus" label="Edit Test Grade" @click="editTestGrade()"/>
          </Dialog>
       </div>
       <DataTable :value="studentsCompleted" :paginator="true" :rows="20" sortMode="multiple" :selection.sync="selectedStu" dataKey="uname" style="margin-top: 12px">
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
      </TabPanel>
    </TabView>
  <Toast/>
  </div>
</template>

<script>
import BasicStudentList from '../../components/lists/BasicStudentList'
import StudentListGradeMode from '../../components/lists/StudentListGradeMode'
import TabView from 'primevue/tabview';
import TabPanel from 'primevue/tabpanel';
import Button from 'primevue/button';
import StudentListDataTable from "../../components/lists/StudentListDataTable";
import DataTable from "primevue/datatable";
import Column from 'primevue/column';
import ColumnGroup from 'primevue/columngroup';
import Toast from 'primevue/toast';
import InputText from "primevue/components/inputtext/InputText";
import Dialog from 'primevue/dialog';
export default {
  name: "TeachDetailStudentPage",
  components: {
    BasicStudentList,
    StudentListGradeMode,
    TabView,
    TabPanel,
    Button,
    StudentListDataTable,
    DataTable,
    Column,
    ColumnGroup,
    Toast,
    InputText,
    Dialog
  },
  data() {
    return {
      state: false,
      msg: 'Network Error',
      students: null,
      studentsEnrolled: null,
      studentsCompleted: null,
      isViewingGrades: true,
      selectedStu: null,
      testGradeEntered: null,
      displayEdit: false
    }
  },
  mounted() {
    this.getStudents()
    this.getStudentsEnrolled()
    this.getStudentsCompleted()
  },
  methods: {
    generateFinalGrades: function(){
      this.$axios.request({
        url: this.$url + 'students/calculate/' + this.$route.params.code + '/'+10+'/'+20+'/'+20+'/'+20+'/'+20+'/'+10+'/',
        method: 'GET'
      }).then(response => {
        let data = response.data
        console.log(data)
        // if (data.state === true) {
        //   this.state = true
        //
        // } else {
        //   this.state = false
        //   this.msg = data.error
        // }
      })
    },
    getStudents: function () {
      this.$axios.request({
        url: this.$url + 'students/code/' + this.$route.params.code + '/',
        method: 'GET'
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.state = true
          this.students = data.data.students
        } else {
          this.state = false
          this.msg = data.error
        }
      })
    },
    getStudentsEnrolled: function () {
      this.$axios.request({
        url: this.$url + 'students/code/status/' + this.$route.params.code + '/enrolled/',
        method: 'GET'
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.state = true
          this.studentsEnrolled = data.data.students
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
    toggleGradeView: function () {
      this.isViewingGrades = !this.isViewingGrades
    },
    editTestGrade: function () {
      this.$axios.request({
        url: this.$url + 'student/uname/code/grade/' + this.selectedStu.uname + '/' + this.$route.params.code + '/' + this.testGradeEntered + "/" ,
        method: 'GET'
      }).then(response => {
        console.log(response)
        let data = response.data
        if (data.state === true) {
          this.state = true
          this.displayEdit = false
          this.$toast.add({severity:'success', summary: 'Success ', detail:'Test grade edited!', life: 3000});
          this.getStudentsCompleted()
        } else {
          this.state = false
          this.msg = data.error
        }
      })
    },
    openEdit: function() {
        this.displayEdit = true
        this.testGradeEntered = this.selectedStu.test_grade
    }
  }
}
</script>

<style scoped>

</style>