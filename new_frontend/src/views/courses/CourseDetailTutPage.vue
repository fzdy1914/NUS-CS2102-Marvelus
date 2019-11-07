<template>
  <div v-if="tutorial">
    <TutorialBasicInfo :tutorial="tutorial"/>

    <div>
      <div class="title-font">List of TAs:</div>

      <DataTable :value="TAs" style="margin-bottom: 20px">
        <Column field="name" header="TA Name"></Column>
        <Column field="major" header="Major"></Column>
        <Column field="email" header="E-mail"></Column>
        <Column field="year" header="Year"></Column>
      </DataTable>
    </div>
    <div class="title-font">This is all students in your tutorial:</div>
    <BasicStudentList :students="students"/>
  </div>
  <div v-else>
    <div class="title-font">You are assigned to  any tutorial group :(</div>
  </div>
</template>

<script>
import BasicStudentList from "../../components/lists/BasicStudentList";
import TutorialBasicInfo from "../../components/TutorialBasicInfo";
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';

export default {
  name: "CourseDetailTutPage",
  components: {
    BasicStudentList,
    TutorialBasicInfo,
    DataTable,
    Column
  },
  data() {
    return {
      state: false,
      msg: 'Network Error',
      tutorial: null,
      students: null,
      TAs: [],
    }
  },
  mounted() {
    this.getTutorial()
    this.getStudents()
  },
  methods: {
    getTutorial: function () {
      this.$axios.request({
        url: this.$url + 'tutorials/uname/code/' + this.$store.state.username + '/' + this.$route.params.code + '/',
        method: 'GET'
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.state = true
          this.tutorial = data.data.tutorials[0]
          this.getTAs()
        } else {
          this.state = false
          this.msg = data.error
        }
      })
    },
    getStudents: function () {
      this.$axios.request({
        url: this.$url + 'students/uname/code/' + this.$store.state.username + '/' + this.$route.params.code + '/',
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
    getTAs: function () {
      this.$axios.request({
        url: this.$url + 'TAs/' + this.$route.params.code + '/'+this.tutorial.group_num +'/',
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
  }
}
</script>

<style scoped>
.title-font{
  font-size: 20px; text-align: left;margin-left: 15px; font-weight: bold
}
</style>