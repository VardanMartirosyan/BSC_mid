import logging
import os
from pathlib import Path


def get_root_directory():
    projectName = "BSC_MidLevel"
    currentPath = Path(__file__)
    projectRootPath = (str(currentPath).split(projectName))[0] + projectName

    return projectRootPath


def loger(level, message, fileName=(get_root_directory()+"\Log_\\file.txt"), ):
    logging.basicConfig(level=logging.INFO, filename=fileName, filemode="a",
                        format="%(asctime)-12s %(levelname)s %(message)s",
                        datefmt="%d-%m-%Y %H:%M:%S")
    if level == "INFO":
        logging.info(message)
        print(f"'{level}' - {message}")
    elif level == "DEBUG":
        logging.debug(message)
        print(f"'{level}' - {message}")
    elif level == "WARNING":
        logging.warning(message)
        print(f"'{level}' - {message}")
    elif level == "ERROR":
        logging.error(message)
        print(f"'{level}' - {message}")

get_root_directory()