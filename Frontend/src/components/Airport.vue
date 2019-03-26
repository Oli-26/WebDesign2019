<template>
	<div class="hello">
		<h1> {{ name }}.</h1>
		
       
     
       <div>
       
    <sui-card-group :items-per-row="3">
        <div v-for="carrier in carriers">  
            <a class="item" v-bind:href=carrier target="_blank">    
                
                      
                    <sui-card>
                        <img src="../assets/logo.png" />
                        <sui-card-content>
                            <sui-card-header> {{carrier }} </sui-card-header>
                            
                          </sui-card-content>
                          <sui-card-content extra>
                            <sui-icon name="user" />
                            Carrier
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
                name : null,
                carriers: []
            }
        },        
        created() {
            
            getAirports(this.$route.params.airportCode)
                .then(response => {
                    console.log(response.data)
                    this.name = response.data["name"]
                    for(var i = 0; i < response.data["uri-list"].length; i++){
                        
                        this.carriers.push(response.data[i])
                        
                    }
                }) 
        }  
    }
    
    
    
</script>