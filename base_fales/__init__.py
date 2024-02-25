from flask import Flask
from flask import render_template

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    @app.route("/")
    def display_main_page():
        return render_template("index.html")
    @app.route("/words")
    def display_words1():
        return render_template("words.html")
    
    @app.route("/wordsold")
    def display_words2():
        return render_template("oldwords.html")
    





    return app