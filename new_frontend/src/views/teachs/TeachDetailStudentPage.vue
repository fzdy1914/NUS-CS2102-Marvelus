<template>
  <div>
    <TabView class="p-tabview">
      <TabPanel header="Enrolled students">
        <div class="title-font">
          Students enrolled in this module:
          <Button v-if="selectedEnrollStu" style="float: right; margin-right: 15px" label="Mark As Completed" @click="markCompleted(selectedEnrollStu.uname)"/>
        </div>
        <DataTable :value="studentsEnrolled" :selection.sync="selectedEnrollStu" sortMode="multiple" style="margin-top: 12px">
          <Column selectionMode="single" headerStyle="width: 3em"></Column>
          <Column field="name" header="Student Name"></Column>
          <Column field="matriculation_num" header="Matriculation number"></Column>
          <Column field="major" header="Major"></Column>
          <Column field="year" header="Year" :sortable="true"></Column>
          <Column field="email" header="Email"></Column>
        </DataTable>
      </TabPanel>
      <TabPanel header="Completed students">
        <div class="title-font">
          Students completed this module:
          <Button v-if="isViewingGrades" style="float: right; margin-right: 15px" label="Info" @click="toggleGradeView()"/>
          <Button v-else style="float: right; margin-right: 15px" label="Grades" @click="toggleGradeView()"/>
          <Button style="float: right; margin-right: 4px" label="GenerateFinalGrades" @click="openGrading()"/>
          <Button v-if="selectedStu" icon="pi pi-plus" style="float: right; margin-right: 4px" label="Edit Test Grade" @click="openEdit()"/>
          <Dialog header="Test Grade" :visible.sync="displayEdit" :modal="true">
             <InputText v-model="testGradeEntered" type="number" style="margin-right: 5px"/>
             <Button icon="pi pi-plus" label="Edit Test Grade" @click="editTestGrade()"/>
          </Dialog>
          <Dialog header="Generate Final Grade" :visible.sync="displayBellCurve" :style="{width: '80vw'}" :modal="true" >
            <div class="text-font">
              Enter bell curve percentage to generate final grade for all students completed in current year:
              (All grades percentage must add up to 1. Use 0 if you do not wish to have that grade)</div>
            <div class="p-grid" style="margin:20px;">
              <div class="p-col " >
                <span style="width: 200px">
                  <label for="a">A:   </label>
                  <InputText id="a" type="number" min="0" v-model="a" style="width: 100px" />%
                 </span>
              </div>
              <div class="p-col">
                <span  style="width: 100px" >
                  <label for="b">B: </label>
                  <InputText id="b" type="number" min="0" v-model="b" style="width: 100px" />%
               </span>
              </div>
              <div class="p-col">
                 <span  style="width: 100px" >
                    <label for="c">C: </label>
                    <InputText id="c" type="number" min="0" v-model="c" style="width: 100px" />%
                  </span>
              </div>
            </div>
            <div class="p-grid" style="margin:20px;">
                <div class="p-col " >
                  <span style="width: 200px">
                    <label for="d">D:   </label>
                    <InputText id="d" type="number" min="0" v-model="d" style="width: 100px" />%
                   </span>
                </div>
                <div class="p-col">
                  <span  style="width: 100px" >
                    <label for="e">E: </label>
                    <InputText id="e" type="number" min="0" v-model="e" style="width: 100px" />%
                 </span>
                </div>
                <div class="p-col">
                   <span  style="width: 100px" >
                      <label for="f">F: </label>
                      <InputText id="f" type="number" min="0" v-model="f" style="width: 100px" />%
                    </span>
                </div>
              </div>
            <template #footer>
                <Button label="Generate Final Grades" icon="pi pi-check" @click="generateFinalGrades()" />
                <Button label="Back" icon="pi pi-times" @click="closeGrading()" class="p-button-secondary"/>
            </template>
          </Dialog>
        </div>
        <DataTable :value="studentsCompleted" sortMode="multiple" :selection.sync="selectedStu" dataKey="uname" style="margin-top: 12px">
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
import TabView from 'primevue/tabview';
import TabPanel from 'primevue/tabpanel';
import Button from 'primevue/button';
import DataTable from "primevue/datatable";
import Column from 'primevue/column';
import Toast from 'primevue/toast';
import InputText from "primevue/components/inputtext/InputText";
import Dialog from 'primevue/dialog';

export default {
  name: "TeachDetailStudentPage",
  components: {
    TabView,
    TabPanel,
    Button,
    DataTable,
    Column,
    Toast,
    InputText,
    Dialog
  },
  data() {
    return {
      state: false,
      msg: 'Network Error',
      studentsEnrolled: null,
      studentsCompleted: null,
      isViewingGrades: true,
      selectedEnrollStu: null,
      selectedStu: null,
      testGradeEntered: null,
      displayEdit: false,
      displayBellCurve:false,
      a:null,
      b:null,
      c:null,
      d:null,
      e:null,
      f:null
    }
  },
  mounted() {
    this.getStudentsEnrolled()
    this.getStudentsCompleted()
  },
  methods: {
    closeGrading:function(){
      this.displayBellCurve=false;
    },
    openGrading: function(){
      this.displayBellCurve =true;
      this.a = null;
      this.b = null;
      this.c = null;
      this.d = null;
      this.e = null;
      this.f = null;
    },
    generateFinalGrades: function(){
      this.$axios.request({
        url: this.$url + 'students/calculate/' + this.$route.params.code + '/'+this.a+'/'+this.b+'/'+this.c+'/'+this.d+'/'+this.e+'/'+this.f+'/',
        method: 'GET'
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.state = true
          this.studentsCompleted = data.data.students
          this.$toast.add({severity:'success', summary: 'Success ', detail:'Final grade generated!', life: 3000});
          this.displayBellCurve = false;
        } else {
          this.state = false
          this.msg = data.error
          this.$toast.add({severity:'error', summary: 'Error Message ', detail:this.msg, life: 3000});
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
    },
    markCompleted: function (uname) {
      this.$axios.request({
        url: this.$url + 'students/code/complete/' + this.$route.params.code + '/' + uname + '/',
        method: 'GET'
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.state = true
          this.getStudentsEnrolled()
          this.getStudentsCompleted()
          this.$toast.add({severity:'success', summary: 'Success ', detail:'Student Marked As Completed!', life: 3000});
        } else {
          this.state = false
          this.msg = data.error
        }
      })
    },
  }
}
</script>

<style scoped lang="scss">
.p-tabview {
  margin-left: 15px;
  margin-right: 15px;
}

</style>