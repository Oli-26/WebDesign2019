<template>
	<sui-card class="airport_card">
		<sui-card-content>
			<sui-image src="static/images/airport_card.png" size="large" /><br /><br />
			<sui-card-header>
					{{ airport.city }}
			</sui-card-header>
			{{ airport.name }}
			<sui-divider />
			<router-link :to="`/Airports/${airport['code']}`">
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
    },
  }
}

</script>