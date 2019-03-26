<template>
	<div class="Airports">
		<sui-card-group :items-per-row="3">
				<sui-card class="airport_card" v-for="airport in airports">
						<sui-card-content>
							<sui-image src="static/images/airport_card.png" size="large" /><br /><br />
							<sui-card-header>
									{{ airport.city }}
							</sui-card-header>
							{{ airport.name }}
							<sui-divider />
							<router-link :to="{ path: '/Airports/' + airport.code}">
								<div>
									{{ airport.code }}
									<span slot="right">
										<sui-icon name="angle right" />
									</span>
								</div>
							</router-link>
					</sui-card-content>
				</sui-card>
		</sui-card-group>
    </div>
</template>

<script>
    import { getAirports } from '../api'
    export default {
        data () {
            return {
                airports: []
            }
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