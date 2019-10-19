import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    username: null,
    isAdmin: false,
    isProf: true
  },
  mutations: {
    setUsername (state, username) {
      state.username = username
    },
    isAdmin (state, isAdmin) {
      state.isAdmin = isAdmin
    },
    isProf (state, isProf) {
      state.isProf = isProf
    }
  },
  actions: {

  }
})
