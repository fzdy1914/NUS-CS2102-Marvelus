<template>
  <div style="font-size: 20px; text-align: left;margin-left: 15px;margin-right: 15px;">
    <DataTable :value="students" :paginator="true" :rows="20" sortMode="multiple">
      <Column field="name" header="Student Name"></Column>
      <Column field="matriculation_num" header="Matriculation number"></Column>
      <Column field="major" header="Major"></Column>
      <Column field="year" header="Year"></Column>
      <Column field="email" header="Email"></Column>
      <Column field="final_grade" header="Course Final Grade" v-if="isSelectCandidate" :sortable="true"></Column>
      <Column field="group_num" header="Year" :sortable="true" v-if="isSelectTutor"></Column>
      <Column header="operation" v-if="isProf">
        <button class="btn btn-primary approve">Appprove</button>
        <button class="btn btn-primary reject">Reject</button>
      </Column>
    </DataTable>
  </div>
</template>

<script>
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import ColumnGroup from 'primevue/columngroup';
export default {
  name: 'BasicStudentList',
  components: {
    DataTable,
    Column,
    ColumnGroup
  },
  props: {
    students: Array,
    isProf: Boolean,
    isSelectTutor: Boolean,
    isSelectCandidate: Boolean
  },
  methods: {

  }
}
</script>

<style scoped>
  .name, .major, .year {
    width: 150px;
  }
  .email, .matnum {
    width: 300px;
  }
  .operation {
    width: 200px;
  }
  .grpNum {
    width: 150px;
  }
  .reject {
    background-color: #D94600;
    border-color: #BB3D00;
  }
  .btn {
    padding: 3px 8px;
  }
</style>
