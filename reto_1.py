def is_anagrama(palabra:str,texto:str)->bool:
    """
    Funcion para comprobar si una palabra es anagrama de la otra

    Atributos: 
     - palabra : str
     - texto : str
    
    Return:
     - anagrama : bool
    """
    anagrama = False
    if len(palabra) != len(texto):
        return anagrama
    else:
        for index, letra in enumerate(palabra):
            if texto.find(letra) == index:
                return anagrama
        anagrama = True
        return anagrama



def run()->None:
    """
    Metodo para ejecutar el scrip

    Atributos:
     - None

    Return:
     - None
    """
    palabra_1 = input("Inserte la primera palabra: ")
    palabra_2 = input("Inserte la segunda palabra: ")
    print(is_anagrama(palabra = palabra_1, texto = palabra_2))


if __name__ == '__main__':
    run()