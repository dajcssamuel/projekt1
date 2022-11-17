function sendPost(){
    const data = JSON.stringify({
        nev: document.getElementById("nev").value,
        leiras: document.getElementById("leiras").value,
        meret: document.getElementById("meret").value,
        ar: document.getElementById("ar").value
      });
      
      navigator.sendBeacon('http://127.0.0.1:5000/savedetails/', data);
      console.log(data);
    }