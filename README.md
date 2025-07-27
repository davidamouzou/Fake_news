# Fake News Detection

This project aims to detect fake news using machine learning techniques. It includes data exploration, model building, and evaluation, with a focus on identifying misleading or false information in news articles.

## Project Structure

```
Fake_news/
├── app.py                      # Main application script
├── data/
│   └── fake_news_dataset.csv   # Dataset for training/testing
├── notebooks/
│   ├── 01_exploration.ipynb    # Data exploration
│   ├── 02_modelisation.ipynb   # Model building
│   ├── 03_evaluation.ipynb     # Model evaluation
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
└── venv/                       # Python virtual environment
```

## Dataset

The dataset (`data/fake_news_dataset.csv`) contains news articles labeled as real or fake. It is used for training and evaluating the machine learning models.

## Setup

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd Fake_news
   ```
2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   *(If `requirements.txt` is missing, create it and list all necessary packages, e.g., pandas, scikit-learn, jupyter, numpy, etc.)*

## Usage

- **Jupyter Notebooks:**
  - Explore the data, build models, and evaluate results using the notebooks in the `notebooks/` directory.
  - Launch Jupyter:
    ```bash
    jupyter notebook
    ```
- **Main Application:**
  - Run the main script (if implemented):
    ```bash
    python app.py
    ```

## Requirements

- Python 3.7+
- See `requirements.txt` for a full list of dependencies.

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements.# Fake_news
