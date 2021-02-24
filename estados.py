from funcionalidades import Funciones

class Estados_financieros:
    def __init__(self):
        self._funcionalidades = Funciones()
        

    def _balance_general(self):
        print('---\nGENERANDO BALANCE GENERAL\n---')
        print('Empezaremos sumando todos los activos, después los pasivos y por último el capital contable')

        #Declarando variables para después operarlas
        print('\n-DECLARANDO ACTIVOS-')
        activos_circulantes_nombres, activos_circulantes_valores = self._funcionalidades._declarar('¿Cuántos activos circulantes vas a declarar?: ', 'activos circulantes')
        activos = self._funcionalidades._manipular_lista(activos_circulantes_valores, tipo='suma')
        print(f'Total actual de activos = {activos}')
        activos_no_circulantes_nombres, activos_no_circulantes_valores = self._funcionalidades._declarar('¿Cuántos activos no circulantes vas a declarar?: ', 'activos no circulantes', tipo='depreciable')
        activos = self._funcionalidades._manipular_lista(activos_no_circulantes_valores, tipo='suma', resultado=activos)
        print(f'Total actual de activos = {activos}')
        activos_diferidos_nombres, activos_diferidos_valores = self._funcionalidades._declarar('¿Cuántos activos diferidos vas a declarar?: ', 'activos diferos')
        activos = self._funcionalidades._manipular_lista(activos_diferidos_valores, tipo='suma', resultado=activos)
        print(f'TOTAL ACTVOS = {activos}')

        print('\n-DECLARANDO PASIVOS-')
        pasivos_circulantes_nombres, pasivos_circulantes_valores = self._funcionalidades._declarar('¿Cuántos pasivos circulantes vas a declarar?: ', 'pasivos circulantes')
        pasivos = self._funcionalidades._manipular_lista(pasivos_circulantes_valores, tipo='suma')
        print(f'Total actual de pasivos = {pasivos}')
        pasivos_no_circulantes_nombres, pasivos_no_circulantes_valores = self._funcionalidades._declarar('¿Cuántos pasivos no circulantes vas a declarar?: ', 'pasivos no circulantes')
        pasivos = self._funcionalidades._manipular_lista(pasivos_no_circulantes_valores, tipo='suma', resultado=pasivos)
        print(f'Total actual de pasivos = {pasivos}')
        pasivos_diferidos_nombres, pasivos_diferidos_valores = self._funcionalidades._declarar('¿Cuántos pasivos diferidos vas a declarar?: ', 'pasivos diferos')
        pasivos = self._funcionalidades._manipular_lista(pasivos_diferidos_valores, tipo='suma', resultado=pasivos)
        print(f'TOTAL PASIVOS = {pasivos}')

        print('\n-DECLARANDO CAPITAL CONTABLE-')
        capital_contable_nombres, capital_contable_valores = self._funcionalidades._declarar('¿Por cuántos elementos estará compuesto tu capital contable?: ', 'capital contable')
        capital_contable = self._funcionalidades._manipular_lista(capital_contable_valores, tipo='suma')
        print(f'TOTAL CAPITAL CONTABLE = {capital_contable}')

        terminar = input('-Presiona ENTER para ver los resultados de tu balance general-')
        #Solo agregué esto para que den enter y después se impriman todos los resultados

        #Imprimiendo Todos los resultados
        print('-' * 80)
        self._funcionalidades._imprimir(activos_circulantes_nombres, activos_circulantes_valores, 'Activos circulantes')
        self._funcionalidades._imprimir(activos_no_circulantes_nombres, activos_no_circulantes_valores, 'Activos no circulantes')
        self._funcionalidades._imprimir(activos_diferidos_nombres, activos_diferidos_valores, 'Activos diferidos')
        print(f'\nTOTAL ACTVOS = {activos}\n------\n')

        self._funcionalidades._imprimir(pasivos_circulantes_nombres, activos_circulantes_valores, 'Pasivos circulantes')
        self._funcionalidades._imprimir(pasivos_no_circulantes_nombres, pasivos_no_circulantes_valores, 'Pasivos no circulantes')
        self._funcionalidades._imprimir(pasivos_diferidos_nombres, activos_diferidos_valores, 'Pasivos diferidos')
        print(f'\nTOTAL PASIVOS = {pasivos}\n------\n')

        self._funcionalidades._imprimir(capital_contable_nombres, capital_contable_valores, 'Capital contable')
        print(f'\nTOTAL CAPITAL CONTABLE = {capital_contable}\n------\n')
        print('-' * 80)
        print(f'ACTIVOS = {activos} | PASIVOS + CAPITAL CONTABLE = {pasivos + capital_contable}')
        print('-' * 80)



    def _estado_de_resultados(self):
        print('---\nESTADO DE RESULTADOS\n---')
        print('📱Irémos declarando los valores necesarios para deducir la utilidad neta:')

        #Declarando variables para operarlas
        print('\n-DEDUCIENDO UTILIDAD BRUTA-')
        utilidad_bruta_nombres, utilidad_bruta_valores = self._funcionalidades._declarar('(EL VALOR DE CADA IMPORTE O GASTO QUE DECLARES TIENE QUE SER NEGATIVO)\n¿Cuántos elementos declararás para calcular la utilidad bruta?: ', 'Utilidades brutas')
        utilidad_bruta = self._funcionalidades._manipular_lista(utilidad_bruta_valores, tipo='suma')
        print(f'Total utilidad bruta = {utilidad_bruta}')

        print('\n-DEDUCIENDO UTILIDAD EN OPERACIÓN-')
        utilidad_en_operacion_nombres, utilidad_en_operacion_valores = self._funcionalidades._declarar('(EL VALOR DE CADA IMPORTE O GASTOS QUE DECLARES TIENE QUE SER NEGATIVO)\n¿Cuántos elementos declararás para calcular la Utilidad en operacion?: ', 'Utilidades en operacion')
        utilidad_en_operacion = self._funcionalidades._manipular_lista(utilidad_en_operacion_valores, tipo='suma')
        print(f'Total utilidad en operación = {utilidad_en_operacion}')

        print('\n-DEDUCIENDO UTILIDAD ANTES DE IMPUESTOS-')
        utilidad_antes_de_impuestos_nombres, utilidad_antes_de_impuestos_valores = self._funcionalidades._declarar('(EL VALOR DE CADA IMPORTE O GASTOS QUE DECLARES TIENE QUE SER NEGATIVO)\n¿Cuántos elementos declararás para calcular la Utilidad antes de impuestos (Aquí se declaran otras ganancias y otros gastos)?: ', 'Utilidades antes de impuestos')
        utilidad_antes_de_impuestos = self._funcionalidades._manipular_lista(utilidad_antes_de_impuestos_valores, tipo='suma')
        print(f'Total utilidad antes de impuestos = {utilidad_antes_de_impuestos}')

        print('\n-DEDUCIENDO UTILIDAD NETA-')
        utilidad_con_impuestos_nombres, utilidad_con_impuestos_valores = self._funcionalidades._declarar('(EL VALOR DE CADA IMPORTE O GASTOS QUE DECLARES TIENE QUE SER NEGATIVO)\n¿Cuántos elementos declararás para calcular la utilidad neta (Aquí se declaran impuestos como ISR y PTU)?: ', 'Utilidades con impuestos')
        utilidad_con_impuestos = self._funcionalidades._manipular_lista(utilidad_con_impuestos_valores, tipo='suma')
        print(f'Total utilidad neta = {utilidad_con_impuestos}')

        terminar = input('-Presiona ENTER para ver toda la graficación de tu estado de resultados-')
        #Solo agregué esto para que den enter y darles los resultados

        #Imprimiendo Todos los resultados
        print('-' * 80)
        self._funcionalidades._imprimir(utilidad_bruta_nombres, utilidad_bruta_valores)
        print(f'\nTOTAL UTILIDAD BRUTA = {utilidad_bruta}\n--------')
        self._funcionalidades._imprimir(utilidad_en_operacion_nombres, utilidad_en_operacion_valores)
        print(f'\nTOTAL UTILIDAD EN OPERACIÓN = {utilidad_en_operacion}\n--------')
        self._funcionalidades._imprimir(utilidad_antes_de_impuestos_nombres, utilidad_antes_de_impuestos_valores)
        print(f'\nTOTAL UTILIDAD ANTES DE IMPUESTOS = {utilidad_antes_de_impuestos}\n--------')
        self._funcionalidades._imprimir(utilidad_con_impuestos_nombres, utilidad_con_impuestos_valores)
        print('-' * 80)
        print(f'-\nTOTAL UTILIDAD NETA = {utilidad_con_impuestos}\n-')
        print('-' * 80)