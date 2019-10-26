<template>

  <div>
    <Button label = "Back" @click="goBack()"/>
    This is Tut Detail Info:
    <div>Course Code: {{ $route.params.code }}</div>
    <div>Group Num: {{ $route.params.group_num }}</div>
    <div>
      <h3>List of TA</h3>
      <Button label="Add New " @click="openAddTA()" />
      <DataTable :value="TAs">
        <Column field="name" header="TA Name"></Column>
        <Column field="uname" header="User Name"></Column>
        <Column field="brand" header="..."></Column>
        <Column field="color" header="..."></Column>
      </DataTable>
    </div>
    <Dialog header="Add TA" :visible.sync="displayTA" :style="{width: '50vw'}" :modal="true">

      <Dropdown v-model="selectedTA" :options="notInTAs" optionLabel="uname" placeholder="Select a TA" />

        <template #footer>
            <Button label="Yes" icon="pi pi-check" @click="addTA()" />
            <Button label="No" icon="pi pi-times" @click="closeAddTA()" class="p-button-secondary"/>
        </template>
    </Dialog>
    <div>
      <h3>List of Forums</h3>
      <Button label="Add New " @click="openAddForum()" />
      <DataTable :value="Forums">
        <Column field="name" header="Forum Name"></Column>
        <Column field="fid" header="Forum ID"></Column>
        <Column field="brand" header="..."></Column>
        <Column field="color" header="..."></Column>
      </DataTable>
    </div>
    <Dialog header="Add Forum" :visible.sync="displayForum" :style="{width: '50vw'}" :modal="true">

      <Dropdown v-model="selectedForum" :options="notInForums" optionLabel="fid" placeholder="Select a Forum" />

        <template #footer>
            <Button label="Yes" icon="pi pi-check" @click="addForum()" />
            <Button label="No" icon="pi pi-times" @click="closeAddForum()" class="p-button-secondary"/>
        </template>
    </Dialog>
    <div>
      <h3>List of Students</h3>
      <Button label="Add New " @click="openAddStu()" />
      <DataTable :value="Students">
        <Column field="name" header="Student Name"></Column>
        <Column field="uname" header="User Name"></Column>
        <Column field="brand" header="..."></Column>
        <Column field="color" header="..."></Column>
      </DataTable>
    </div>

<Button label="Show" icon="pi pi-external-link" @click="test()" />
<Dialog header="Add New Student" :visible.sync="display" :style="{width: '50vw'}" :modal="true">

  <Dropdown v-model="selectedStu" :options="noAttendStus" optionLabel="uname" placeholder="Select a student" />

    <template #footer>
        <Button label="Yes" icon="pi pi-check" @click="addStudent()" />
        <Button label="No" icon="pi pi-times" @click="closeAddStu()" class="p-button-secondary"/>
    </template>
</Dialog>
<Toast/>
  </div>
</template>

<script>

  import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import ColumnGroup from 'primevue/columngroup';
