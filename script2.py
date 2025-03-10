import sys
from Bio import Entrez ##Importing Entrez module form Bioython as it'll interact with biological databases

def search_entrez(database, search_term):
    """Searches in Entrez and returns WebEnv and QueryKey"""
    Entrez.email = "your_email@domain" ##!IMPORTANT! It's required an email to use the Entrez API
    handle = Entrez.esearch(db=database, term=search_term, usehistory="y", retmax=4) ##Retrieves sequences in FASTA format based on the previous search

    record = Entrez.read(handle) ##Reads the search results
    handle.close() ##Closes the handle to prevent memory leaks (Very Important)
    return record["WebEnv"], record["QueryKey"] ## Returns identifiers needed for later data retrieval

def fetch_fasta(database, webenv, query_key):
    """Fetches sequences from Entrez and returns them in FASTA format."""
    handle = Entrez.efetch(db=database, query_key=query_key, WebEnv=webenv, rettype="fasta", retmode="text") ##Retrieves sequences in FASTA format based on the previous search

    fasta_data = handle.read() ##Reads the data
    handle.close() ##Closes the handle
    return fasta_data ##Returns data formatted as FASTA

def main():
    if len(sys.argv) < 3: ##Checks if the required arguments are provided
        print("Usage: python script.py <database> <search_term> [output_file]") ##Prints usage instructions
        sys.exit(1) ##Exits the program with an error code

    database = sys.argv[1] ##Gets the database to query
    search_term = sys.argv[2] ##Gets the search term
    output_file = sys.argv[3] if len(sys.argv) > 3 else None ##Gets the output file name only if it is provided

    webenv, query_key = search_entrez(database, search_term) ##Performs the Entrez search
    fasta_data = fetch_fasta(database, webenv, query_key) ##Retrieves the FASTA data

    if output_file:
        with open(output_file, "w") as f: ##Saves the data to a file if an output filename is specified
            f.write(fasta_data)
        print(f"Sequências salvas em {output_file}") #If everything is okay, it gives an confirmation message
    else:
        print(fasta_data) #Prints the data to standard output

if __name__ == "__main__":
    main() ##Runs the script if executed directly
