<template>

  <div>

    This is Teach Tut List:
    <div>Code: {{ $route.params.code }}</div>

<!--    <DataTable :value="tutorials">-->
<!--      <Column field="group_num" header="Group Number"></Column>-->
<!--      <Column field="action" header="Action">-->
<!--        <Button label="View" @click="goTutorial(group_num)"/>-->
<!--      </Column>-->
<!--    </DataTable>-->

<DataView :value="tutorials" :layout="layout" :paginator="true" :rows="20" :lazy="true" >
	<template #list="tutorials" >
		<div class="p-col-12">
            <div class="car-details">
              <div class="p-col-12" >
<!--                    <img :src="'demo/images/car/' + slotProps.data.brand + '.png'" :alt="slotProps.data.brand"/>-->
                  <div class="p-grid">
                      <div class="p-col-9">Group Number: <b>{{tutorials.data.group_num}}</b></div>
                      <div class="p-col-9">TA Amount: <b></b></div>
                    <div class="p-col-3">
                        <Button  icon="pi pi-search " @click="goTutorial(tutorials.data.group_num)" ></Button>
                    </div>
                      <div class="p-col-9">Student Amount: <b></b></div>
<!--                 <div class="p-col-12">Color: <b>{{slotProps.data.color}}</b></div>-->
                  </div>
              </div>
<!--              <div class="p-col-3">-->
<!--                <Button  icon="pi pi-search "></Button>-->
<!--              </div>-->

            </div>
        </div>
	</template>
<!--	<template #grid="tutorials">-->
<!--		<div>Group Number: <b>{{tutorials.data.group_num}}</b></div>-->
<!--	</template>-->
</DataView>

  </div>

</template>

<script>
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import ColumnGroup from 'primevue/columngroup';
import Button from 'primevue/button';
import DataView from 'primevue/dataview';


export default {
  name: "TeachDetailTutListPage",
  components:{
    DataTable,
    Column,
    ColumnGroup,
    Button,
    DataView
  },
  props:{
    tutorials:Array
  },
  methods: {
    goTutorial: function (group_num) {
      console.log(group_num);
      this.$router.push({name: 'TeachDetailTutDetail', params: {group_num: group_num}})
    }
  }
  // mounted() {
  //
  // }
}
</script>

<style scoped>

</style>