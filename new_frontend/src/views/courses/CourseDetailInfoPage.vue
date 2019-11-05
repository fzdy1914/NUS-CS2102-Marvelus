<template>
  <div>
    <div class="title-font">Course Info</div>
    <div class="text-font" v-if=course> {{course.info}} </div>
    <div class="title-font">Lecture Time</div>
    <div class="text-font" v-if=course> {{course.start_time}}-{{course.end_time}}, {{course.lec_day}}</div>
    <div class="title-font">This is all Profs:</div>
    <BasicProfList style="font-size: 20px; text-align: left;margin-left: 15px;margin-right: 15px;" :profs="profs"/>
    <div class="title-font">This is all TAs:</div>
    <StudentListDataTable style="font-size: 20px; text-align: left;margin-left: 15px;margin-right: 15px;":peoples="TAs"/>
  </div>
</template>

<script>
import StudentListDataTable from "../../components/lists/StudentListDataTable";
import BasicProfList from "../../components/lists/BasicProfList";

export default {
  name: "CourseDetailInfoPage",
  components: {StudentListDataTable, BasicProfList},
  data() {
    return {
      state: false,
      msg: 'Network Error',
      course: null,
      profs: null,
      TAs: null
    }
  },
  mounted() {
    this.getCourse()
    this.getProfs()
    this.getTAs()
  },
  methods: {
    getCourse: function () {
      this.$axios.request({
        url: this.$url + 'course/code/' + this.$route.params.code + '/',
        method: 'GET'
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.state = true
          this.course = data.data.course
        } else {
          this.state = false
          this.msg = data.error
        }
      })
    },
    getProfs: function () {
      this.$axios.request({
        url: this.$url + 'profs/code/' + this.$route.params.code + '/',
        method: 'GET'
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.state = true
          this.profs = data.data.profs
        } else {
          this.state = false
          this.msg = data.error
        }
      })
    },
    getTAs: function () {
      this.$axios.request({
        url: this.$url + 'TAs/code/' + this.$route.params.code + '/',
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
    }
  }
}
</script>

<style scoped>
  .title-font{
    font-size: 20px; text-align: left;margin-left: 15px; font-weight: bold;
  }
  .text-font{
    font-size: 16px; text-align: left;margin-left: 15px;
  }
</style>