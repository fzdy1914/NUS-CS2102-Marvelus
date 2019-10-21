<template>
  <div class="sidebar-menu">
    <div class="p-menu p-component">
      <ul class="p-menu-list p-reset">
        <li class="p-menuitem" :class="{ active: isInfoActive }" @click="goInfo()">
          <a class="p-menuitem-link">Course Info</a>
        </li>
        <li class="p-menuitem" :class="{ active: isStudentActive }" @click="goStudent()">
          <a class="p-menuitem-link">Students</a>
        </li>
        <li class="p-menuitem">
          <a class="p-menuitem-link">Requests</a>
        </li>
        <li class="p-menuitem">
          <a class="p-menuitem-link">TAs</a>
        </li>
        <li class="p-menuitem" :class="{ active: isTutActive }" @click="goTuts()">
          <a class="p-menuitem-link">Tutorials</a>
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
      return this.$route.name == 'TeachDetailTutList' || this.$route.name == 'TeachDetailTutDetail'
    },
    isStudentActive: function () {
      return this.$route.name == 'TeachDetailStudent'
    },
  },
  methods: {
    goInfo: function () {
      if (this.$route.name != 'TeachDetailInfo') {
        this.$router.push({name: 'TeachDetailInfo', params: {code: this.$route.params.code}})
      }
    },
    goTuts: function () {
      if (this.$route.name != 'TeachDetailTutList') {
        this.$router.push({name: 'TeachDetailTutList', params: {code: this.$route.params.code}})
      }
    },
    goStudent: function () {
      if (this.$route.name != 'TeachDetailStudent') {
        this.$router.push({name: 'TeachDetailStudent', params: {code: this.$route.params.code}})
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