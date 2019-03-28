<template lang="html">
  <div>
        <div class="dropdown1">
          <sui-dropdown 
            
            fluid
            :options="airports"
            placeholder="Select Primary Airport"
            search
            selection
            v-model="selected1"
          />    
        </div>
        <div class="dropdown2">
          <sui-dropdown
            fluid
            :options="airports"
            placeholder="Select Secondary Airport"
            search
            selection
            v-model="selected2"
          />
      </div>
      <p></p>
      <div>
      <sui-card-group :items-per-row="2">         
              
            <sui-card>
              <sui-dimmer :active="dimmer1Active" inverted>
                <sui-loader>Loading...</sui-loader>
              </sui-dimmer>
                <sui-card-content>
                    <sui-card-header> {{this.selected1}} data </sui-card-header>
                    <div id="chart">
                      <apexchart type=pie width=350 :options="minutes1ChartOptions" :series="minutes1Series" />
                    </div>
                    
                  </sui-card-content>
                  <sui-card-content extra>
                    <sui-icon name="user" />
                    <router-link :to="{path: '/Carriers' }">  
                      link
                    </router-link>
                    </sui-card-content>
            </sui-card>
          
            <sui-card>
              <sui-dimmer :active="dimmer2Active" inverted>
                <sui-loader>Loading...</sui-loader>
              </sui-dimmer>
                <sui-card-content>
                    <sui-card-header> {{this.selected2}} data </sui-card-header>
                    <div id="chart">
                      <apexchart type=pie width=350 :options="minutes2ChartOptions" :series="minutes2Series" />
                    </div>
                    
                  </sui-card-content>
                  <sui-card-content extra>
                    <sui-icon name="user" />
                    <router-link :to="{path: '/Carriers' }">  
                      link
                    </router-link>
                    </sui-card-content>
            </sui-card>
        </sui-card-group>
    </div>
      
      
  </div>

</template>




<script>

    import { getAirports } from '../api'
    import { getMinutes } from '../api'
    
    export default {
        
      name: 'Loading',
      
      
        data () {
            return {

                name : "",
                airports: [],
                selected1 : null,
                selected2 : null,
                airportCode : null,
                
                dimmer1Active: true,
                dimmer2Active: true,
                
                minutes1Series: [],
                minutes1ChartOptions: {
                  labels: ['Late aircraft', 'Carrier', 'Security', 'Weather', 'National <br/> Aviation <br/> System'],
                  responsive: [{
                    breakpoint: 480,
                    options: {
                      chart: {
                        width: 200
                      },
                      legend: {
                        position: 'bottom'
                      }
                    }
                  }]
                },
                
                minutes2Series: [],
                minutes2ChartOptions: {
                  labels: ['Late aircraft', 'Carrier', 'Security', 'Weather', 'National <br/> Aviation <br/> System'],
                  responsive: [{
                    breakpoint: 480,
                    options: {
                      chart: {
                        width: 200
                      },
                      legend: {
                        position: 'bottom'
                      }
                    }
                  }]
                }
                
            }
        },        
        created() {
            airportCode : this.$route.query.airportcode;
            selected2 : this.$route.query.airportcode;
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
                }),
            
            getMinutes(this.selected1, this.$route.query.airportcode, this.monthToInt)
                .then(response => {
                    console.log(response.data)
                    this.minutes1Series.push(response.data["minutes-data"]["late-aircraft"])
                    this.minutes1Series.push(response.data["minutes-data"]["carrier"])
                    this.minutes1Series.push(response.data["minutes-data"]["security"])
                    this.minutes1Series.push(response.data["minutes-data"]["weather"])
                    this.minutes1Series.push(response.data["minutes-data"]["nas"])
                    this.dimmer1Active = false
                }),
            getMinutes(this.selected2, this.$route.query.airportcode, this.monthToInt)
                .then(response => {
                    console.log(response.data)
                    this.minutes2Series.push(response.data["minutes-data"]["late-aircraft"])
                    this.minutes2Series.push(response.data["minutes-data"]["carrier"])
                    this.minutes2Series.push(response.data["minutes-data"]["security"])
                    this.minutes2Series.push(response.data["minutes-data"]["weather"])
                    this.minutes2Series.push(response.data["minutes-data"]["nas"])
                    this.dimmer2Active = false
                })
        }
       
        
    }
    
    
</script>