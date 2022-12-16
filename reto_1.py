def is_anagrama(palabra:str,texto:str)->bool:
    """
    Funcion para comprobar si una palabra es anagrama de la otra

    Atributos: 
     - palabra : str
     - texto : str
    
    Return:
     - anagrama : bool
    """    
    if len(palabra) != len(texto):
        return False
    else:
        for index, letra in enumerate(palabra):
            if texto.find(letra) == index:
                return False
        return True


if __name__ == '__main__':
    palabra_1 = input("Inserte la primera palabra: ").lowe()
    palabra_2 = input("Inserte la segunda palabra: ").lower()
    print(is_anagrama(palabra = palabra_1, texto = palabra_2))