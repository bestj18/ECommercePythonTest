## Requirements
- Python 3.8 or later
- Google Chrome browser
- ChromeDriver (installed and on your PATH)
- Selenium (`pip install selenium`)
- Pytest (`pip install pytest`)

## Setup and Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/selenium-ecommerce-tests.git
   cd selenium-ecommerce-tests
   ```
2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate
   ```
3. Install the required packages:
   ```bash
   pip install selenium pytest
   ```

## Running the Tests
- To run all tests in a browser window:
  ```bash
  pytest tests/
  ```
- To run tests in headless mode (no browser window):
  ```bash
  pytest tests/ --headless
  ```

## Tests Included
- **Login Test**: Fills in email and password and verifies that the account page loads.
- **Search Test**: Searches for a keyword and checks that the search results page opens.
- **Checkout Test**: Adds a product to the cart and proceeds to the order page.

## Key Concepts
- **Page Object Model (POM)**: Organizes page interactions in classes to keep tests clean.
- **Pytest Fixtures**: Sets up and tears down the browser automatically for each test.
- **Implicit Waits**: Ensures elements are available before interacting.

## About Me
I’m Dylan Best, a Quality Assurance Analyst. I built this project to practice automation and to showcase my skills. I’m interested in improving test reliability and exploring new testing tools.

## Contact
If you have questions or feedback, feel free to reach out.