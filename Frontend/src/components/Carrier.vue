<template>
	<div class="Carriers">
		<h1>Carriers</h1>
		<p>This is carriers page with carrierID {{ this.$route.params.carrierID }}</p>
		<router-link to="/HelloWorld">Routing demonstration</router-link>
	</div>
</template>


<script>
    import { getAirports } from '../api'
    export default {
        
        data () {
            return {
                uris : []
            }
        },        
        created() {
            
            getCarriers(this.$route.params.carrierID)
                .then(response => {
                    console.log(response.data)
                    for(var i = 0; i < response.data.length; i++){
                        
                        
                    }
                })    
        }
    }
</script>