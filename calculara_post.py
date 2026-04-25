import math


# ------------------ UTILIDADES ------------------

def es_numero(token):
    try:
        float(token)
        return True
    except:
        return False


def validar_parentesis(expr):
    stack = []
    for c in expr:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0


# ------------------ PARSER ------------------

def evaluar(expr):
    expr = expr.strip()

    # Caso 1: número simple
    if es_numero(expr):
        return float(expr)

    # Validación básica de paréntesis
    if not validar_parentesis(expr):
        raise ValueError("ERROR! Expresion no valida")

    # Quitar paréntesis externos redundantes
    while expr.startswith('(') and expr.endswith(')'):
        inner = expr[1:-1].strip()
        if not validar_parentesis(inner):
            break
        expr = inner

    tokens = expr.split(' ')

    # VALIDACIÓN DE ESPACIOS EXACTOS
    if '' in tokens:
        raise ValueError("ERROR! Expresion no valida")

    # ------------------ OPERACIONES BINARIAS ------------------
    if len(tokens) == 3:
        a, b, op = tokens

        if not (op in ['+', '-', '*', '/']):
            raise ValueError("ERROR! Expresion no valida")

        val1 = evaluar(a)
        val2 = evaluar(b)

        if op == '+':
            return val1 + val2
        elif op == '-':
            return val1 - val2
        elif op == '*':
            return val1 * val2
        elif op == '/':
            if val2 == 0:
                raise ZeroDivisionError
            return val1 / val2

    # ------------------ OPERACIONES UNARIAS ------------------
    elif len(tokens) == 2:
        a, op = tokens
        val = evaluar(a)

        if op == 'sqroot':
            if val < 0:
                raise ValueError("RAIZ_NEGATIVA")
            return math.sqrt(val)

        elif op == 'sqr':
            return val ** 2

        elif op == 'sen':
            return math.sin(math.radians(val))

        elif op == 'cos':
            return math.cos(math.radians(val))

        elif op == 'tan':
            return math.tan(math.radians(val))

        else:
            raise ValueError("ERROR! Expresion no valida")

    else:
        raise ValueError("ERROR! Expresion no valida")


# ------------------ OPERACIONES ESPECIALES ------------------

def operaciones_especiales(expr):
    tokens = expr.strip()[1:-1].split(' ')

    if len(tokens) != 3:
        return None

    a, b, op = tokens

    if not (a.isdigit() and b.isdigit()):
        return None

    a = int(a)
    b = int(b)

    if op == 'div':
        return a // b
    elif op == '%':
        return a % b
    else:
        return None


def factorial(expr):
    tokens = expr.strip()[1:-1].split(' ')

    if len(tokens) != 2:
        return None

    a, op = tokens

    if op == 'fact!' and a.isdigit():
        n = int(a)
        res = 1
        for i in range(1, n + 1):
            res *= i
        return res

    return None


# ------------------ MAIN ------------------

def main():
    print("=== Calculadora Postfija ===")
    print("Autores: Karla-26007325, Victoria, Sebastian-26007186")

    while True:
        entrada = input("calculadora_p >> ")

        if entrada == "quit":
            print("Saliendo ...")
            print("Gracias por usar nuestra calculadora.")
            break

        try:
            # Número directo
            if es_numero(entrada):
                print("respuesta >>", float(entrada))
                continue

            # Operaciones especiales
            if entrada.startswith('(') and entrada.endswith(')'):
                esp = operaciones_especiales(entrada)
                if esp is not None:
                    print("respuesta >>", esp)
                    continue

                fact = factorial(entrada)
                if fact is not None:
                    print("respuesta >>", fact)
                    continue

            # Evaluación normal
            resultado = evaluar(entrada)
            print("respuesta >>", resultado)

        except ZeroDivisionError:
            print("respuesta >> ERROR! Division entre cero")

        except ValueError as e:
            if str(e) == "RAIZ_NEGATIVA":
                print("respuesta >> ERROR! Raiz cuadrada negativa")
            else:
                print("respuesta >> ERROR! Expresion no valida")


if __name__ == "__main__":
    main()