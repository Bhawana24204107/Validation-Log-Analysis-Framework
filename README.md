# Validation Log Analysis Framework

A Python-based automation framework for parsing, analyzing, and reporting validation logs. This project demonstrates how validation engineers can automate regression log analysis and generate professional reports in TXT, CSV, and HTML formats.

---

## Features

- Multi-file log parsing
- PASS / FAIL / WARNING / ERROR / TIMEOUT detection
- Individual log analysis
- Overall regression summary
- TXT report generation
- CSV report generation
- HTML report generation
- Logging support
- Exception handling
- Modular Python architecture

---

## Project Architecture

```
               Validation Logs
                      │
                      ▼
              +----------------+
              |   Log Parser   |
              +----------------+
                      │
                      ▼
              +----------------+
              | Log Analyzer   |
              +----------------+
                      │
                      ▼
             +------------------+
             | Report Generator |
             +------------------+
                │      │      │
                ▼      ▼      ▼
              TXT    CSV    HTML
```

---

## Folder Structure

```
Validation-Log-Analysis-Framework
│
├── Logs/
│   ├── test1.log
│   ├── test2.log
│   ├── test3.log
│   ├── test4.log
│   └── test5.log
│
├── config/
│
├── src/
│   ├── parser.py
│   ├── analyzer.py
│   ├── logger.py
│   ├── report.py
│   ├── utils.py
│   └── __init__.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Technologies Used

- Python
- Object-Oriented Programming (OOP)
- pathlib
- logging
- csv
- HTML
- Exception Handling

---

## Output

The framework automatically generates:

- Validation_Report.txt
- Validation_Report.csv
- Validation_Report.html
- validation.log

---

## Future Enhancements

- Configuration file (`config.json`)
- Command-line interface (`argparse`)
- Unit testing (`pytest`)
- Multi-threaded log processing
- Interactive HTML dashboard
- ZIP log archive support
- Trend analysis across regression runs

---

## Applications

This framework is useful for:

- Post-Silicon Validation
- Pre-Silicon Validation
- Regression Log Analysis
- Automation Framework Development
- Validation Engineering
- Python Automation

---

## Author

**Bhawana**

M.Tech VLSI Design

Validation Automation | Python | Post-Silicon Validation
