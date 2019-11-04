<template>
  <div class="text-font">
     {{tutorial.code}} {{tutorial.group_num}} {{tutorial.start_time}}-{{tutorial.end_time}}, {{tutorial.tut_day}}
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
    .text-font{
        font-size: 16px; text-align: left;margin-left: 15px;
    }
</style>
