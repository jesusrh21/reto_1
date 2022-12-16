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


if __name__ == '__main__':
    palabra_1 = input("Inserte la primera palabra: ").lowe()
    palabra_2 = input("Inserte la segunda palabra: ").lower()
    print(is_anagrama(palabra = palabra_1, texto = palabra_2))