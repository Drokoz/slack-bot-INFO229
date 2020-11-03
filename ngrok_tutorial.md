# Tutorial ngrok

Tutorial para asignatura INFO229 de Universidad Austral de Chile, en la documentación se encontrará todas las referencias.

1. Introducción
2. Instalar ngrok
3. Comandos básicos
4. Conectar ngrok con Slack
5. Documentación

# 1. Introducción
## ¿Qué es ngrok? y para que sirve

Ngrok es una aplicación que habilta la exposición de un servidor local a internet, de una forma muy sencilla. El programa crea un puente entre el servidor local y un subdominio de ngrok.com.
Esto sirve para poder desarrollar software de una manera más cómoda ya que no es necesario algún servidor para poder interconectar servicios. Por ejemplo con slack podemos crear un servidor local y conectarlo con ngrok para poder usar Events API. Esto es parte muy importante para la implementación de bot ya que nos deja escuchar y reaccionar en tiempo real a eventos que pasen en el espacio de trabajo, así el bot poder responder a ellos.

# 2.Instalar ngrok

Para todo sistema operativo se necesitará descargar el paquete o ejecutable correspondiente en el siguiente [link](https://ngrok.com/download)
y deberá crearse una cuenta. Puede usar su cuenta google, github o crearse una desde 0 con email y contraseña.

*Nota: Se recomienda partir por la creación de la cuenta*

## Ubuntu o OSX

Para instalar ngrok en ubuntu
1. Abrir terminal en el directorio donde esté el paquete y ejecutar
```
unzip ngrok.zip
```
2. Conectar ngrok con tu cuenta
```
./ngrok authtoken <your_auth_token>
```

3. Verificar instalación y conectividad con el siguiente comando:
```
./ngrok version
```

*Nota: ngrok es sólo un ejecutable para poder seguir usandolo necesitas tenerlo en el directorio*
## WINDOWS

1. Descargar zip y ejecutar .exe que está adentro

# 3. Comandos básicos

Podrá ver toda la  documentación de ngrok [aquí](https://ngrok.com/docs). Siempre se ejecuta con ./ngrok <comando>

### Comandos:
   1. http	<puerto>	  -> Crea un tunel http en el puerto dado. 
   2. start <archivo>   -> Crea un tunel con un archivo de configuración
   3. tcp <puerto>      -> Crea un tunel TCP
   4. tls	<puerto>	    -> Crea un tunel TLS
   
### Ejemplos:
    1. ./ngrok http 80                    # servicio público URL para el puerto 80
    2. ./ngrok http -subdomain=baz 8080   # puerto 8080 habilitado en baz.ngrok.io
    3. ./ngrok http foo.dev:80            # tunel para a host:port en vez de localhost
    4. ./ngrok http https://localhost     # expose a local https server
    5. ./ngrok tcp 22                     # Tunel TCP de trafico para puerto 22
    6. ./ngrok tls -hostname=foo.com 443  # trafico TLS de foo.com a puerto 443
    7. ./ngrok start foo                  # empieza el tunel del contenido del archivo foo

# 4. Conectar ngrok con Slack

Para poder conectar ngrok con Slack se debe crear un puente entre el local:host y Slack. local:host no tiene una conexión real y continua con internet general, sólamente funciona desde la computadora. Esto se puede ver en el siguiente diagrama:
![alt text](https://cloud.githubusercontent.com/assets/32463/25376866/940435fa-299d-11e7-9ee3-08d9427417f6.png "Diagrama")

En este tutorial se usará el puerto 3000.

1. Crearemos un servidor ngrok: 
```
ngrok http 3000
```
Con el siguiente output

```
ngrok by @inconshreveable                                       (Ctrl+C to quit)
                                                                                
Session Status                online                                            
Account                       cuenta              
Version                       2.3.35                                            
Region                        United States (us)                                
Web Interface                 http://127.0.0.1:4040                             
Forwarding                    http://6b2839.ngrok.io -> http://localhost:3000
Forwarding                    https://6b2839.ngrok.io-> http://localhost:3000
                                                                                
Connections                   ttl     opn     rt1     rt5     p50     p90       
                              0       0       0.00    0.00    0.00    0.00      

```
2. Copiamos el link de https. En este caso "https://6b2839.ngrok.io"

3. Iniciamos nuestra app de bot

*Nota: En este momento ya deberiamos tener una aplicación que pueda escuchar eventos para esto dejo el [Link](https://github.com/slackapi/python-slack-sdk/tree/main/tutorial) tutorial en GitHub de Slack, está bien explicado y servirá para esto en especial el apartado 3 "03-responding-to-slack-events.md".La app también debemos abrirla en el puerto 3000*

4. Vamos a api.slack y seguimos los siguientes pasos:
    1. En la sección "Features" nos vamos a "*Event Subscriptions*"
    2. En "Request URL" ponemos nuestro link https y le agregamos /slack/events. Por ejemplo "https://6b2839.ngrok.io/slack/events". Esto es para que todas las consultas que se hagan sobre los eventos sean dirigidas a la "carpeta" /slacks/events. Si hicieron la aplicación con el Github mencionado antes, el link que conecta al bot y el servidor es con esa carpeta. Una vez insertado el link debería salir que está verificado. Por ejemplo:
    
    ![alt text](https://user-images.githubusercontent.com/1573454/30185162-644d0cb8-93ee-11e7-96af-55fe10d9d5c8.png "Request URL")
    
    3. Bajamos un poco y nos vamos a "Subscribe to bot events" y seleccionamos los que deseamos que estén activos para nuestro bot. Por ejemplo:
    
    ![alt text](https://user-images.githubusercontent.com/164546/97811582-609f6980-1c30-11eb-8e2a-861109b46bde.png "Events")
    
Y terminamos, esto debería hacer que nuestro bot pueda reaccionar a los eventos en nuestro canal.

5. Documentación

Links de donde se sacó la información: 

1.[Pagina de ngrok](https://ngrok.com/)

2.[Slack Github Events API](https://github.com/slackapi/python-slack-events-api/tree/main/example)

3.[Slack Github Tutorial](https://github.com/slackapi/python-slack-sdk/tree/main/tutorial)
