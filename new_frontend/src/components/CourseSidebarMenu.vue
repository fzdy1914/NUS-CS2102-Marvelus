<template>
  <div class="sidebar-menu">
    <div class="p-menu p-component">
      <ul class="p-menu-list p-reset">
        <li class="p-menuitem" :class="{ active: isInfoActive }" @click="goInfo()">
          <a class="p-menuitem-link ">Course Info</a>
        </li>
        <li class="p-menuitem" :class="{ active: isTutActive }" @click="goTut()">
          <a class="p-menuitem-link " >Tutorial</a>
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
  name: "CourseSideBarMenu",
  computed: {
    isInfoActive: function () {
      return this.$route.name == 'CourseDetail' || this.$route.name == 'CourseDetailInfo'
    },
    isTutActive: function () {
      return this.$route.name == 'CourseDetailTut'
    },
  },
  methods: {
    goInfo: function () {
      if (this.$route.name != 'CourseDetailInfo') {
        this.$router.push({name: 'CourseDetailInfo', params: {code: this.$route.params.code}})
      }
    },
    goTut: function () {
      if (this.$route.name != 'CourseDetailTut') {
        this.$router.push({name: 'CourseDetailTut', params: {code: this.$route.params.code}})
      }
    },
  }
}
</script>

<style scoped>
.sidebar-menu {
  display: inline-block;
  float: left;
  /*font-family: Arial Rounded MT;*/
}

.active {
  background-color: #dedede;
}
</style>