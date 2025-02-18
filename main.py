from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def obtener_ip_usuario():
    # Intentamos obtener la IP real del cliente desde el encabezado 'X-Forwarded-For'
    ip_usuario = request.headers.get('X-Forwarded-For', request.remote_addr)

    # Si hay varios valores en 'X-Forwarded-For', tomamos el primero
    if ip_usuario:
        ip_usuario = ip_usuario.split(',')[0]  # Asegura que obtengas solo la IP original

    return f'La IP del usuario que accedió a la aplicación es: {ip_usuario}'


if __name__ == '__main__':
    # Se asegura de que la aplicación Flask escuche en todas las interfaces de red
    app.run(host='0.0.0.0', port=5000)
