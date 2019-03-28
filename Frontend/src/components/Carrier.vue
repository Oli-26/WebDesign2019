<template>
	<div class="Carrier">
    <p> {{ this.month }}</p>
		<sui-container class="ui segment title_container">
            <h2 is="sui-header"> {{ this.carrierName }}</h2>
    </sui-container>
	        
        <sui-card-group :items-per-row="3">         
              
            <sui-card>
              <sui-dimmer :active="dimmer1Active" inverted>
                <sui-loader>Loading...</sui-loader>
              </sui-dimmer>
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
               <sui-dimmer :active="dimmer2Active" inverted>
                <sui-loader>Loading...</sui-loader>
              </sui-dimmer>
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
               <sui-dimmer :active="dimmer3Active" inverted>
                <sui-loader>Loading...</sui-loader>
              </sui-dimmer>
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
                monthInt : null,

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
            monthsToInt() {
              var months = {
                'January' : '01',
                'February' : '02',
                'March' : '03',
                'April' : '04',
                'May' : '05',
                'June' : '06',
                'July' : '07',
                'August' : '08',
                'Sepember' : '09',
                'October' : '10',
                'November' : '11',
                'December' : '12'
            }
                console.log(this.month)
                var m = this.month
                console.log(months.m)
                return months.m
            
            }
         
       
        
        },
        created() {
            getCarriers(this.$route.params.carrierCode)
                .then(response => {
                    console.log(response.data)
                    this.carrierName = response.data['carrier-name']
                    this.carrierURI = response.data["statistics-uri"]
                    for(var i = 0; i < response.data["airport-uris"].length; i++){
                        this.airportURIs.push(response.data["airport-uris"][i])
                        
                    }
                }),
            getFlights(this.$route.params.carrierCode, "None", this.monthToInt)
                .then(response => {
                    console.log(response.data)
                    this.flightsSeries.push(response.data["flights-data"]["cancelled"])
                    this.flightsSeries.push(response.data["flights-data"]["ontime"])
                    this.flightsSeries.push(response.data["flights-data"]["delayed"])
                    this.flightsSeries.push(response.data["flights-data"]["diverted"])
                    this.dimmer1Active = false
                }),
            getMinutes(this.$route.params.carrierCode, "None", this.monthsToInt)
                .then(response => {
                    console.log(response.data)
                    this.minutesSeries.push(response.data["minutes-data"]["late-aircraft"])
                    this.minutesSeries.push(response.data["minutes-data"]["carrier"])
                    this.minutesSeries.push(response.data["minutes-data"]["security"])
                    this.minutesSeries.push(response.data["minutes-data"]["weather"])
                    this.minutesSeries.push(response.data["minutes-data"]["nas"])
                    this.dimmer2Active = false
                }),
            getAmount(this.$route.params.carrierCode, "None", this.monthsToInt)
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
        
    }
</script>