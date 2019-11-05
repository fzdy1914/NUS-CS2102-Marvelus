<template>
  <div>
    <DataTable :value="peoples" sortMode="multiple">
      <Column field="name" header="Student Name" v-if="isShowingStudent"></Column>
      <Column field="name" header="TA Name" v-else></Column>
      <Column field="matriculation_num" header="Matriculation number"></Column>
      <Column field="major" header="Major"></Column>
      <Column field="final_grade" header="Course Final Grade" v-if="isSelectCandidate" :sortable="true"></Column>
      <Column field="year" header="Year" :sortable="true"></Column>
      <Column field="email" header="Email"></Column>
    </DataTable>
  </div>
</template>

<script>
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import ColumnGroup from 'primevue/columngroup';
export default {
  name: "StudentListDataTable",
  props: {
    isSelectCandidate: Boolean,
    peoples: Array,
    isShowingStudent: Boolean
  },
  components: {
    DataTable,
    Column,
    ColumnGroup,
  }
}
</script>

<style scoped>
</style>