from flask import Flask, request, jsonify 
#request para recibir datos del cliente 
#jsonfy conveierte estructuras de python en JSON
#flask era para poder interactuar con APIS

app = Flask(__name__) #ninicia el servidor

#lista de pokemones
pokemons = [
    {"id": 1, "name": "Bulbasaur", "type": "Grass/Poison"},
    {"id": 2, "name": "Charmander", "type": "Fire"},
    {"id": 3, "name": "Squirtle", "type": "Water"}
]

@app.route("/")
#ejecutar esa funcion en API 
def inicio():
    return {"mensaje": "Bienvenida a tu API de Pokemon"}
#una funcion donde se mostrara un mensaje de inicio, en la pagina 

# GET - obtener todos los pokemones
@app.route("/pokemons", methods=["GET"])
#mostrar la lista de pokemones 
def get_pokemons(): #creamos una funcion para transformar los datos de los pokemones el JSON
    return jsonify(pokemons)

# GET - obtener un pokemon por ID
@app.route("/pokemons/<int:pokemon_id>", methods=["GET"])
#recibira un entero para mostrar el pokemon 
def get_pokemon(pokemon_id):
    for p in pokemons: 
        if p["id"] == pokemon_id:
            return jsonify(p)
    return {"error": "Pokemon no encontrado"}, 404
#esta funcion es para buscar dentro de la lista, el error 404 es no encontrado 
#es para buscar un pokemon con su ID

# POST - agregar un nuevo pokemon
@app.route("/pokemons", methods=["POST"])
def add_pokemon():
    nuevo = request.get_json()  #lee los datos en forma de JSON
    #Se verifica que no se repita el ID
    for p in pokemons:
        if p["id"] == nuevo["id"]:
            return{"error" : "El pokemon ya existe "},400
    #si el id no existe entonces
    #se verifica que los atributos si sean del tipo establecido
    if isinstance(nuevo["id"],int) and isinstance(nuevo["name"],str) and isinstance(nuevo["type"],str):
        pokemons.append(nuevo) #si son del tipo se agregan al diccionario
        return{"mensaje":"pokemon agregado correctamente"},201
    else :
        return{"Error":"No se puede agregar el pokemon"},401
#esta funcion es para crear dentro de la API

@app.route("/pokemons/<int:pokemon_id>", methods=["DELETE"])
def delete_pokemon(pokemon_id): 
    for p in pokemons:
        if p["id"] == pokemon_id:
            pokemons.remove(p)
            return{"mensaje":"pokemon eliminado correctamente "},200
    return{"Error": "Pokemon no encontrado"},404

@app.route("/pokemons/<int:pokemon_id>",methods=["PUT"])
def update_pokemon(pokemon_id):
    actualizar = request.get_json()
    for p in pokemons:
        if p["id"] == pokemon_id:
            if "name" in actualizar and isinstance(actualizar["name"],str):
                p["name"] = actualizar["name"]
            if "type" in actualizar and isinstance(actualizar["type"],str):
                p["type"] = actualizar["type"]
    
            return{"Mensaje":"El pokemon fue actualizado correctamente","data":p},200
    return{"Error":"Pokemon no ecnontrado"},404
        

if __name__ == "__main__":
    app.run(debug=True)
    #arranca el servidor
