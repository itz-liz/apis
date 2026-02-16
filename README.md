# apis
Creacion de API's

# Aplicacion 000
1. Primero instalas fastapi[standard]
2. EL coidgo de partida es de fast api
3. Para ver la documentacion al finalizar de la url simplemnete pones /docs 

# Aplicacion 001
1. Hacer una agenda, en este caso con sqlite3 con estos parametros  
  
|  Contactos    |              | 
|:-------------:|:------------:|
| id_contacto   | int PK       |
| nombre        | varchar (100)|
|email          | varchar (100)|
|telefono       | varchar (100)|  

Insertar 100 registros

2. Hacer un /docs  

| No.      | Propiedad| Detalle  |
|----------|----------|:----------:|
|1| Description|Endpoint de Bienvenida|
|2| Summary|Endpoint de BIenvenida a la agenda|
|3| Method|GET|
|4| Endpoint|/|
|5| Authentication|NA|
|6| Query param|NA|
|7| Path param|NA|
|8| Data|NA|
|9| Status Code|202|
|10| Response|{"message":"Agenda", "datetime": "timestamp"}|
|11| Response Type|application/json|
|12| Status Code (error)|NA|
|13| Response Type(error) |NA|
|14| Response (error)|NA|
|15| cURL|curl -X GET http://127.0.0.1:8000/|

3. Consultar todos los contactos  

| No.      | Propiedad| Detalle  |
|----------|----------|:----------:|
|1| Description|Endpoint para consultar todos los contactos|
|2| Summary|Regresa los contactos paginados|
|3| Method|GET|
|4| Endpoint|/v1/contactos|
|5| Authentication|NA|
|6| Query param|limit:int&skip:int|
|7| Path param|NA|
|8| Data|NA|
|9| Status Code|202|
|10| Response|{"table":"contactos", "items": [{"id_contacto":int, "nombre": str,"email": str, "telefono": str}],"count":int, "datetime": timestamp, "message":"Datos consultados exitosamente",limit":10,"skip":0}|
|11| Response Type|application/json|
|12| Status Code (error)|400, 401, 403, 404, 409, 422, 500, 501, 502, 503, 504|
|13| Response Type(error) |applicaction/json|
|14| Response (error)|{"detail":"Parámetros inválidos", "datetime":"timestamp"} / {"detail":"Direccion Incorrecta", "datetime":"timestamp"} / {"detail":"No puedes entrar Acceso prohibido", "datetime":"timestamp"} / {"detail":"No se encontraron contactos", "datetime":"timestamp"} / {"detail":"Conflicto: contacto duplicado", "datetime":"timestamp"} / {"detail":"Error de validación", "datetime":"timestamp"} / {"detail":"Error interno al consultar contactos", "datetime":"timestamp"} / {"detail":"Error de comunicación con servidor externo", "datetime":"timestamp"} / {"detail":"Servicio no disponible", "datetime":"timestamp"} / {"detail":"Tiempo de espera agotado", "datetime":"timestamp"}|
|15| cURL|curl -X GET http://127.0.0.1:8000/|


4. Buscar Contactos  

| No.      | Propiedad| Detalle  |
|----------|----------|:----------:|
|1| Description|Endpoint para buscar un contacto|
|2| Summary|Regresa el contacto buscado|
|3| Method|GET|
|4| Endpoint|/v1/contactos/{id_contacto}|
|5| Authentication|NA|
|6| Query param|NA|
|7| Path param|id_contacto:int|
|8| Data|NA|
|9| Status Code|202|
|10| Response|{"table":"contactos", "items":[{"id_contacto":int, "nombre": str,"email": str, "telefono": str}],"count":int,"datetime": timestamp, "message":"Datos consultados exitosamente"}|
|11| Response Type|application/json|
|12| Status Code (error)|400|
|13| Response Type(error) |application/json|
|14| Response (error)|{"table": "contactos","item": {},"count": 0, "datetime": timestamp, "message": "Contacto no encontrado"} / {"detail":"Error al buscar el registro", "datetime":"timestamp"}|
|15| cURL|curl -X GET http://127.0.0.1:8000/v1/contactos/3|  


5. Insertar contacto  

| No.      | Propiedad| Detalle  |
|----------|----------|:----------:|
|1| Description|Endpoint para insertar un contacto|
|2| Summary|Inserta un contacto validando campos|
|3| Method|POST|
|4| Endpoint|/v1/contactos|
|5| Authentication|NA|
|6| Query param|NA|
|7| Path param|NA|
|8| Data|{"nombre": str, "email": str, "telefono": str}|
|9| Status Code|201|
|10| Response|{"table":"contactos", "item": {"id_contacto":int, "nombre": str, "email": str, "telefono": str}, "datetime": timestamp, "message":"Contacto insertado exitosamente"}|
|11| Response Type|application/json|
|12| Status Code (error)|400|
|13| Response Type(error) |application/json|
|14| Response (error)|{"detail":"Error en la base de datos", "datetime":"timestamp"} / {"message":"Campos vacios", "datetime":"timestamp"}|
|15| cURL|curl -X POST http://127.0.0.1:8000/v1/contactos -H "Content-Type: application/json" -d '{"nombre":"Liz", "email":"liz@email.com", "telefono":"1234567890"}'|

