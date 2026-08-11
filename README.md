# Selenium automation demo

This demontration contains simple Selenium automation scripts that demonstrate browser actions and data extraction from websites. 
The included examples show how to locate elements, interact with pages (for example adding an item to the cart on Amazon), and by using of XPath/CSS selectors for automation.

Prerequisites
- Python 3.8+
- A virtual environment (recommended)
- Browser driver compatible with your browser (e.g., chromedriver) placed on PATH or configured in the scripts

How to run
1. Create and activate a virtual environment, then install dependencies:
```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```
2. Run an example script:
```
python amazon_add_to_cart.py    # for file 1
python xpath_automation.py      # for file 2
```
