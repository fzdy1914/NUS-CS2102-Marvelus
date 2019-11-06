<template>
  <div>
    <CourseSidebarMenu v-if="$route.name.indexOf('Course') >=0"/>
    <AssistSideBarMenu v-else/>
    <div class="placeholder">
      <router-view/>
    </div>
  </div>
</template>

<script>
import CourseSidebarMenu from '../../components/CourseSidebarMenu'
import AssistSideBarMenu from "../../components/AssistSidebarMenu";
export default {
  name: "CourseDetailPage",
  components:{
    AssistSideBarMenu,
    CourseSidebarMenu
  }
}
</script>

<style scoped>
.placeholder {
  width: calc(100% - 175px);
  float:right;
}
</style>