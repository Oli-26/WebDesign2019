import axios from 'axios'

export function testFunction()  {
        //var resp = axios.get('/airports/ATL?content-type=text/csv')
        //    .then( response => {
        //        return response.data
       //     })
            
        //let list = {};
        
          try {
            return axios.get('/airports')
          } catch (error) {
            console.error(error)
          }
        
        //list = axios.get('/airports').then(function(result) {
          
          //  console.log(result.data)
         //   list = result.data
        //    console.log(result.data[0])
            
      // });
        
       // return getAirports;
        
        
}
