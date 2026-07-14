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

    # -------------------------------------------------
    # HTML REPORT
    # -------------------------------------------------

    def generate_html(self, file_results, overall_results):

        html_path = self.output_directory / "Validation_Report.html"

        with open(html_path, "w") as html:

            html.write("""
<!DOCTYPE html>
<html>

<head>

<title>Validation Report</title>

<style>

body{
font-family:Arial;
margin:40px;
}

table{
border-collapse:collapse;
width:80%;
}

th,td{
border:1px solid black;
padding:10px;
text-align:center;
}

th{
background:#d9ead3;
}

</style>

</head>

<body>

<h1>Validation Log Analysis Report</h1>

<table>

<tr>

<th>File</th>
<th>PASS</th>
<th>FAIL</th>
<th>WARNING</th>
<th>ERROR</th>
<th>TIMEOUT</th>

</tr>
""")

            for file_name, result in file_results.items():

                html.write(f"""
<tr>
<td>{file_name}</td>
<td>{result["PASS"]}</td>
<td>{result["FAIL"]}</td>
<td>{result["WARNING"]}</td>
<td>{result["ERROR"]}</td>
<td>{result["TIMEOUT"]}</td>
</tr>
""")

            html.write(f"""
<tr>

<th>Overall</th>

<th>{overall_results["PASS"]}</th>
<th>{overall_results["FAIL"]}</th>
<th>{overall_results["WARNING"]}</th>
<th>{overall_results["ERROR"]}</th>
<th>{overall_results["TIMEOUT"]}</th>

</tr>

</table>

</body>

</html>
""")

        return html_path