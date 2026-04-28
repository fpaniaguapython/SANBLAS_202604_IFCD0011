import modulo_47_ejercicio_credenciales as credenciales

if __name__=='__main__':
    email = input('Introduce tu email:')
    password = input('Introduce tu contraseña:')

    credenciales.guardar_credenciales(email, password)

    print('Las credenciales se han guardado satisfactoriamente')