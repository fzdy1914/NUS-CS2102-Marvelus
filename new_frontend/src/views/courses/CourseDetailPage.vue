<template>
  <div>
    <SidebarMenu/>
    <div class="placeholder">
      <router-view/>
    </div>
  </div>
</template>

<script>
import SidebarMenu from '../../components/SidebarMenu'
export default {
  name: "CourseDetailPage",
  components:{
    SidebarMenu
  }
}
</script>

<style scoped>
.placeholder {
  width: calc(100% - 175px);
  float:right;
}
</style>