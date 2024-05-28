alfabeto_portugues = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def codificar_ou_decodificar():
    def digitar_inteiro():
        for _ in range(30):
            try:
                num_cifra = int(input('Digite um numero inteiro para a cifra: '))
                return num_cifra
            except ValueError:
                print('Digita um INTEIRO!!')

    def encode(msg, num_cifra):
        result = ''
        for char in msg:
            if char in alfabeto_portugues:
                index = (alfabeto_portugues.index(char) + num_cifra) % len(alfabeto_portugues)
                result += alfabeto_portugues[index]
            else:
                result += char
        return result

    def decode(msg, num_cifra):
        result = ''
        for char in msg:
            if char in alfabeto_portugues:
                index = (alfabeto_portugues.index(char) - num_cifra) % len(alfabeto_portugues)
                result += alfabeto_portugues[index]
            else:
                result += char
        return result

    for n in range(3):
        encode_or_decode = input('Digite "encode" para codificar ou "decode" para decodificar. \n').lower()
        if encode_or_decode == 'encode':
            msg = input('Qual mensagem gostaria de codificar? \n').lower()
            num_cifra = digitar_inteiro()
            mensagem_codificada = encode(msg, num_cifra)
            print('Mensagem codificada:', mensagem_codificada)
            break
        elif encode_or_decode == 'decode':
            msg = input('Qual mensagem gostaria de decodificar? \n').lower()
            num_cifra = digitar_inteiro()
            mensagem_decodificada = decode(msg, num_cifra)
            print('Mensagem decodificada:', mensagem_decodificada)
            break
        else:
            if n >= 2:
                print('RETIRE-SE')

codificar_ou_decodificar()
