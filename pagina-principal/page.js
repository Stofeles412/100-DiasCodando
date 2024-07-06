function openMenu(){
    var abrir = document.getElementById("nav-ul")
    var icone = document.getElementById("icone-menu")

    if(abrir.style.display == "block"){
        abrir.style.display = "none"
        icone.src = 'menu.png'
    }else{
        abrir.style.display = "block"
         icone.src = 'menu-fechado.png'
    }
}