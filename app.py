from flask import Flask
from flask import render_template
import os
from os import listdir
from os.path import isfile, join


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gallery')
def gallery():
    # Chemin du répertoire contenant les images
    image_folder = os.path.join('static', 'images')
    # Liste des fichiers dans le répertoire
    images = os.listdir(image_folder)
    # Filtrer les fichiers pour ne garder que les images (en supposant des extensions jpg et png)
    images = [img for img in images if img.endswith('.jpg') or img.endswith('.png')]
    return render_template('gallery.html', images=images)

if __name__ == '__main__':
    app.run(debug=True)