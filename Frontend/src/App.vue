<template>
  <div id="app">
    <div id="header">
      <div id="top_line"></div>
      <div id="main_header">
        <div id="logo_container"><img id="logo" src="./assets/temp_logo.png" /></div>
        <div id="breadcrumb_container">
          <strong>Home</strong> / Airports
        </div>
      </div>
    </div>
    <div id="content">
      <div id="left">
        
        <p>{{ date.month }} / {{  date.year  }}</p>
        <month-picker @change="showDate"></month-picker>
        
      </div>
    </div>
    <router-view id="view"/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  margin:0;
  padding:0;
}

#logo_header {
  width:100%;
}

#top_line {
  height:20px;
  background-color: #397c7f;
}

#main_header {
  height:80px;
  width:100%;
  background-color: #FFF;
}

#logo_container{
  display:inline-block;
  width:300px;
  height:100px;
}

#logo {
  position:absolute;
  height:120px;
  top:-5px;
  z-index:99;
}

#breadcrumb_container{
  position:absolute;
  display: inline-block;
  color: #397c7f;
  top:60px;
  left:270px;
  font-size:18pt;
}

#content {
  width:100%;
}

#left {
  position:absolute;
  display:inline-block;
  float:left;
  width:200px;
  height:100%;
  background-color: #8ac3c6;
  text-align:center;
  z-index:0;
}

#view {
  position:relative;
  display:inline-block;
  left:200px;
  padding:10px;
}

</style>
        
        
        
 

<script>
import MonthPicker from 'vue-month-picker'

export default {
	data() {
		return {
			date: {
				from: null,
				to: null,
				month: null,
				year: null
			}
		}
	},

	methods: {
		showDate (date) {
			this.date = date
		}
	}
}
</script>       