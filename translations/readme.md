Add the needed translation files here.

To extract the translation files use:

```
pybabel extract -F ./translations/babel.cfg -k _l -o ./translations/messages.pot --input-dirs=.
```

To create a language file use e.g. de

```
pybabel init -i ./translations/messages.pot -d translations -l de
```

To compile the translated text use:

```
pybabel compile -d translations
```

The translation files are mainitained in a repo and translated on Transifex [https://www.transifex.com/wpia/landingpage-1/dashboard/](https://www.transifex.com/wpia/landingpage-1/dashboard/).


The translation file are stored in this files structure translations/XX/LC_MESSAGES/messages.po with XX as language code.