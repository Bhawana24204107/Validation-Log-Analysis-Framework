from src.parser import LogParser
from src.analyzer import LogAnalyzer
from src.report import ReportGenerator
from src.logger import Logger


def main():

    parser = LogParser("Logs")
    analyzer = LogAnalyzer()
    report = ReportGenerator("Output")
    logger = Logger("Output")

    file_results = {}

    overall_results = {
        "PASS": 0,
        "FAIL": 0,
        "WARNING": 0,
        "ERROR": 0,
        "TIMEOUT": 0
    }

    log_files = parser.get_log_files()

    print("=" * 60)
    print("Validation Log Analysis")
    print("=" * 60)

    for file in log_files:

        logger.info(f"Processing {file.name}")

        print(f"\nProcessing : {file.name}")

        log_lines = parser.read_log_file(file)

        if not log_lines:

            logger.warning(f"{file.name} is empty or could not be read.")

            continue

        file_result = analyzer.analyze(log_lines)

        file_results[file.name] = file_result

        for key, value in file_result.items():
            print(f"{key:<10}: {value}")

        for key, value in file_result.items():
            overall_results[key] += value

    print("\n" + "=" * 60)
    print("Overall Summary")
    print("=" * 60)

    for key, value in overall_results.items():
        print(f"{key:<10}: {value}")

    txt_path = report.generate_report(file_results, overall_results)
    csv_path = report.generate_csv(file_results, overall_results)


    logger.info("TXT Report Generated")
    logger.info("CSV Report Generated")
    

    print("\n" + "=" * 60)
    print("Reports Generated Successfully")
    print("=" * 60)
    print(f"TXT  : {txt_path}")
    print(f"CSV  : {csv_path}")
    


if __name__ == "__main__":
    main()