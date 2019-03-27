<template>
	<div class="Carriers">
        <sui-card-group :items-per-row="3" stackable>
            <CarrierCard v-for="carrier in carriers" :carrier="carrier"" />
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