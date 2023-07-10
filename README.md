# Desafio do Bootcamp DIO - Ciências de Dados com Python
Atividades relacionadas ao bootcamp Potência Tech powered by iFood | Ciências de Dados com Python

#  * Protótipo de Sistema Bancário *

## Objetivo Geral
Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato.

## Desafio
Contratado por um banco para desenvolver um protótio para um futuro sistema. 
Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python.
Para a primeira versão do sistema devemos implementar apenas 3 operações:
- DEPOSITAR
- SACAR
- EXIBIR EXTRATO

## Tela do protótipo
Exibirá 4 opções:
  - DEPOSITAR
  - SACAR
  - EXIBIR EXTRATO
  - ENCERRAR O SISTEMA
Após cada operação, o sistema voltará à tela de opções.

## REGRAS
### Operação de Depósito
- Só serão aceitos depósitos de valores numéricos positivos e maiores do que zero.
- Só existem uma agência, uma conta corrente e um correntista não identificados.
- O armazenamento da operação é feita em memória e em uma variável única.
- Cada depósito deverá ser exibido na operação de Exibir Extrato.

### Operação de Saque
- Só serão aceitos saques de valores numéricos positivos e maiores do que zero.
- O limite de operações de saque é de no máximo 3.
- Só serão realizados saques no valor de até R$ 500,00 por operação.
- Quando o saldo em conta for inferior ao pedido de saque, a operação não acontecerá 
  e um aviso será exibido na tela, informando falta de saldo.
- O armazenamento da operação é feita em memória e em uma variável única.
- Cada saque deverá ser exibido na operação de Exibir Extrato.

### Operação de Exibir Extrato
- Listar os depósitos realizados durante a instância de uso do protótipo.
- Listar os saques realizados durante a instância de uso do protótipo.
- Na ausência de operações, será exibida uma mensagem, informando que não houve movimentação.
- Os valores serão apresentados no formato R$ ###.## (duas casas decimais, identificando a moeda local).
- O saldo resultante do balanço das operações de saques e depósitos será exibido ao final do extrato.
