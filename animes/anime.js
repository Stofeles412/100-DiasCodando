function openMenu(){
    var abrir = document.getElementById("nav-ul")
    var icone = document.getElementById("icone-menu")
    if(abrir.style.display == 'block'){
        abrir.style.display = 'none'
        icone.src = ('../imagens/sinal-de-seta-para-baixo-para-navegar.png')
      
       
    }else{
        abrir.style.display = 'block'
        icone.src = ('../imagens/pra-cima.png')

      
    }
}
confirm ("ATENÇÃO: ESSE ARTIGO PODE CONTER SPOILER DO ANIME !!")