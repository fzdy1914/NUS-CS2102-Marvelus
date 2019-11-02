<template>
  <div>
    <div style="font-size: 20px; text-align: left;margin-left: 15px; font-weight: bold;">This is all tutorials:</div>
      <DataView :value="tutorials" :layout="'list'" :paginator="true" :rows="20" :lazy="true" >
        <template #list="tutorials" >
          <div class="p-col-12">
            <div class="car-details">
              <div class="p-col-12" >
                <div class="p-grid">
                    <div class="p-col-9">Group Number: <b>{{tutorials.data.group_num}}</b></div>
                    <div class="p-col-9">TA Amount: <b>{{tutorials.data.TAAmount}}</b></div>
                  <div class="p-col-3">
                      <Button  icon="pi pi-search " @click="goTutorial(tutorials.data.group_num)" ></Button>
                  </div>
                    <div class="p-col-9">Student Amount: <b>{{tutorials.data.stuAmount}}</b></div>
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

/*  body .p-paginator .p-paginator-pages .p-paginator-page.p-highlight {*/
/*    background-color: #9c1b1b;*/
/*    color: #ffffff;*/
/*}*/
</style>