<template>
  <div style="font-size: 20px; text-align: left;">
      <template class="test_grade" v-if="student.test_grade">{{student.test_grade}}</template>
      <template class="test_grade" v-else>NA</template>
      <Button style="float: right;" class="p-button-warning" label="Edit" @click="openEditDialog()"/>
      <Dialog header="Edit test grade " :visible.sync="display">
          <div> Editing test grade for {{this.student.name}} in {{this.$route.params.code}}. </div>
          <input type="text" placeholder="Please enter grade" v-model="grade">
          <Button style="float: right;"  icon="pi pi-check" @click="editTestGrade()"/>
      </Dialog>
  </div>
</template>

<script>
import Button from 'primevue/button';
import Dialog from 'primevue/dialog';
export default {
  name: 'GradeEditBox',
  components:{
    Button,
    Dialog
  },
  data() {
    return {
      display: false,
      grade: ''
    }
  },
  props: {
      student: null
  },
  methods: {
    openEditDialog: function () {
      this.display = true
      this.grade = this.student.test_grade
    },
    editTestGrade: function () {
        this.$axios.request({
        url: this.$url + 'students/code/' + this.$route.params.code + '/' + this.student.uname,
        method: 'POST',
        data: this.grade
      }).then(response => {
          let data = response.data
          if (data.state === true) {
          } else {
            this.error = data.error
          }
        })
    }
  }
}
</script>

<style scoped>

</style>
