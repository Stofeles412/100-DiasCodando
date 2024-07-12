function openMenu(){
    var abrir = document.getElementById("nav-ul")
    var icone = document.getElementById("icone-menu")

    if(abrir.style.display == "block"){
        abrir.style.display = "none"

        icone.src = ('../imagens/sinal-de-seta-para-baixo-para-navegar.png')
        
         
       
    }else{
        abrir.style.display = "block"
        icone.src = ('../imagens/pra-cima.png')
       
    }
  
}

var zoom =  false;

function ampliarImg(){
    var zoom = document.getElementById("main-img")
    if(zoom.style.width == '90%'){
        zoom.style.width = '100%'
        
    }else{
    zoom.style.width = '90%'
   

    }
}
confirm ("você aceita cookies ?")
