# PDF Generator from CSV

This Python script generates a multi-page PDF file from a CSV file using the `FPDF` library. Each topic in the CSV file is displayed as a header on each page, with lined pages for writing notes.

## Introduction

This script reads topics and the number of pages for each topic from a CSV file and generates a PDF file with each topic as the header. Each page contains lines for writing notes, and the topic is also displayed in the footer.

## Prerequisites

- Python 3.x
- `FPDF` library
- `pandas` library

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Dishaa01423/pdf-generator.git
    cd pdf-generator
    ```

2. Create and activate a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Prepare a `topics.csv` file with the following structure:

    ```csv
    Topic,Pages
    Topic 1,2
    Topic 2,3
    ```

2. Run the script:

    ```bash
    python generate_pdf.py
    ```

3. The generated PDF file will be saved as `output.pdf`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## License

This project is licensed under the MIT License.

