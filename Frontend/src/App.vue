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
        <!-- <p id="selected_date">{{ date.month }} / {{  date.year  }}</p> -->
        <p id="selected_date">Month</p>
          <month-picker id="month_input" @change="showDate"></month-picker>       
      </div>
      <router-view id="view" :month="`${date['month']}`"/>
    </div>
  </div>
</template>


<style>
a {
  color: #397c7f !important;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
}
a:hover {
  color:#8ac3c6 !important;
}

.button {
  margin:0 auto;
  width:10em;
  height:2em;
  line-height:2em;
  background-color:#a3dadd !important;
  color:#FFF;
  font-weight:600;
  font-size:14pt;
  border-radius:25px;
  border:2px solid;
  transition:.1s;
}

.button:hover {
  background-color:#FFF !important;
  color:#397c7f;
  border:2px solid #397c7f;
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

#logo:hover {
  height:125px;
  transition:.1s;
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
  width:calc(100vw - 240px);
}

.search {
  /*margin-bottom:25px;*/
  display:inline-block;
  float:right;
}

.title_container {
  display:inline-block !important;
  width:calc(100vw - 240px - 50px - 5*14px) !important;
  margin-top:0 !important;
}

.title_container_carriers {
  display:inline-block !important;
  width:calc(100vw - 240px - 50px - 3*14px) !important;
  margin-top:0 !important;
}

.title_container_descriptive {
  display:inline-block !important;
  width:calc(100vw - 240px - 150px - 2*14px) !important;
  margin-top:0 !important;
}

.card_group {
  width:calc(100vw - 240px - 50px) !important;
}

.airport_card {
  text-align: center;
  flex-grow:0;
  flex-shrink:0 !important;
  width:calc(33% - 2*14px) !important;
}

.carrier_card {
  text-align: center;
  flex-grow:0 !important;
  flex-shrink:0 !important;
  padding:0 !important;
  width:calc(33% - 2*14px) !important;
}

.statistics_card {
  text-align: center;
  flex-grow:0;
  flex-shrink:0 !important;
  width:calc(33% - 2*14px) !important;
  height:200px;
}

.statistics_card>sui-card-header {
  text-align:left;
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

.month-picker-year {
  display:none !important;
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
  name: 'app',
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
			this.date = date;
		}
	}
}
</script>       