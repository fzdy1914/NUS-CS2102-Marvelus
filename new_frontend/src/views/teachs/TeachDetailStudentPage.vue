<template>
  <div>
    This is all students under this module:
    <BasicStudentList style="font-size: 20px; text-align: left;margin-left: 15px;margin-right: 15px;" :students="students"/>
  </div>
</template>

<script>
import BasicStudentList from '../../components/lists/BasicStudentList'

export default {
  name: "TeachDetailStudentPage",
  components: {
    BasicStudentList
  },
  data() {
    return {
      state: false,
      msg: 'Network Error',
      students: null,
    }
  },
  mounted() {
    this.getStudents()
  },
  methods: {
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
    }
  }
}
</script>

<style scoped>

</style>