import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    username: null
  },
  mutations: {
    setUsername (state, username) {
      state.username = username
    }
  }
})

export default store
