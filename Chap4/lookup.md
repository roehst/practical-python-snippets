Existem 2 estratégias para chamar métodos de objetos.

1. Mandar mensagem pro objeto; ele tenta responder a mensagem, e manda para a classe pai responder se não souber como. Até que no final da cadeia o objeto base não responde e dá erro. Pode ser cacheado, teoricamente.
2. Quando compilar o programa, determinar qual a classe de cada objeto, calcular quais as funções para cada método, e criar uma tabela de métodos e funções, eliminando a noção de herança em runtime.

Ponto principal de objetos
1. Encapsulamento

Ponto principal de classes
1. Fazer objetos
2. Estabelecer interfaces/contratos
3. Como escolher entre classe/objeto e função operando sobre dados?
	- Pessoalmente prefiro classes em Python pois objetos podem ter qualquer shape.
	- Em linguagens tipadas é mais fácil assegurar que uma estrutura de dados tem um shape.
	- Se o código tem umas poucas estruturas e muitos métodos, prefiro usar estruturas.
	- Se o domínio realmente se parece com objetos se comunicando, prefiro objetos.
		- Ex: simulações de muitos agentes

Cool mentions:
1. Eiffel: forte foco em design by contract
2. Smalltalk: tudo é objeto, tudo é troca de mensagem
3. Erlang/Elixir: atores são nada mais que objetos puristas e concorrentes