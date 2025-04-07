def slice_simple():
    texto = "Awesome"
    print(texto.lower()[0:3])
    medio = int(len(texto)/2)
    print (texto[medio-1:medio+2])
    print(texto.lower()[:4] + texto.lower()[-3:])
    # Código a implementar, se debe utilizar la variable 'texto' para resolver el ejercicio.
    # No se debe modificar la definición de la función, ni ingresar otro valor mediante input.


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_slice_simple_test.py` o `python tp3_slice_simple_test.py`
