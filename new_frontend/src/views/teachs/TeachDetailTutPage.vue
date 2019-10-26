<template>
  <div>
    <div style="font-size: 20px; text-align: left;margin-left: 15px; font-weight: bold;">This is all tutorials:</div>
    <BasicTutorialList style="font-size: 20px; text-align: left;margin-left: 15px;margin-right: 15px;" :tutorials="tutorials"/>
  </div>
</template>

<script>
import BasicTutorialList from "../../components/lists/BasicTutorialList";
export default {
  name: "TeachDetailTutPage",
  components: {BasicTutorialList},
  data() {
    return {
      state: false,
      msg: 'Network Error',
      tutorials: null
    }
  },
  mounted() {
    this.getTutorials()
  },
  methods: {
    getTutorials: function () {
      this.$axios.request({
        url: this.$url + 'tutorial/code/' + this.$route.params.code + '/',
        method: 'GET'
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.state = true
          this.tutorials = data.data.tutorials
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