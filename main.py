from usuarios import acciones

accion1 = input("""
Bienvenido Que deseas hacer:
    - Registrarme [r]
    - Login [l]
""")

hazEl = acciones.Acciones()

if accion1 == 'r':
    hazEl.registro()
 
elif accion1 == 'l':
    hazEl.login()
 
else:
    print('\npor favor ingresa una accion correcta [r] para registro o [l] para login')
