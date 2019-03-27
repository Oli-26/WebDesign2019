<template>
	<sui-card class="airport_card" >
		<sui-card-content>
			<sui-image :src="`../static/images/carriers/${carrier['carrier-code']}.png`" size="large" /><br /><br />
			<sui-card-header>
					{{ carrier['carrier-name'] }} | {{ carrier['carrier-code'] }}
			</sui-card-header>
			<sui-divider />
			<router-link :to="`/Carriers/${carrier['carrier-code']}`" >
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
    }
  }
}

</script>

<style>
.button {
	margin:0 auto;
	padding:0px 10px !important;
	background-color:#a3dadd !important;
	color:#FFF;
	font-weight:600;
	font-size:1.5em;
	border-radius:15%;
	border:2px solid;
}

.button:hover {
	background-color:#FFF !important;
	color:#397c7f;
	border:2px solid #397c7f;
}
</style>