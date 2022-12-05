'''
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 '''
def is_anagrama(str1,str2):
    s1 = str1.replace(' ','')
    s1.lower()
    s2 = str2.replace(' ','')
    s2.lower()
    return sorted(s1) == sorted(s2)

if __name__=='__main__':
    s1 = input('Escriba primer String\n')
    s2 = input('Escriba segundo String\n')

    print(is_anagrama(s1,s2))



