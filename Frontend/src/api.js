import axios from 'axios'

export function getAirports(airportCode = "None")  {

    try {
        if(airportCode == "None"){
            return axios.get('/airports')
        }else{
            return axios.get('/airports/' + airportCode)
        }
    } catch (error) {
        console.error(error)
    }
}



export function getCarriers(carrierCode = "None", airportCode = "None")  {
    try {
        if(carrierCode != "None"){
            if(airportCode != "None"){
                return axios.get('/carriers/' + carrierCode + "?airport-code="+airportCode)
            }else{
                return axios.get('/carriers/' + carrierCode)
            }
            
        }else{
            if(airportCode != "None"){
                return axios.get("/carriers?airport-code="+airportCode)
            }else{
                return axios.get("/carriers")
            }
           
        }

    } catch (error) {
        console.error(error)
    }
        
}



export function getStatistics(carrierCode, airportCode = "None")  {
    try {
        return axios.get('/carriers/' + carrierCode + "/statistics?airport-code="+airportCode)

    } catch (error) {
        console.error(error)
    }
}


export function getFlights(carrierCode, airportCode = "None", month) {
    try {
        if(airportCode == "None"){
            return  axios.get('/carriers/' + carrierCode + "/statistics/flights?month="+month)
        }else{
            return  axios.get('/carriers/' + carrierCode + "/statistics/flights?airport-code="+airportCode+"&month="+month)
        }

    }catch (error) {
        console.error(error)
    }
    
}



export function getMinutes(carrierCode, airportCode = "None", month, delayType = "None") {
    try {
        if(airportCode == "None"){
            return  axios.get('/carriers/' + carrierCode + "/statistics/delays/minutes?month="+month)
        }else{
            return  axios.get('/carriers/' + carrierCode + "/statistics/delays/minutes?airport-code="+airportCode+"&month="+month)
        }

    }catch (error) {
        console.error(error)
    }
    
}



export function getAmount(carrierCode, airportCode = "None", month, delayType = "None") {
    try {
        if(airportCode == "None"){
            return  axios.get('/carriers/' + carrierCode + "/statistics/delays/amount?month="+month)
        }else{
            return  axios.get('/carriers/' + carrierCode + "/statistics/delays/amount?airport-code="+airportCode+"&month="+month)
        }

    }catch (error) {
        console.error(error)
    }
    
}

export function getAverages(carrierCode, airportCode1, airportCode2, month){
    try {
        
        return  axios.get('/carriers/' + carrierCode + "/statistics/delays/minutes/averages?airport-code1="+airportCode1+"&airport-code2="+airportCode2+"&month="+month)
        

    }catch (error) {
        console.error(error)
    }
}


