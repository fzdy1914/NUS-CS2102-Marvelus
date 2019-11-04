<template>
  <div>
    <TabView class="p-tabview">
      <!--<TabPanel header="All students">-->
        <!--<div style="font-size: 20px; text-align: left;margin-left: 15px; font-weight: bold;">Students completed or enrolled in this module:</div>-->
        <!--<BasicStudentList :students="students"/>-->
      <!--</TabPanel>-->
      <TabPanel header="Enrolled students">
        <div style="font-size: 20px; text-align: left;margin-left: 15px; font-weight: bold;">Students enrolled in this module:</div>
        <StudentListDataTable :peoples="studentsEnrolled" />
      </TabPanel>
      <TabPanel header="Completed students">
        <div style="font-size: 20px; text-align: left;margin-left: 15px; margin-right: 15px; font-weight: bold;">
          Students completed this module:
          <Button label="Generate final result" @click="calculate()" />
          <Button v-if="isGradeMode" style="float: right" class="p-button-warning" label="View Basic Info" @click="toggleGradeMode()"/>
          <Button v-else style="float: right" class="p-button-warning" label="View/Edit Grades" @click="toggleGradeMode()"/>
        </div>
        <StudentListGradeMode :students="studentsCompleted" :isGradeMode="this.isGradeMode"/>
      </TabPanel>
    </TabView>
  </div>
</template>

<script>
import BasicStudentList from '../../components/lists/BasicStudentList'
import StudentListGradeMode from '../../components/lists/StudentListGradeMode'
import TabView from 'primevue/tabview';
import TabPanel from 'primevue/tabpanel';
import Button from 'primevue/button';
import StudentListDataTable from "../../components/lists/StudentListDataTable";
export default {
  name: "TeachDetailStudentPage",
  components: {
    BasicStudentList,
    StudentListGradeMode,
    TabView,
    TabPanel,
    Button,
    StudentListDataTable
  },
  data() {
    return {
      state: false,
      msg: 'Network Error',
      students: null,
      studentsEnrolled: null,
      studentsCompleted: null,
      isGradeMode: false
    }
  },
  mounted() {
    this.getStudents()
    this.getStudentsEnrolled()
    this.getStudentsCompleted()
  },
  methods: {
    calculate:function(){
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
        url: this.$url + 'students/code/enrolled/' + this.$route.params.code + '/',
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
        url: this.$url + 'students/code/completed/' + this.$route.params.code + '/',
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
    toggleGradeMode: function () {
      this.isGradeMode = !this.isGradeMode
    }
  }
}
</script>

<style scoped>

</style>