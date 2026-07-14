from pathlib import Path
import csv


class ReportGenerator:

    def __init__(self, output_directory):

        self.output_directory = Path(output_directory)

        self.output_directory.mkdir(exist_ok=True)

    # -------------------------------------------------
    # TXT REPORT
    # -------------------------------------------------

    def generate_report(self, file_results, overall_results):

        report_path = self.output_directory / "Validation_Report.txt"

        with open(report_path, "w") as report:

            report.write("=" * 60 + "\n")
            report.write("Validation Log Analysis Report\n")
            report.write("=" * 60 + "\n\n")

            for file_name, result in file_results.items():

                report.write(f"File : {file_name}\n")
                report.write("-" * 40 + "\n")

                for key, value in result.items():
                    report.write(f"{key:<10}: {value}\n")

                report.write("\n")

            report.write("=" * 60 + "\n")
            report.write("Overall Summary\n")
            report.write("=" * 60 + "\n")

            for key, value in overall_results.items():
                report.write(f"{key:<10}: {value}\n")

        return report_path

    # -------------------------------------------------
    # CSV REPORT
    # -------------------------------------------------

    def generate_csv(self, file_results, overall_results):

        csv_path = self.output_directory / "Validation_Report.csv"

        with open(csv_path, "w", newline="") as csv_file:

            writer = csv.writer(csv_file)

            writer.writerow([
                "File Name",
                "PASS",
                "FAIL",
                "WARNING",
                "ERROR",
                "TIMEOUT"
            ])

            for file_name, result in file_results.items():

                writer.writerow([
                    file_name,
                    result["PASS"],
                    result["FAIL"],
                    result["WARNING"],
                    result["ERROR"],
                    result["TIMEOUT"]
                ])

            writer.writerow([])

            writer.writerow([
                "Overall",
                overall_results["PASS"],
                overall_results["FAIL"],
                overall_results["WARNING"],
                overall_results["ERROR"],
                overall_results["TIMEOUT"]
            ])

        return csv_path

   