## This repository contains my submissions for the ValueBlue technical tests.

---

##  Assignment Overview

### 1. Value_Blue_Test_1
This repository contains an automated browser test written in **Python**, using **Selenium**, **pytest**, and **pytest-bdd** (Cucumber/Gherkin style).  
The test validates page navigation, link presence, and content within the "Domain Names" box while avoiding false positives.

### 2. Value_Blue_Test_2
This project contains automated tests written in **Python** using **pytest** and **requests**.  
It performs full CRUD validation (Create, Get, Update, Delete) on an API endpoint that manages objects.

## 3. Additional File
- **Challenge-3-DCT-Jyoti Arora.pdf** – Solution of Challenge 3

---

## Running the Tests
Run all tests:
```bash
pytest -v
```

Run a single test:
```bash
pytest -v -k test_update_object
```

Generate a test report:
```bash
pytest -v --html=report.html
```

## Test Results of Challenge 2
tests/test_crud_operations.py::test_create_object PASSED                                                         [ 25%]
tests/test_crud_operations.py::test_get_object PASSED                                                            [ 50%]
tests/test_crud_operations.py::test_update_object PASSED                                                         [ 75%]
tests/test_crud_operations.py::test_delete_object PASSED                                                         [100%]

================================================== 4 passed in 8.84s ==================================================


## 🚀 About
## Author : JYOTI ARORA
  




