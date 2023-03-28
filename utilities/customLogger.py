import logging


class LogGen:
    @staticmethod
    def loggen(self):
        logger = logging.getLogger(__name__)
        fileHandler = logging.FileHandler('logfile2.log')
        logging.basicConfig(filename="D:\\Credence Python Projects by Tushar Sir\\OrangeHrm\\Logs\\automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger.addHandler(fileHandler)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
