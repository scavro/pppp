def min (num1, num2):
    if num1 < num2:
        return num1
    elif num1 == num2:
        return "Los dos numeros son iguales"
    else:
        return num2

def peticion_numeros():
    while True:
        entrada = input("Por favor, ingrese un número positivo: ")
        
        # Verificar si la entrada contiene solo dígitos y posiblemente un punto decimal
        if not (entrada.replace('.', '', 1).isdigit() and entrada.count('.') <= 1):
            print("Error: Ha introducido un carácter no numérico. Por favor, introduzca solo números.")
            continue
        
        try:
            num = float(entrada)
            if num > 0:
                return num
            else:
                print("Error: El número debe ser mayor que 0.")
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")


num1 = peticion_numeros()
num2 = peticion_numeros()

x = min(num1, num2)

print("El menor de los dos numero es:",x)

