from Files.Languages import *
import configparser
from Config.Config import changeValues, getConfigValue
import locale
import gettext
from Files.Extensions import *

# config = configparser.ConfigParser()
# config.read('settings.ini')
# language = config.get("Languages", "language")
# languages = ""
#
#
language = Languages.getLanguage()
locale.setlocale(locale.LC_ALL, str(language))
el = gettext.translation('base', localedir='locales', languages=[str(language)], fallback=False)
el.install()
_ = el.gettext

languageSelected = getConfigValue("Languages", "language")
# print(languageSelected)
# # print(Languages.idioms.index("Spanish"))
#
# print(Extensions.types)
# print(_(Extensions.types))

for i in Extensions.types:
    print(_(i))