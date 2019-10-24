<template>
    <div>
        This is all students requesting to join the module:
        <!--<BasicStudentList :students="students" :isProf="true"/>-->
      <div>
        <table class="table table-bordered table-hover" :students="students">
          <thead>
            <tr>
              <th>Name</th>
              <th>Major</th>
              <th>Email</th>
                <th>Operation</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="student in students" :key="student.uname">
              <td class="name">{{ student.name }}</td>
              <td class="major">{{ student.major }}</td>
              <td class="email">{{ student.email }}</td>
              <td class="operation">
                <button class="btn btn-primary approve" @click="approveRequest(student.uname)">Approve</button>
                <button class="btn btn-primary reject" @click="rejectRequest(student.uname)">Reject</button>
              </td>
            </tr>
          </tbody>
        </table>
        </div>
    </div>
</template>

<script>
import BasicStudentList from '../../components/lists/BasicStudentList'
export default {
  name: "TeachDetailRequestsPage",
  components: {BasicStudentList},
    props: {
        students: Array,
    },
  data() {
    return {
      state: false,
      msg: 'Network Error',
      students: null
    }
  },
  mounted() {
    this.getStudents()
  },
  methods: {
    getStudents: function () {
      this.$axios.request({
        url: this.$url + 'requests/code/' + this.$route.params.code + '/',
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
    approveRequest: function(uname){

        console.log('hihi'+uname)
      this.$axios.request({
        url: this.$url + 'requests/approve/' + uname +'/'+ this.$route.params.code+'/',
        method: 'GET'
      }).then(response => {
        console.log(response)
        let data = response.data
        if (data.state === true) {
          this.state = true
          this.getStudents()
        } else {
          this.state = false
          this.msg = data.error
        }
      })
    },
    rejectRequest: function(uname){
      this.$axios.request({
        url: this.$url + 'requests/reject/' + uname +'/'+ this.$route.params.code+'/',
        method: 'GET'
      }).then(response => {
        console.log(response)
        let data = response.data
        if (data.state === true) {
          this.state = true
          this.getStudents()
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
  .name, .major {
    width: 150px;
  }
  .email {
    width: 350px;
  }
  .operation {
    width: 200px
  }
  .reject {
    background-color: #D94600;
    border-color: #BB3D00;
  }
  .btn {
    padding: 3px 8px;
  }
</style>