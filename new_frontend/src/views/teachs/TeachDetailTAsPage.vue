<template>
  <div>
  This is all tutors under the module:
    <div>
      <StudentListDataTable :peoples="tas" />
    </div>
    <br/>
    <br/>
    <Button label="Add more tutors" icon="pi pi-plus" @click="openAddTA()" />
    <Dialog header="Add New Tutors" :visible.sync="display" :style="{width: '50vw'}" :modal="true">
      <!--<BasicStudentList :students="candidates" :is-select-candidate="true"/>-->
      Eligible candidates who have completed the module and obtained grade 'A' or 'B':
      <StudentListDataTable :peoples="candidates" :is-select-candidate="true"/>
      <br/>
      <Dropdown v-model="selectedCandidate" :options="candidates" optionLabel="name" placeholder="Select a tutor" />
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
    Column,
    ColumnGroup,
    BasicStudentList
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
          console.log(this.tas)
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
          console.log(this.candidates)
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
        console.log(response)
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