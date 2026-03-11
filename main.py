import re


def somar(a, b):
    return a + b


def multiplicar(a, b):
    return a * b


def interpretar_mensagem(msg: str):

    msg = msg.lower().strip()

   
    add_match = re.search(r"(-?\d+)\s*\+\s*(-?\d+)", msg)
    if add_match:
        a = int(add_match.group(1))
        b = int(add_match.group(2))
        return "somar", a, b

 
    mul_match = re.search(r"(-?\d+)\s*(?:por|x|vezes|\*)\s*(-?\d+)", msg)
    if mul_match:
        a = int(mul_match.group(1))
        b = int(mul_match.group(2))
        return "multiplicar", a, b

   
    simple = re.search(r"(somar|multiplicar)\s+(-?\d+)\s+.*?(-?\d+)", msg)
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
        elif op == "multiplicar":
            resultado = multiplicar(a, b)
        else:
            raise RuntimeError("Operação desconhecida")
        print(f"Resultado: {resultado}")
    except Exception as e:
        print("Erro:", e)


if __name__ == "__main__":
    main()
