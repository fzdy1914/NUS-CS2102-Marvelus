<template>
  <div>
    <div style="text-align: left">
      <Button class="p-button-raised" icon="pi pi-arrow-left" label ="Back"  @click="goBack()" style="margin-left: 15px;"/>
    </div>
    <TutorialBasicInfo :tutorial="tutorial" style="margin-top: 5px"/>
    <div>
      <div class="title-font" style="margin-bottom: 20px">
        List of TAs:
        <Button class="p-button-raised" icon="pi pi-plus" style="float: right; margin-right: 15px" label="Add New TA" @click="openAddTA()"/>
      </div>

      <DataTable :value="TAs">
        <Column field="name" header="TA Name"></Column>
        <Column field="major" header="Major"></Column>
        <Column field="email" header="E-mail"></Column>
        <Column field="year" header="Year"></Column>
      </DataTable>
    </div>
    <Dialog header="Add TA" :visible.sync="displayTA" :style="{width: '80vw'}" :modal="true">
      <DataTable :value="notInTAs" :selection.sync="selectedTA"  >
        <Column selectionMode="single" headerStyle="width: 3em"></Column>
        <Column field="name" header="TA Name"></Column>
        <Column field="major" header="Major"></Column>
        <Column field="matriculation_num" header="Matriculation Number"></Column>
        <Column field="year" header="Year"></Column>
      </DataTable>
        <template #footer>
            <Button label="Yes" icon="pi pi-check" @click="addTA()" />
            <Button label="No" icon="pi pi-times" @click="closeAddTA()" class="p-button-secondary"/>
        </template>
    </Dialog>

    <div>
      <div class="title-font" style="margin-top: 20px; margin-bottom: 20px">
        List of Forums:
        <Button class="p-button-raised" icon="pi pi-plus" style="float: right; margin-right: 15px" label="Add New Forum" @click="openAddForum()"/>
      </div>
      <DataTable :value="Forums">
        <Column field="fid" header="Forum Number"></Column>
        <Column field="title" header="Forum Title"></Column>
      </DataTable>
    </div>
    <Dialog header="Add Forum" :visible.sync="displayForum" :style="{width: '80vw'}" :modal="true">
        <DataTable :value="notInForums" :selection.sync="selectedForum"  >
          <Column selectionMode="single" headerStyle="width: 3em"></Column>
            <Column field="fid" header="Forum Number"></Column>
            <Column field="title" header="Forum Title"></Column>
          </DataTable>
        <template #footer>
            <Button label="Yes" icon="pi pi-check" @click="addForum()" />
            <Button label="No" icon="pi pi-times" @click="closeAddForum()" class="p-button-secondary"/>
        </template>
    </Dialog>
    <div>
      <div class="title-font" style="margin-top: 20px; margin-bottom: 20px">
        List of Students:
        <Button class="p-button-raised" icon="pi pi-plus" style="float: right; margin-right: 15px" label="Add New Student" @click="openAddStu()"/>
        <Button v-if="selectedAttend" class="p-button-success" style="float: right; margin-right: 5px" icon="pi pi-plus" label="Attendance" @click="openAttendance()" />
      </div>

      <DataTable :value="Students" :selection.sync="selectedAttend" dataKey="uname">
        <Column selectionMode="single" headerStyle="width: 3em"></Column>
        <Column field="name" header="Student Name"></Column>
        <Column field="major" header="Major"></Column>
        <Column field="matriculation_num" header="Matriculation Number"></Column>
        <Column field="attendance_grade" header="Attendance Grade"></Column>
        <Column field="year" header="Year"></Column>
      </DataTable>
    </div>
      <Dialog header="Tutorial Attendance" :visible.sync="displayAttendance" :style="{width: '80vw'}" :modal="true">
        <DataTable :value="attendances"  >
          <Column field="attend_week" header="Attended Week"></Column>
          <Column field="group_num" header="Tut Group"></Column>
        </DataTable>
        <div style="margin-top: 10px">
          <div class="text-font" style="display: inline-block; float: left">Enter the attended week for the student:</div>
          <InputText placeholer="eg:6" type="number" v-model="attendWeek" style="margin-right: 10px"/>
          <Button v-if="selectedAttend" class="p-button-success" icon="pi pi-plus" label="Attendance" @click="addAttendance()" />
        </div>
    </Dialog>

    <Dialog header="Add New Student" :visible.sync="display" :style="{width: '80vw'}" :modal="true">
         <DataTable :value="noAttendStus" :selection.sync="selectedStu" selectionMode="single" >
            <Column field="name" header="Student Name"></Column>
            <Column field="uname" header="User Name"></Column>
            <Column field="matriculation_num" header="Matriculation Number"></Column>
            <Column field="year" header="Year"></Column>
          </DataTable>
      <template #footer>
        <Button label="Yes" icon="pi pi-check" @click="addStudent()" />
        <Button label="No" icon="pi pi-times" @click="closeAddStu()" class="p-button-secondary"/>
      </template>
    </Dialog>
  <Toast/>
  </div>
</template>

<script>
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import Button from 'primevue/button';
import Dialog from 'primevue/dialog';
import Toast from 'primevue/toast';
import InputText from "primevue/components/inputtext/InputText";
import TutorialBasicInfo from "../../components/TutorialBasicInfo";

