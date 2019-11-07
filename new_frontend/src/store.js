import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    username: null,
    name: null,
    isAdmin: false,
    isProf: false,
    isTA: false
  },
  mutations: {
    setUsername (state, username) {
      state.username = username
    },
    setName (state, name) {
      state.name = name
    },
    isAdmin (state, isAdmin) {
      state.isAdmin = isAdmin
    },
    isProf (state, isProf) {
      state.isProf = isProf
    },
    isTA (state, isTA) {
      state.isTA = isTA
    }
  },
  actions: {

  }
})
