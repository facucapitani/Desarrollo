vegetariana = input("¿Quieres una pizza vegetariana? (Si/No): ")

# Definir los ingredientes disponibles para cada tipo de pizza
vegetariana_ingredientes = ["pepinos", "champiñones", "aceitunas", "pimientos"]
no_vegetariana_ingredientes = ["pepperoni", "salchicha", "bacón"]

# Mostrar el menú de ingredientes disponibles según la elección del usuario
if vegetariana.upper() == "Si":
    print("Ingredientes disponibles:")
    for i, ingrediente in enumerate(vegetariana_ingredientes):
        print(f"{i+1}. {ingrediente}")
    ingrediente_c = int(input("Elige un ingrediente (1-4): "))
    ingrediente_elegido = vegetariana_ingredientes[ingrediente_c - 1]
else:
    print("Ingredientes disponibles:")
    for i, ingredientes in enumerate(no_vegetariana_ingredientes):
        print(f"{i+1}. {ingredientes}")
    ingrediente_c = int(input("Elige un ingrediente (1-3): "))
    ingrediente_elegido = no_vegetariana_ingredientes[ingrediente_c - 1]

# Mostrar la pizza elegida y sus ingredientes
print(f"Tu pizza {'' if vegetariana.upper() == 'Si' else 'no '}es vegetariana.")
print(f"Ingredientes: mozzarella, tomate, {ingrediente_elegido}")