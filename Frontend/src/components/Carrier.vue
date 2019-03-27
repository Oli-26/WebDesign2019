<template>
	<div class="Carrier">
		<h1> {{ this.carrierName }}</h1>
		<p>This is carriers page with carrierID</p>
		<router-link to="/HelloWorld">Routing demonstration</router-link>
	        
        <sui-card-group :items-per-row="3">         
              
            <sui-card>
               
                <sui-card-content>
                    <sui-card-header> Flights data </sui-card-header>
                    <div id="chart">
                      <apexchart type=pie width=380 :options="flightChartOptions" :series="series" />
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
                      <apexchart type=pie width=380 :options="flightChartOptions" :series="series" />
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
                      <apexchart type=pie width=380 :options="flightChartOptions" :series="series" />
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
    
    import { getCarriers } from '../api'
    export default {
        
        data () {
            return {
                carrierName : null,
                statisticsURI : null,
                airportURIs : [],
                
                series: [44, 55, 13, 43],
                flightChartOptions: {
                  labels: ['Ontime', 'Delayed', 'Diverted', 'Cancelled'],
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