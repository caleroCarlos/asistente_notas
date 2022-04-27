# Modulos
import usuarios.usuario as modelo
import notas.accionesN

## Clases ##
class Acciones:
    
    def registro(self):
        # Pedir los datos
        print('\nInicializando proceso de registro...')
        nombre = input('Dime tu nombre: ')
        apellidos = input('Dime tus apellidos: ')
        email = input('Ingresa una direccion de correo: ')
        password = input('Crea una contraseña: ')

        # Creo usuario (intancio la clase usuario del modulo Usuarios)
        usuario = modelo.Usuario(nombre, apellidos, email,password)
        # Registro de usuario
        registro = usuario.registrar() # llamo el metodo registrar 

        # Comprobacion de registro
        if registro[0] >= 1:
            print(f'\nUsuario {registro[1].nombre} ha sido registrado con el emai {registro[1].email}')
        else:
            print('\nAlgo ha salido mal con el registro')

    def login(self):
        # Pedir los datos
        print('\nInicializando identificacion...')

        try:
            email = input('Introduce tu correo: ')
            password = input('Introduce tu contraseña: ')
            
            # Instancio la clase usuariop para utilizar el metodo identificar
            usuario = modelo.Usuario('', '', email, password) 
            
            # Uso el metod identificar en mi nuevo objeto
            login = usuario.identificar()

            # Comprobacion si el login es correcto
            if email == login[3]:
                print(f'\nBienvenido {login[1]}, tu regisro fue el {login[5]}')
                self.proximasAcciones(login)

        except Exception as e:
            print(type(e).__name__)
            print('Login incorrecto, asegurate que tu correo o contraseña sean correctos')

    def proximasAcciones(self, usuario):
        print('''
        Menu
        - Crear nota [c]
        - Mostrar tus notas [m]
        - Eliminar nota [e]
        - Salir [s]
        ''')
        accion = input('\n ¿Que deseas hacer? ')
        hazEl = notas.accionesN.Acciones()
        
        if accion == 'c':
            hazEl.crearN(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == 'm':
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == 'e':
            hazEl.eliminar(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == 's':
            print(f'Hasta pronto {usuario[1]}')
            exit()

