<template>
	<div class="Airports">
		<p>{{ this.month }}</p>
		<sui-card-group :items-per-row="3" stackable>
			<AirportCard v-for="airport in airports" :airport="airport" :month="`${month}`" :key="airport.code" />
		</sui-card-group>
    </div>
</template>

<script>
    import { getAirports } from '../api'
    import AirportCard from './AirportCard'

    export default {
        data () {
            return {
                airports: []
            }
        },   
        props: {
        	month: null,
        },
        components: {
        	AirportCard
        },
        created() {
            
            getAirports()
                .then(response => {
                    console.log(response.data)
                    for(var i = 0; i < response.data.length; i++){
                        console.log(response.data[i].name)
                        var name_city = response.data[i].name.split(":")
                        response.data[i].city = name_city[0]
                        response.data[i].name = name_city[1]
                        response.data[i].code = response.data[i].uri.substring(10,13);
                        if(response.data[i] != null){
                            this.airports.push(response.data[i])
                        }
                    }
                }) 
        }  
    }
    
    
    
</script>

<style>
.airport_card {
	text-align: center;
}
</style>