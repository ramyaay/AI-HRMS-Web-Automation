# AI HRMS Web Automation

**Project Overview**

This project focuses on automating the testing of an AI-based Human Resource Management System (HRMS) web application.
It is built using Python, Selenium WebDriver, and pytest to ensure the reliability and functionality of core HRMS features such as authentication, employee management, and workflow processes.

The framework follows the Page Object Model (POM) design pattern to improve maintainability, scalability, and reusability of test scripts.

**Tech Stack**

* **Programming Language:** Python
* **Automation Tool:** Selenium WebDriver
* **Testing Framework:** Pytest
* **Design Pattern:** Page Object Model (POM)
* **Reporting:** Allure Reports (if configured)
  
**Project Structure**

AI-HRMS-Web-Automation/

├── tests/              # Test cases for different modules
├── pages/              # Page Object classes for UI interactions
├── utils/              # Utility/helper functions
├── config/             # Configuration files (if available)
├── requirements.txt    # Project dependencies
├── pytest.ini          # Pytest configuration
├── reports/            # Test execution reports
└── allure-report/      # Allure generated reports

**Key Features**

* Automated UI testing for HRMS web application
* Implementation of Page Object Model for better code structure
* Reusable and maintainable test scripts
* Pytest-based test execution and assertions
* Support for generating detailed test reports

**How to Execute Tests**

**1. Install Dependencies**

pip install -r requirements.txt

**2. Run Test Cases**

pytest

**3. Generate Allure Report (Optional)**

pytest --alluredir=reports
allure serve reports

**Reporting**

The framework supports test reporting using Allure.
After execution, reports can be viewed to analyze test results, failures, and execution details.

**Future Enhancements**

* Integration with CI/CD tools (e.g., Jenkins)
* Cross-browser execution support
* Parallel test execution
* Enhanced logging and reporting

**Author**
Ramya
