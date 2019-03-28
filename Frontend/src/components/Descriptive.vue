<template lang="html">
  <div>
        <div class="dropdown1">
          <sui-dropdown 
            
            fluid
            :options="airports"
            placeholder="Select Primary Airport"
            search
            selection
            v-model="selected2"
          />    
        </div>
        <div class="dropdown2">
          <sui-dropdown
            fluid
            :options="airports"
            placeholder="Select Secondary Airport"
            search
            selection
            v-model="selected1"
          />
      </div>
  
  </div>
</template>




<script>

    import { getAirports } from '../api'
    import { getFlights } from '../api'
    
    export default {
        
      name: 'Loading',
      current: null,
      
      
        data () {
            return {

                name : "",
                airports: [],
                selected1 : null,
                selected2 : null,
                airportCode : null,
            }
        },        
        created() {
            airportCode : this.$route.query.airportcode;
            getAirports()
                .then(response => {
                    console.log(response.data)
                    for(var i = 0; i < response.data.length; i++){
                        console.log(response.data[i].name)
                        var name_city = response.data[i].name.split(":")
                        //response.data[i].city = name_city[0]
                        //response.data[i].name = name_city[1]
                        response.data[i].code = response.data[i].uri.substring(10,13);
                        this.airports.push({key : response.data[i].code, value : response.data[i].code, text: response.data[i].name})
                    }
                }) 
        }
       
        
    }
    
    
</script>