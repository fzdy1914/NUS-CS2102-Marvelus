<template>
  <div>
    <div v-if="state">
      <table class="table table-bordered table-hover">
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Operation</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="channel in channels" :key="channel.id">
            <td class="id">{{ channel.id }}</td>
            <td class="name"><a @click="goEvents(channel.id)">{{ channel.name }}</a></td>
            <td class="operation">
              <button class="btn btn-primary edit" data-toggle="modal" data-target="#editChannel" @click="loadChannel(channel, true)">Edit</button>
              <button class="btn btn-primary delete" data-toggle="modal" data-target="#editChannel" @click="loadChannel(channel, false)">Delete</button>
            </td>
          </tr>
        </tbody>
      </table>
      <nav>
        <ul class="pagination">
          <li v-bind:class="{ disabled: startPage === 1 }">
            <a @click="startPage=prevPage"><span>&laquo;</span></a>
          </li>
          <li v-for="index in indexArray" :key="index" :class="{ active: index === currentPage}">
            <a @click="goPage(index)">{{ index }}</a>
          </li>
          <li v-bind:class="{ disabled: endPage === maxPage }">
            <a @click="startPage=nextPage"><span>&raquo;</span></a>
          </li>
        </ul>
      </nav>
      <div class="modal fade" id="editChannel" tabindex="-1" role="dialog" aria-hidden="true">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <button type="button" class="close" data-dismiss="modal">&times;</button>
              <h4 v-if="isEdit" class="modal-title">
                Edit the channel
              </h4>
              <h4 v-else class="modal-title">
                Delete the channel
              </h4>
            </div>
            <div class="modal-body">
              <form>
                <div class="form-group">
                  <label>Id: {{ channelId }}</label>
                </div>
                <div v-show="error" class="form-group error">
                  <label>Error: {{ error }}</label>
                </div>
                <div class="form-group">
                  <label>Name</label>
                  <input v-if="isEdit" type="text" class="form-control" placeholder="Channel Name" v-model="channelName"/>
                  <p v-else>{{ channelName }}</p>
                </div>
              </form>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-default" data-dismiss="modal" id="close">Close</button>
              <button v-if="isEdit" type="button" class="btn btn-primary" @click="submit">Submit</button>
              <button v-else type="button" class="btn btn-primary delete" @click="deleteChannel">Delete</button>
            </div>
            </div>
        </div>
      </div>
    </div>
    <div v-else>
      <h3>{{ msg }}</h3>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AdminChannelList',
  data () {
    return {
      msg: 'Network Error',
      channels: null,
      count: null,
      state: false,

      offset: 0,
      limit: 10,
      startPage: 1,
      currentPage: 1,

      channelId: '',
      channelName: '',
      error: null,
      isEdit: true
    }
  },
  mounted () {
    let parse = this.$util.parse
    this.startPage = parse(this.$route.query.startPage) || 1
    this.currentPage = parse(this.$route.query.currentPage) || 1
    this.offset = parse(this.$route.query.offset)
    this.updateChannelList()
  },
  methods: {
    goPage: function (index) {
      this.$router.push({
        name: 'AdminChannelList',
        query: {
          offset: (index - 1) * this.limit,
          limit: this.limit,
          currentPage: index,
          startPage: this.startPage
        }
      })
    },
    goEvents: function (channelId) {
      this.$router.push({
        name: 'AdminEventList',
        query: {
          channelId: channelId,
          startPage: 1,
          currentPage: 1
        }
      })
    },
    updateChannelList: function () {
      this.$axios.request({
        url: this.$url + 'channels/',
        method: 'GET',
        params: {
          'offset': this.offset,
          'limit': this.limit
        }
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.state = true
          this.channels = data.data.channels
          this.count = data.data.count
        } else {
          this.state = false
          this.msg = data.error
        }
      })
    },
    submit: function () {
      this.$axios.request({
        url: this.$url + 'channels/',
        method: 'POST',
        data: {
          id: this.channelId,
          name: this.channelName
        }
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.replaceChannel(data.data.channel)
          this.channelId = ''
          this.channelName = ''
          this.error = null
          document.getElementById('close').click()
        } else {
          this.error = data.error
        }
      })
    },
    deleteChannel: function () {
      this.$axios.request({
        url: this.$url + 'channels/',
        method: 'DELETE',
        data: {
          id: this.channelId
        }
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.removeChannel()
          this.channelId = ''
          this.channelName = ''
          this.error = null
          document.getElementById('close').click()
        } else {
          this.error = data.error
        }
      })
    },
    loadChannel: function (channel, isEdit) {
      this.isEdit = isEdit
      this.channelId = channel.id
      this.channelName = channel.name
    },
    replaceChannel: function (channel) {
      for (let i = 0; i < this.channels.length; i++) {
        if (this.channels[i].id === channel.id) {
          this.channels.splice(i, 1, channel)
        }
      }
    },
    removeChannel: function () {
      for (let i = 0; i < this.channels.length; i++) {
        if (this.channels[i].id === this.channelId) {
          this.channels.splice(i, 1)
        }
      }
    }
  },
  watch: {
    '$route' (to, from) {
      let parse = this.$util.parse
      this.offset = parse(to.query.offset)
      this.channelId = parse(to.query.channelId)
      if (to.query.startPage) {
        this.startPage = parse(to.query.startPage)
      }
      if (to.query.currentPage) {
        this.currentPage = parse(to.query.currentPage)
      }
      this.updateChannelList()
    }
  },
  computed: {
    maxPage: function () {
      return Math.ceil(this.count / this.limit)
    },
    endPage: function () {
      return this.startPage + 9 < this.maxPage ? this.startPage + 9 : this.maxPage
    },
    prevPage: function () {
      return this.startPage - 10 < 1 ? 1 : this.startPage - 10
    },
    nextPage: function () {
      return this.endPage === this.maxPage ? this.startPage : this.endPage + 1
    },
    indexArray: function () {
      return this.$util.generateArray(this.startPage, this.endPage)
    }
  }
}
</script>

<style scoped>
  .id {
    width: 100px;
  }
  .name {
    width: 600px;
  }
  .operation {
    width: 200px;
  }
  .delete {
    background-color: #D94600;
    border-color: #BB3D00;
  }
  .btn {
    padding: 3px 8px;
  }
  .error {
    color: #D94600;
  }
</style>
