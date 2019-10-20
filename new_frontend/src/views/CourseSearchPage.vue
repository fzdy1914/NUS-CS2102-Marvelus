<template>
    <div>
        <NavBar :whichActive="'search'"/>
        <DataView :value="courses" :layout="'list'">
            <template #list="slotProps">
                <div class="p-col-12">
                    <div class="car-details">
                        <div>
                            <div class="p-grid">
                                <div class="p-col-4">Code: <b>{{slotProps.data.code}}</b></div>
                                <div class="p-col-4">Title: <b>{{slotProps.data.title}}</b></div>
                                <div class="p-col-4"><Button>Request</Button></div>
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
export default {
    name: "CourseSearchPage",
    components: {
        NavBar,
        DataView
    },
    data () {
        return {
            msg: 'Network Error',
            courses: null,
            state: false,
        }
    },
    mounted () {
        this.getCourses(null)
    },
    methods: {
        getCourses: function (keyword) {
            this.$axios.request({
            url: keyword ? this.$url + 'courses/search/' + keyword + '/' : this.$url + 'courses/search/',
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
        }
    }
}
</script>

<style scoped>

</style>