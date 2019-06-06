<template>
  <div class="date-picker">
    <div class="date-input">
      <input class="form-control" type="text" placeholder="Since date" @focus="trueSinceDateBox" :value="sinceDate" readonly />
      <span>&nbsp;-&nbsp;</span>
      <input class="form-control" type="text" placeholder="Until date" @focus="trueUntilDateBox" :value="untilDate" readonly />
    </div>
    <transition name="fade">
      <div class="date-box" v-if="dateBoxFlag">
        <div class="day-select">
          <div>
            <button @click="reduceYear">&laquo;</button>
            <button @click="reduceMonth">&lt;</button>
          </div>
          <div>
            <input type="text" @click="selected" v-model="year" />-
            <input type="text" @click="selected" v-model="month" />
          </div>
          <div>
            <button @click="addMonth">&gt;</button>
            <button @click="addYear">&raquo;</button>
          </div>
        </div>
        <div class="day-screen">
          <div>
            <span v-for="(week, index) in weekDay" :key="index">{{ week }}</span>
          </div>
          <div @click="selectDay">
            <span v-for="day in previousMonth" class="previousMonth" :key="day"> {{ day }} </span>
            <span v-for="day in monthDay[month - 1]" v-bind:class="isActive(day)" class="currentMonth" :key="day+40">
              {{ day }}
            </span>
            <span v-for="day in nextMonth" class="nextMonth" :key="day+80">{{ day }}</span>
          </div>
        </div>
        <div class="date-clear" @click="clearDate">
          <span>clear</span>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  name: 'DoubleDatePicker',
  data () {
    return {
      dateBoxFlag: false,
      year: 0,
      month: 0,
      day: 0,
      previousMonth: [],
      nextMonth: [],
      weekDay: ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa'],
      monthDay: [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],

      isSince: true,
      sinceYear: 0,
      sinceMonth: 0,
      sinceDay: 0,
      untilYear: 0,
      untilMonth: 0,
      untilDay: 0
    }
  },
  mounted () {
    let parse = this.$util.parse
    let sinceDate = parse(this.$route.query.sinceDate)
    let untilDate = parse(this.$route.query.untilDate)
    if (sinceDate) {
      sinceDate = new Date(sinceDate)
      this.sinceYear = sinceDate.getFullYear()
      this.sinceMonth = sinceDate.getMonth() + 1
      this.sinceDay = sinceDate.getDate()
    }
    if (untilDate) {
      untilDate = new Date(untilDate - 86400000)
      this.untilYear = untilDate.getFullYear()
      this.untilMonth = untilDate.getMonth() + 1
      this.untilDay = untilDate.getDate()
    }
  },
  computed: {
    date () {
      if (this.year === 0 || this.month === 0 || this.day === 0) {
        return ''
      }
      return this.year + '-' + this.month + '-' + this.day
    },
    sinceDate () {
      if (this.sinceYear === 0 || this.sinceMonth === 0 || this.sinceDay === 0) {
        return ''
      }
      return this.sinceYear + '-' + this.sinceMonth + '-' + this.sinceDay
    },
    untilDate () {
      if (this.untilYear === 0 || this.untilMonth === 0 || this.untilDay === 0) {
        return ''
      }
      return this.untilYear + '-' + this.untilMonth + '-' + this.untilDay
    }
  },
  watch: {
    year: function (val) {
      let reg = /^[1-9]\d*$/g
      if (!reg.test(val)) {
        let date = new Date()
        this.year = date.getFullYear()
      }
      if (val < 0) {
        this.year = 1
      }
      if (val > 9999) {
        this.year = 9999
      }
      this.dayScreen()
    },
    month: function (val) {
      let reg = /^[1-9]\d*$/g
      if (!reg.test(val)) {
        let date = new Date()
        this.month = date.getMonth() + 1
      }
      if (val < 1) {
        this.month = 1
      }
      if (val > 12) {
        this.month = 12
      }
      this.dayScreen()
    }
  },
  methods: {
    clearDate () {
      if (this.isSince) {
        this.sinceYear = 0
        this.sinceMonth = 0
        this.sinceDay = 0
        this.$emit('updateSinceDate', this.sinceDate)
      } else {
        this.untilYear = 0
        this.untilMonth = 0
        this.untilDay = 0
        this.$emit('updateUntilDate', this.untilDate)
      }
      this.dateBoxFlag = false
    },
    isActive (index) {
      if (index === this.day) {
        return {
          active: true
        }
      }
    },
    trueSinceDateBox () {
      this.year = this.sinceYear
      this.month = this.sinceMonth
      this.day = this.sinceDay
      this.isSince = true
      if (this.date === '') {
        let date = new Date()
        this.year = date.getFullYear()
        if (this.isLeapYear(this.year)) {
          this.monthDay[1] = 29
        } else {
          this.monthDay[1] = 28
        }
        this.month = date.getMonth() + 1
        this.day = date.getDate()
      }
      this.dayScreen()
      this.dateBoxFlag = true
    },
    trueUntilDateBox () {
      this.year = this.untilYear
      this.month = this.untilMonth
      this.day = this.untilDay
      this.isSince = false
      if (this.date === '') {
        let date = new Date()
        this.year = date.getFullYear()
        if (this.isLeapYear(this.year)) {
          this.monthDay[1] = 29
        } else {
          this.monthDay[1] = 28
        }
        this.month = date.getMonth() + 1
        this.day = date.getDate()
      }
      this.dayScreen()
      this.dateBoxFlag = true
    },
    addYear () {
      this.year++
      if (this.isLeapYear(this.year)) {
        this.monthDay[1] = 29
      } else {
        this.monthDay[1] = 28
      }
    },
    reduceYear () {
      this.year--
      if (this.isLeapYear(this.year)) {
        this.monthDay[1] = 29
      } else {
        this.monthDay[1] = 28
      }
    },
    addMonth () {
      this.month++
      if (this.month > 12) {
        this.month = 1
        this.year++
      }
    },
    reduceMonth () {
      this.month--
      if (this.month < 1) {
        this.month = 12
        this.year--
      }
    },
    selected (e) {
      e.target.select()
    },
    selectDay (e) {
      let targetClass = e.target.className
      if (targetClass === 'previousMonth') {
        if (this.month === 1) {
          this.month = 12
          this.year--
        } else {
          this.month = this.month - 1
        }
        this.day = parseInt(e.target.innerText)
      } else if (targetClass === 'nextMonth') {
        if (this.month === 12) {
          this.month = 1
          this.year++
        } else {
          this.month = this.month + 1
        }
        this.day = parseInt(e.target.innerText)
      } else {
        this.day = parseInt(e.target.innerText)
      }
      if (this.isSince) {
        this.sinceYear = this.year
        this.sinceMonth = this.month
        this.sinceDay = this.day
        this.$emit('updateSinceDate', this.sinceDate)
      } else {
        this.untilYear = this.year
        this.untilMonth = this.month
        this.untilDay = this.day
        this.$emit('updateUntilDate', this.untilDate)
      }
      this.dateBoxFlag = false
    },
    dayScreen () {
      let firstDate = new Date(this.year, this.month - 1, 1)
      let firstWeek = firstDate.getDay()
      let preMonthDay = null
      if (this.month === 1) {
        preMonthDay = this.monthDay[11]
      } else {
        preMonthDay = this.monthDay[this.month - 2]
      }
      for (let i = 0; i < preMonthDay; i++) {
        this.previousMonth[i] = i + 1
      }
      if (firstWeek === 0) {
        this.previousMonth = this.previousMonth.slice(-7)
      } else {
        this.previousMonth = this.previousMonth.slice(-firstWeek)
      }

      let endDate = new Date(this.year, this.month - 1, this.monthDay[this.month - 1])
      let endWeek = endDate.getDay()
      let nextMonthDay = null
      if (this.month === 12) {
        nextMonthDay = this.monthDay[0]
      } else {
        nextMonthDay = this.monthDay[this.month]
      }
      for (let i = 0; i < nextMonthDay; i++) {
        this.nextMonth[i] = i + 1
      }
      if (endWeek === 6) {
        this.nextMonth = this.nextMonth.slice(0, 7)
      } else {
        this.nextMonth = this.nextMonth.slice(0, 6 - endWeek)
      }
    },
    isLeapYear (year) {
      return year % 100 === 0 ? (year % 400 === 0) : (year % 4 === 0)
    }
  }
}
</script>

