from pathlib import Path


class LogParser:

    def __init__(self, log_directory):
        self.log_directory = Path(log_directory)

    def get_log_files(self):
        """
        Returns all .log files present in the log directory.
        """
        return list(self.log_directory.glob("*.log"))

    def read_log_file(self, file_path):
        """
        Reads one log file and returns all lines.
        """

        try:

            with open(file_path, "r") as file:
                return file.readlines()

        except FileNotFoundError:
            print(f"ERROR : {file_path} not found.")
            return []

        except PermissionError:
            print(f"ERROR : Permission denied for {file_path}")
            return []

        except Exception as e:
            print(f"Unexpected Error : {e}")
            return []