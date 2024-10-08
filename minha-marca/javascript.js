function Mostrar(){
    var botao = document.getElementById("botao-projetos")
    var projetos = document.getElementById("art-projetos")
    if(projetos.style.display == "none"){
        projetos.style.display = "block"
         botao.innerText = "Ocultar"
         botao.style.color = "blue"
      
      
    }else{
        projetos.style.display = "none"
           botao.innerText = "Veja Mais"
        botao.style.color = "blueviolet"
     
      
    }
}