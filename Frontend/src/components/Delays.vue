<template>
	<div class="Delays">
		<h1>Delays</h1>
		<p>This is delays page with carrierID {{ this.$route.params.carrierID }}</p>
        <router-link to="/carriers/:carrierID/statistics/delays/minutes">Go to Minutes</router-link><br>
        <router-link to="/carriers/:carrierID/statistics/delays/amount">Go to Amount</router-link><br>
		<router-link to="/carriers/:carrierID/statistics">Back to carriers {{ this.$route.params.carrierID }}</router-link>
	</div>
</template>