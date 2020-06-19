Add the needed translation files here.

To extract the tarnslation files use:

pybabel extract -F ./translations/babel.cfg -k _l -o ./translations/messages.pot --input-dirs=.

To create a language file use e.g. de

pybabel init -i ./translations/messages.pot -d translations -l de

To compile the tanslated text use:

pybabel compile -d translations
