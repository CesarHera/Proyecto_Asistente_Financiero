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

        cuantas = input(texto)
        try:
            cuantas = int(cuantas)
        except ValueError:
            print('Ingresa un número')
            return self._declarar(texto, nombre_lista)

        if cuantas == 0:
            nombres.append(f'No se declararon {nombre_lista}')
            valores.append(0)
            return nombres, valores

        for i in range(cuantas):
            nombre = input(f'¿Cómo se llama el valor número {i + 1}?: ')
            nombres.append(nombre)
            valor = int(input('¿Qué valor tiene?: '))
            if tipo == 'depreciable':
                depreciacion = int(input('¿Cuánto se ha depreciado (si no sabes teclea 0)?: '))
                valor -= depreciacion
            valores.append(valor)
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
