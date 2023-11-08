# Pocillo-Termosensible

## ¿Cuál es el problema a resolver?

Muchas veces al usar recipientes como pocillos u ollas desconocemos sus temperaturas. Esto puede ser peligroso si el contenido está muy caliente, ya que al consumirlo o manipularlo se podrían generar quemaduras. Si bien es cierto que a la gran mayoría nos ha ocurrido al menos una vez y no es nada de gravedad, además de ser incómodo, una exposición prologada a este tipo de heridas puede llegar a tener efectos negativos en la salud del individuo. De igual forma, si el contenedor es de un tamaño más grande, o  guarda algún material con una temperatura excesiva, se aumentaría la posibilidad de un accidente verdaderamente trágico. 

Es así que surge la idea de un pocillo termosensible, capaz de indicar con exactitud los grados a los cuales está el contenido del mismo, con el fin de exponerle la información al usuario y este se mantenga precavido. En un primer plano, la idea es aplicada a un pocillo de cerámica porque es uno de los elementos que se usan con más frecuencia a la hora de ingerir bebidas, sin embargo, en un futuro se podría desarrollar el proyecto en diferentes contextos como ollas, calderos, o incluso máquinas de producción industrial.

## ¿Cómo lo llevamos a cabo?

Tuvimos varios inconvenientes a la hora de materializar esta increíble idea, el primero fue pensar en los cómos: Cómo vamos a medir la temperatura, cómo vamos a juntar todo, cómo vamos a notificar al usuario cuando su bebida esté lista, cómo vamos a diseñar la PCB. Con todas estas dudas en la cabeza, fuimos adelantando el proyecto y resolviéndolas una por una; medimos la temperatura con una sonda de 3V; para juntar todo, abandonamos la idea de modificar un pocillo y diseñamos un portavasos con todas las funciones que requeríamos y el hardware escondido bajo el mismo; para notificar al usuario, haremos uso de un pequeño display y un buzzer, periféricos de uso sencillo pero efectivo; y lo más difícil del proyecto, definir cómo se va a hacer la PCB, para eso tuvimos que documentarnos profundamente acerca de la manufactura de esta tecnología, y realizar un boceto general del cómo se iba a conectar cada periférico a la ESP-32.

