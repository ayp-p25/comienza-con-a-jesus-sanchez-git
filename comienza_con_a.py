"""
Ejercicio : comienza co A
• Jesús Alejandro Sánchez Muñoz 
• 758377 
• Igenieria Mecanica 
• Algoritmos y Programcion 
• ESI232B2 
• Jorge Zaldivar 
• 13/feb/25 
• 5 min
"""

Palabra = input("Dime una palabra que quisieras saber que empiece con A: \n ")
if Palabra.lower()[0]== "a" or Palabra[0]== "á": 
    print(Palabra, " empieza con A ")
else:
    print(Palabra , "no empieza con A")
