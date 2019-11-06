<template>
  <div>
    <div class="title-font">Tut Detail Info:</div>
    <div class="text-font">
     {{tutorial.code}} {{tutorial.group_num}} {{tutorial.start_time}}-{{tutorial.end_time}}, {{tutorial.tut_day}}
    </div>
  </div>

</template>


<script>
export default {
  name: "TutorialBasicInfo",
  props: {
    tutorial: null
  }
}
</script>

<style scoped>
</style>
