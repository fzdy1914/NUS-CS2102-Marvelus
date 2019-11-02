<template>
  <div>
    <div class="course-card" v-for="course in courses" @click="goCourse(course.code)" @mousemover.native="hover = true" @mouseleave.native="hover = false">
      <div class="course-code"> {{course.code}} </div>
      <div class="course-title title-font"> {{course.title}} </div>
      <div class="course-detailed-info"> {{course.title}} </div>
    </div>
<!--    <Card>-->
<!--    <template slot="header">-->
<!--        <img alt="user header" src="demo/images/usercard.png">-->
<!--    </template>-->
<!--    <template slot="title">-->
<!--        Advanced Card-->
<!--    </template>-->
<!--    <template slot="content">-->
<!--        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Inventore sed consequuntur error repudiandae numquam deserunt-->
<!--        quisquam repellat libero asperiores earum nam nobis, culpa ratione quam perferendis esse, cupiditate neque quas!-->
<!--    </template>-->
<!--    <template slot="footer">-->
<!--        <Button icon="pi pi-check" label="Save" class="p-button-raised" />-->
<!--        <Button icon="pi pi-times" label="Cancel" class="p-button-raised p-button-secondary" style="margin-left: .5em" />-->
<!--    </template>-->
<!--</Card>-->
  </div>
</template>

<script>
export default {
  name: "TeachListPage",
  props:{
    courses:Array
  },
  methods: {
    goCourse: function (code) {
      this.$router.push({name: 'TeachDetail', params: {code: code}})
    }
  },
  data(){
    return {
      hover:false,
    };
  }
}
</script>

<style scoped>

  .title-font{
    font-weight: Bold;
    font-size: 25px;
  }
  .course-card {
    display: inline-block;
    background-color: #ffffff;
    /*border: #FFFFFF solid 1px;*/
    float: left;
    padding: 20px;
    margin: 10px;
    max-width: 280px;
    max-height: 240px;
    min-width: 210px;
    min-height: 180px;
    width: 28%;
    height: 28%;
    /*border-radius: 10px;*/
    /*background: white;*/
    /*margin: auto;*/
    /*margin-top: 5%;*/
    /*max-width: 30%;*/
    /*padding: 20px 50px;*/
    box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
    transition: all 0.3s cubic-bezier(.25,.8,.25,1);
  }
  .course-card:hover{
    background: #ffffff;
    border-top-left-radius: 10px;
    border-bottom-left-radius: 10px;
    animation-name: example;
    animation-duration: 0.25s;
    border-left: 8px solid #1976d2;
    box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22);
  }
  .course-code{
    font-size: 14px;
    color: grey;
    text-align: left;
  }
  .course-title{
    margin-top: 5px;
    /*font-size: 20px;*/
    text-align: left;
    height: 100px;
  }
  .course-detailed-info{
    font-size: 12px;
    color: grey;
    text-align: left;
    height: 50px;
  }

</style>