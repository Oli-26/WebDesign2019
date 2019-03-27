<template>
	<div class="Airport">
        <sui-container class="ui segment title_container">
    		<h1 is="sui-header"> {{ city }}</h1>
            <h2 is="sui-header"> {{ name }}</h2>
		</sui-container>
        <sui-card-group :items-per-row="3" stackable>
            <CarrierCard v-for="carrier in carriers" :carrier="carrier" />
        </sui-card-group>
	</div>
</template>

<script>
    import { getAirports } from '../api'
    import CarrierCard from './CarrierCard'

    export default {
        props: {
            airport: {
                type: Object,
            }
        },
        components: {
            CarrierCard
        },
        data () {
            return {
                name : null,
                carriers: [],
                city: null,
            }
        },        
        created() {
            
            getAirports(this.$route.params.airportCode)
                .then(response => {
                    console.log(response.data)
                    var name_city = response.data.name.split(":")
                    this.city = name_city[0]
                    this.name = name_city[1]
                    for(var i = 0; i < response.data["uri-list"].length; i++){
                        console.log(response.data["uri-list"][i])
                        response.data.id = i;
                        this.carriers.push(response.data["uri-list"][i])
                        
                    }
                }) 
        }  
    }
    
    
    
</script>

<style>
.title_container {
    width:100% !important;
}

.airport_card {
    text-align: center;
}
</style>