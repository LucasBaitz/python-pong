const data = document.querySelector('.data');
const tempo = document.querySelector('.tempo');
const iniciar = document.querySelector('#iniciar');
const parar = document.querySelector('#parar');
const reiniciar = document.querySelector('#reiniciar');
const temporizador = document.querySelector('#temporizador');


let segundos = 0
let contagem;

// Funções para mudar os segundos e atualizar o horario
function criaSegundos(segundos) {
    const dataS = new Date(segundos * 1000)
    console.log(dataS)
    return dataS.toLocaleTimeString('PT-BR', {
        hour12: false,
        timeZone: 'UTC',
    });
    
};

function contagemSecs() {
    contagem = setInterval(function() {
            segundos++;
            tempo.innerHTML = criaSegundos(segundos);
    }, 1000);
}



// Pegars os eventos e agir de acordo
iniciar.addEventListener('click', function(e) {
    contagemSecs()
});

parar.addEventListener('click', function(e) {
    clearInterval(contagem)

});

reiniciar.addEventListener('click', function(e) {
    rodando = false
    tempo.innerHTML = '00:00:00'
    segundos = 0
    clearInterval(salvaTempo)
});