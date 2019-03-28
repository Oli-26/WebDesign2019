<template>
	<div class="Carriers">
        <div class="search">
            <sui-input type="text" v-model="searchQuery" placeholder="Search..." icon="search"></sui-input>
        </div>
        <sui-card-group :items-per-row="3" stackable>
            <CarrierCard v-for="carrier in filteredList" :carrier="carrier" />
        </sui-card-group>
	</div>
</template>


<script>
    import { getCarriers } from '../api'
    import CarrierCard from './CarrierCard'

    export default {
        components: {
            CarrierCard
        },
        props: {
            month: null
        },
        data () {
            return {
                carriers : [],
                searchQuery: ''
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
        },
        computed: {
            filteredList(){
                var self = this
                if(this.searchQuery){
                    return this.carriers.filter(function(carrier) {
                        return carrier['carrier-name'].toLowerCase().includes(self.searchQuery.toLowerCase()) | carrier['carrier-code'].toLowerCase().includes(self.searchQuery.toLowerCase());
                    })
                }else{
                   return this.carriers;
                }
            }
        }
    }
</script>