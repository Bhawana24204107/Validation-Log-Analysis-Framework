class LogAnalyzer:

    def analyze(self, log_lines):
        """
        Analyze a single log file and return the statistics.
        """

        results = {
            "PASS": 0,
            "FAIL": 0,
            "WARNING": 0,
            "ERROR": 0,
            "TIMEOUT": 0
        }

        for line in log_lines:

            status = line.split(":")[0].strip()

            if status in results:
                results[status] += 1

        return results