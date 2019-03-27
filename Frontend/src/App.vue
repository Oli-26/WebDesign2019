<template>
  <div id="app">
    <div id="header">
      <div id="top_line"></div>
      <div id="main_header">
        <div id="logo_container">
          <router-link to="/">
            <img id="logo" src="./assets/temp_logo.png" />
          </router-link>
        </div>
        <sui-container class="ui breadcrumbs">
          <sui-breadcrumb>
            <h2>
              <sui-breadcrumb-section active link>
                <router-link to="/">Airports</router-link>
              </sui-breadcrumb-section>
              <sui-breadcrumb-divider />
              <sui-breadcrumb-section link>
                <router-link to="/Carriers">Carriers</router-link> 
              </sui-breadcrumb-section>
            </h2>
          </sui-breadcrumb>
        </sui-container>
      </div>
    </div>
    <div id="content">
      <div id="left">
        <p id="selected_date">{{ date.month }} / {{  date.year  }}</p>
        <month-picker id="month_input" @change="showDate"></month-picker>
        
      </div>
      <router-view id="view"/>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
a {
  color: #397c7f !important;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
}
a:hover {
  color:#8ac3c6 !important;
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  margin:0;
  padding:0;
  color:#397c7f !important;
}

#header {
  position:fixed;
  width:100%;
  z-index:10;
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
  color: #397c7f !important;
  top:60px;
  left:270px;
  font-size:18pt;
}

.breadcrumbs {
  position:absolute;
  display: inline-block;
  color: #397c7f;
  top:60px;
  left:270px;
  font-size:18pt;
}

#left {
  position:fixed;
  width:240px;
  height:100%;
  padding-top:125px;
  background-color: #8ac3c6;
  text-align:center;
  z-index:5;
}

#selected_date {
  font-size:16pt;
  color:#FFF;
  font-weight:900;
}

#view {
  position:absolute;
  left:240px;
  top:100px;
  padding:25px;
  z-index:1;
}

#month_input {
  width:220px;
  margin:0 auto;
  padding:10px;
  background-color:#FFF;
  color:#397c7f;
  border:none !important;
  box-shadow: none !important;
  font-size:10pt;
}

.month-picker {
  box-shadow: none !important;
}

.month-picker-year button {
  background-color:#a3dadd !important;
  border:none !important;
  color:#FFF !important;
  padding-bottom:5px !important;
}
.month-picker-year button:hover {
  background-color:#FFF !important;
  border:none !important;
  color:#397c7f !important;
}

.month-picker-month {
  flex-basis:calc(50% - 4px) !important;
  padding:10px !important;
  margin:2px !important;
  border:none !important;
  box-shadow:none !important;
  background-color:#FFF !important;
  color:#397c7f;
}

.month-picker-month.selected {
  font-weight:normal !important;
  font-size:10pt !important;
  background-color:#a3dadd !important;
  color:#FFF !important;
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