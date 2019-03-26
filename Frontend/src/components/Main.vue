<template>
	<div class="hello">
		<h1>This is our super fancy frontend.</h1>
		<p>Components are next. </p>
		<router-link to="/HelloWorld">Routing demonstration</router-link>
       
     
       <div>
       
    <sui-card-group :items-per-row="3">
        <div v-for="airport in airports">  
            <a class="item" v-bind:href=airport.uri target="_blank">    
                
                      
                    <sui-card>
                        <img src="../assets/logo.png" />
                        <sui-card-content>
                            <sui-card-header> {{airport.name }} </sui-card-header>
                            
                          </sui-card-content>
                          <sui-card-content extra>
                            <sui-icon name="user" />
                            Airport
                            </sui-card-content>
                        
                    </sui-card>
                
               
            </a>    
        </div>
     </sui-card-group>
  </div>
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
                        if(response.data[i] != null){
                            this.airports.push(response.data[i])
                        }
                    }
                }) 
        }  
    }
    
    
    
</script>