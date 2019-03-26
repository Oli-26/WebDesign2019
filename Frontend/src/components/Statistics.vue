<template>
	<div class="Statistics">
		<h1>Statistics</h1>
		<p>This is statistics page with carrierID {{ this.$route.params.carrierID }}</p>
		<router-link to="/carriers/:carrierID">Back to carriers {{ this.$route.params.carrierID }}</router-link>
	</div>
</template>