from datetime import datetime
from modules.logger.log_formatter import ColorlessFormatter, ColorfulFormatter

import logging
import os

class Logger():
    def __init__(self, dev:bool = False) -> None:
        self.init_logs_dir()
        self.ch, self.fh, self.logger = self.init_logger(dev)
        pass

    def init_logs_dir(self):
        # Make logs directory
        try:
            os.scandir("logs")
        except FileNotFoundError:
            os.makedirs("logs")

    def init_logger(self, dev):
        """Initialise the logging system"""
        
        logger = logging.getLogger("CattoBotto")
        log_start = datetime.now().strftime("%Y%m%d_%H%M%S")
        #Formatters
        formatter = ColorlessFormatter()
        colorformatter = ColorfulFormatter()
        if dev:
            logger.setLevel(logging.DEBUG)
        else:
            logger.setLevel(logging.INFO)
        
        # File handler init
        fh = logging.FileHandler(f'./logs/cattobotto_{log_start}.log')
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        # Console handler init
        ch = logging.StreamHandler()
        ch.setFormatter(colorformatter)
        logger.addHandler(ch)
        
        return ch, fh, logger
    
    def error(self, text):
        self.logger.error(text)

    def info(self, text):
        self.logger.info(text)

    def warn(self, text):
        self.logger.warning(text)