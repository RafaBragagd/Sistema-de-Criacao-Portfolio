const cabecalho = document.querySelector(".cabecalho");
const principal = document.querySelector(".Principal");
let ultimaPos   = 0;


function sentido() {
    let atualPos    = window.scrollY;
    const ativaFunc = cabecalho.getBoundingClientRect();
    if(atualPos > (ativaFunc.height + 10)){
        cabecalho.classList.add("cabecalhoFixed")
        principal.classList.add("PrincipalMargem")
        if(atualPos > ultimaPos) {
            cabecalho.classList.add("cabecalhoSubir");
        } else {
            cabecalho.classList.remove("cabecalhoSubir");
            cabecalho.classList.add("cabecalhoFixed");
        }
    } else if(atualPos === 0){
        cabecalho.classList.remove("cabecalhoFixed")
        principal.classList.remove("PrincipalMargem")
    }
    
        

    ultimaPos = atualPos;
}

sentido();
document.addEventListener('scroll', sentido);