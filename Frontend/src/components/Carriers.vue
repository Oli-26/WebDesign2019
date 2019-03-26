<template>
	<div class="Carriers">
		<h1>Carriers</h1>
		<p>This is carriers page with carrierID {{ this.$route.params.carrierID }}</p>
        
		<router-link to="/HelloWorld">Routing demonstration</router-link>
        
        
        <sui-card-group :items-per-row="3">
        <div v-for="carrier in carriers">  
            <a class="item" v-bind:href=carrier.uri target="_blank">    
                
                      
                    <sui-card>
                        <img src="../assets/logo.png" />
                        <sui-card-content>
                            <sui-card-header> {{carrier.name }} </sui-card-header>
                            
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
</template>


<script>
    import { getCarriers } from '../api'
    export default {
        
        data () {
            return {
                carriers : []
            }
        },        
        created() {
            
            getCarriers()
                .then(response => {
                    
                    for(var i = 0; i < response.data.length; i++){
                        console.log(response.data[i])
                        this.carriers.push(response.data[i])
                        
                    }
                    console.log(this.carriers)
                })    
        }
    }
</script>