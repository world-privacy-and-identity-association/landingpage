from flask import Flask
from flask import render_template, redirect
from flask_babel import Babel, gettext
from flask import jsonify
from flask_language import Language, current_language
from flaskext.markdown import Markdown
from markdown.extensions import Extension
from datetime import date
from flask import send_file
import os

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
    'supportdomain':app.config.get("SUPPORTDOMAIN"),
    'supportcertdomain':app.config.get("SUPPORTCERTDOMAIN"),
    'sha1':app.config.get("SHA1"),
    'sha256':app.config.get("SHA256"),
    'orgacert':app.config.get("ORGACERT"),
    'orgacertsupport':app.config.get("ORGACERTSUPPORT"),
    'community':app.config.get("COMMUNITY"),
    'year':date.today().year
}

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
    return render_template('roots.html', languages=get_languages(), conf=conf, orga=conf['orgacert'].split("/"))

@app.route('/community')
def community():
    return render_template('community.html', languages=get_languages(), conf=conf)

@app.route('/support')
def support():
    return render_template('support.html', languages=get_languages(), conf=conf, orga=conf['orgacertsupport'].split("/"))
    
@app.route('/supportfile')
def downloadSupportCert ():
    supportkey = os.path.join(app.root_path, "keys", "support.crt")
    return send_file(supportkey, as_attachment=True)

@app.route('/links')
def links():
    return render_template('links.html', languages=get_languages(), conf=conf)