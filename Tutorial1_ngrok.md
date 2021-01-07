<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tutorial1_ngrok</title>
  <link rel="stylesheet" href="https://stackedit.io/style.css" />
</head>

<body class="stackedit">
  <div class="stackedit__html"><h1 id="tutorial-ngrok">Tutorial ngrok</h1>
<p>Tutorial para asignatura INFO229 de Universidad Austral de Chile, en la documentación se encontrará todas las referencias.</p>
<ol>
<li>Introducción</li>
<li>Instalar ngrok</li>
<li>Comandos básicos</li>
<li>Conectar ngrok con Slack</li>
<li>Documentación</li>
</ol>
<h1 id="introducción">1. Introducción</h1>
<h2 id="¿qué-es-ngrok-y-para-que-sirve">¿Qué es ngrok? y para que sirve</h2>
<p>Ngrok es una aplicación que habilta la exposición de un servidor local a internet, de una forma muy sencilla. El programa crea un puente entre el servidor local y un subdominio de <a href="http://ngrok.com">ngrok.com</a>.<br>
Esto sirve para poder desarrollar software de una manera más cómoda ya que no es necesario algún servidor para poder interconectar servicios. Por ejemplo con slack podemos crear un servidor local y conectarlo con ngrok para poder usar Events API. Esto es parte muy importante para la implementación de bot ya que nos deja escuchar y reaccionar en tiempo real a eventos que pasen en el espacio de trabajo, así el bot poder responder a ellos.</p>
<h1 id="instalar-ngrok">2.Instalar ngrok</h1>
<p>Para todo sistema operativo se necesitará descargar el paquete o ejecutable correspondiente en el siguiente <a href="https://ngrok.com/download">link</a><br>
y deberá crearse una cuenta. Puede usar su cuenta google, github o crearse una desde 0 con email y contraseña.</p>
<p><em>Nota: Se recomienda partir por la creación de la cuenta</em></p>
<h2 id="ubuntu-o-osx">Ubuntu o OSX</h2>
<p>Para instalar ngrok en ubuntu</p>
<ol>
<li>Abrir terminal en el directorio donde esté el paquete y ejecutar</li>
</ol>
<pre><code>unzip ngrok.zip
</code></pre>
<ol start="2">
<li>Conectar ngrok con tu cuenta</li>
</ol>
<pre><code>./ngrok authtoken &lt;your_auth_token&gt;
</code></pre>
<ol start="3">
<li>Verificar instalación y conectividad con el siguiente comando:</li>
</ol>
<pre><code>./ngrok version
</code></pre>
<p><em>Nota: ngrok es sólo un ejecutable para poder seguir usandolo necesitas tenerlo en el directorio</em></p>
<h2 id="windows">WINDOWS</h2>
<ol>
<li>Descargar zip y ejecutar .exe que está adentro</li>
</ol>
<h1 id="comandos-básicos">3. Comandos básicos</h1>
<p>Podrá ver toda la  documentación de ngrok <a href="https://ngrok.com/docs">aquí</a>. Siempre se ejecuta con ./ngrok </p>
<h3 id="comandos">Comandos:</h3>
<ol>
<li>http		  -&gt; Crea un tunel http en el puerto dado.</li>
<li>start    -&gt; Crea un tunel con un archivo de configuración</li>
<li>tcp       -&gt; Crea un tunel TCP</li>
<li>tls		    -&gt; Crea un tunel TLS</li>
</ol>
<h3 id="ejemplos">Ejemplos:</h3>
<pre><code>1. ./ngrok http 80                    # servicio público URL para el puerto 80
2. ./ngrok http -subdomain=baz 8080   # puerto 8080 habilitado en baz.ngrok.io
3. ./ngrok http foo.dev:80            # tunel para a host:port en vez de localhost
4. ./ngrok http https://localhost     # expose a local https server
5. ./ngrok tcp 22                     # Tunel TCP de trafico para puerto 22
6. ./ngrok tls -hostname=foo.com 443  # trafico TLS de foo.com a puerto 443
7. ./ngrok start foo                  # empieza el tunel del contenido del archivo foo
</code></pre>
<h1 id="conectar-ngrok-con-slack">4. Conectar ngrok con Slack</h1>
<p>Para poder conectar ngrok con Slack se debe crear un puente entre el local:host y Slack. local:host no tiene una conexión real y continua con internet general, sólamente funciona desde la computadora. Esto se puede ver en el siguiente diagrama:<br>
<img src="https://cloud.githubusercontent.com/assets/32463/25376866/940435fa-299d-11e7-9ee3-08d9427417f6.png" alt="alt text" title="Diagrama"></p>
<p>En este tutorial se usará el puerto 3000.</p>
<ol>
<li>Crearemos un servidor ngrok:</li>
</ol>
<pre><code>ngrok http 3000
</code></pre>
<p>Con el siguiente output</p>
<pre><code>ngrok by @inconshreveable                                       (Ctrl+C to quit)
                                                                                
