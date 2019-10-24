<template>
    <div>
        This is all tutors under the module:
        <div>
            <BasicStudentList :students="tas" :is-select-tutor="true"/>
        </div>
      <Button label="Add more tutors" icon="pi pi-plus" @click="openAddTA()" />
      <Dialog header="Add New Tutors" :visible.sync="display" :style="{width: '50vw'}" :modal="true">
        <BasicStudentList :students="candidates"/>
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
    export default {
        name: "TeachDetailTAsPage",
      props: {
        tas: Array,
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
        Button,
        Dialog,
        Dropdown,
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
        //   this.$axios.request({
        //     url: this.$url + 'student/addtut/' +this.selectedCandidate.uname +'/'+ this.$route.params.code + '/'+this.$route.params.group_num +'/',
        //     method: 'GET'
        //   }).then(response => {
        //     console.log(response)
        //     let data = response.data
        //     if (data.state === true) {
        //       this.state = true
        //       this.display = false
        //       this.getStudents()
        //     } else {
        //       this.state = false
        //       this.msg = data.error
        //     }
        //   })
        },
      }
    }
</script>

<style scoped>
  .name, .grpNum {
    width: 150px;
  }
  .email {
    width: 350px;
  }
</style>