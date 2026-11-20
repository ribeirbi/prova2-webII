# Respostas — Prova Prática Individual de DW2 — Versão A

Nome: Bianca Ribeiro Cavalcante
RA: 3111392613009

## R1 (Item 10)

Status da página  /  : 302

Status da API  /api/palestrantes  : 401

Explicação: A página `/` redireciona para a tela de entrada, por isso recebe 302.
Já a API verifica o login diretamente e devolve 401 sem redirecionar.

## R2 (Item 11)

Status observado: 405

Explicação: O método POST não é permitido para essa rota,
pois /api/palestrantes está configurada para responder somente a GET.
