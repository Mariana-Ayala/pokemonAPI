# PokemonAPI

This is a simple API built with **Flask** that return basic information about some Pokémon.
It was created as a learning project to practice APIs and Python.

---
## Installation and Usage
  - Clone the repository:
   git clone https://github.com/Mariana-Ayala/pokemon.git
  - Install dependencies
    pip install flask
  - Run the server
    python app.py

## Endpoints
  - `Get /pokemons` - returns the list of all pokemons
  - `Get /pokemons/<id>` - return the details of a specific Pokémon
  - `POST /pokemons` - Add a new Pokémon (send JSON in the request body)
  - `DELETE /pokemons/<id>` - Delete a Pokémon by ID
  * example: 
      GET http://127.0.0.1:5000/pokemons/1

## Technologies
  * Python
  * Flask

## Tools 
  * Postman (for testing the API) <!-- Usado para probar la API -->

## To Do
  - Add more Pokémon
  - Delete Pokémon with ID
    
## Author
  Mariana Ayala 
