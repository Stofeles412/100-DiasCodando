function openMenu(){
    var abrir = document.getElementById("nav-ul")
    var icone = document.getElementById("icone-menu")

    if(abrir.style.display == "block"){
        abrir.style.display = "none"
        icone.src = ""
    }else{
        abrir.style.display = "block"
    }
}