from flask import Flask

from helper import pets

app = Flask(__name__)

# Main route
@app.route('/')
def index():
  return '''
  <h1>Adopt a Pet!</h1>
  <p>Browse through the links below to find your new furry friend:</p>
  <ul>
    <li>
      <a href="/animals/dogs">Dogs</a>
    </li>
    <li>
    <a href="/animals/cats">Cats</a>
    </li>
    <li>
      <a href="/animals/rabbits">Rabbits</a>
    </li>
  </ul>
  '''

# Animal-list route
@app.route('/animals/<pet_type>')
def animals(pet_type):
  html = f"<h1>List of {pet_type}</h1>"
  html += "<ul>"
  number = -1
  for pet in pets[pet_type]:
    number -= number
    element = pet.get('name', 'ERROR')
    html += f'<li><a href="/animals/{pet_type}/{number}">{element}</a></li>'
  html += "</ul>"
  return html

# Pet-detail route
@app.route('/animals/<string:pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
  pet = pets[pet_type][pet_id]
  print(pet)
  pet_id += 1
  html = f"<h1>This is {pet_type} number {pet_id}"

  element = pet.get('name', 'ERROR')
  html += f'<h1>Name: {element}</h1>'
  element = pet.get('age', 'ERROR')
  html += f'<h2>Age: {element}</h2>'
  element = pet.get('breed', 'ERROR')
  html += f'<h3>Breed: {element}</h3>'
  element = pet.get('description', 'ERROR')
  html += f'<p>Description: {element}</p>'
  element = pet.get('url', 'ERROR')
  html += f'<img src="{element}"></img>'
  return html

app.run(debug=True, host="0.0.0.0")
