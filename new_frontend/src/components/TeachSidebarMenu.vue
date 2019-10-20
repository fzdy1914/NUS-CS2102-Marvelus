<template>
  <div class="sidebar-menu">
    <div class="p-menu p-component">
      <ul class="p-menu-list p-reset">
        <li class="p-menuitem" :class="{ active: isInfoActive }" @click="goInfo()">
          <a class="p-menuitem-link">Course Info</a>
        </li>
        <li class="p-menuitem">
          <a class="p-menuitem-link">Students</a>
        </li>
        <li class="p-menuitem">
          <a class="p-menuitem-link">Requests</a>
        </li>
        <li class="p-menuitem">
          <a class="p-menuitem-link">TAs</a>
        </li>
        <li class="p-menuitem" :class="{ active: isTutActive }" @click="goTut()">
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
  name: "TeachSideBarMenu",
  computed: {
    isInfoActive: function () {
      return this.$route.name == 'TeachDetail' || this.$route.name == 'TeachDetailInfo'
    },
    isTutActive: function () {
      return this.$route.name == 'TeachDetailTut'
    },
  },
  methods: {
    goInfo: function () {
      if (this.$route.name != 'TeachDetailInfo') {
        this.$router.push({name: 'TeachDetailInfo', params: {code: this.$route.params.code}})
      }
    },
    goTut: function () {
      if (this.$route.name != 'TeachDetailTut') {
        this.$router.push({name: 'TeachDetailTut', params: {code: this.$route.params.code}})
      }
    },
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