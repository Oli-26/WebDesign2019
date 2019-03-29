<template>
	<sui-card class="airport_card" >
		<sui-card-content>
			<sui-image :src="`../static/images/carriers/${carrier['carrier-code']}.png`" size="large" /><br /><br />
			<sui-card-header>
					{{ carrier['carrier-name'] }} | {{ carrier['carrier-code'] }}
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
	border-radius:25px;
	border:2px solid;
	transition:.1s;
}

.button:hover {
	background-color:#FFF !important;
	color:#397c7f;
	border:2px solid #397c7f;
}
</style>