print("rehacer IO Ej_03  con  'elif y else>'");
edad = int(input("Ingere su edad : "));
if edad < 0:
    raise ValueError("error");
elif edad <= 2:
    print("Bebé");
elif edad <= 10:
    print("Chico");
elif edad <= 15:
    print("Generación T");
elif edad <= 20:
    print("Generación Z");
elif edad <= 30:
    print("Generación Y");
elif edad <= 40:
    print("Generación X");
else:
    print("Baby boomer");

