from funcionalidades import Funciones
from estados import Estados_financieros


class Asistente_Financiero:
    def __init__(self):
        self._usuario = None
        self._funcionalidades = Funciones()
        self._estados = Estados_financieros()


    @property
    def usuario(self):
        return self._usuario
    
    @usuario.setter
    def usuario(self, nuevo_usuario):
        print(f'El nombre de usuario ahora es {nuevo_usuario}')
        self._usuario = nuevo_usuario

    @usuario.deleter
    def usuario(self):
        print('El nombre de usuario no puede ser borrado, pero si puedes reemplazarlo asignandole otro valor')



    def iniciar(self):
        print('---\nMENU PRINCIPAL\n---')
        print(f'¡Bienvenido{" " + self._usuario if self._usuario != None else ""}! ¿En qué te puedo ayudar?')
        print('🚧¡SI ES TU PRIMERA VEZ UTILIZANDO ESTE PROGRAMA TE SUGIERO QUE LEAS BIEN TODOS LOS PRINTS PARA QUE TE SEA MÁS FÁCIL SU USO!')
        eleccion = self._funcionalidades._seleccionador(('Definiciones de términos utilizados', 'Elaborar un estado financiero', 'Salir de el programa'))
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
        elección = self._funcionalidades._seleccionador(('Balance General', 'Estado de resultados', 'Estado de cambios en la situación financiera', 'Estado de variaciones en el capital cotable'))
        if elección == '1':
            print('-->BALANCE GENERAL')
            print("""Antes de iniciar deberas tener listos los siguientes datos: 
📱Activos - Activos circulantes, activos no circulantes, activos diferidos
📱Pasivos - Pasivos circulantes, pasivos no circulantes, pasivos diferidos
📱Capital contable
Si no comprendes algúnos de estos términos te sugiero que vayas a el apartado de <Definiciones> en el Menú principal
O bien, si tienes todos los datos listos podemos comenzar""")
            elección = self._funcionalidades._seleccionador(('Comenzar', 'Ir al menú principal', 'Elegir otro estado financiero'))
            if elección == '1':
                print('--> BALANCE GENERAL')
                self._estados._balance_general()
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
            elección = self._funcionalidades._seleccionador(('Comenzar', 'Ir al menú principal', 'Elegir otro estado financiero'))
            if elección == '1':
                print('--> ESTADO DE RESULTADOS')
                self._estados._estado_de_resultados()
            elif elección == '2':
                print('--> MENÚ PRINCIPAL')
                self.iniciar()
            elif elección == '3':
                self.estados_financieros_menu()
        elif elección == '3':
            print('Ejecutando Estado de cambios en la situación financiera')
        elif elección == '4':
            print('Ejecutando Estado de variaciones en el capital contable')



if __name__ == '__main__':
    financiero = Asistente_Financiero()
    financiero._usuario = 'Cesar' #Coloca tu nombre
    financiero.iniciar()