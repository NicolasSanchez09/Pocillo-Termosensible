# Pocillo-Termosensible

## ¿Cuál es el problema a resolver?

Muchas veces al usar recipientes como pocillos u ollas desconocemos sus temperaturas. Esto puede ser peligroso si el contenido está muy caliente, ya que al consumirlo o manipularlo se podrían generar quemaduras. Si bien es cierto que a la gran mayoría nos ha ocurrido al menos una vez y no es nada de gravedad, además de ser incómodo, una exposición prologada a este tipo de heridas puede llegar a tener efectos negativos en la salud del individuo. De igual forma, si el contenedor es de un tamaño más grande, o  guarda algún material con una temperatura excesiva, se aumentaría la posibilidad de un accidente verdaderamente trágico. 

![image](https://github.com/NicolasSanchez09/Pocillo-Termosensible/assets/145717659/ec917255-da52-4e00-8b6f-727df27eb7c4)


Es así que surge la idea de un pocillo termosensible, capaz de indicar con exactitud los grados a los cuales está el contenido del mismo, con el fin de exponerle la información al usuario y este se mantenga precavido. En un primer plano, la idea es aplicada a un pocillo de cerámica porque es uno de los elementos que se usan con más frecuencia a la hora de ingerir bebidas, sin embargo, en un futuro se podría desarrollar el proyecto en diferentes contextos como ollas, calderos, o incluso máquinas de producción industrial.

## ¿Cómo lo llevamos a cabo?

Tuvimos varios inconvenientes a la hora de materializar esta increíble idea, pero el primero fue pensar en los 'cómos';
 ¿Cómo vamos a medir la temperatura?, ¿cómo vamos a juntar todo?, ¿cómo vamos a notificar al usuario cuando su bebida esté lista?, ¿cómo vamos a diseñar la PCB?..

Con todas estas dudas en la cabeza, fuimos avanzando en el proyecto hasta resolverlas una por una. 
En primer lugar, decidimos medir la temperatura con una sonda de 3V, debidamente impermeable, para introducirla directamente en el pocillo cómo un pitillo. De otra forma, adaptamos la idea de modificar un pocillo, para diseñar un portavasos con todas las funcionalidadess integradas, que tuviera el hardware escondido en la zona inferior. Así pues, se lograría un producto más versátil, ya que podría adaptarse a diferentes tamaños y formas de pocillos, pero además más útil, porque al público se le haría más cómodo comprar un servicio extra que le sirve a lo que ya tiene, a tener que adquirir algo que nuevo con una funcionalidad de más. Por otra parte, para notificar al usuario, elegimos hacer uso de un pequeño display y un buzzer, periféricos de uso sencillo pero efectivo, que no solo mostrarán en pantalla de forma dinámica si la bebida está lista para consumo, sino que además alertarán al usuario cuando esta llegue a determinada temperatura. Finalmente, lo más difícil del proyecto fue definir cómo se iba a diseñar la PCB, para eso tuvimos que documentarnos profundamente acerca de la manufactura de esta tecnología, y realizar un boceto general del cómo se iba a conectar cada periférico a la ESP-32 de forma efectiva, y pequeña, puesto que las dimensiones de un pocillo estándar no son algo exageradas.

# Las distintas fases del Proyecto

Como bien se resaltó en el anterior apartado, el proceso de creación del proyecto tuvo distintos percances, así que daremos un recorrido guiado por las distintas y más importantes fases de este proceso: 

## Fase de *planeación*

En la que se dio solución a algunos de los "cómos" previamente enunciados. Por ejemplo, en esta fase de planeación, definimos las tecnologías que se ibana usar, haciendo uso del diagrama de caja negra:

![image](https://github.com/NicolasSanchez09/Pocillo-Termosensible/assets/145825532/53749662-557d-44ff-9393-fc735cfd4337)

Como se aprecia en la imagen, hasta ese momento, no se tenía contemplado el uso de un buzzer para notificar al usuario, pero fue una buena idea que surgió más adelante junto con otras más, la importancia de esta etapa recae, principalmente en que, al tener que mirar cómo se va a llevar a cabo el proyecto, nos dimos cuenta de las diferentes dificultades que conllevaba, y fuimos capaces de coregir los fallos para evolucionar hacia un resultado más eficiente.

Luego de realizar este diagrama, se decidió llevar a cabo el diagrama tecnológico, en el que se definiría concretamente qué dispositivo de hardware, ya sea sensor o actuador, se iba a usar para cada función como se puede ver en la siguiente imagen:

![image](https://github.com/NicolasSanchez09/Pocillo-Termosensible/assets/145825532/5ad2268b-6cde-450f-bfbe-822f1ad6d677)

Ahora bien, en este punto aún no se ha añadido el buzzer al plan de acción, pero para mostrar cuál es el que se va a usar, adjuntaré link de compra en mercado libre y una foto: https://articulo.mercadolibre.com.co/MCO-608847377-buzzer-alarma-chicharra-3v-a-24v-dc-zumbador-grande-arduino-_JM#position=1&search_layout=stack&type=item&tracking_id=e0f2a067-7c86-415b-b5b0-ef70a2830b28

![image](https://github.com/NicolasSanchez09/Pocillo-Termosensible/assets/145825532/1673b827-4085-4ac0-b9c4-7491be77eac8)

Una vez definidas las tecnologías con las que íbamos a trabajar, nos efrentábamos, sin saberlo, a la fase más difícil de este largo camino: La Fase de Acción.

## Fase de *acción*

Lo dicho, la fase más complicada del proceso. Al tratar de llevar todo a cabo y aterrizarlo al plano de la realidad, nos dimos cuenta de que realmente había mucho por corregir. Tuvimos que abandonar la idea de un pocillo como tal, debido a que no era práctico adicionar todo el hardware a un simple pocillo de cerámica, por sugerencia del profe, se decidió continuar con la misma idea pero desde una base para el pocillo, es decir, un portavasos con todas las funciones ya mencionadas. Se modeló la base y el soporte del display en OnShape para poderlo imprimir en PLA, se lo enviamos a El grandioso Carlos Mario, quien nos hizo el favor (a cambio de un módico precio) de imprimirlo. 

Ya estaba la base del proyecto hablando en términos generales, pero en términos electrónicos, no había una base, una PCB a la que se pudiera conectar todo para su correcto funcionamiento. Y es con esta, aparentemente, simple tarea, que el proyecto se complicó en gran medida.

Primero, realizar un diagrama de cómo se conectaría todo a la ESP-32, luego, estudiar cómo se transforma eso en una PCB, para finalmente, darnos cuenta de que estaba mal y tener que repetir ese mismo proceso al menos tres veces.

Finalmente, el diseño de las conecciones en Qucs quedó de la siguiente manera: 

![image](https://github.com/NicolasSanchez09/Pocillo-Termosensible/assets/145825532/3799e650-d350-49ad-aabc-8187ab5e34b6)

Y, con este "boceto" de circuito, la PCB quedaría de la siguiente manera, representada en 3D gracias a las herramientas de simulación de KiCad

![image](https://github.com/NicolasSanchez09/Pocillo-Termosensible/assets/145825532/59dbe784-b218-462a-b49f-ce4cf3d5b38d)


