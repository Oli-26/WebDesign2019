<template>
	<sui-card class="airport_card" >
		<sui-card-content>
			<sui-image src="static/images/airport_card.png" size="large" /><br /><br />
			<sui-card-header>
					{{ airport.city }}
			</sui-card-header>
			{{ airport.name }}
			<sui-divider />
			<router-link :to="`/Airports/${airport['code']}`" >
				<div class="button">
					{{ airport.code }} <span slot="right"> > </span>
				</div>
			</router-link>
		</sui-card-content>
	</sui-card>
</template>

<script>
export default{
  name: "AirportCard",
  props: {
    airport: {
      type: Object,
      required: true,
    }
  }
}

</script>

<style>
.button {
	margin:0 auto;
	width:10em;
	height:2em;
	line-height:2em;
	background-color:#a3dadd !important;
	color:#FFF;
	font-weight:600;
	font-size:14pt;
	border-radius:15%;
	border:2px solid;
	transition:.1s;
}

.button:hover {
	background-color:#FFF !important;
	color:#397c7f;
	border:2px solid #397c7f;
}

</style>