class Funciones:
    def __init__(self):
        pass



    def _seleccionador(self, opciones):
        contador = 1
        for i in opciones:
            print(f'{contador}.- {i}')
            contador += 1
        eleccion = input('¿Cuál eliges?: ')
        contador = 1
        for i in opciones:
            if eleccion == str(contador):
                return eleccion
            contador += 1

        print("-" * 50)
        print('Elíge una opción correcta | Reiniciando elección...')
        return self._seleccionador(opciones)



    def _declarar(self, texto, nombre_lista, tipo='default'): #Ayuda a crear dos listas de un mismo tema, una con los nombres y otra con valores
        nombres = []
        valores = []

        cuantas = input(texto) #Este bloque pregunta cuantos valores declarará el usuario y así se hacen dos list, una que guardará los nombres y otra para valores
        try:
            cuantas = int(cuantas)
        except ValueError:
            print('INGRESA UN NÚMERO | REINICIANDO PREGUNTA')
            return self._declarar(texto, nombre_lista)

        if cuantas == 0:
            nombres.append(f'No se declararon {nombre_lista}')
            valores.append(0)
            return nombres, valores

        contador = 1
        
        while contador < cuantas: #Aquí se va declarando el nombre y valor de cada elemento, si no ingresa datos admitidos, se reinicia la declaración
            nombre = input(f'¿Cómo se llama el valor número {contador}?: ')
            valor = input('¿Qué valor tiene?: ')
            try:
                valor = int(valor)
            except ValueError:
                print(f'Ingresa NUMEROS | REINICIANDO VALOR {contador}')
                continue
            
            nombres.append(nombre)

            if tipo == 'depreciable': #Añadí esta opción para restarle alguna depreciación a los valores al mismo tiempo que se declaran
                depreciacion = int(input('¿Cuánto se ha depreciado (RECUERDA DECLARAR DEPRECIACIONES CON VALORES NEGATIVOS)?: '))
                valor -= depreciacion

            valores.append(valor)
            contador += 1

        return nombres, valores



    def _imprimir(self, lista_nombres, lista_valores, nombre='', tipo='imprimir_nombre'): #Ayuda recorrer toda la estructura e ir imprimiendo cada valor
        if tipo != '':
            print(f'{nombre.upper()}')
        for i in range(len(lista_nombres)):
            print(f'{lista_nombres[i]} = {lista_valores[i]}')

    

    def _manipular_lista(self, lista, tipo='default', resultado=0): #Ayuda a obtener resultados con la estructura de datos ingresada, depende de qué se busque hacer.
        if tipo == 'values':
            for i in lista.values():
                resultado += i
            return resultado
        elif tipo == 'keys':
            keys_list = []
            for i in lista():
                keys_list.append(i)
            return keys_list
        elif tipo == 'suma':
            for i in lista:
                resultado += i
            return resultado
        else:
            print(f'La función manipular_lista la tienes que usar con values, keys o suma, no con tipo={tipo}')