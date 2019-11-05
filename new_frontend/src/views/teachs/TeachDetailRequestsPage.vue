<template>
  <div>
    <div>
      <div class="title-font">
        This is all students requesting to join the module:
        <Button v-if="selectedStu" class="p-button-danger" style="float: right; margin-right: 15px" label="Reject" @click="approveRequest(selectedStu.uname)"/>
        <Button v-if="selectedStu" class="p-button-success" style="float: right; margin-right: 5px" label="Approve" @click="rejectRequest(selectedStu.uname)"/>
      </div>
    </div>
    <DataTable :value="students" sortMode="multiple" :selection.sync="selectedStu" dataKey="uname" style="margin-top: 12px">
      <Column selectionMode="single" headerStyle="width: 3em"></Column>
      <Column field="name" header="Student Name"></Column>
      <Column field="matriculation_num" header="Matriculation number"></Column>
      <Column field="major" header="Major"></Column>
      <Column field="year" header="Year"></Column>
      <Column field="enroll_year" header="Enroll Year"></Column>
      <Column field="email" header="Email"></Column>
    </DataTable>
  </div>
</template>

<script>
import BasicStudentList from '../../components/lists/BasicStudentList'
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import Button from 'primevue/button';
import Dialog from 'primevue/dialog';
export default {
  name: "TeachDetailRequestsPage",
  components: {
    BasicStudentList,
    DataTable,
    Column,
    Button,
    Dialog
  },
  data() {
    return {
      state: false,
      msg: 'Network Error',
      students: null,
      selectedStu: null
    }
  },
  mounted() {
    this.getStudents()
  },
  methods: {
    getStudents: function () {
      this.$axios.request({
        url: this.$url + 'requests/code/' + this.$route.params.code + '/',
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
    approveRequest: function(uname){
      this.$axios.request({
        url: this.$url + 'requests/approve/' + uname +'/'+ this.$route.params.code+'/',
        method: 'GET'
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.state = true
          this.getStudents()
        } else {
          this.state = false
          this.msg = data.error
        }
      })
    },
    rejectRequest: function(uname){
      this.$axios.request({
        url: this.$url + 'requests/reject/' + uname +'/'+ this.$route.params.code+'/',
        method: 'GET'
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.state = true
          this.getStudents()
        } else {
          this.state = false
          this.msg = data.error
        }
      })
    }
  }
}
</script>

<style scoped>
  .name, .major, .year {
    width: 150px;
  }
  .email, .matnum {
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