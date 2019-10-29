<template>
  <div>
    <div style="font-size: 20px; text-align: left;margin-left: 15px; font-weight: bold;">This is all students in your tutorial:</div>
    <BasicStudentList style="font-size: 20px; text-align: left;margin-left: 15px;margin-right: 15px;" :students="students"/>
  </div>
</template>

<script>
import BasicStudentList from "../../components/lists/BasicStudentList";
export default {
  name: "CourseDetailTutPage",
  components: {BasicStudentList},
  data() {
    return {
      state: false,
      msg: 'Network Error',
      tutorial: null,
      students: null
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
    }
  }
}
</script>

<style scoped>

</style>