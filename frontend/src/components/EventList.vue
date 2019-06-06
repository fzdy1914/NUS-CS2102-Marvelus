<template>
  <div>
    <table class="table table-bordered table-hover">
      <thead>
        <tr>
          <th>ID</th>
          <th>Title</th>
          <th>Date</th>
          <th>Channel</th>
          <th>Likes</th>
          <th v-if="isAdmin">Operation</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="event in events" :key="event.id">
          <td class="id">{{ event.id }}</td>
          <td class="title"><a @click="goEvent(event.id)">{{ event.title }}</a></td>
          <td class="date">{{ $util.getDate(event.timestamp) }}</td>
          <td class="channel">{{ event.channel }}</td>
          <td class="likes">{{ event.likes }}</td>
          <td class="operation" v-if="isAdmin">
            <button class="btn btn-primary edit" @click="editEvent(event.id)">Edit</button>
            <button class="btn btn-primary delete" data-toggle="modal" data-target="#deleteEvent" @click="loadEvent(event)">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'EventList',
  props: {
    events: Array,
    isAdmin: Boolean
  },
  methods: {
    goEvent: function (eventId) {
      this.$router.push({
        name: 'Event',
        params: {
          eventId: eventId
        },
        query: {
          startPage: 1,
          currentPage: 1
        }
      })
    },
    editEvent: function (eventId) {
      this.$emit('editEvent', eventId)
    },
    loadEvent: function (event) {
      this.$emit('loadEvent', event)
    }
  }
}
</script>

<style scoped>
  .id, .date, .channel {
    width: 150px;
  }
  .title {
    width: 550px;
  }
  .likes {
    width: 100px;
  }
  .operation {
    width: 200px
  }
  .delete {
    background-color: #D94600;
    border-color: #BB3D00;
  }
  .btn {
    padding: 3px 8px;
  }
</style>
