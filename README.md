A beginner-friendly and interactive data exploration tool built with Python, NumPy, and Streamlit.
This project demonstrates core NumPy skills — array creation, slicing, reshaping, broadcasting, statistics, and performance benchmarking — using a simple, user-friendly UI.

📌 Features
🔹 1. Upload & Convert CSV to NumPy

Upload any CSV file

Automatically converts it into a NumPy array

Displays sample rows and column names

🔹 2. Explore Array Properties

Shape, size, dtype, dimensions

Minimum & maximum values

Clean JSON-style info panel

🔹 3. Mathematical & Statistical Operations

Mean, median, std, sum

Axis-wise (0, 1) or full-array statistics

🔹 4. Array Reshaping

Change the dimensions of your dataset

Error-handling for invalid shapes

🔹 5. Broadcasting

Add vectors to arrays using NumPy broadcasting

Demonstrates one of NumPy’s most powerful features

🔹 6. Save & Load Arrays

Save arrays as .npy files

Load saved NumPy arrays back into the app

🔹 7. Performance Benchmarking

Compare execution speed of:

NumPy operations

Pure Python list operations

See how vectorization improves performance!

📂 Project Structure
numpy_data_explorer/
│
├── app.py               # Streamlit UI
├── explorer.py          # Core NumPy logic
├── utils.py             # Helper functions (optional)
├── requirements.txt     # Required dependencies
├── README.md            # Documentation
│
├── data/
│   └── sample.csv       # Example dataset
│
└── tests/
    └── test_explorer.py # Optional tests

🛠️ Installation
1. Clone the repository
git clone https://github.com/YOUR_USERNAME/numpy-data-explorer.git
cd numpy-data-explorer

2. Create a virtual environment
python -m venv .venv

3. Activate the environment
Windows (PowerShell):
.\.venv\Scripts\Activate.ps1

CMD:
.\.venv\Scripts\activate.bat

Mac/Linux
source .venv/bin/activate

4. Install dependencies
pip install -r requirements.txt

▶️ Run the Application
streamlit run app.py


Your app will open automatically on:

http://localhost:8501

🧪 Testing (optional)
pytest -q

📊 Sample CSV

A small dataset is included at:

data/sample.csv


You can replace it with your own dataset to explore different values.

🤝 Contributions

Pull requests are welcome!
If you want to improve UI, add new operations, or fix a bug — feel free.

⭐ If you like this project

Give it a star on GitHub — it motivates me to build more open-source projects!

📧 Author

Diya Diwakar
💼 Python • Data Science | NumPy • Pandas • ML beginner