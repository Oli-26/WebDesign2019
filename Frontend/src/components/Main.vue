<template>
	<div class="hello">
		<h1>This is our super fancy frontend.</h1>
		<p>Components are next. {{ response }}</p>
		<router-link to="/HelloWorld">Routing demonstration</router-link>
		<sui-card>
	      <img src="../assets/logo.png" />
	      <sui-card-content>
	        <sui-card-header>Card demo</sui-card-header>
	        <sui-card-meta>Joined in 2013</sui-card-meta>
	        <sui-card-description>Kristy is an art director living in New York.</sui-card-description>
	      </sui-card-content>
	      <sui-card-content extra>
	        <sui-icon name="user" />
        22 Friends</sui-card-content>
    </sui-card>
	</div>
</template>

<script>
    import { testFunction } from '../api'
    export default {
        
        data () {
            return {
                response: "None"
            }
        },        
        created() {
            this.response = testFunction()
               
        }
        
        
    }
    
    
    
</script>