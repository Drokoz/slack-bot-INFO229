
<h1 id="introducción-a-node.js">Introducción a Node.JS</h1>
<p><img src="https://www.arsys.es/blog/file/uploads/2019/05/mayo-2019-nodejs.jpg" alt="Logo"></p>
<h2 id="¿qué-es">¿Qué es?</h2>
<p>Primero debemos entender que Node.js está basado en el lenguaje de programación JavaScript, este lenguaje beneficia el desarrollo de servidores ya que unifica el idioma y el formato de datos (JSON) esto se ve harto al hacer consultas o respuestas a servidores.</p>
<h3 id="entonces-¿que-es-node.js">Entonces, ¿Que es Node.js?</h3>
<p>Node.js es un entorno en tiempo de ejecución multiplataforma que principalmente se usa para la etapa de comunicación con el servidor con el desarrollo de algún software, páginas web, entre otras.</p>
<p>Node.js fue creado por los desarrolladores originales de JavaScript. Lo transformaron de algo que solo podía ejecutarse en el navegador en algo que se podría ejecutar en los ordenadores como si de aplicaciones independientes se tratara. Gracias a Node.js se puede ir un paso más allá en la programación con JavaScript no solo creando sitios web interactivos, sino teniendo la capacidad de hacer cosas que otros lenguajes de secuencia de comandos como Python pueden crear.</p>
<h2 id="¿para-qué-sirve">¿Para qué sirve?</h2>
<p>Node.js utiliza un modelo de solicitudes y respuestas sin bloqueo controlado por eventos que lo hace ligero y eficiente.</p>
<p>La idea principal de Node.js es usar una combinación entre su modelo y ser controlado por eventos para seguir siendo liviano y eficiente frente a las aplicaciones en tiempo real de uso de datos que se ejecutan en los dispositivos.</p>
<p>Node.js realmente brilla es en la creación de aplicaciones de red rápidas, ya que es capaz de manejar una gran cantidad de conexiones simultáneas con un alto nivel de rendimiento, lo que equivale a una alta escalabilidad.</p>
<h2 id="¿como-funciona">¿Como funciona?</h2>
<p>En comparación con las técnicas tradicionales de servicio web donde cada conexión (que crea una solicitud) genera un nuevo subproceso, ocupando la RAM del sistema y regularmente maximizando la cantidad de RAM disponible, en cambio, Node.js opera en un solo subproceso, utilizando el modelo mencionado anteriormente, lo que le permite soportar decenas de miles de conexiones al mismo tiempo mantenidas en el bucle de eventos.</p>
<p><img src="https://uploads.toptal.io/blog/image/92835/toptal-blog-image-1471270373483-e0bb1f43465b6646a91c347c793629e2.png" alt="EjemploNodeJS"></p>
<p>Cuando hay una nueva solicitud se genera un tipo de evento.</p>
<ul>
<li>El servidor empieza a procesarlo y, cuando hay una operación de<br>
bloqueo de solicitud, no espera hasta que se complete y en su lugar<br>
crea una función de devolución de llamada.</li>
<li>El servidor comienza en el acto a procesar otro evento (tal vez otra<br>
solicitud) y cuando finaliza la operación de solicitud continuará<br>
trabajando en esta, ejecutando la devolución de llamada tan pronto<br>
como tenga tiempo.</li>
</ul>
<p><img src="https://uploads.toptal.io/blog/image/92837/toptal-blog-image-1471270642718-64d896e7eac3cce483ac7dd8226b50da.png" alt="EjemploServidores"><br>
Por esta razón podemos concluir que tiene muy poca sobrecarga.</p>
<h2 id="ventajas-de-node.js">Ventajas de Node.js</h2>
<ol>
<li>Como Node.js está basado en JavaScript permite poder ser una forma simple y fácil de aprender a utilizarlo. En especial por programadores de Java.</li>
<li>El modelo de entrada y salida (consultas y respuestas) impulsado por eventos ayuda mucho en el manejo simultáneo de peticiones.</li>
<li>Tiene una basta comunidad por lo que ayuda bastante a la hora de problemas.</li>
<li>Node.js es unas de las plataformas de software más utilizada en este momento estando por encima en entornos de ejecución y lenguajes de programación como PHP y C a la vez que tiene un tiempo de ejecución (tiempo real) muy superior.</li>
<li>No es un código muy complejo, pero requiere muchas más líneas de codificación y mayor comprensión que el lenguaje PHP.</li>
<li>El envío de archivos de gran peso también se puede realizar mediante el uso de la tecnología Node.js.</li>
</ol>
<h2 id="desventajas">Desventajas</h2>
<ol>
<li>
<p>Un CPU de cálculo intensivo bloqueará la receptividad del Node.js, por lo que una plataforma de roscado es un mejor enfoque.</p>
</li>
<li>
<p>Utilizando Node.js con una base de datos relacional es aún bastante doloroso ya que la entrega de datos de este no es muy compatible.</p>
</li>
</ol>
<h1 id="conclusión">Conclusión</h1>
<p>Node.js es una de las tecnologías más usadas hoy en día, y se ha convertido en una de las plataformas más populares utilizadas para el desarrollo de aplicaciones web, aplicaciones de escritorio y servicios.<br>
Si el caso de uso no contiene operaciones intensivas del CPU ni el acceso a los recursos de bloqueo, puedes aprovechar los beneficios de Node.js y disfrutar de aplicaciones de red rápidas y escalables. Bienvenido a la web en tiempo real.</p>
<h2 id="tutoriales-recomendados">Tutoriales recomendados</h2>
<ul>
<li><a href="https://xurxodev.com/como-crear-un-api-rest-con-node-js/">Primeros Pasos</a></li>
<li><a href="https://www.arsys.es/blog/soluciones/desplegar-nodejs/">Aplicación en un Servidor Cloud</a></li>
<li><a href="https://www.w3schools.com/nodejs/">w3schools</a></li>
</ul>
<h1 id="documentación">Documentación</h1>
<ul>
<li><a href="https://www.toptal.com/nodejs/por-que-demonios-usaria-node-js-un-tutorial-caso-por-caso">¿Porque usar Node.js?</a></li>
<li><a href="https://nodejs.org/es/">Documentación de Node.js</a></li>
<li><a href="https://es.wikipedia.org/wiki/Node.js">Wikipedia: Node.js</a></li>
<li><a href="https://expressjs.com/es/">Express</a></li>
</ul>

