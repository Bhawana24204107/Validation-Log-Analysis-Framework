import logging
from pathlib import Path


class Logger:
    def __init__(self, output_directory):
        """
        Initializes the logger.
        Creates the Output directory if it does not exist.
        Creates validation.log inside the Output directory.
        """

        # Create Output directory if it does not exist
        output_dir = Path(output_directory)
        output_dir.mkdir(exist_ok=True)

        # Path of the log file
        log_path = output_dir / "validation.log"

        # Configure logging
        logging.basicConfig(
            filename=log_path,
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s",
            filemode="a"
        )

        # Create logger object
        self.logger = logging.getLogger("ValidationLogger")

        # Start of execution
        self.logger.info("=" * 60)
        self.logger.info("Validation Log Analysis Started")

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def close(self):
        """
        Logs the completion of the program.
        """
        self.logger.info("Validation Log Analysis Completed Successfully")
        self.logger.info("=" * 60)