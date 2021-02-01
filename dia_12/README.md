# DIA 12
---
**Scope y Namespace**

**Scope**
El alcance de un nombre es la región de un programa en la que ese nombre tiene significado. El intérprete determina esto en tiempo de ejecución en función de dónde se produce la definición del nombre y en qué parte del código se hace referencia al nombre.

**Local**
* El intérprete de python crea un nuevo espacio de nombres cada vez que se ejecuta una función.
* Ese espacio de nombres es local a la función y permanece hasta que la función termina.
* La variable no puede ser utilizada fuera de la función ni por otra diferente.

**Global**
* El espacio de nombres global contiene cualquier nombre definido en el nivel del programa principal. Python crea el espacio de nombres global cuando se inicia el cuerpo del programa principal y permanece hasta que termina el intérprete. Si la variable fue utilizada cuando es invocada alguna función, esta internamente la puede modificar pero solo de forma local ya que luego vuelve a tomar el mismo valor que tenia antes de ser usada por la función.

**Palabra Clave "global"**
* Permite que la variable sea moficada en cualquier parte del cogido donde sea invocada

