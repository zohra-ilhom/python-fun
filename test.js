window.onload = function checkstorage() 
{
    var langs_abrv = localStorage.getItem('language');
    var city = localStorage.getItem('city');
    var selected_temp = localStorage.getItem('measure');

    //alert(langs_abrv + city + selected_temp);

    var url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + keyFile.appid + "&lang=" + langs_abrv + "&units=" + selected_temp ;
    

    
    
    fetch(url)
    .then(response => {
        return response.json();
    })
    .then(response => {
        console.log(response.main)
        console.log(response.main.temp)
        const html = `
        <ul> City: ${response.name} </ul>
        <ul> Actual tempreture: ${response.main.temp} </ul>
        <ul> Feels like: ${response.main.feels_like} </ul>
        <ul> Humidity: ${response.main.humidity} </ul>
            `
        document.querySelector('#app').innerHTML= html;
        });


};



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
//testing if the importing the api key from the js file we've added under .gitignore is working



function trigger() 
{
    var lang = document.getElementById("language").value;
    var langs = lang.toLowerCase();
    var city = document.getElementById("city").value;
    var unit_temp = document.getElementById("metric").value;
    //alert("language selected is " + langs + " and city selected is " + city + " and measure is " + unit_temp);

    




    if (langs in language_list) {
        langs_abrv = (language_list[langs]);
    }

    if (unit_temp in tempreture_measure) {
        selected_temp = (tempreture_measure[unit_temp]);
    }

    var url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + keyFile.appid + "&lang=" + langs_abrv + "&units=" + selected_temp ;
    //console.log(url)

    
    
    fetch(url)
    .then(response => {
        return response.json();
    })
    .then(response => {
        console.log(response.main)
        console.log(response.main.temp)
        const html = `
        <ul> City: ${response.name} </ul>
        <ul> Actual tempreture: ${response.main.temp} </ul>
        <ul> Feels like: ${response.main.feels_like} </ul>
        <ul> Humidity: ${response.main.humidity} </ul>
            `
        document.querySelector('#app').innerHTML= html;
        });

    
        document.getElementById('weather_form').reset();

        //storing to local storage user input for city, language and measure 
        localStorage.setItem('language', langs_abrv)
        localStorage.setItem('city', city)
        localStorage.setItem('measure', selected_temp)
        console.log(localStorage);
    
}


// if i change div input-container to a form then the api call doesnt work the first time
//<form class="input-container" id="weather_form" action="#"> is it becuase of the action ? wtf
// to reset form after input is submitted 
//e.preventdefault 