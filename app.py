from flask import Flask

from helper import pets

app = Flask(__name__)


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


@app.route('/animals/<pet_type>')
def animals(pet_type):
  html = f"<h1>List of {pet_type}</h1>"
  html += "<ul>"
  for pet in pets[pet_type]:
    element = pet.get('name', 'ERROR')
    html += f"<li>{element}</li>"
  html += "</ul>"
  return html


@app.route('/animals/<string:pet_type>')
def animals_list(pet_type):
  html = f"<h1>List of {pet_type}"
  return html


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


@app.route('/dogs')
def dogs():
  return '''What is Lorem Ipsum?
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.

Why do we use it?
It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).


Where does it come from?
Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.

The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.

Where can I get some?
There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.'''


@app.route('/cats')
def cats():
  return '''
  cat

  Artikel
  Diskussion
  Läs
  Redigera
  Redigera wikitext
  Visa historik

  Verktyg

  För andra betydelser, se Cat (olika betydelser).
  cat[1] är ett Unixverktyg och kommando som utvecklades i början av 1970-talet.[2] Namnet är kortform för det engelska ordet concatenate som betyder sammanfoga.

  cat har flera användningsområden. De huvudsakliga är att sammanfoga innehållet i filer och att läsa innehållet i filer.[1] Ett ytterligare användningsområde är att skriva en ny textfil.[3] Detta är lämpligt om det avsedda innehållet är mycket enkelt eller i en del mycket speciella situationer, annars är textredigerare som vi bättre.

  Ett relaterad kommando i äldre Microsoft- och DOS-baserade operativsystem är type.[4]
  '''


#STOP


@app.route('/horses')
def horses():
  return "nun"


app.run(debug=True, host="0.0.0.0")
