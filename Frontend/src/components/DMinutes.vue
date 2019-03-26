<template>
	<div class="DelaysMinutes">
		<h1>Delays Minutes</h1>
		<p>This is delays mintues page with carrierID {{ this.$route.params.carrierID }}</p>
		<router-link to="/carriers/:carrierID/statistics">Back to statistics with {{ this.$route.params.carrierID }}</router-link>
	</div>
</template>