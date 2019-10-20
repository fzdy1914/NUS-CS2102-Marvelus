<template>
  <div class="sidebar-menu">
    <div class="p-menu p-component">
      <ul class="p-menu-list p-reset">
        <li class="p-menuitem" :class="{ active: isInfoActive}">
          <a class="p-menuitem-link">Course Info</a>
        </li>
        <li class="p-menuitem">
          <a class="p-menuitem-link">Tutorial</a>
        </li>
        <li class="p-menuitem">
          <a class="p-menuitem-link">Forum</a>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: "SideBarMenu",
  computed: {
    isInfoActive: function () {
      return this.$route.name == 'CourseDetail' || this.$route.name == 'CourseDetailInfo'
        || this.$route.name == 'AssistDetail' || this.$route.name == 'AssistDetailInfo'
    }
  }
}
</script>

<style scoped>
.sidebar-menu {
  display: inline-block;
  float: left;
}
.active {
  background-color: #dedede;
}
</style>