<template>
  <div>
    <DataTable :value="TAs" >
        <Column field="name" header="TA Name"></Column>
        <Column field="major" header="Major"></Column>
        <Column field="matriculation_num" header="Matriculation Number"></Column>
        <Column field="email" header="Email"></Column>
        <Column field="year" header="Year"></Column>
    </DataTable>
  </div>
</template>

<script>
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
export default {
  name: 'BasicTAList',
  props: {
    TAs: Array,
    isProf: Boolean
  },
  components:{
    DataTable,
    Column,
  },
  methods: {
  }
}
</script>

<style scoped>
</style>
