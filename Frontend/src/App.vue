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
        <p id="selected_date">{{ date.month }} / {{  date.year  }}</p>
        <month-picker id="month_input" @change="showDate"></month-picker>
        
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
  width:240px;
  height:100%;
  padding-top:50px;
  background-color: #8ac3c6;
  text-align:center;
  z-index:0;
}

#selected_date {
  font-size:16pt;
  color:#FFF;
  font-weight:900;
}

#view {
  position:relative;
  display:inline-block;
  left:240px;
  padding:10px;
  width: 1800px;
}

#month_input {
  width:220px;
  margin:0 auto;
  padding:10px;
  background-color:#0f9ca2;
  color:#FFF;
  border:none;
  box-shadow: none !important;
  font-size:10pt;
}

.month-picker-year button {
  background-color:#a3dadd !important;
  border:none !important;
  color:#FFF !important;
  padding-bottom:5px !important;
}
.month-picker-year button:hover {
  background-color:#397c7f !important;
  border:none !important;
  color:#FFF !important;
}

.month-picker-month {
  flex-basis:calc(50% - 4px) !important;
  padding:10px !important;
  margin:2px !important;
  border:none !important;
  box-shadow:none !important;
  background-color:#a3dadd !important;
  color:#000;
}

.month-picker-month.selected {
  font-weight:normal !important;
  font-size:10pt !important;
  background-color:#397c7f !important;
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