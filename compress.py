class Compress():

    # def __init__(self,texto,compressed,values):
    #     self.texto = texto
    #     self.compressed = compressed
    #     self.values = values

    def compress(self,texto):
        self.texto = texto
        self.values = {}
        lista = texto.split(" ") #SEPARANDO LAS PALABRAS POR ESPACIOS Y METO EN UNA LISTA
        lista_2 = []
        lista_numeros = [] #ACA ALMACENO LOS INDICES DE CADA PALABRA
        indices = None
        for palabra in lista:
            if palabra not in lista_2: #ACA TENGO UNA LISTA DE LAS PALABRAS QUE NO SE REPITEN
                lista_2.append(palabra)
        for index,caracter in enumerate(lista_2):
            self.values[caracter] = index+1
        for i in lista:
            indices = self.values[i]
            lista_numeros.append(indices)
            
        return lista_numeros,self.values               

    def uncompress(self,compressed,values):
        lista = compressed
        llaves = list(values.keys())
        valores = list(values.values())
        palabra = 0
        lista_nueva = []
        texto = ""
        for i in lista:
            palabra = llaves[valores.index(i)]
            lista_nueva.append(palabra)
        texto = " ".join(lista_nueva)
        return texto