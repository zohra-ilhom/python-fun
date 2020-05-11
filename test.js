console.log('hello world');


var language_list = {
        'english': "en",
        'russian': "ru",
        'turkish': "tr",
        'farsi': "fa",

}

var tempreture_measure = {
    'kelvin': "",
    'celcius': "metric",
    'fehrenhite': "imperial",

}

//console.log(keyFile.appid);
//testing if the importing the api key from the js file we've added under ignore is working



function trigger() 
{
    var lang = document.getElementById("language").value;
    var langs = lang.toLowerCase();
    var city = document.getElementById("city").value;
    var unit_temp = document.getElementById("metric").value;
    alert("language selected is " + langs + " and city selected is " + city + " and measure is " + unit_temp);

    if (langs in language_list) {
        langs_abrv = (language_list[langs]);
    }

    if (unit_temp in tempreture_measure) {
        selected_temp = (tempreture_measure[unit_temp]);
    }

    var url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + keyFile.appid + "&lang=" + langs_abrv + "&units=" + selected_temp ;
    console.log(url)

    
    
    fetch(url)
    .then(response => {
        return response.json();
    })
    .then(response => {
        console.log(response.main)
        console.log(response.main.temp)
        const html = `
        <p> City: ${response.name} </p>
        <p> Actual tempreture: ${response.main.temp} </p>
        <p> Feels like: ${response.main.feels_like} </p>
        <p> Humidity: ${response.main.humidity} </p>
            `
        document.querySelector('#app').innerHTML= html;
        });
    
    
    
    
    
    





        

        
    
}
