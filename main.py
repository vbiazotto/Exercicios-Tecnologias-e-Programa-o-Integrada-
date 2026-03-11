import re


def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("Divisão por zero")
    return a / b


def interpretar_mensagem(msg: str):

    msg = msg.lower().strip()

   
    add_match = re.search(r"(-?\d+)\s*\+\s*(-?\d+)", msg)
    if add_match:
        a = int(add_match.group(1))
        b = int(add_match.group(2))
        return "somar", a, b

  
    sub_match = re.search(r"(-?\d+)\s*[-–]\s*(-?\d+)", msg)
    if sub_match:
        a = int(sub_match.group(1))
        b = int(sub_match.group(2))
        return "subtrair", a, b

 
    div_match = re.search(r"(-?\d+)\s*(?:dividido por|/|:|\u00F7)\s*(-?\d+)", msg)
    if div_match:
        a = int(div_match.group(1))
        b = int(div_match.group(2))
        return "dividir", a, b

    mul_match = re.search(r"(-?\d+)\s*(?:por|x|vezes|\*)\s*(-?\d+)", msg)
    if mul_match:
        a = int(mul_match.group(1))
        b = int(mul_match.group(2))
        return "multiplicar", a, b

    simple = re.search(r"(somar|subtrair|multiplicar|dividir)\s+(-?\d+)\s+.*?(-?\d+)", msg)
    if simple:
        op = simple.group(1)
        a = int(simple.group(2))
        b = int(simple.group(3))
        return op, a, b

    raise ValueError("Não foi possível interpretar a mensagem")


def main():
    print("Bem-vindo à calculadora simples!")
    texto = input("Digite a operação: ")
    try:
        op, a, b = interpretar_mensagem(texto)
        if op == "somar":
            resultado = somar(a, b)
        elif op == "subtrair":
            resultado = subtrair(a, b)
        elif op == "multiplicar":
            resultado = multiplicar(a, b)
        elif op == "dividir":
            resultado = dividir(a, b)
        else:
            raise RuntimeError("Operação desconhecida")
        print(f"Resultado: {resultado}")
    except Exception as e:
        print("Erro:", e)


if __name__ == "__main__":
    main()
