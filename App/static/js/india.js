function updateMap() {
  console.log("Updating map with realtime data")
  
  $.getJSON("/static/js/stateData.json", function(json) {
      jdata = json['state'];
      });

 fetch("https://api.covid19india.org/data.json")
      .then(response => response.json())
      .then(rsp => {
          data = rsp['statewise']
          statesData = data.slice(1,data.keys().length)
          var tot_active = data[0]['active']
          var tot_confirmed = data[0]['confirmed']
          tot_deaths = data[0]['deaths']
          tot_recoverd = data[0]['recovered']
           // document.getElementById('smname').innerHTML = tot_confirmed;
          statesData.forEach(element => {
              stateName = element.state;
              totalCases = element.confirmed;
              activeCases = element.active;
              deaths = element.deaths;
              // document.getElementById('smname').innerHTML = tot_confirmed;
              recovered = element.recovered;

              var count = Object.keys(jdata).length;
              for (i=0; i<=count;i++){
              try{
                  if(jdata[i]['name'] === stateName){
                  latitude = jdata[i]['latitude']
                  longitude = jdata[i]['longitude']
                  // console.log(stateName, latitude, longitude)
                  break;
                  }
              }
              catch{
                  console.log('stateName')
                  }
              }

              cases = totalCases;
              if (cases>1000){
                  color = "rgb(255, 0, 0)";
              }

              else{
                  color = `rgb(${cases}, 0, 0)`;
              }

              // Mark on the map
              new mapboxgl.Marker({
                  draggable: false,
                  color: color
              }).setLngLat([longitude, latitude])
                  .setPopup(new mapboxgl.Popup({ offset: 25 }) // add popups
                  .setHTML('<b>' + stateName + '</b><p>' +'Confirmed : '+ totalCases + '</p><p>' + 'Active : '+ activeCases + '</p><p>' + 'Recovered : '+ recovered + '</p><p>' + 'Deaths : '+ deaths + '</p>'))
              .addTo(map); 
              

          });
      });
}

let interval = 20000;
setInterval( updateMap, interval); 


fetch("/allgraphs/")
  .then(response => response.json())
  .then(rsp => {
      stateCode = rsp["stateCode"]
      states = rsp["states"]
      confirmed = rsp["confirmedCases"]
      active = rsp["activeCases"]
      recovered = rsp["recoveredCases"]
      dead = rsp["deathCases"]
function ConfirmedCases(){
new Chart(document.getElementById("line-chart"), {
type: 'line',
data: {
  labels: stateCode,
  datasets: [{ 
      data: confirmed,
      label: "Cases",
      backgroundColor: "rgba(62, 149, 205, 0.5)",
      borderColor : "rgba(62, 149, 205, 1)",
      pointBackgroundColor: "rgba(62, 149, 205, 1)",
      fill: true
    }
  ]
},
options: {
  title: {
    display: true,
    text: 'India State Wise Cases'
  },
  scaleShowValues:true,
  scales:{
    xAxes:[{
      ticks:{
        autoSkip:true
      }
    }]
  },
  responsive: true,    
}
});
}
ConfirmedCases()

function ActiveCases(){
new Chart(document.getElementById("line-chart3"), {
type: 'line',
data: {
  labels: stateCode,
  datasets: [{ 
      data: active,
      label: "Active",
      backgroundColor: " rgba(96, 96, 96, 0.5)",
      borderColor : " rgba(96, 96, 96, 1)",
      pointBackgroundColor: " rgba(96, 96, 96, 1)",
      fill: true
    }
  ]
},
options: {
  title: {
    display: true,
    text: 'Active Cases'
  },
  scaleShowValues:true,
  scales:{
    xAxes:[{
      ticks:{
        autoSkip:true
      }
    }]
  },
  responsive: true,
}
});
}
ActiveCases()

function RecoveredCases(){
new Chart(document.getElementById("line-chart2"), {
type: 'line',
data: {
  labels: stateCode,
  datasets: [{ 
      data: recovered,
      label: "Recovered",
      backgroundColor: "rgba(123, 239, 178, 0.2)",
      borderColor: "rgba(30, 130, 76, 1)",
      pointBackgroundColor: "rgba(0, 177, 106, 1)",
      fill: true
    }
  ]
},
options: {
  title: {
    display: true,
    text: 'Recovered Cases'
  },
  scaleShowValues:true,
  scales:{
    xAxes:[{
      ticks:{
        autoSkip:true
      }
    }]
  },
  responsive: true,
}
});
}
RecoveredCases()

function DeathCases(){
new Chart(document.getElementById("line-chart4"), {
type: 'line',
data: {
  labels: stateCode,
  datasets: [{ 
      data: dead,
      label: "Deaths",
      backgroundColor: "rgba(255, 0, 0, 0.2)",
      borderColor : "rgba(255, 0, 0, 0.8)",
      pointBackgroundColor: "rgba(255, 0, 0, 0.6)",
      fill: true
    }
  ]
},
options: {
  title: {
    display: true,
    text: 'Deaths Cases'
  },
  scaleShowValues:true,
  scales:{
    xAxes:[{
      ticks:{
        autoSkip:true
      }
    }]
  },
  responsive: true,
}
});
}
DeathCases()

});