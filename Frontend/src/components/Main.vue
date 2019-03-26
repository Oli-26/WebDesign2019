<template>
	<div class="Airports">
		<sui-card-group :items-per-row="3">
			<sui-card class="airport_card" v-for="airport in airports">
				<sui-card-content>
					<sui-image src="static/images/airport_card.png" size="large" /><br /><br />
					<sui-card-header> {{ airport.name }} </sui-card-header>
					<sui-divider />
					<sui-card-content extra>
						{{ airport.uri }} <span slot="right"><sui-icon name="angle right" /></span>
					</sui-card-content>
				</sui-card-content>
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
                }) 
        }  
    }
    
    
    
</script>

<style>
sui-card-header {
	height:200px !important;
}
</style>