
<p align="center">
<a href="https://www.python.org/" title="Go to Python homepage"><img src="https://img.shields.io/badge/Made%20with-Python-FED564?logo=python&amp;logoColor=white" alt="Made with Python"></a>
<a href="https://www.ncbi.nlm.nih.gov/books/NBK25500/" title="Entrez API Documentation">
  <img src="https://img.shields.io/badge/Powered%20by-Entrez%20API-FED564?logo=databricks&logoColor=white" alt="Powered by Entrez API">
</a>
</p>

<p align="center">
  <h3 align="center">🔬 Entrez Retriever - Sequence Fetcher</h3>
This project is a command-line script that retrieves sequences from the NCBI Entrez database using the Entrez API. The script allows users to specify the database, search term, and output format. It supports any Entrez database, including Nucleotide, Protein, Genome, SNP, Taxonomy, and PubMed.
</p>

## Authors
A group of 4 students from ESTBarreiro with their school id number assigned.
- Bianca Silva, 202300273
- Erica Alaiz, 202300154
- Filipa Fernandes, 202300218
- Melissa Rocha, 202101023

---

## 📋 Index

- [📝 Introduction](#-introduction)
- [⚙️ Features](#️-features)
- [💻 Installation](#-installation)
- [🚀 Usage](#-usage)
- [📜 License](#-license)

---

## 📝 Introduction

This script retrieves biological sequences from the NCBI Entrez database in FASTA format using the Entrez API, displaying the results in the terminal (STDOUT). It supports various databases, search terms, and command-line arguments to customize searches.

---

## ⚙️ Features

- 📡 Uses the Entrez API to retrieve sequences
- 🔍 Allows users to specify the database to query
- 📌 Accepts search terms via command-line arguments
- 🕒 Uses the Entrez "history" API for efficient queries
- 📜 Outputs sequences in FASTA format to `STDOUT`
- 📂 Optional feature: Saves results to a `.fasta` file
- 🛠️ Structured into independent functions for modularity
- 📑 Well-documented with function descriptions and usage instructions

---

## 💻 Installation

### Prerequisites
- Python 3.10+
- `Biopython` package

### Installation Steps

1. Clone the repository:
   ```sh
   git clone https://github.com/Polytechnic-Projects/EntrezRetriever.git
   cd EntrezRetriever
   ```

2. Install dependencies:
   ```sh
   pip install biopython
   ```

---

## 🚀 Usage

### Basic Usage
Run the script with the required parameters:
```sh
python script.py <database> "<search_term>"
```

### Example
Retrieve `COX1` gene sequences from `nucleotide` database:
```sh
python script.py nucleotide "Homo sapiens[organism] AND COX1"
```

### Save to File
To save results to a `.fasta` file, add the name of the fasta file:
```sh
python script.py nucleotide "Homo sapiens[organism] AND COX1" sequences.fasta
```

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

### 🔗 References
- [NCBI Entrez API](https://www.ncbi.nlm.nih.gov/books/NBK25500/)
- [Biopython Documentation](https://biopython.org/wiki/Documentation)

