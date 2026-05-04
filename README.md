# TRABALHO-PROGRAMACAO-BASICA
Primeiramente declaramos uma lista de strings chamada "estoque" onde serão adicionados os produtos cadastrados pelo usuário do sistema.

Em seguida, declaramos as funções que conterão a lógica necessária para cada funcionalidade do sistema. São essas "cadastrar_produto", "remover_produto" e "listar_produto".

Em "cadastrar produto" criamos a variável "nome" que vai receber o input do usuário. Existe uma validação do input que verifica se nome não é vazio, caso seja, printamos no console uma mensagem de erro. A validação é feita por um if, visto que no python, quando uma string está vazia, ela retorna false.

Em "remover_produto" fazemos a mesma coisa, porém a diferença é que verificamos se o nome do produto inserido contém na lista "estoque". Caso contenha, removemos, caso não contenha, retornamos uma mensagem de erro.

Em "listar_produtos", verificamos se a lista estoque não está vazia. Visto que se estiver vazia, ela retornaria false.
Caso não esteja vazia, fazemos um for loop para iterar por toda a lista e printer cada string contida nela.

Por ultimo, temos a declaração da funçao "executar_sistema" onde vamos de fato utilizer essas funções. 
Para isso, criamos um while para manter o codigo em execução enquanto o usuário utiliza as funcionalidades.

Declaramos a variável "entrada" que receberá um inteiro, esse inteiro deverá condizer com a opção do menu que o usuário deseja utilizar, caso o usuário coloque um valor inexistente dentre as opções, para não quebrar a execução, nós adicionamos um try except para mostrar uma mensagem de erro.

Utilizamos um switch case para chamar a função correspondente ao input do usuário.
