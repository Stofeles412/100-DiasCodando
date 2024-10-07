function Mostrar(){
    var botao = document.getElementById("botao-projetos")
    var projetos = document.getElementById("art-projetos")
    if(projetos.style.display == "none"){
        projetos.style.display = "block"
          botao.innerText = "Ocultar"
      
    }else{
        projetos.style.display = "none"
     
      
    }
}