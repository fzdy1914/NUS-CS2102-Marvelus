<template>
  <div>
    <DataTable :value="profs" :paginator="true" :rows="20" sortMode="multiple">
      <Column field="name" header="Prof Name"></Column>
      <Column field="expr" header="Experience" :sortable="true"></Column>
      <Column field="email" header="Email"></Column>
    </DataTable>
  </div>
</template>

<script>
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import ColumnGroup from 'primevue/columngroup';
export default {
  name: 'BasicProfList',
  components: {
    DataTable,
    Column,
    ColumnGroup
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
