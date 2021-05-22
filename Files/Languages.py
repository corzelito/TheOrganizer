import configparser
import locale
import gettext

class Languages:
    idioms = ("English", "Spanish")

    def getLanguage():
        config = configparser.ConfigParser()
        config.read('settings.ini')
        languageSelected = config.get("Languages", "language")

        if languageSelected == "Spanish":
            language = "es_ES"
            return str(language)
        else:
            language = "en"
            return str(language)

    def setLanguage():
        language = Languages.getLanguage()
        locale.setlocale(locale.LC_ALL, str(language))
        el = gettext.translation('base', localedir='locales', languages=[str(language)], fallback=False)
        el.install()
        _ = el.gettext
