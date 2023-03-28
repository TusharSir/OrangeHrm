import configparser

config = configparser.RawConfigParser()
config.read("D:\\Credence Python Projects by Tushar Sir\\nopcommerceApp\\Configurations\\config2.ini")


class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url= config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUseremail():
        username= config.get('common info', 'username')
        return username

    @staticmethod
    def getUserPassword():
        username= config.get('common info', 'password')
        return username
