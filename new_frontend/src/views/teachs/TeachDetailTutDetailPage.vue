<template>
  <div>
    This is Tut Detail Info:
    <div>Course Code: {{ $route.params.code }}</div>
    <div>Group Num: {{ $route.params.group_num }}</div>
  </div>
</template>

<script>
export default {
  name: "TeachDetailTutDetailPage",
  data() {
    return {

    }
  },
  mounted() {

  }
}
</script>

<style scoped>

</style>