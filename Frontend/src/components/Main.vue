<template>
	<div class="Airports">
		<sui-card-group :items-per-row="3">
			<sui-card class="airport_card" v-for="(value, key) in airports">
				<sui-image src="/src/assets/airport_card.png" />
				{{ key }} ; {{ value }}
			</sui-card>
		</sui-card-group>
    </div>
</template>

<script>
    import { getAirports } from '../api'
    import AirportCard from './AirportCard';
    export default {
        
        data () {
            return {
                airports: []
            }
        },    
        components: {
    		AirportCard,
  		},    
        created() {
            
            getAirports()
                .then(response => {
                    console.log(response.data)
                    for(var i = 0; i < response.data.length; i++){
                        console.log(response.data[i].name)
                        if(response.data[i] != null){
                            this.airports.push(response.data[i])
                        }
                    }
                    //return response.data
                    
                })
               
        }
       
        
    }
    
    
    
</script>

<style>
	.airport_card {
		
	}
</style>