function passeImg(){
    var div1 = document.getElementById("containe1")
    var div2 = document.getElementById("containe2")
    var div3 =document.getElementById("containe3")
    var div4 = document.getElementById("containe4")
    if(div1.classList.contains ("hidden")){
        div1.classList.remove("hidden")
        div2.classList.remove("hidden")
        div3.classList.add("hidden")
        div4.classList.add("hidden")


    }else{
        div1.classList.add("hidden")
        div2.classList.add("hidden")
        div3.classList.remove("hidden")
        div4.classList.remove("hidden")
    
      
    }
}