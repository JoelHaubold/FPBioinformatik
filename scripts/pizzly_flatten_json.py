import sys
import json
from collections import OrderedDict

outFile = snakemake.output[0]
inJson = snakemake.input[0]

with open(inJson) as f:
	JJ = json.load(f,object_pairs_hook=OrderedDict)
fusions = JJ['genes']

outf = open(outFile,'w')

outf.write('\t'.join("geneA.name geneA.id geneB.name geneB.id paircount splitcount transcripts.list".split()))
outf.write('\n')
for gf in fusions:
    gAname = gf['geneA']['name']
    gAid   = gf['geneA']['id']
    gBname = gf['geneB']['name']
    gBid   = gf['geneB']['id']
    pairs  = str(gf['paircount'])
    split  = str(gf['splitcount'])
    txp = [tp['fasta_record'] for tp in gf['transcripts']]

    outf.write('\t'.join([gAname, gAid, gBname, gBid, pairs, split, ';'.join(txp)]))
	outf.write('\n')
outf.close
