<template>
  <div>
    <div class="title-font" style="margin-bottom: 20px">
        This is all tutors under the module:
        <Button class="p-button-raised" icon="pi pi-plus" style="float: right; margin-right: 15px" label="Add more tutors" @click="openAddTA()"/>
      </div>
    <div>
      <StudentListDataTable :peoples="tas" />
    </div>
    <Dialog header="Add New Tutors" :visible.sync="display" :style="{width: '55vw'}" :modal="true">
      Eligible candidates who have completed the module and obtained grade 'A' or 'B':
      <DataTable :value="candidates" :selection.sync="selectedCandidate" dataKey="uname">
        <Column selectionMode="single" headerStyle="width: 3em"></Column>
        <Column field="name" header="TA Name"></Column>
        <Column field="matriculation_num" header="Matriculation number"></Column>
        <Column field="major" header="Major"></Column>
        <Column field="final_grade" header="Course Final Grade"></Column>
        <Column field="year" header="Year"></Column>
      </DataTable>
      <br/>
      <template #footer>
        <Button label="Yes" icon="pi pi-check" @click="addTA()" />
        <Button label="No" icon="pi pi-times" @click="closeAddTA()" class="p-button-secondary"/>
      </template>
    </Dialog>
  </div>
</template>

<script>
import Button from 'primevue/button';
import Dialog from 'primevue/dialog';
import Dropdown from 'primevue/dropdown';
import BasicStudentList from '../../components/lists/BasicStudentList';
import StudentListDataTable from "../../components/lists/StudentListDataTable";
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import ColumnGroup from 'primevue/columngroup';
export default {
  name: "TeachDetailTAsPage",
  props: {
  },
  data() {
    return {
      state: false,
      msg: 'Network Error',
      tas: null,
      candidates: null,
      display: false,
      selectedCandidate: null
    }
  },
  components:{
    StudentListDataTable,
    Button,
    Dialog,
    Dropdown,
    DataTable,
    Column
  },
  mounted() {
    this.getTAs()
  },
  methods: {
    getTAs: function () {
      this.$axios.request({
        url: this.$url + 'TAs/code/' + this.$route.params.code + '/',
        method: 'GET'
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.state = true
          this.tas = data.data.TAs
        } else {
          this.state = false
          this.msg = data.error
        }
      })
    },
    closeAddTA:function(){
      this.display = false
    },
    openAddTA: function(){
      this.display = true
      this.$axios.request({
        url: this.$url + 'candidates/code/' + this.$route.params.code + '/',
        method: 'GET'
      }).then(response => {
        let data = response.data
        console.log(response)
        if (data.state === true) {
          this.state = true
          this.candidates = data.data.students
        } else {
          this.state = false
          this.msg = data.error
        }
      })
    },
    addTA: function(){
      this.$axios.request({
        url: this.$url + 'candidates/add/' +this.selectedCandidate.uname +'/'+ this.$route.params.code+'/',
        method: 'GET'
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.state = true
          this.display = false
          this.getTAs()
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