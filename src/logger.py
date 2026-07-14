import logging
from pathlib import Path


class Logger:

    def __init__(self, output_directory):

        log_path = Path(output_directory) / "validation.log"

        logging.basicConfig(
            filename=log_path,
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )

        self.logger = logging.getLogger("ValidationLogger")

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)