##Exercicio em Python
Estou fazendo o BootCamp Santander Cibersegurança #2 e neste BootCamp foi proposto o seguinte exercicio:

###Descrição
Você foi encarregado de criar um sistema simples que verifica a integridade de arquivos, comparando o hash fornecido pelo usuário com o hash real do arquivo. Na função verificar_hashes que irá receber uma lista de hashes e compará-los com os valores esperados para cada arquivo. Seu objetivo é verificar se o hash calculado é igual ao hash esperado.

###Entrada
Uma lista de pares de hashes (hash calculado e hash esperado), separados por vírgulas, e cada par separado por ponto e vírgula.

###Saida
Para cada par de hashes fornecido, o código imprime o resultado "Correto" ou "Inválido".

###Exemplos

Entrada	| Saída
abc123, abc123 |	Correto
def456, def789 |Inválido
123abc, 123abc; 456def,456def	| Correto Correto
