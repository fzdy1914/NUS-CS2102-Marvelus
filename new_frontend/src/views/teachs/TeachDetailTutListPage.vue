<template>
  <div>
    <div style="margin-bottom: 20px" class="title-font">This is all tutorials:</div>
      <DataView :value="tutorials" :layout="'list'" :lazy="true" >
        <template #list="tutorials" >
          <div class="p-col-12">
            <div class="tutorial-details">
              <div class="p-col-12" >
                <div class="p-grid">
                    <div class="p-col-9">Group Number: <b>{{tutorials.data.group_num}}</b></div>
                    <div class="p-col-9">TA Amount: <b>{{tutorials.data.TAAmount}}</b></div>
                  <div class="p-col-3">
                      <Button  icon="pi pi-search " @click="goTutorial(tutorials.data.group_num)" ></Button>
                  </div>
                    <div class="p-col-9">Student Amount: <b>{{tutorials.data.stuAmount}}</b></div>
                  <div class="p-col-9">Time: <b>{{tutorials.data.start_time}}-{{tutorials.data.end_time}}, {{tutorials.data.tut_day}}</b></div>
                </div>
              </div>
            </div>
          </div>
        </template>
      </DataView>
  </div>
</template>

<script>
import Button from 'primevue/button';
import DataView from 'primevue/dataview';
import Paginator from 'primevue/paginator';

export default {
  name: "TeachDetailTutListPage",
  components:{
    Button,
    DataView,
    Paginator
  },
  props:{
    tutorials:Array
  },
  methods: {
    goTutorial: function (group_num) {
      this.$router.push({name: 'TeachDetailTutDetail', params: {group_num: group_num}})
    }
  }
}
</script>

<style scoped>
.tutorial-details {
  border-bottom: 1px solid #d9dad9;
}
</style>