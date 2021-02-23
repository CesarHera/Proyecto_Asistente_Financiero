class Asistente_Financiero_AI:

    def __init__(self):
        self.usuario = 'Cesar'




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
        
        print(eleccion)
        print("-" * 50)
        print('Elíge una opción correcta | Reiniciando elección...')
        return self._seleccionador(opciones)


    

    def iniciar(self):
        print('---\nMENU PRINCIPAL\n---')
        print(f'¡Bienvenido {" " + self.usuario if self.usuario != None else ""}! ¿En qué te puedo ayudar?')
        print('🚧¡SI ES TU PRIMERA VEZ UTILIZANDO ESTE PROGRAMA TE SUGIERO QUE LEAS BIEN TODOS LOS PRINTS PARA QUE TE SEA MÁS FÁCIL SU USO!')
        eleccion = self._seleccionador(('Definiciones de términos utilizados', 'Elaborar un estado financiero', 'Salir de el programa'))
        if eleccion == '1':
            print('--> Definiciones')
        elif eleccion == '2':
            print('--> Estados financieros')
            self.estados_financieros_menu()
        elif eleccion == '3':
            print('--> Saliendo del programa')

    def estados_financieros_menu(self): #Seleccionamos cuál estado financiero se ejecutará
        print('---\nMENU DE ESTADOS FINANCIEROS\n---')
        print('Estos son los estados financieros que puedo elaborar por tí:')
        elección = self._seleccionador(('Balance General', 'Estado de cambios en la situación financiera', 'Estado de resultados', 'Estado de variaciones en el capital cotable'))
        if elección == '1':
            print('-->BALANCE GENERAL')
            print("""Antes de iniciar deberas tener listos los siguientes datos: 
📱Activos - Activos circulantes, activos no circulantes, activos diferidos
📱Pasivos - Pasivos circulantes, pasivos no circulantes, pasivos diferidos
📱Capital contable
Si no comprendes algúnos de estos términos te sugiero que vayas a el apartado de <Definiciones> en el Menú principal
O bien, si tienes todos los datos listos podemos comenzar""")
            elección = self._seleccionador(('Comenzar', 'Ir al menú principal', 'Elegir otro estado financiero'))
            if elección == '1':
                print('--> BALANCE GENERAL')
                self.balance_general()
            elif elección == '2':
                print('--> MENÚ PRINCIPAL')
                self.iniciar()
            elif elección == '3':
                self.estados_financieros_menu()
        elif elección == '2':
            print('-->ESTADO DE RESULTADOS')
            print("""Antes de iniciar debes tener listos los siguiestes datos:
📱Ventas
📱Costos de ventas
📱Gastos de operación
📱Otras ganancias
📱Otros gastos
📱Impuesto Sobre Renta (ISR)
📱Participación de los Trabajadores en las Utilidades (PTU)
Si no comprendes algúnos de estos términos te sugiero que vayas a el apartado de <Definiciones> en el Menú principal
O bien, si tienes todos los datos listos podemos comenzar""")
            elección = self._seleccionador(('Comenzar', 'Ir al menú principal', 'Elegir otro estado financiero'))
            if elección == '1':
                print('--> ESTADO DE RESULTADOS')
                self.estado_de_resultados()
            elif elección == '2':
                print('--> MENÚ PRINCIPAL')
                self.iniciar()
            elif elección == '3':
                self.estados_financieros_menu()
        elif elección == '3':
            print('Ejecutando Estado de cambios en la situación financiera')




    def balance_general(self):
        print('---\nGENERANDO BALANCE GENERAL\n---')
        print('Empezaremos sumando todos los activos, después los pasivos y por último el capital contable')

        #Declarando variables para después operarlas
        print('DECLARANDO ACTIVOS')
        activos_circulantes_nombres, activos_circulantes_valores = self.declarar('¿Cuántos activos circulantes vas a declarar?: ', 'activos circulantes')
        activos = self.manipular_lista(activos_circulantes_valores, tipo='suma')
        print(f'Total actual de activos = {activos}')
        activos_no_circulantes_nombres, activos_no_circulantes_valores = self.declarar('¿Cuántos activos no circulantes vas a declarar?: ', 'activos no circulantes', tipo='depreciable')
        activos = self.manipular_lista(activos_no_circulantes_valores, tipo='suma', resultado=activos)
        print(f'Total actual de activos = {activos}')
        activos_diferidos_nombres, activos_diferidos_valores = self.declarar('¿Cuántos activos diferidos vas a declarar?: ', 'activos diferos')
        activos = self.manipular_lista(activos_diferidos_valores, tipo='suma', resultado=activos)
        print(f'TOTAL ACTVOS = {activos}')

        print('DECLARANDO PASIVOS')
        pasivos_circulantes_nombres, pasivos_circulantes_valores = self.declarar('¿Cuántos pasivos circulantes vas a declarar?: ', 'pasivos circulantes')
        pasivos = self.manipular_lista(pasivos_circulantes_valores, tipo='suma')
        print(f'Total actual de pasivos = {pasivos}')
        pasivos_no_circulantes_nombres, pasivos_no_circulantes_valores = self.declarar('¿Cuántos pasivos no circulantes vas a declarar?: ', 'pasivos no circulantes')
        pasivos = self.manipular_lista(pasivos_no_circulantes_valores, tipo='suma', resultado=pasivos)
        print(f'Total actual de pasivos = {pasivos}')
        pasivos_diferidos_nombres, pasivos_diferidos_valores = self.declarar('¿Cuántos pasivos diferidos vas a declarar?: ', 'pasivos diferos')
        pasivos = self.manipular_lista(pasivos_diferidos_valores, tipo='suma', resultado=pasivos)
        print(f'TOTAL PASIVOS = {pasivos}')

        print('DECLARANDO CAPITAL CONTABLE')
        capital_contable_nombres, capital_contable_valores = self.declarar('¿Por cuántos elementos estará compuesto tu capital contable?: ', 'capital contable')
        capital_contable = self.manipular_lista(capital_contable_valores, tipo='suma')
        print(f'TOTAL CAPITAL CONTABLE = {capital_contable}')

        terminar = input('-Presiona ENTER para ver los resultados de tu balance general-')
        #Solo agregué esto para que den enter y después se impriman todos los resultados

        #Imprimiendo Todos los resultados
        print('-' * 80)
        self.imprimir(activos_circulantes_nombres, activos_circulantes_valores, 'Activos circulantes')
        self.imprimir(activos_no_circulantes_nombres, activos_no_circulantes_valores, 'Activos no circulantes')
        self.imprimir(activos_diferidos_nombres, activos_diferidos_valores, 'Activos diferidos')
        print(f'--\nTOTAL ACTVOS = {activos}\n--')

        self.imprimir(pasivos_circulantes_nombres, activos_circulantes_valores, 'Pasivos circulantes')
        self.imprimir(pasivos_no_circulantes_nombres, pasivos_no_circulantes_valores, 'Pasivos no circulantes')
        self.imprimir(pasivos_diferidos_nombres, activos_diferidos_valores, 'Pasivos diferidos')
        print(f'--\nTOTAL PASIVOS = {pasivos}\n--')

        self.imprimir(capital_contable_nombres, capital_contable_valores, 'Capital contable')
        print(f'--\nTOTAL CAPITAL CONTABLE = {capital_contable}\n--')
        print('-' * 80)
        print(f'ACTIVOS = {activos} | PASIVOS + CAPITAL CONTABLE = {pasivos + capital_contable}')
        print('-' * 80)




    def declarar(self, texto, nombre_lista, tipo='default'): #Ayuda a crear dos listas de un mismo tema, una con los nombres y otra con valores
        nombres = []
        valores = []

        cuantas = input(texto)
        try:
            cuantas = int(cuantas)
        except ValueError:
            print('Ingresa un número')
            return self.declarar(texto, nombre_lista)

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



    
    def manipular_lista(self, lista, tipo='default', resultado=0): #Ayuda a obtener resultados con la estructura de datos ingresada, depende de qué se busque hacer.
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
            print(tipo)




    def imprimir(self, lista_nombres, lista_valores, nombre='', tipo='imprimir_nombre'): #Ayuda recorrer toda la estructura e ir imprimiendo cada valor
        if tipo != '':
            print(f'{nombre.upper()}')
        for i in range(len(lista_nombres)):
            print(f'{lista_nombres[i]} = {lista_valores[i]}')




    def estado_de_resultados(self):
        print('Irémos declarando los valores necesarios para deducir la utilidad neta.')

        #Declarando variables para operarlas
        print('DEDUCIENDO UTILIDAD BRUTA')
        utilidad_bruta_nombres, utilidad_bruta_valores = self.declarar('(EL VALOR DE CADA IMPORTE/GASTO QUE DECLARES TIENE QUE SER NEGATIVO)\n¿Cuántos elementos declararás para calcular la utilidad bruta?: ', 'Utilidades brutas')
        utilidad_bruta = self.manipular_lista(utilidad_bruta_valores, tipo='suma')
        print(f'Total utilidad bruta = {utilidad_bruta}')

        print('DEDUCIENDO UTILIDAD EN OPERACIÓN')
        utilidad_en_operacion_nombres, utilidad_en_operacion_valores = self.declarar('(EL VALOR DE CADA IMPORTE/GASTOS QUE DECLARES TIENE QUE SER NEGATIVO)\n¿Cuántos elementos declararás para calcular la Utilidad en operacion?: ', 'Utilidades en operacion')
        utilidad_en_operacion = self.manipular_lista(utilidad_en_operacion_valores, tipo='suma')
        print(f'Total utilidad en operación = {utilidad_en_operacion}')

        print('DEDUCIENDO UTILIDAD ANTES DE IMPUESTOS')
        utilidad_antes_de_impuestos_nombres, utilidad_antes_de_impuestos_valores = self.declarar('(EL VALOR DE CADA IMPORTE/GASTOS QUE DECLARES TIENE QUE SER NEGATIVO)\n¿Cuántos elementos declararás para calcular la Utilidad antes de impuestos (Aquí se declaran otras ganancias y otros gastos)?: ', 'Utilidades antes de impuestos')
        utilidad_antes_de_impuestos = self.manipular_lista(utilidad_antes_de_impuestos_valores, tipo='suma')
        print(f'Total utilidad antes de impuestos = {utilidad_antes_de_impuestos}')

        print('DEDUCIENDO UTILIDAD NETA')
        utilidad_con_impuestos_nombres, utilidad_con_impuestos_valores = self.declarar('(EL VALOR DE CADA IMPORTE/GASTOS QUE DECLARES TIENE QUE SER NEGATIVO)\n¿Cuántos elementos declararás para calcular la utilidad neta (Aquí se declaran impuestos como ISR y PTU)?: ', 'Utilidades con impuestos')
        utilidad_con_impuestos = self.manipular_lista(utilidad_con_impuestos_valores, tipo='suma')
        print(f'Total utilidad neta = {utilidad_con_impuestos}')

        terminar = input('-Presiona ENTER para ver toda la graficación de tu estado de resultados-')
        #Solo agregué esto para que den enter y darles los resultados

        #Imprimiendo Todos los resultados
        print('-' * 80)
        self.imprimir(utilidad_bruta_nombres, utilidad_bruta_valores)
        print(f'---\nTOTAL UTILIDAD BRUTA = {utilidad_bruta}\n---')
        self.imprimir(utilidad_en_operacion_nombres, utilidad_en_operacion_valores)
        print(f'---\nTOTAL UTILIDAD EN OPERACIÓN = {utilidad_en_operacion}\n---')
        self.imprimir(utilidad_antes_de_impuestos_nombres, utilidad_antes_de_impuestos_valores)
        print(f'---\nTOTAL UTILIDAD ANTES DE IMPUESTOS = {utilidad_antes_de_impuestos}\n---')
        self.imprimir(utilidad_con_impuestos_nombres, utilidad_con_impuestos_valores)
        print('-' * 80)
        print(f'---\nTOTAL UTILIDAD NETA = {utilidad_con_impuestos}\n---')
        print('-' * 80)





if __name__ == '__main__':
    #No pospongas

    financiero = Asistente_Financiero_AI()
    financiero.iniciar()