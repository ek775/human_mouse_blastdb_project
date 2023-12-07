# human_mouse_blastdb_project
Final project for BINF5240

# Overview
Objective is to create a blast pair alignment SQL database for two species proteomes - in my example case "Mouse" and "Human". The utility of this database is based on the frequent use of mouse models in research, where the objective is to find analogous biological effects in humans. This database makes it easy to access and compare such proteins in a programmatic fashion across multiple loci simultaneously.

The scripts in this repository can be used to establish your own blast pair database and mount it on a server for interface access and searchability. 

# Reference Proteomes:
mus musculus (GRCm39): [https://www.uniprot.org/proteomes/UP000000589](url)
homo sapiens (GRCh38.p14: [https://www.uniprot.org/proteomes/UP000005640](url)

# Setting Up the Database
To establish the Database, first download the desired proteomes from uniprot or another source and use NCBI BLAST tools to process the data. Format the Blast output of each directional alignment using "-outfmt 5" to obtain the files in XML format.

Each file can then be passed to the extract_alignment.py script to filter out poor alignments and organize the data into a tabular format. (*Currently this is very memory intensive, I intend to implement batch processing in the future)

To set up the database, pass the resulting CSV files to the pairwise_db_creation.py script as separate arguments. This should establish a SQLite database and populate it with the blast results in two tables named based on the file names passed to it.