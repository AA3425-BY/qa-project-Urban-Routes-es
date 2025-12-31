# Urban Routes Project

## Project Description
This project contains automated tests to validate the user flow in the **Urban Routes** application.
The tests are written using the **Page Object Model (POM)** ​​architecture, which allows for a clear and maintainable code structure.

## Technologies and Techniques Used

- **Language**: Python 3.13
- **Test Automation**: Selenium WebDriver
- **Test Framework**: Pytest
- **Architecture**: Page Object Model (POM)
- **Suggested IDE**: PyCharm

Techniques used included:
- Explicit waits to ensure that elements are available before interacting with them.
- Asserts to validate the expected behavior of the interface.
- Robust locators using `By.XPATH` and `By.CLASS_NAME`.
  
## Some Implemented Tests

- Add a credit card as a payment method
- Verify the number of ice creams selected
- Validate that the "Find a Car" modal appears when requesting a taxi

## How to Run the Tests
1- Clone the following repository to your computer (if you haven't already): git clone git@github.com:username/qa-project-Urban-Routes-es.git
cd qa-project-Urban-Routes-es
2- You need to have the following packages installed: pip install selenium pytest
Configure the WebDriver for the browser you will use (ChromeDriver) and make sure it is accessible in your PATH.
Run the tests using Pytest

## Author
Adiaris Santana
GitHub: AA3425-BY
Sprint 8
