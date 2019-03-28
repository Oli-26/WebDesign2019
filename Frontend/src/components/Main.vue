<template>
	<div class="Airports">
		<p>{{ this.month }}</p>
        <div class="search">
            <sui-input type="text" v-model="searchQuery" placeholder="Search..." icon="search"></sui-input>
        </div>
		<sui-card-group id="cardgroup" :items-per-row="3">
			<AirportCard v-for="airport in filteredList" :airport="airport" :month="`${month}`" :key="airport.code" />
		</sui-card-group>
    </div>
</template>

<script>
    import { getAirports } from '../api'
    import AirportCard from './AirportCard'

    export default {
        data() {
            return {
                airports: [],
                searchQuery: ''
            }
        },   
        props: {
        	month: null
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
        },
        computed: {
            filteredList(){
                var self = this
                if(this.searchQuery){
                    return this.airports.filter(function(airport) {
                        return airport.name.toLowerCase().includes(self.searchQuery.toLowerCase());
                    })
                }else{
                   return this.airports;
                }
            }
        }  
    }
    
    
    
</script>