import Button from 'primevue/button';
import Dialog from 'primevue/dialog';
import Dropdown from 'primevue/dropdown';
import Toast from 'primevue/toast';
export default {
  name: "TeachDetailTutDetailPage",
  data() {
    return {
      state: false,
      msg: 'Network Error',
      TAs: null,
      notInTAs: null,
      Students: null,
      Forums: null,
      display:false,
      displayTA: false,
      displayForum:false,
      notInForums:null,
      selectedStu: null,
      selectedTA: null,
      selectedForum: null,
      noAttendStus:null,
      messages: [],
    }
  },
  components:{
    DataTable,
    Column,
    ColumnGroup,
    Button,
    Dialog,
    Dropdown,
    Toast
  },
  mounted() {
    this.getTAs()
    this.getStudents()
    this.getForums()
  },methods: {
    goBack: function(){
       this.$router.push({name: 'TeachDetailTutList', params: {code: this.$route.params.code}})
    },
    test: function(){
      console.log("test toast");
      this.$toast.add({severity:'success', summary: 'Success ', detail:'Student added in!', life: 3000});
    },
    closeAddForum: function(){
      this.displayForum = false;
    },
    openAddForum: function(){
      this.displayForum = true
      this.$axios.request({
        url: this.$url + 'forums/notin/' + this.$route.params.code + '/'+ this.$route.params.group_num +'/' ,
        method: 'GET'
      }).then(response => {
        let data = response.data
        console.log(response)
        if (data.state === true) {
          this.state = true
          this.notInForums = data.data.forums
          console.log(this.notInForums)
        } else {
          this.state = false
          this.msg = data.error
        }
      })
    },
    addForum: function(){
      this.$axios.request({
        url: this.$url + 'forums/addtut/' + this.$route.params.code + '/'+this.$route.params.group_num +'/'+ this.selectedForum.fid+'/',
        method: 'GET'
      }).then(response => {
        console.log(response)
        let data = response.data
        if (data.state === true) {
          this.state = true
          this.displayForum = false
          this.$toast.add({severity:'success', summary: 'Success ', detail:'Forum added in!', life: 3000});
          this.getForums()
        } else {
          this.state = false
          this.msg = data.error
        }
      })
    },
    closeAddStu:function(){
      this.display = false
    },
    openAddStu: function(){
      this.display = true
      this.$axios.request({
        url: this.$url + 'students/noattend/' + this.$route.params.code + '/',
        method: 'GET'
      }).then(response => {
        let data = response.data
        console.log(response)
        if (data.state === true) {
          this.state = true
          this.noAttendStus = data.data.students
          console.log(this.noAttendStus)
        } else {
          this.state = false
          this.msg = data.error
        }
      })
    },
    addStudent: function(){
      this.$axios.request({
        url: this.$url + 'student/addtut/' +this.selectedStu.uname +'/'+ this.$route.params.code + '/'+this.$route.params.group_num +'/',
        method: 'GET'
      }).then(response => {
        console.log(response)
        let data = response.data
        if (data.state === true) {
          this.state = true
          this.display = false
          this.$toast.add({severity:'success', summary: 'Success ', detail:'Student added in!', life: 3000});
          this.getStudents()
        } else {
          this.state = false
          this.msg = data.error
        }
      })
    },
    openAddTA: function(){
      this.displayTA = true
      this.$axios.request({
        url: this.$url + 'TAs/notin/' + this.$route.params.code + '/'+this.$route.params.group_num +'/',
        method: 'GET'
      }).then(response => {
        let data = response.data
        console.log(response)
        if (data.state === true) {
          this.state = true
          this.notInTAs = data.data.TAs
          console.log(this.notInTAs)
        } else {
          this.state = false
          this.msg = data.error
        }
      })
    },
    addTA: function(){
      this.$axios.request({
        url: this.$url + 'TAs/addtut/' +this.selectedTA.uname +'/'+ this.$route.params.code + '/'+this.$route.params.group_num +'/',
        method: 'GET'
      }).then(response => {
        console.log(response)
        let data = response.data
        if (data.state === true) {
          this.state = true
          this.displayTA = false
          this.$toast.add({severity:'success', summary: 'Success ', detail:'TA added in!', life: 3000});
          this.getTAs()
        } else {
          this.state = false
          this.msg = data.error
        }
      })
    },
    closeAddTA:function(){
      this.displayTA = false
    },
    getTAs: function () {
      this.$axios.request({
        url: this.$url + 'TAs/' + this.$route.params.code + '/'+this.$route.params.group_num +'/',
        method: 'GET'
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.state = true
          this.TAs = data.data.TAs
          console.log(this.TAs)
        } else {
          this.state = false
          this.msg = data.error
        }
      })
    },
    getStudents: function () {
      this.$axios.request({
        url: this.$url + 'students/' + this.$route.params.code + '/'+this.$route.params.group_num +'/',
        method: 'GET'
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.state = true
          this.Students = data.data.students
          console.log(this.Students)
        } else {
          this.state = false
          this.msg = data.error
        }
      })
    },
    getForums: function () {
      this.$axios.request({
        url: this.$url + 'forums/' + this.$route.params.code + '/'+this.$route.params.group_num +'/',
        method: 'GET'
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.state = true
          this.Forums = data.data.forums
          console.log(this.Forums)
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