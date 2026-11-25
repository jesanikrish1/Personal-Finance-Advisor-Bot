# Personal Finance Advisor Bot — PS-67

## Project overview
This is a student-friendly finance education web app. Users enter monthly take-home income and expenses. Python calculates a suggested 50–30–20 budget, compares the entered amounts with the guideline, and explains budgeting, savings, emergency funds and SIP basics in simple language.

**Important:** This project is for education only. It is not financial advice. SIP/mutual-fund returns are market-linked and are not guaranteed.

## Project structure
```text
Personal_Finance_Advisor_Bot_PS67/
├── app.py                         # Streamlit web application
├── analyzer.py                    # Budget calculations and comparison
├── explainer.py                   # Simple educational responses
├── report_generator.py             # Creates downloadable PDF
├── requirements.txt                # Python dependencies
├── .env.example                    # Optional future API key example
├── .gitignore
├── tests/
│   └── test_analyzer.py            # Budget calculation tests
├── screenshots/                    # Illustrative UI previews
├── outputs/
│   └── sample_budget_summary.pdf   # Example generated report
├── Report.pdf                      # Assignment report
├── Code.zip                        # Source code archive
└── README.md                        # This setup guide
```

## Requirements
- Windows 10/11, macOS or Linux
- Python 3.10 or newer
- Internet connection for installing Python packages
- Chrome, Edge, Firefox or another modern browser

## Setup and run (Windows — step by step)

### Step 1: Extract the ZIP
1. Download `Submission_Package.zip`.
2. Right-click the ZIP file.
3. Select **Extract All**.
4. Open the extracted `Personal_Finance_Advisor_Bot_PS67` folder.

### Step 2: Install Python
1. Download Python from https://www.python.org/downloads/
2. Run the installer.
3. On the first installer screen, tick **Add Python to PATH**.
4. Complete installation.
5. Open Command Prompt and check:
   ```bat
   python --version
   ```
   If `python` is not recognized, try:
   ```bat
   py --version
   ```

### Step 3: Open terminal in the project folder
1. Open the extracted project folder in File Explorer.
2. Click the address bar, type `cmd`, and press Enter.
3. Command Prompt should open at the project folder.

### Step 4: Create a virtual environment
Run:
```bat
python -m venv .venv
```
If Windows uses the `py` launcher instead:
```bat
py -m venv .venv
```

### Step 5: Activate the virtual environment
In Command Prompt:
```bat
.venv\Scripts\activate
```
If using PowerShell:
```powershell
.\.venv\Scripts\Activate.ps1
```
When activated, you should see `(.venv)` at the beginning of the command line.

### Step 6: Install required libraries
```bat
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Step 7: Run the application
```bat
python -m streamlit run app.py
```
Streamlit will show a local address, usually:
```text
http://localhost:8501
```
Open that address in your browser. Keep the terminal window open while using the app.

### Step 8: Use the application
1. Enter your monthly take-home income in the left sidebar.
2. Enter monthly needs, wants and savings/investments.
3. Click **Calculate my budget**.
4. Review the suggested 50–30–20 allocation and expense comparison.
5. Enter a question about budgeting, savings, emergency funds or SIPs.
6. Click **Ask** to see an educational explanation.
7. Click **Download budget report (PDF)** to save the summary.

## Run the tests
From the project folder with the virtual environment activated:
```bat
python -m pytest -q
```
The included tests check the 50–30–20 calculation and handling of negative values.

## Common problems
- **`python` is not recognized:** reinstall Python and enable “Add Python to PATH”; or use `py` instead of `python`.
- **`pip` is not recognized:** use `python -m pip` rather than `pip`.
- **Streamlit is not recognized:** activate `.venv` and install requirements, then run `python -m streamlit run app.py`.
- **Port 8501 is already in use:** run `python -m streamlit run app.py --server.port 8502` and open the new address.
- **Package installation fails:** check your internet connection and confirm Python 3.10+ is installed.

## GitHub (optional)
1. Create a new repository on GitHub.
2. Open Command Prompt in this project folder.
3. Run:
   ```bat
   git init
   git add .
   git commit -m "Initial Personal Finance Advisor Bot"
   git branch -M main
   git remote add origin YOUR_GITHUB_REPOSITORY_URL
   git push -u origin main
   ```
Replace `YOUR_GITHUB_REPOSITORY_URL` with the URL of your own repository.

## Current implementation note
The Q&A module uses a small offline educational response library, so it works without an API key. It is structured so an LLM can be added later, while Python should remain responsible for exact budget calculations. The screenshot files are illustrative previews; capture screenshots of the running app if your instructor requires real application evidence.
