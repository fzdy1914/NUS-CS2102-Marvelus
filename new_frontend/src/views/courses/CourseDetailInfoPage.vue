<template>
  <div>
    <div style="font-size: 20px; text-align: left;margin-left: 15px; font-weight: bold;">Course Info</div>
    <div style="font-size: 16px; text-align: left;margin-left: 15px;" v-if=course> {{course.info}} </div>
    <div style="font-size: 20px; text-align: left;margin-left: 15px; font-weight: bold;">This is all Profs:</div>
    <BasicProfList style="font-size: 20px; text-align: left;margin-left: 15px;margin-right: 15px;" :profs="profs"/>
    <div style="font-size: 20px; text-align: left;margin-left: 15px; font-weight: bold;">This is all TAs:</div>
    <BasicTAList style="font-size: 20px; text-align: left;margin-left: 15px;margin-right: 15px;" :TAs="TAs"/>
  </div>
</template>

<script>
import BasicTAList from "../../components/lists/BasicTAList";
import BasicProfList from "../../components/lists/BasicProfList";

export default {
  name: "CourseDetailInfoPage",
  components: {BasicTAList, BasicProfList},
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

</style>