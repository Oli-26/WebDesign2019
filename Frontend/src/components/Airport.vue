<template>
	<div class="Airport">
        <sui-segment class="title_container_carriers" >
            <h1 is="sui-header" style="display:inline">Carriers | {{ city }}</h1>
            <div class="search">
                <sui-input type="text" v-model="searchQuery" placeholder="Search..." icon="search"></sui-input>
            </div>
            <h3 is="sui-header">{{ name }}</h3>
        </sui-segment>
        <sui-card-group class="card_group" :items-per-row="3" stackable>
            <CarrierCard v-for="carrier in filteredList" :carrier="carrier" :code="code" />
        </sui-card-group>
	</div>
</template>

<script>
    import { getAirports } from '../api'
    import CarrierCard from './CarrierCard'

    export default {
        props: {
            month: null,
            airport: {
                type: Object,
            },
        },
        components: {
            CarrierCard
        },
        data () {
            return {
                name : null,
                carriers: [],
                city: null,
                searchQuery: '',
                code : null,
            }
        },        
        created() {
            this.code = this.$route.params.airportCode,
            getAirports(this.$route.params.airportCode)
                .then(response => {
                    console.log(response.data)
                    var name_city = response.data.name.split(":")
                    this.city = name_city[0]
                    this.name = name_city[1]
                    for(var i = 0; i < response.data["uri-list"].length; i++){
                        console.log(response.data["uri-list"][i])
                        response.data.id = i;
                        this.carriers.push(response.data["uri-list"][i])
                        
                    }
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