
# Desafio - Sistema Bancãrio com Python 📚💻

## Versão 1

## Objetivo Geral
- Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato.


## Operação de depósito
- Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

## Operação de saque
- O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

## Operação de extrato
- Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações. Os valores devem ser exibidos utilizando o formato R$ xxx.xx. Exemplo:1500.45 = R$ 1500.45

## Versão 2

## Objetivo Geral
- Separar as funções de saque,depósito e extrato em funções. Criar duas novas funções: cadastrar usuário (cliente) e cadastrar conta bancária 

## Desafio
- Precisamos deixar nosso código mais modularizado, para isso vamos criar funções para as operações existentes: sacar, depositar e visualizar o extrato. Além disso, para a versão 2 do nosso sistema, precisamos criar duas novas funções: criar usuário(cliente do banco) e criar nova conta corrente (vincular com usuário)

## Separação em funções
- Devemos criar funções para todas as operações do sistema. Para exercitar tudo o que aprendemos neste módulo, cada função vai ter uma regra na passagem de argumentos. O retorno e a forma como serão chamadas, pode ser definida por você da forma que achar melhor

## Saque
- A função saque deve receber os argumentos apenas por nome (keyword only). Sugestão de argumentos: Saldo, valor, extrato, limite, numero_saques, limite_saques. Sugestão de retorno: saldo e extrato

## Depósito

- A função de depósito deve receber os argumentos apenas por posição (positional only). Sugestão de argumentos: saldo, valor, extrato. Sugestão de retorno: saldo e extrato

## Extrato

- A função extrato deve receber os argumentos por posição e nome (positional only e keyword only). Argumentos posicionais: saldo. Argumentos nomeados: extrato.

## Novas funções

- Precisamos criar duas novas funções: criar usuário e criar conta corrente. Fique a vontade para adicionar mais funções, exemplo: Listar contas

## Criar usuário (cliente)

- O programa deve armazenar os usuários em uma lista, um usuário e composto por: nome, data de nacimento, cpf e endereço. O endereço é uma string com formato: logradouro, numero - bairro cidade/sigla estado. Deve ser armazenado somente os números do CPF. Não podemos cadastrar 2 usuários com o mesmo cpf

## Criar conta corrente

- O programa deve armazenar contas em uma lista, uma conta é composta por: agência, número da conta e usuário. O número da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001". O usuário pode ter mais de uma conta, mas uma conta pertence somente a um usuário

## Dica

Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do cpf informado para cada usuário da lista



