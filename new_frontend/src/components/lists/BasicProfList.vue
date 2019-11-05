<template>
  <div>
    <DataTable :value="profs" sortMode="multiple">
      <Column field="name" header="Prof Name"></Column>
      <Column field="expr" header="Experience" :sortable="true"></Column>
      <Column field="email" header="Email"></Column>
    </DataTable>
  </div>
</template>

<script>
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
export default {
  name: 'BasicProfList',
  components: {
    DataTable,
    Column
  },
  props: {
    profs: Array,
    isProf: Boolean
  },
  methods: {
  }
}
</script>

<style scoped>
</style>
