# Tarea 1:

## Temas a evaluar:

listas, if...else, arreglos, clases, herencia.

## Instrucciones

Tiempo para la prueba: 300 minutos
fecha hora de entrega: sabado 15, 11:55pm

### Clase Person

crear una clase ```Person```:
 - id:entero
 - name:cadena
 - age:entero

 - metodo constructor (```__init__```) tiene parametros: id, name, age
 - metodo representacion (```__repr__```) devolvera una cadena asi:
```bash
Person(id:1, name:bal, age:39)
```

### Clase Developer

crear otra clase ```Developer``` - que debe heredar de ```Person```:
- salary:flotante,
- language:cadena

- metodo constructor (```__init__```) tiene parametros: id, name, age, salary, language.
- metodo representacion (```__repr__```) devolvera una cadena asi:
```bash
Dev(id:1, name:bal, age:39, salary:1000.0, language:python)
```

### Clase Roster

crear otra clase ```Roster```:
- variable de instancia:
    - developerList: lista vacia(```[]```)
- metodo constructor (```__init__```) sin parametros
- metodo ```getDeveloperList()``` retorna la developerList
- metodo ```addDeveloper(Developer)```
- metodo ```addDeveloperData(id, name, age, salary, language)```
- metodo ```deleteDeveloper(id)```
- metodo ```updateDeveloper(id, name, age, salary, language)```
- metodo ```getDeveloperById(id)```
    - si lo encuentra retorna Developer
    - si no lo encuentra retorna None
- metodo ```getTotalSalary()```
    - retorna la suma de todos los salarios de los dev
- metodo ```getDevCountByLanguage()```
    - retorna un diccionario con los distintos lenguajes y cuantos developers saben ese lenguaje.
- metodo ```getTotalSalaryByLanguage()```
    - retorna un diccionario con los distintos lenguajes y la sumas de los salarios que siguen ese lenguaje.
