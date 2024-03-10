from flask import Flask
from flask import render_template

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config['TEMPLATES_AUTO_RELOAD'] = True

    @app.route("/")
    def display_main_page():
        return render_template("index.html")
    @app.route("/words")
    def display_words1():
        return render_template("words.html")
    
    @app.route("/wordsold")
    def display_words2():
        return render_template("oldwords.html")
    
    @app.route("/words/ava")
    def display_ava():
        return render_template("ava.html")
    
    @app.route("/words/vibe")
    def display_vibe():
        return render_template("vibe.html")
    
    @app.route("/wordsold/sovparshiv")
    def display_sovparshiv():
        return render_template("sovparshiv.html")
    
    @app.route("/wordsold/shnurky")
    def display_shnurky():
        return render_template("shnurky.html")
    

    





    return app