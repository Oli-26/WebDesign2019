<template>
	<div class="Carrier">
		<sui-container class="ui segment title_container">
            <h2 is="sui-header">Statistics | {{ this.carrierName }}</h2>
            <h5 is="sui-header" v-if="airportCode != null">Airport: {{ this.airportCode }}</h5>
            <router-link v-if="airportCode" :to="`/Carriers/${carrierCode}/averages?airportCode=${airportCode}`" > 
              <button class="ui right floated button">Compare airports</button>
            </router-link>
            <router-link v-else :to="`/Carriers/${carrierCode}/averages`" > 
              <button class="ui right floated button">Compare Airports</button>
            </router-link>
        </sui-container>
	        
        <sui-card-group :items-per-row="3" stackable>         
              
            <sui-card>
              <sui-dimmer :active="dimmer1Active" inverted>
                <sui-loader>Loading...</sui-loader>
              </sui-dimmer>
                <sui-card-content>
                    <sui-card-header> General flight statistics </sui-card-header>
                    <div class="chart">
                      <apexchart type=pie width=350 :options="flightChartOptions" :series="flightsSeries" />
                    </div>
                    
                  </sui-card-content>
              
            </sui-card>

            <sui-card>
               <sui-dimmer :active="dimmer2Active" inverted>
                <sui-loader>Loading...</sui-loader>
              </sui-dimmer>
                <sui-card-content>
                    <sui-card-header> Delay causes (delay in minutes) </sui-card-header>
                    <div class="chart">
                      <apexchart type=pie width=350 :options="minutesChartOptions" :series="minutesSeries" />
                    </div>
                    
                  </sui-card-content>
                 
            </sui-card>
            
            
            
                      <sui-card>
               <sui-dimmer :active="dimmer3Active" inverted>
                <sui-loader>Loading...</sui-loader>
              </sui-dimmer>
                <sui-card-content>
                    <sui-card-header> Delay causes (number of delays) </sui-card-header>
                    <div class="chart">
                      <apexchart type=pie width=350 :options="amountChartOptions" :series="amountSeries" />
                    </div>
                    
                  </sui-card-content>
                
                
            </sui-card>
        </sui-card-group> 
        
        
        <sui-container class="ui">
            
        </sui-container>
        
    
    </div>
</template>

<style>
button {
  height:auto;
  padding:0px !important;
  color:#397c7f;
}
</style>


<script>
    import { getCarriers } from '../api'
    import { getFlights } from '../api'
    import { getMinutes } from '../api'
    import { getAmount } from '../api'

    export default {
        name: "carrier",
        props: {
          month: null,
        },
        data () {
            return {
                carrierCode : null,
                carrierName : null,
                statisticsURI : null,
                airportURIs : [],
                
                airportCode: null,

                dimmer1Active: true,
                dimmer2Active: true,
                dimmer3Active: true,
              
                flightsSeries: [],
                flightChartOptions: {
                  labels: ['Cancelled', 'On time', 'Delayed', 'Diverted'],
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
                
                minutesSeries: [],
                minutesChartOptions: {
                  labels: ['Late aircraft', 'Carrier', 'Security', 'Weather', 'National <br/> Aviation <br/> System'],
                  style: {
                    colors: ['red','blue','purple','black']
                  },
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
                
                amountSeries: [],
                amountChartOptions: {
                  labels: ['Late aircraft', 'Carrier', 'Security', 'Weather', 'National<br/>  Aviation<br/> System'],
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
                  "September" : 9,
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
        created (){
        
        },
        methods: {
          loadData: function (){
            this.dimmer1Active = true
            this.dimmer2Active = true
            this.dimmer3Active = true
            this.airportURIs.length = 0
            this.flightsSeries.length = []
            this.minutesSeries.length = []
            this.amountSeries.length = []
            this.carrierCode = this.$route.params.carrierCode
            this.airportCode = this.$route.query.airportcode
            // if(this.airportCode == "undefined"){
            //     this.airportCode = "None"
            // }
            console.log(this.carrierCode)
            getCarriers(this.$route.params.carrierCode)
                .then(response => {
                    this.carrierName = response.data['carrier-name']
                    console.log("carrier name = " + this.carrierName)
                    this.carrierURI = response.data["statistics-uri"]
                    for(var i = 0; i < response.data["airport-uris"].length; i++){
                        this.airportURIs.push(response.data["airport-uris"][i])
                        
                    }
                })
            getFlights(this.$route.params.carrierCode, this.$route.query.airportcode, this.monthToInt)
                .then(response => {
                    console.log(response.data)
                    this.flightsSeries.push(response.data["flights-data"]["cancelled"])
                    this.flightsSeries.push(response.data["flights-data"]["ontime"])
                    this.flightsSeries.push(response.data["flights-data"]["delayed"])
                    this.flightsSeries.push(response.data["flights-data"]["diverted"])
                    this.dimmer1Active = false
                })
            getMinutes(this.$route.params.carrierCode, this.$route.query.airportcode, this.monthToInt)
                .then(response => {
                    console.log(response.data)
                    this.minutesSeries.push(response.data["minutes-data"]["late-aircraft"])
                    this.minutesSeries.push(response.data["minutes-data"]["carrier"])
                    this.minutesSeries.push(response.data["minutes-data"]["security"])
                    this.minutesSeries.push(response.data["minutes-data"]["weather"])
                    this.minutesSeries.push(response.data["minutes-data"]["nas"])
                    this.dimmer2Active = false
                })
            getAmount(this.$route.params.carrierCode, this.$route.query.airportcode, this.monthToInt)
                .then(response => {
                    console.log(response.data)
                    this.amountSeries.push(response.data["amount-data"]["late-aircraft"])
                    this.amountSeries.push(response.data["amount-data"]["carrier"])
                    this.amountSeries.push(response.data["amount-data"]["security"])
                    this.amountSeries.push(response.data["amount-data"]["weather"])
                    this.amountSeries.push(response.data["amount-data"]["nas"])
                    this.dimmer3Active = false
                })
          }
        },
        watch: {
          month: function() {
            this.loadData();
          }
        },
        created() {
            this.loadData();
        }
        
    }
</script>