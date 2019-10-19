<template>
    <div>
        <div v-for="course in courses">{{ course.code }}</div>
    </div>
</template>

<script>
export default {
    name: "CourseDetailPage",
    props:{
        courses:Array
    }
}
</script>

<style scoped>

</style>