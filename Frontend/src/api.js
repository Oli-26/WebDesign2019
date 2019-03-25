import axios from 'axios'

export function testFunction () {
        var resp = axios.get('/airports')
            .then( response => {
                return response
            })
        console.log(resp);
        return resp;
}
