<template>
	<div class="Carriers">
		<h1>Carriers</h1>
		<p>This is carriers page with carrierID {{ this.$route.params.carrierCode }}  name : {{ this.carrierName }}</p>
		<router-link to="/HelloWorld">Routing demonstration</router-link>
	</div>
</template>


<script>
    import { getCarriers } from '../api'
    export default {
        
        data () {
            return {
                carrierName : null,
                statisticsURI : null,
                airportURIs : []
            }
        },        
        created() {
            
            getCarriers(this.$route.params.carrierCode)
                .then(response => {
                    console.log(response.data)
                    this.carrierName = response.data.name
                    this.carrierURI = response.data["statistics-uri"]
                    for(var i = 0; i < response.data["airport-uris"].length; i++){
                        this.airportURIs.push(reponse.data["airport-uris"][i])
                        
                    }
                })    
        }
    }
</script>