<template>
	<div class="Flights">
		<h1>Flights</h1>
		<p>This is flights page with carrierID {{ this.$route.params.carrierID }}</p>
		<router-link to="/carriers/:carrierID/statistics">Back to statistics with {{ this.$route.params.carrierID }}</router-link>
	</div>
</template>