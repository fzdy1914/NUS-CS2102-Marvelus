<template>
    <div>
        This is all students requesting to join the module:
      <div>
        <!--<DataTable :value="students" :paginator="true" :rows="20" sortMode="multiple" v-for="student in students" :key="student.uname">
          <Column field="name" header="TA Name"></Column>
          <Column field="matriculation_num" header="Matriculation number"></Column>
          <Column field="major" header="Major"></Column>
          <Column field="year" header="Year" sortable="true"></Column>
          <Column field="email" header="Email"></Column>
          <Column header="Operation">
              <button class="btn btn-primary approve" >Approve</button>
              <button class="btn btn-primary reject" >Reject</button>
          </Column>
        </DataTable>-->
        <table class="table table-bordered table-hover" :students="students" :sticky-header=true>
          <thead>
            <tr>
              <th>Name</th>
                <th>Matriculation number</th>
              <th>Major</th>
              <th>Year</th>
              <th>Email</th>
                <th>Operation</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="student in students" :key="student.uname">
              <td class="name">{{ student.name }}</td>
                <td class="matnum">{{ student.matriculation_num }}</td>
              <td class="major">{{ student.major }}</td>
              <td class="year">{{ student.year }}</td>
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
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import ColumnGroup from 'primevue/columngroup';
export default {
  name: "TeachDetailRequestsPage",
  components: {
    BasicStudentList,
    DataTable,
    Column,
    ColumnGroup,
  },
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
  .name, .major, .year {
    width: 150px;
  }
  .email, .matnum {
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