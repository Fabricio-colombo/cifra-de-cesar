# Cifra de César
A cifra de César, também conhecida como criptografia de César, é uma técnica de criptografia clássica e simples, nomeada em homenagem a Júlio César, que a utilizava para proteger mensagens militares confidenciais. Esta cifra é um tipo de cifra de substituição, onde cada letra do texto original (plaintext) é substituída por outra letra que está um número fixo de posições à frente no alfabeto. Esse número fixo é chamado de chave.

## Quem Era César
Júlio César foi um líder militar e político romano, amplamente reconhecido como um dos maiores estrategistas da história. Ele viveu entre 100 a.C. e 44 a.C., e desempenhou um papel crucial na transformação da República Romana no Império Romano. César é famoso por suas conquistas militares, especialmente na Gália, e por suas reformas políticas e sociais. Ele também foi um dos primeiros a utilizar técnicas de criptografia para proteger informações sensíveis, incluindo a cifra que leva seu nome.

### Como Funciona
Escolha da Chave: Seleciona-se um número inteiro que será usado como a chave de deslocamento.
Substituição: Para cifrar uma mensagem, cada letra do texto original é substituída pela letra que está um número de posições à frente no alfabeto, conforme a chave escolhida.
Alfabeto Circular: O alfabeto é tratado de forma circular, ou seja, após a letra 'Z', volta-se para a letra 'A'.

Exemplo
Vamos considerar uma chave de 3. O alfabeto é deslocado conforme abaixo:

A -> D
B -> E
C -> F
...
X -> A
Y -> B
Z -> C
Para cifrar a palavra "HELLO" com a chave 3, cada letra seria substituída da seguinte forma:

H -> K
E -> H
L -> O
L -> O
O -> R
Portanto, "HELLO" cifrado com a chave 3 se torna "KHOOR".

### Descriptografia
Para decifrar a mensagem, o processo é invertido. Cada letra do texto cifrado é deslocada um número fixo de posições para trás, conforme a chave escolhida.
