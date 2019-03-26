<template>
	<div class="DelaysAmount">
		<h1>Delays Amount</h1>
		<p>This is delays amount page with carrierID {{ this.$route.params.carrierID }}</p>
		<router-link to="/carriers/:carrierID/statistics">Back to statistics with {{ this.$route.params.carrierID }}</router-link>
	</div>
</template>