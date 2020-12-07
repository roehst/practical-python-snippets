1. Sobre módulos

- __all__
- importlib
- __init__.py

2. Sobre exceções

- O melhor é *não* tratar
- Só se trata exceção quando se tem o que fazer
- Quanto mais barulhentos os programas, melhor
- Exceção é uma ferramenta de controle de execução: "não sei o que fazer neste caso, devolvo o controle parar quem souber lidar"
- Exceção fica na stack
- Quando mais expecífica a exceção, melhor
- Em C, uma exceção é feita com um mark/jump
- Em Java, as excepções precisam fazer parte do tipo de uma função com o tag "throws IOError" ou precisam ser tratadas na função

3. Sobre funções

- Funções são objetos: decoradores, por exemmplo, retornam funções
- Um módulo pode ser tão-somente um dict e funções: {"mean: mean, "sum": sum}["mean"](x)
- Se uma função tiver um _yield_ em seu código, ela vira um gerador. Um gerador yield varios values. Quando termina seus valores, o gerador envia uma exceção:

	def f():
		for i in range(100):
			yield i

		raise IterationFinished()

E este código pode ser usador:

	for i in f():
		print(f)
