print("rehacer IO Ej_03  con parámetros de '>'");

edad = int(input("Ingrese su edad : "));
if edad < 0:
    raise ValueError("error");
elif 10 > edad > 0:
    print("Bebé");
elif 15 > edad > 10:
    print("Chico");
elif 20 > edad > 15:
    print("Generación Z");
elif 30 > edad > 20:
    print("Generación Y");
elif 50 > edad > 30:
    print("Generación X");
else:
    print("Baby boomer");

