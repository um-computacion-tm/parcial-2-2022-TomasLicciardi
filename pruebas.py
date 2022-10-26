# x = "Hola Mundo!"

# for i in x:
    # print(i, end="")

# print(x[0])

# for i in x:
#     print(x[i])

# lista = ["G","X","l","J", "M"]
# lista_nueva = [[]]
# lista_nueva.append(lista)

# print(lista)
# print(lista_nueva)

# for i in range(len(lista_nueva)):
#     print

# x = "HOLA COMO ANDAS CAPO TODO BIEN"
# y = x.split()
# print(y)
# listita = []
# for index,caracter in enumerate(x):
#     if caracter == " ":
#         index -= 1
#         while index >=0:
#             listita.append(caracter)
#             index -= 1

# print(listita)

'''lista_valor_nueva = []
        self.values = []
        for index,caracter in enumerate(self.texto):
            if caracter == " ":
                while index >= 0 or index > index[caracter]:
                    self.compressed.append(caracter)
                    index -= 1
                lista_valor.append(self.compressed)
                self.compressed.clear()
                for i in range(len(lista_valor)):
                    self.compressed.append(i+1)
                lista_valor.clear()
                # for i in range(self.compressed): fijarse de ponerlo al final
                #     lista_valor.append(i+1)
                
            elif caracter[index] == :
                caracter = index'''



def compress(texto):
        texto = texto
        values = {}
        lista = texto.split(" ")
        lista_2 = []
        lista_numeros = []
        indices = None
        for palabra in lista:
            if palabra not in lista_2: #ACA TENGO UNA LISTA DE LAS PALABRAS QUE NO SE REPITEN
                lista_2.append(palabra)
        for index,caracter in enumerate(lista_2):
            values[caracter] = index+1
        for i in lista:
            indices = values[i]
            lista_numeros.append(indices)
        return lista_numeros,values

# x = compress("TDD o Test-Driven Development (desarrollo dirigido por tests) es una práctica de programación que consiste en escribir primero las pruebas (generalmente unitarias), después escribir el código fuente que pase la prueba satisfactoriamente y, por último, refactorizar el código escrito. Con esta práctica se consigue, entre otras cosas, un código más robusto, más seguro, más mantenible y una mayor rapidez en el desarrollo. En este post voy a centrarme solamente en cómo TDD afecta al diseño de software, si queréis más información, hay una introducción bastante buena en la Wikipedia y Carlos Blé tiene disponible online un libro muy completo. Además, en esta infografía os contamos en qué consiste TDD, en qué principios se basa (SOLID) y cuáles son sus ventajas y desventajas. Y, si quieres profundizar aún más, te recomendamos que le eches un vistazo a TDD, una metodología para gobernarlos a todos y Molecule: desarrollo TDD en Ansible.")
# print(x)

y = compress("Hola mundo Hola estoy en el parcial de Computacion y de Informatica. Hola mundo Hola")
print(y)
# for x in dicc.keys():
#     print(x)

# saludo = "TDD o Test-Driven Development (desarrollo dirigido por tests) es una practica de programacion que consiste en escribir primero las pruebas (generalmente unitarias), despues escribir el codigo fuente que pase la prueba satisfactoriamente y, por ultimo, refactorizar el codigo escrito.Con esta practica se consigue, entre otras cosas, un codigo mas robusto, mas seguro, mas mantenible y una mayor rapidez en el desarrollo.En este post voy a centrarme solamente en como TDD afecta al diseno de software, si quereis mas informacion, hay una introduccion bastante buena en la Wikipedia y Carlos Ble tiene disponible online un libro muy completo. Ademas, en esta infografia os contamos en que consiste TDD, en que principios se basa (SOLID) y cuales son sus ventajas y desventajas. Y, si quieres profundizar aun mas, te recomendamos que le eches un vistazo a TDD, una metodologia para gobernarlos a todos y Molecule: desarrollo TDD en Ansible."
# lisas = []
# for i in saludo.split():
#     if i not in lisas:
#         lisas.append(i)
# print(lisas)
# print(saludo.split())

def uncompress(compressed,values):
        lista = compressed
        llaves = list(values.keys())
        texto = ""
        for index in lista:
            texto = " ".join(llaves)
            texto = str(texto)
        return texto


# xd = ["Hola", "Mundo", "Hola"]

# string = "".join(xd)
# print(str(string))

