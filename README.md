# PDF Generator from CSV

This Python script generates a multi-page PDF file from a CSV file using the `FPDF` library. Each topic in the CSV file is displayed as a header on each page, with lined pages for writing notes. 

##Prerequisites

Python 3.x
FPDF library
pandas library

##Installation

1. Clone this repository to your local machine.
    git clone https://github.com/yourusername/pdf-generator.git
    cd pdf-generator
   
3. Install the required Python libraries.
    pip install fpdf pandas
   
##Usage

1. Prepare a CSV file named topics.csv in the following format:
    Topic,Pages
    Topic1,3
    Topic2,2
    ...
    Topic: The topic header to be displayed on each page.
    Pages: The number of pages for this topic.
   
2. Run the script.
    python generate_pdf.py
   
4. The script will generate a file named output.pdf in the same directory.

##Contributing

Contributions are welcome! If you find a bug or have a feature request, please open an issue. Feel free to fork the repository and submit a pull request.

##License

This project is licensed under the MIT License - see the LICENSE file for details.
