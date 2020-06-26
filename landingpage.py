from flask import Flask
from flask import render_template, redirect
from flask_babel import Babel, gettext
from flask import jsonify
from flask_language import Language, current_language
from flaskext.markdown import Markdown
from markdown.extensions import Extension
from datetime import date

app = Flask(__name__)
#app.register_blueprint(filters.blueprint)
babel = Babel(app)
lang = Language(app)

class EscapeHtml(Extension):
    def extendMarkdown(self, md, md_globals):
        del md.preprocessors['html_block']
        del md.inlinePatterns['html']

md = Markdown(app, extensions=[EscapeHtml()])

# Load config
app.config.from_pyfile('config.py')

conf={
    'appname':app.config.get("APP_NAME"), 
    'logo':app.config.get("LOGO"),
    'favicon':app.config.get("FAVICON"),
    'domain':app.config.get("DOMAIN"),
    'sha1':app.config.get("SHA1"),
    'sha256':app.config.get("SHA256"),
    'community':app.config.get("COMMUNITY"),
    'year':date.today().year
}

#current_year = 
#conf.year = "- " + str(current_year)
#if current_year == 2021:
#    conf.year = ""


@lang.allowed_languages
def get_allowed_languages():
    return app.config['LANGUAGES'].keys()

@lang.default_language
def get_default_language():
    return 'en'

@babel.localeselector
def get_locale():
    return str(current_language)

def get_languages():
    return app.config['LANGUAGES']


@app.route('/')
@app.route('/index')
def main():
        return render_template('index.html', languages=get_languages(), conf=conf)

def rel_redirect(loc):
    r = redirect(loc)
    r.autocorrect_location_header = False
    return r


@app.route("/language/<string:language>")
def set_language(language):
    lang.change_language(language)
    return rel_redirect("/")

@app.route('/about')
def about():
        return render_template('about.html', languages=get_languages(), conf=conf)

@app.route('/rootcert')
def roots():
        return render_template('roots.html', languages=get_languages(), conf=conf)

@app.route('/community')
def community():
        return render_template('community.html', languages=get_languages(), conf=conf)
