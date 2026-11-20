// JavaScript do cliente - Prova Pratica Individual de DW2.
//
// Este arquivo e carregado em todas as paginas, pela base. Por isso o
// codigo confere se os elementos existem antes de usa-los.

var lista = document.getElementById("lista");
var botaoAtualizar = document.getElementById("atualizar");


// Escreve uma mensagem na tela, sem recarregar a pagina.
function mostrarAviso(texto) {
  var aviso = document.getElementById("aviso-js");

  if (aviso) {
    aviso.textContent = texto;
  }
}


// Esvazia a lista e a redesenha com os dados recebidos.
// "dados" e um array de objetos, como o que a API devolve.
function desenharLista(dados) {
  lista.innerHTML = "";

  for (var i = 0; i < dados.length; i = i + 1) {
    var item = document.createElement("li");
    item.textContent = dados[i].nome + " — " + dados[i].tema;
    lista.appendChild(item);
  }

  mostrarAviso(dados.length + " registro(s) lido(s) sem recarregar a página.");
}


if (botaoAtualizar && lista) {

  botaoAtualizar.addEventListener("click", function () {

       fetch("/api/palestrantes")
      .then(function (resposta) {
        if (!resposta.ok) {
          throw new Error("Erro ao consultar a API.");
        }
        return resposta.json();
      })
      .then(function (dados) {
        desenharLista(dados);
      })
      .catch(function () {
        mostrarAviso("Nao foi possivel atualizar a lista.");
      });
  });

}
