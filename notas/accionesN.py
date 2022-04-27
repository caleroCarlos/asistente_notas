# Modulos
import notas.notas as modelo

# Clases

class Acciones:
    def crearN(self, usuario):
        print(f'\n Ok. Crear nueva nota...')

        titulo = input('Introduce el titulo de la nueva nota:')
        descripcion = input('Crea el contenido de la nota: ')

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f'\nNota {nota.titulo} guardada exitosamente')
        else:
            print(f'No se ha guardado la nota, por favor volverlo a intentar')

    def mostrar(self, usuario):
        print(f'\nVale {usuario[1]}, aqui tines tus notas')

        nota = modelo.Nota(usuario[0])
        notas = nota.listar()

        for i in notas:
            print('\n------------------------------------------------')
            print(f'Titulo: {i[2]}')
            print(f'{i[3]}')
            print('\n------------------------------------------------')

    def eliminar(self, usuario):
        print(f'Ok {usuario[1]}, vamos a borrar notas.')
        
        titulo = input('Introduce el titulo de la nota a borrar: ')

        nota = modelo.Nota(usuario[0], titulo,)
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f'Hemos eliminado la nota: {nota.titulo}')
        else:
            print('No se ha borrado la nota, intentalo nuevamente.')