<template>
	<div>
		<p>
			{{ recv_text }}
		</p>
	</div>
</template>

<script>
	export default {
		name: 'HelloWorld',
		data () {
			return {
				recv_url: 'http://localhost:8000/api/recv_api/',
				recv_text: ''
			}
		},
		created () {
			this.$http.get(this.recv_url).then(function (response) {
				this.recv_text = response.data
			}, function (response) {
				this.recv_text = 'error'
			})
		}
	}
</script>
