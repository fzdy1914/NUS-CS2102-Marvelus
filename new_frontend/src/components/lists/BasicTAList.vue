<template>
  <div>
<!--    <table class="table table-bordered table-hover">-->
<!--      <thead>-->
<!--        <tr>-->
<!--          <th>Name</th>-->
<!--          <th>Major</th>-->
<!--          <th>Email</th>-->
<!--          <th v-if="isProf">Operation</th>-->
<!--        </tr>-->
<!--      </thead>-->
<!--      <tbody>-->
<!--        <tr v-for="TA in TAs" :key="TA.uname">-->
<!--          <td class="name">{{ TA.name }}</td>-->
<!--          <td class="major">{{ TA.major }}</td>-->
<!--          <td class="email">{{ TA.email }}</td>-->
<!--        </tr>-->
<!--      </tbody>-->
<!--    </table>-->

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
  .name, .major {
    width: 150px;
  }
  .email {
    width: 350px;
  }
  .operation {
    width: 200px
  }
  .reject {
    background-color: #D94600;
    border-color: #BB3D00;
  }
  .btn {
    padding: 3px 8px;
  }
</style>