Session Status                online                                            
Account                       cuenta              
Version                       2.3.35                                            
Region                        United States (us)                                
Web Interface                 http://127.0.0.1:4040                             
Forwarding                    http://6b2839.ngrok.io -&gt; http://localhost:3000
Forwarding                    https://6b2839.ngrok.io-&gt; http://localhost:3000
                                                                                
Connections                   ttl     opn     rt1     rt5     p50     p90       
                              0       0       0.00    0.00    0.00    0.00      

</code></pre>
<ol start="2">
<li>
<p>Copiamos el link de https. En este caso “<a href="https://6b2839.ngrok.io">https://6b2839.ngrok.io</a>”</p>
</li>
<li>
<p>Iniciamos nuestra app de bot</p>
</li>
</ol>
<p><em>Nota: En este momento ya deberiamos tener una aplicación que pueda escuchar eventos para esto dejo el <a href="https://github.com/slackapi/python-slack-sdk/tree/main/tutorial">Link</a> tutorial en GitHub de Slack, está bien explicado y servirá para esto en especial el apartado 3 “<a href="http://03-responding-to-slack-events.md">03-responding-to-slack-events.md</a>”.La app también debemos abrirla en el puerto 3000</em></p>
<ol start="4">
<li>
<p>Vamos a api.slack y seguimos los siguientes pasos:</p>
<ol>
<li>En la sección “Features” nos vamos a “<em>Event Subscriptions</em>”</li>
<li>En “Request URL” ponemos nuestro link https y le agregamos /slack/events. Por ejemplo “<a href="https://6b2839.ngrok.io/slack/events">https://6b2839.ngrok.io/slack/events</a>”. Esto es para que todas las consultas que se hagan sobre los eventos sean dirigidas a la “carpeta” /slacks/events. Si hicieron la aplicación con el Github mencionado antes, el link que conecta al bot y el servidor es con esa carpeta. Una vez insertado el link debería salir que está verificado. Por ejemplo:</li>
</ol>
<p><img src="https://user-images.githubusercontent.com/1573454/30185162-644d0cb8-93ee-11e7-96af-55fe10d9d5c8.png" alt="alt text" title="Request URL"></p>
<ol start="3">
<li>Bajamos un poco y nos vamos a “Subscribe to bot events” y seleccionamos los que deseamos que estén activos para nuestro bot. Por ejemplo:</li>
</ol>
<p><img src="https://user-images.githubusercontent.com/164546/97811582-609f6980-1c30-11eb-8e2a-861109b46bde.png" alt="alt text" title="Events"></p>
</li>
</ol>
<p>Y terminamos, esto debería hacer que nuestro bot pueda reaccionar a los eventos en nuestro canal.</p>
<h1 id="documentación">5. Documentación</h1>
<p>Links de donde se sacó la información:</p>
<p>1.<a href="https://ngrok.com/">Pagina de ngrok</a></p>
<p>2.<a href="https://github.com/slackapi/python-slack-events-api/tree/main/example">Slack Github Events API</a></p>
<p>3.<a href="https://github.com/slackapi/python-slack-sdk/tree/main/tutorial">Slack Github Tutorial</a></p>
</div>
</body>

</html>
