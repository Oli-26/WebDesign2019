import axios from 'axios'

export function getAirports()  {

          try {
            return axios.get('/airports')
          } catch (error) {
            console.error(error)
          }
        
      
        
        
}

export function getAirport(id)  {

          try {
            return axios.get('/airports/' + id)
          } catch (error) {
            console.error(error)
          }
        
      
        
        
}
