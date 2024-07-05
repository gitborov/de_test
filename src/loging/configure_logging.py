import logging
import os


def configure_logging(log_file_path):
    logger = logging.getLogger(os.path.basename(__name__))
    logger.setLevel(logging.DEBUG)

    # Создание обработчика для файла
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(logging.INFO)
    console_out = logging.StreamHandler()
    console_out.setLevel(logging.DEBUG)
    # Создание форматтера для логгирования
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Добавление обработчика в логгер
    logger.addHandler(file_handler)
    logger.addHandler(console_out)

    return logger