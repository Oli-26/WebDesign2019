<template>
	<div class="Carrier">
    <p> {{ this.month }}</p>
		<h1> {{ this.carrierName }}</h1>
	        
        <sui-card-group :items-per-row="3">         
              
            <sui-card>
               
                <sui-card-content>
                    <sui-card-header> Flights data </sui-card-header>
                    <div id="chart">
                      <apexchart type=pie width=350 :options="flightChartOptions" :series="flightsSeries" />
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
               
                <sui-card-content>
                    <sui-card-header> Delays minutes data </sui-card-header>
                    <div id="chart">
                      <apexchart type=pie width=350 :options="minutesChartOptions" :series="minutesSeries" />
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
               
                <sui-card-content>
                    <sui-card-header> Delays amount data </sui-card-header>
                    <div id="chart">
                      <apexchart type=pie width=350 :options="amountChartOptions" :series="amountSeries" />
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
    
    import { getFlights } from '../api'
    import { getMinutes } from '../api'
    import { getAmount } from '../api'
    import { getCarriers } from '../api'
    export default {
        props: {
          month: null
        },
        data () {
            return {
                carrierName : null,
                statisticsURI : null,
                airportURIs : [],
                
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
        created() {
            getFlights(this.$route.params.carrierCode)
                .then(response => {
                    console.log(response.data)
                    this.flightsSeries.push(response.data["flights-data"]["cancelled"])
                    this.flightsSeries.push(response.data["flights-data"]["ontime"])
                    this.flightsSeries.push(response.data["flights-data"]["delayed"])
                    this.flightsSeries.push(response.data["flights-data"]["diverted"])
                }),
            getMinutes(this.$route.params.carrierCode)
                .then(response => {
                    console.log(response.data)
                    this.minutesSeries.push(response.data["minutes-data"]["late-aircraft"])
                    this.minutesSeries.push(response.data["minutes-data"]["carrier"])
                    this.minutesSeries.push(response.data["minutes-data"]["security"])
                    this.minutesSeries.push(response.data["minutes-data"]["weather"])
                    this.minutesSeries.push(response.data["minutes-data"]["nas"])
                }),
            getAmount(this.$route.params.carrierCode)
                .then(response => {
                    console.log(response.data)
                    this.amountSeries.push(response.data["amount-data"]["late-aircraft"])
                    this.amountSeries.push(response.data["amount-data"]["carrier"])
                    this.amountSeries.push(response.data["amount-data"]["security"])
                    this.amountSeries.push(response.data["amount-data"]["weather"])
                    this.amountSeries.push(response.data["amount-data"]["nas"])
                }),
            getCarriers(this.$route.params.carrierCode)
                .then(response => {
                    console.log(response.data)
                    this.carrierName = response.data.name
                    this.carrierURI = response.data["statistics-uri"]
                    for(var i = 0; i < response.data["airport-uris"].length; i++){
                        this.airportURIs.push(response.data["airport-uris"][i])
                        
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