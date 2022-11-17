var url = "http://127.0.0.1:5000/view";
var id = "view";

async function generator(url, id) {
    var request = await new XMLHttpRequest()

request.open('GET', url, true)
request.onload = function () {
  // Begin accessing JSON data here
  var data = JSON.parse(this.response)
view(data, request, id);

}

request.send()
  }

  function view(data, request, id){
      if(id == "view"){
    if (request.status >= 200 && request.status < 400) {
         data.forEach((query) => {
          console.log(request.status);
          var div = document.createElement("tr");
            var mainContainer = document.getElementById(id);
          div.innerHTML = "<td>"+query.id+"</td><td><input id='nev"+query.id+"' placeholder='"+query.nev+"' value='"+query.nev+"'/></td><td><input id='leiras"+query.id+"' placeholder='"+query.leiras+"' value='"+query.leiras+"'/></td><td><input id='meret"+query.id+"' placeholder='"+query.meret+"' value='"+query.meret+"'/></td><td><input id='ar"+query.id+"' placeholder='"+query.ar+"' value='"+query.ar+"'/></td>"+"<button onclick = 'deleterecord("+query.id+")' type = 'submit' value='Submit'>Törlés</button>"+"<button onclick = 'update("+query.id+")'>Frissítés</button>" ;
          mainContainer.appendChild(div)
        })
      } else {
        console.log('error')
      }}
  }

async function generate_html(){
await generator(url, id);
}

function deleterecord(id){
  const data = JSON.stringify({
    id: parseInt(id)
  });
  
  navigator.sendBeacon('http://127.0.0.1:5000/deleterecord/', data);
  console.log(data);
}
function update(id){
  const data = JSON.stringify({
    id: id,
    nev: document.getElementById("nev"+id).value,
    leiras: document.getElementById("leiras"+id).value,
    meret: document.getElementById("meret"+id).value,
    ar: document.getElementById("ar"+id).value
  });
  
  navigator.sendBeacon('http://127.0.0.1:5000/updatedetails/', data);
  console.log(data);
}

generate_html();
