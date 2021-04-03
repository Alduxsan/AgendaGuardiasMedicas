# REFERENCIAS DE REQUEST PARA API MEDIGUARD

## LOGEO EN LA API
Para realizar los demás requests es necesario que el usuario primero se loguee a la API y guarde/use el __Token__ que se le devuelve en respuesta.

__ENDPOINT PARA LOGIN:__

### /api/api_login

__Al endpoint de api_login debe entregarse un json con el siguiente formato:__

{"username":"username","password":"password"}


## CONSULTAS DESDE USUARIOS MÉDICOS

Una vez realizado el logeo en la api los siguientes endpoints se encontraran disponibles para los __usuarios que pertenecen al grupo Médicos__.

### /guardias_disponibles 
Devuelve una lista de guardias (y sus atributos) con el atributo *disponible=True* y cuyo valor de *min_ranking* sea mayor o igual al valor de *ranking* del médico
asociado al usuario logeado

### /guardias_disponibles/pk
Devolverá la guardia que figure con el mismo id que el valor que se le haya pasado como **pk** .

### /guardias_filtro/?dep=parametro1-parametro2-parametro3
Devuelve una lista de guardias (y sus atributos) cuyo valor en el atributo **departamento** sea igual a alguno de los valores pasados como parámetros, 
tenga el atributo *disponible=True* y cuyo valor de *min_ranking* sea mayor o igual al valor de *ranking* del médico
asociado al usuario logeado .
Es importante destacar que luego de __guardias_filtro/__ debe colocarse __dep=__ y acto seguido separar cada nombre de departamento (que debe ser escrito
en forma correcta, con su primer letra en mayúscula y el resto en minúsculas) con un guión __-__ sin espacios. En caso de que el nombre tenga espacios
(como "Cerro Largo") debe usarse %20.

### /mis_guardias
Devuelve una lista de todas las guardias (y sus atributos) que tienen al médico asciado al usuario logeado como valor en su atributo **medico**

### /modificar_guardia/pk
Devuelve la guardia (y sus atributos) que posee el valor de id igual al que se haya pasado como parámetro **pk** (pk)
Permite realizar un request de tipo __PUT__ (sería el que utilizaríamos para editar la guardia cuando un medico se anote o borre de ella) cuyo json se 
vería así: 

{
    "id": 1,
    "fecha": "2021-03-29",
    "turno": "23:00 a 05:00",
    "disponible": false,
    "departamento": "Maldonado",
    "min_ranking": 1,
    "centroSalud": "centro_salud_1",
    "medico": 44191764
}


### /medico_datos
Devuelve la instancia de médico (y sus atributos) asociada al usuario logeado

### /medico_datos/pk
Permite hacer un request de tipo __PUT__ y actualizar los datos de la instancia de médico que se le haya pasado como **pk**
Un json para actualizar los datos de un médico se vería así:

{
    "ci": 44191764,
    "ranking": 1,
    "nroCaja": 150,
    "telefono": 98877234,
    "departamento": "Maldonado",
    "direccion": "S/A",
    "usuario": 2
}



