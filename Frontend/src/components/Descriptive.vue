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

    </div>
            <sui-card-group :items-per-row="2">         
              
            <sui-card>
              <sui-dimmer :active="dimmer1Active" inverted>
                <sui-loader>Loading...</sui-loader>
              </sui-dimmer>
                <sui-card-content>
                    <sui-card-header> {{this.selected1}} data </sui-card-header>
                    <div id="chart">
                      <apexchart type=pie width=350 :options="minutes1ChartOptions" :series="meanSeries" />
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
                      <apexchart type=pie width=350 :options="minutes2ChartOptions" :series="standardDSeries" />
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

</template>




<script>

    import { getAirports } from '../api'
    import { getMinutes } from '../api'
    import { getAverages } from '../api'
    
    export default {
       props: {
            month: null,
       }, 
      name: 'Loading',
      
      
        data () {
            return {

                name : "",
                airports: [],
                selected1 : null,
                selected2 : null,
                airportCode : null,
                carrierCode : null,
                
                dimmer1Active: true,
                dimmer2Active: true,
                
                meanSeries: [],
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
                
                standardDSeries: [],
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
            this.airportCode = this.$route.query.airportcode,
            this.carrierCode = this.$route.params.carrierCode,
            this.selected1 = this.$route.query.airportcode,
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
        },
        watch: {
              selected1(){
                console.log("code1 = " + this.selected1 + " code2 = " + this.selected2);
                if(this.selected1 != null && this.selected2 != null){
                    getAverages(this.carrierCode, this.selected1, this.selected2, this.monthToInt)
                        .then(response => {
                            console.log(response.data);
                        })
                }
              
              },
              selected2(){
                console.log("code1 = " + this.selected1 + " code2 = " + this.selected2);
                if(this.selected1 != null && this.selected2 != null){
                    getAverages(this.carrierCode, this.selected1, this.selected2, this.monthToInt)
                        .then(response => {
                            console.log(response.data);
                        })
                }
              },
              month(){
               if(this.selected1 != null && this.selected2 != null){
                    getAverages(this.carrierCode, this.selected1, this.selected2, this.monthToInt)
                        .then(response => {
                            console.log(response.data);
                        })
                }
              
            }
            },
        computed: {
            monthToInt() {
              if(this.month){
                var months = {
                  "January" : 1,
                  "February" : 2,
                  "March" : 3,
                  "April" : 4,
                  "May" : 5,
                  "June" : 6,
                  "July" : 7,
                  "August" : 8,
                  "Sepember" : 9,
                  "October" : 10,
                  "November" : 11,
                  "December" : 12
                }
                console.log(this.month)
                var m = this.month
                console.log(months[m])
                return months[m]
              } else {
                return "all"
              }
            }
        },


  
          
        
    }
    
    
</script>