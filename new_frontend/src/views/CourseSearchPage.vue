<template>
  <div>
    <NavBar :whichActive="'search'"/>
    <div class="searchbar">
      <span class="my-keyword">Keyword:</span>
      <input type="text" placeholder="Enter course code" v-model="keyword" class="my-input" @keyup.enter="getCourses(keyword)"/>
      <Button label="Search" @click="getCourses(keyword)"></Button>
    </div>
    <DataView :value="courses" :layout="'list'">
      <template #list="slotProps">
        <div class="p-col-12">
          <div class="course-details">
            <div>
              <div class="p-grid">
                <div class="p-col-4"><div class="my-content">Code: <b>{{slotProps.data.code}}</b></div></div>
                <div class="p-col-4"><div class="my-content">Title: <b>{{slotProps.data.title}}</b></div></div>
                <div class="p-col-4" v-if="slotProps.data.status === 'enrolled'"><Button label="Enrolled" disabled="disabled"></Button></div>
                <div class="p-col-4" v-else-if="slotProps.data.status === 'completed'" style="color: green;"><Button label="Completed" class="p-button-success" disabled="disabled"></Button></div>
                <div class="p-col-4" v-else-if="slotProps.data.status === 'rejected'"><Button label="Rejected" class="p-button-danger" disabled="disabled"></Button></div>
                <div class="p-col-4" v-else-if="slotProps.data.status === 'requesting'"><Button label="Requesting" disabled="disabled"></Button></div>
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
import Button from 'primevue/button';

export default {
  name: "CourseSearchPage",
  components: {
    NavBar,
    DataView,
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
  },
  watch: {
    'keyword' (to, from) {
      if (to == '') {
        this.getCourses('')
      }
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
  height: 50px;
}
.my-content {
  padding: 7px;
}
</style>