<style scoped>
  .date-picker {
    width: 234px;
    padding: 5px;
    position: relative;
  }
  .date-picker > .date-input > input {
    width: 46.5%;
    margin-top: 3px;
    background-color: #FFFFFF;
    float:left;
  }
  .date-picker > .date-input > span {
    width: 7%;
    float:left;
    margin-top: 6px;
    font-size: 18px;
  }
  .date-picker > .date-input {
    top: 5px;
    background-color: #F8F8F8;
    border-color: #f8f8f8;
    height: 44px
  }
  .date-picker .fade-enter-active, .date-picker .fade-leave-active {
    transition: all 0.5s;
  }
  .date-picker .fade-enter, .date-picker .fade-leave-active {
    opacity: 0;
    transform: translateY(-10px);
  }
  .date-picker > div {
    width: 100%;
    border: 1px solid #EAEAEA;
    border-radius: 5px;
    box-shadow: 2px 2px 2px #eee;
    background: white;
    position: absolute;
    top: 50px;
    left: 0px;
    z-index: 99;
  }
  .date-picker > div div.day-select {
    display: flex;
    height: 30px;
    line-height: 30px;
    color: #888888;
    border-bottom: 1px solid #ccc;
  }
  .date-picker > div div.day-select input, div div.day-select button {
    border: none;
    background: white;
    text-align: center;
    color: #888888;
    cursor: pointer;
  }
  .date-picker > div div.day-select > div:nth-child(1), div:nth-child(3) {
    width: 25%;
    display: flex
  }
  .date-picker > div div.day-select > div:nth-child(1) button, div:nth-child(3) button {
    width: 50%;
  }
  .date-picker > div div.day-select > div:nth-child(2) {
    width: 50%;
    display: flex;
    justify-content: center;
  }
  .date-picker > div div.day-select > div:nth-child(2) input:hover {
    background: #eee;
  }
  .date-picker > div div.day-select > div:nth-child(2) input:nth-child(1) {
    width: 50px;
  }
  .date-picker > div div.day-select > div:nth-child(2) input:nth-child(2) {
    width: 30px;
  }
  .date-picker > div div.day-screen > div {
    width: 234px;
    padding: 0 5px;
    display: flex;
    font-size: 14px;
    justify-content: flex-start;
    flex-wrap: wrap;
  }
  .date-picker > div div.day-screen > div span {
    width: 32px;
    height: 30px;
    text-align: center;
    line-height: 30px;
    border-bottom: 1px solid #ccc;
  }
  .date-picker > div div.day-screen > div:nth-child(1) {
    font-weight: bold;
    background: #F8F8F8;
  }
  .date-picker > div div.day-screen > div:nth-child(2) span.previousMonth, div:nth-child(2) span.nextMonth {
    color: #888888;
  }
  .date-picker > div div.day-screen > div:nth-child(2) span.currentMonth {
    cursor: pointer;
    color: black;
  }
  .date-picker > div div.day-screen > div:nth-child(2) span:hover, div:nth-child(2) span.active {
    background: #21A5EF;
    color: white;
  }
  .date-picker > div div.date-clear {
    font-size: 15px;
    color: red;
    margin: 0 auto;
    height: 28px;
    line-height: 28px;
  }
  .date-picker > div div.date-clear:hover {
    cursor: pointer;
  }
</style>
