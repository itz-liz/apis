# apis
Creacion de API's

# Aplicacion 000
1. Primero instalas fastapi[standard]
2. EL coidgo de partida es de fast api
3. Para ver la documentacion al finalizar de la url simplemnete pones /docs 

# Aplicacion 001
1. Hacer una agenda, en este caso con sqlite3 con estos parametros  


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
|10| Response|{"table":"contactos", "items": [{"id_contacto":int, "nombre": str,"email": str, "telefono": str},]"count":int, "datetime": timestamp, "message":"Datos consultados exitosamente"}|
|11| Response Type|application/json|
|12| Status Code (error)| |
|13| Response Type(error) |NA|
|14| Response (error)||
|15| cURL|curl -X GET http://127.0.0.1:8000/|
