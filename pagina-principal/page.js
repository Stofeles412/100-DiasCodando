function openMenu(){
    var abrir = document.getElementById("nav-ul")
    var icone = document.getElementById("icone-menu")

    if(abrir.style.display == "block"){
        abrir.style.display = "none"
        
         
       
    }else{
        abrir.style.display = "block"
      
       
        
    }
  
}

var zoom =  false;

function ampliarImg(){
    var zoom = document.getElementById("main-img")
    if(zoom.style.width == '90%'){
        zoom.style.width = '110%'
        
    }else{
    zoom.style.width = '90%'
   

    }
}
confirm ("você aceita cookies ?")