export default {
  name: "TeachDetailTutDetailPage",
  data() {
    return {
      state: false,
      msg: 'Network Error',
      TAs: null,
      notInTAs: null,
      Students: null,
      Forums: null,
      display:false,
      displayTA: false,
      displayForum:false,
      displayAttendance: false,
      notInForums:null,
      selectedStu: null,
      selectedTA: null,
      selectedForum: null,
      selectedAttend: null,
      noAttendStus:null,
      attendances:null,
      attendWeek:0,
      messages: [],
      tutorial: null
    }
  },
  components:{
    InputText,
    DataTable,
    Column,
    Button,
    Dialog,
    Toast,
    TutorialBasicInfo
  },
  mounted() {
    this.getTutorial()
    this.getTAs()
    this.getStudents()
    this.getForums()
  },
  methods: {
    openAttendance:function(){
      this.displayAttendance = true
      this.getAttendance();
    },
    getAttendance:function(){
      this.$axios.request({
        url: this.$url + 'attendance/get/' + this.selectedAttend.uname+'/'+ this.$route.params.code + '/'+ this.$route.params.group_num +'/' ,
        method: 'GET'
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.state = true
          this.attendances = data.data.attendances
          this.attendWeek=0;
        } else {
          this.state = false
          this.msg = data.error
        }
      })
    },
    addAttendance: function(){
      this.$axios.request({
        url: this.$url + 'attendance/add/' + this.selectedAttend.uname+'/' +this.$route.params.code + '/'+ this.$route.params.group_num +'/'+this.attendWeek+'/' ,
        method: 'GET'
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.state = true
            this.$toast.add({severity:'success', summary: 'Success ', detail:'Attendance added in!', life: 3000});
            this.getAttendance();
            this.displayAttendance = false
            this.getStudents()
        } else {
          this.state = false
          this.msg = data.error
        }
      })
    },
    goBack: function(){
       this.$router.push({name: 'TeachDetailTutList', params: {code: this.$route.params.code}})
    },
    closeAddForum: function(){
      this.displayForum = false;
    },
    openAddForum: function(){
      this.displayForum = true
      this.$axios.request({
        url: this.$url + 'forums/notin/' + this.$route.params.code + '/'+ this.$route.params.group_num +'/' ,
        method: 'GET'
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.state = true
          this.notInForums = data.data.forums
        } else {
          this.state = false
          this.msg = data.error
        }
      })
    },
    addForum: function(){
      this.$axios.request({
        url: this.$url + 'forums/addtut/' + this.$route.params.code + '/'+this.$route.params.group_num +'/'+ this.selectedForum.fid + '/',
        method: 'GET'
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.state = true
          this.displayForum = false
          this.$toast.add({severity:'success', summary: 'Success ', detail:'Forum added in!', life: 3000});
          this.getForums()
        } else {
          this.state = false
          this.msg = data.error
        }
      })
    },
    closeAddStu:function(){
      this.display = false
    },
    openAddStu: function(){
      this.display = true
      this.$axios.request({
        url: this.$url + 'students/noattend/' + this.$route.params.code + '/',
        method: 'GET'
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.state = true
          this.noAttendStus = data.data.students
        } else {
          this.state = false
          this.msg = data.error
        }
      })
    },
    addStudent: function(){
      this.$axios.request({
        url: this.$url + 'student/addtut/' + this.selectedStu.uname +'/'+ this.$route.params.code + '/'+this.$route.params.group_num + '/',
        method: 'GET'
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.state = true
          this.display = false
          this.$toast.add({severity:'success', summary: 'Success ', detail:'Student added in!', life: 3000});
          this.getStudents()
        } else {
          this.state = false
          this.msg = data.error
        }
      })
    },
    openAddTA: function(){
      this.displayTA = true
      this.$axios.request({
        url: this.$url + 'TAs/notin/' + this.$route.params.code + '/'+ this.$route.params.group_num + '/',
        method: 'GET'
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.state = true
          this.notInTAs = data.data.TAs
        } else {
          this.state = false
          this.msg = data.error
        }
      })
    },
    addTA: function(){
      this.$axios.request({
        url: this.$url + 'TAs/addtut/' +this.selectedTA.uname +'/'+ this.$route.params.code + '/'+this.$route.params.group_num +'/',
        method: 'GET'
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.state = true
          this.displayTA = false
          this.$toast.add({severity:'success', summary: 'Success ', detail:'TA added in!', life: 3000});
          this.getTAs()
        } else {
          this.state = false
          this.msg = data.error
        }
      })
    },
    closeAddTA:function(){
      this.displayTA = false
    },
    getTAs: function () {
      this.$axios.request({
        url: this.$url + 'TAs/' + this.$route.params.code + '/'+this.$route.params.group_num +'/',
        method: 'GET'
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.state = true
          this.TAs = data.data.TAs
        } else {
          this.state = false
          this.msg = data.error
        }
      })
    },
    getStudents: function () {
      this.$axios.request({
        url: this.$url + 'students/' + this.$route.params.code + '/'+this.$route.params.group_num +'/',
        method: 'GET'
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.state = true
          this.Students = data.data.students
        } else {
          this.state = false
          this.msg = data.error
        }
      })
    },
    getForums: function () {
      this.$axios.request({
        url: this.$url + 'forums/' + this.$route.params.code + '/'+this.$route.params.group_num +'/',
        method: 'GET'
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.state = true
          this.Forums = data.data.forums
        } else {
          this.state = false
          this.msg = data.error
        }
      })
    },
    getTutorial: function () {
      this.$axios.request({
        url: this.$url + 'tutorials/' + this.$route.params.code + '/'+this.$route.params.group_num +'/',
        method: 'GET'
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.state = true
          this.tutorial = data.data.tutorials[0]
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
.button-style{
  background-color: #9c1b1b;
  border: #9c1b1b ;
}
.button-style:hover{
  background-color: #b71c1c;
  border: #b71c1c;
}
.button-pos{
  padding-top: 25px;
}
  .list-name{
    text-align: left;
    margin-left: 20px;
  }
</style>