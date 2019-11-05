<template>
  <div>
    <NavBar :whichActive="'search'"/>
    <div class="searchbar">
      <span class="my-keyword">Keyword:</span>
      <input type="text" placeholder="Enter keyword" v-model="keyword" class="my-input"/>
      <Button label="Search" @click="getCourses(keyword)"></Button>
    </div>
    <DataView :value="courses" :layout="'list'">
      <template #list="slotProps">
        <div class="p-col-12">
          <div class="course-details">
            <div>
              <div class="p-grid">
                <div class="p-col-4">Code: <b>{{slotProps.data.code}}</b></div>
                <div class="p-col-4">Title: <b>{{slotProps.data.title}}</b></div>
                <div class="p-col-4" v-if="slotProps.data.status === 'enrolled'" style="color: black;"><b>{{slotProps.data.status}}</b></div>
                <div class="p-col-4" v-else-if="slotProps.data.status === 'completed'" style="color: green;"><b>{{slotProps.data.status}} in {{slotProps.data.enroll_year}}</b></div>
                <div class="p-col-4" v-else-if="slotProps.data.status === 'rejected'" style="color: red;"><b>{{slotProps.data.status}}</b></div>
                <div class="p-col-4" v-else-if="slotProps.data.status === 'requesting'" style="color: black;"><b>{{slotProps.data.status}}</b></div>
                <div class="p-col-4" v-else-if="$store.state.isProf"></div>
                <div class="p-col-4" v-else><Button label="Request" @click="requestModule(slotProps.data.code)"></Button></div>
              </div>
            </div>
          </div>
        </div>
      </template>
    </DataView>
  </div>
</template>

<script>
  import DataView from 'primevue/dataview';
  import NavBar from "../components/NavBar";
  import InputText from 'primevue/inputtext';
  import Button from 'primevue/button';
  export default {
    name: "CourseSearchPage",
    components: {
      NavBar,
      DataView,
      InputText,
      Button
    },
    data () {
      return {
        msg: 'Network Error',
        courses: null,
        state: false,
        keyword: ''
      }
    },
    mounted () {
      this.getCourses(null)
    },
    methods: {
      getCourses: function (keyword) {
        this.$axios.request({
          url: keyword ? this.$url + 'courses/search/' + keyword + '/' : this.$url + 'courses/all/',
          method: 'GET'
        }).then(response => {
          let data = response.data
          if (data.state === true) {
            this.state = true
            this.courses = data.data.courses
          } else {
            this.state = false
            this.msg = data.error
          }
        })
      },
      requestModule: function(code) {
        this.$axios.request({
          url: this.$url + 'students/code/enroll/' + code +'/',
          method: 'GET'
        }).then(response => {
          let data = response.data
          if (data.state === true) {
            this.state = true
            this.students = data.data.students
            this.getCourses(this.keyword)
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
.searchbar{
  background-color: transparent;
  margin-top: -10px;
  margin-bottom: 10px;
  color: #000000;
}
.my-input {
  margin-left: 6px;
  margin-right: 10px;
}
.my-keyword {
  font-size: 16px;
}
.course-details {
  border-bottom: 1px solid #d9dad9;
  height: 40px;
}
</style>