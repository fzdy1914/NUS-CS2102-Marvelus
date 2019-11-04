<template>
  <div>
<!--    <table class="table table-bordered table-hover">-->
<!--      <thead>-->
<!--        <tr>-->
<!--          <th>Name</th>-->
<!--          <th>Expr</th>-->
<!--          <th>Email</th>-->
<!--          <th v-if="isProf">Operation</th>-->
<!--        </tr>-->
<!--      </thead>-->
<!--      <tbody>-->
<!--        <tr v-for="prof in profs" :key="prof.uname">-->
<!--          <td class="name">{{ prof.name }}</td>-->
<!--          <td class="expr">{{ prof.expr }}</td>-->
<!--          <td class="email">{{ prof.email }}</td>-->
<!--          <td class="operation" v-if="isProf">-->
<!--            <button class="btn btn-primary approve">Approve</button>-->
<!--            <button class="btn btn-primary reject">Reject</button>-->
<!--          </td>-->
<!--        </tr>-->
<!--      </tbody>-->
<!--    </table>-->

    <DataTable :value="profs" >
        <Column field="name" header="Prof Name"></Column>
        <Column field="expr" header="Exprience"></Column>
<!--        <Column field="email" header="Matriculation Number"></Column>-->
        <Column field="email" header="Email"></Column>
<!--        <Column field="year" header="Year"></Column>-->
    </DataTable>

  </div>
</template>

<script>
    import DataTable from 'primevue/datatable';
  import Column from 'primevue/column';
export default {
  name: 'BasicProfList',
  props: {
    profs: Array,
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
  .name, .expr {
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
