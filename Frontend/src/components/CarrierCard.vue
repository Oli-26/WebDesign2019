<template>
	<sui-card class="carrier_card" >
		<sui-card-content>
			<sui-image class="carrier_image" :src="`../static/images/carriers/${carrier['carrier-code']}.png`" /><br /><br />
			<sui-card-header>
					{{ carrier['carrier-name'] }}<br />
					{{ carrier['carrier-code'] }}
			</sui-card-header>
			<sui-divider />
			<router-link v-if="code" :to="`/Carriers/${carrier['carrier-code']}?airportcode=${code}`">
				<div class="button">
					View <span slot="right"> > </span>
				</div>
			</router-link>
			<router-link v-else :to="`/Carriers/${carrier['carrier-code']}`">
				<div class="button">
					View <span slot="right"> > </span>
				</div>
			</router-link>
		</sui-card-content>
	</sui-card>
</template>

<script>
export default{
  name: "CarrierCard",
  props: {
    carrier: {
      type: Object,
      required: true,
    },
    code : {
      type : String,
    },
  },
}

</script>