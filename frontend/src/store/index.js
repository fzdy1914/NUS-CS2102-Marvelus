import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    username: null,
    isAdmin: false
  },
  mutations: {
    setUsername (state, username) {
      state.username = username
    },
    isAdmin (state, isAdmin) {
      state.isAdmin = isAdmin
    }
  }
})

export default store
