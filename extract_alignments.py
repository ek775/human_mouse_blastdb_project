"""
Extracts relevant alignment information from xml blast results and stores the data in a csv file for conversion to a sqlite database

Run this script from the CLI: python extract_alignments.py [blast_result file]
"""

from Bio.Blast import NCBIXML
import pandas as pd
import sys

file = sys.argv[1]
assert type(file)==str
assert file[-4:]==".xml"

data = []
result_handle = open(file)
for blast_result in NCBIXML.parse(result_handle):
    for hit_num, alignment in enumerate(blast_result.alignments, start=1):
        for hsp in alignment.hsps:
            if hsp.expect < 1e-5:
                dfi = pd.DataFrame({'accession': alignment.accession, 
                                    'hit_id': alignment.hit_id, 
                                    'hit_def': alignment.hit_def,
                                    'hit_num': hit_num,
                                    'hit_len': hsp.align_length,
                                    'expect': hsp.expect, 
                                    'score': hsp.score,
                                    'query': hsp.query,
                                    'subject': hsp.sbjct,
                                    'match': hsp.match}, 
                                    index=[0])
                data.append(dfi)
df = pd.concat(data, ignore_index=True)
print(df)

#export df as csv
print("Exporting data to CSV...")
out = f"{file[:-4]}.csv"
df.to_csv(out)
print(f"Data saved as {out}")


