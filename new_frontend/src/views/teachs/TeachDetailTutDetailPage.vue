<template>
  <div>
    This is Tut Detail Info:
    <div>Course Code: {{ $route.params.code }}</div>
    <div>Group Num: {{ $route.params.group_num }}</div>
    <div>
      <h3>List of TA</h3>
      <Button label="Add New " @click="" />
      <DataTable :value="TAs">
        <Column field="name" header="TA Name"></Column>
        <Column field="uname" header="User Name"></Column>
        <Column field="brand" header="..."></Column>
        <Column field="color" header="..."></Column>
      </DataTable>
    </div>
    <div>
      <h3>List of Forums</h3>
      <Button label="Add New " @click="" />
      <DataTable :value="Forums">
        <Column field="name" header="Forum Name"></Column>
        <Column field="uname" header="Forum ID"></Column>
        <Column field="brand" header="..."></Column>
        <Column field="color" header="..."></Column>
      </DataTable>
    </div>
    <div>
      <h3>List of Students</h3>
      <Button label="Add New " @click="openAddStu()" />
      <DataTable :value="Students">
        <Column field="name" header="Student Name"></Column>
        <Column field="uname" header="User Name"></Column>
        <Column field="brand" header="..."></Column>
        <Column field="color" header="..."></Column>
      </DataTable>
    </div>

<Button label="Show" icon="pi pi-external-link" @click="openAddStu()" />
<Dialog header="Add New Student" :visible.sync="display" :style="{width: '50vw'}" :modal="true">

  <Dropdown v-model="selectedStu" :options="noAttendStus" optionLabel="uname" placeholder="Select a student" />

    <template #footer>
        <Button label="Yes" icon="pi pi-check" @click="addStudent()" />
        <Button label="No" icon="pi pi-times" @click="closeAddStu()" class="p-button-secondary"/>
    </template>
</Dialog>

  </div>
</template>

<script>

  import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import ColumnGroup from 'primevue/columngroup';
import Button from 'primevue/button';
import Dialog from 'primevue/dialog';
import Dropdown from 'primevue/dropdown';
export default {
  name: "TeachDetailTutDetailPage",
  data() {
    return {
      state: false,
      msg: 'Network Error',
      TAs: null,
      Students: null,
      Forums: null,
      display:false,
      selectedStu: null,
      noAttendStus:null,
    }
  },
  components:{
    DataTable,
    Column,
    ColumnGroup,
    Button,
    Dialog,
    Dropdown
  },
  mounted() {
    this.getTAs()
    this.getStudents()
    this.getForums()
  },methods: {
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
        console.log(response)
        if (data.state === true) {
          this.state = true
          this.noAttendStus = data.data.students
          console.log(this.noAttendStus)
        } else {
          this.state = false
          this.msg = data.error
        }
      })
    },
    addStudent: function(){
      this.$axios.request({
        url: this.$url + 'student/addtut/' +this.selectedStu.uname +'/'+ this.$route.params.code + '/'+this.$route.params.group_num +'/',
        method: 'GET'
      }).then(response => {
        console.log(response)
        let data = response.data
        if (data.state === true) {
          this.state = true
          this.display = false
          this.getStudents()
        } else {
          this.state = false
          this.msg = data.error
        }
      })
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
          console.log(this.TAs)
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
          console.log(this.Students)
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
          console.log(this.Forums)
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