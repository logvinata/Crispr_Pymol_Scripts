## run through pymol, eg.:
## pymol -qc mutate.py 6o0z 
## which means I can't use jup.notebook

##########################################################

"""
#this should be the wrapper, probably in another file
# each "action" inside actually requires several functions
structures_list = ["6o0z.pdb", "6o0y.pdb", 6o0z.pdb"]

for structure in structures_list:
cmd.load(structure) #open structure
#mutate_to_mesyl_phosphate
#chose a rotamer
#export image
#chow electronegativity, export image
#find atoms within distance d from selected atom, export
"""
#import sys
#pdb, selection, mutant = sys.argv[-3:] - I prefer not to use it here, though I like the idea. The script will really be used only once.
#the error message is because pymol unsuccessfully tries to open the command line arguments as files.

##########################################################
form pymol import cmd
#import string

#constants here
crispr_start = 1 #start of crRNA, check it is in the structure file
crispr_end = 20 #last nt of crRNA part in gRNA
tracr_start = 21 # start of tracr part of gRNA
tracr_end = 96 #end of tracr part of gRNA, check it is really there

#open structure in GUI

structure = "6o0z.pdb" #the most important one
cmd.load(structure)

#functions here for now

def mutate_to_mesyl_phospate (chain, number):

"""changes -P=0 in phosphodiester bond to -P=N-MeSO2 (methansulfonyl)
needs chain (one capital letter) and nucleotide number (integer) to define the residue to mutate
does not check if it is mutated already - use rcsb structures only
"""

phosphorus_atom = select_atom(chain,number)

pass



def select_atom(chain, number)
"""creates selection by the name of the chain (e.g. "B") and integer number of the nucleotide residue. The selection is one phosphorous atom and the focus of the pymol picture is centered on it.
Note: tried to check that number is < then len(chain), but it didn't work. Removed all common-sence checks.
"""
cmd.do_select(sel p_atom) #this is empty selection named p_atom
#note: pymol does not raise errors with wrong selections, just makes an empty one
#need to check that the № of atoms in p_atom == 1


#hope return will work this way
return p_atom















