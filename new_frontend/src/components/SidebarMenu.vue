<template>
    <div class="sidebar-menu">
        <Menu :model="items" />
    </div>
</template>

<script>
import Menu from 'primevue/menu'
export default {
    name: "SideBarMenu",
    components: {
        Menu
    },
    data() {
        return {
			items: [
				{
					label: 'Course Info',
					command: () => {
					}
				},
				{
					label: 'Tutorial',
					command: () => {
					}
				},
				{
					label: 'Forum',
					command: () => {
					}
				}
			]
		}
    }
}
</script>

<style scoped>
.sidebar-menu {
    display: inline-block;
    float: left;
}
</style>