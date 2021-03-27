import configparser

from Config.Config import makeConfigFile, getConfigValue

# makeConfigFile()

config = configparser.ConfigParser()
config.read('settings.ini')
# is_orderByYear_checked = config['OrderBy'].getboolean('orderbyyear')
# is_orderByMonth_checked = config['OrderBy'].getboolean('orderbymonth')

# config['OrderBy'].set('orderbyyear', '1')
# print(config.get("OrderBy", "orderbyyear"))
# config.set("OrderBy", "orderbyyear", "1")
# print(config.get("OrderBy", "orderbyyear"))
#
# print("-------------")
# print(getConfigValue("OrderBy", "orderbyyear"))


chkorganizeByYear = getConfigValue("OrderBy", "orderbyyear")
chkorganizeByMonth = getConfigValue("OrderBy", "orderbymonth")
print(chkorganizeByYear)

if chkorganizeByYear == "True" and chkorganizeByMonth == "True":
    print("f")

# print(is_orderByYear_checked, is_orderByMonth_checked)


