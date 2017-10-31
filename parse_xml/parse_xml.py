## The purpose here is to parse blast.xml output to generate a list of hit-species
## The list of hit-species or hit-genus will be used to batch-download specified genomes from NCBI


import xml.etree.ElementTree as ET
## module parseing xml file
import argparse

##################################################

parser = argparse.ArgumentParser(description = 'The purpose of this is to parse blast.xml output to generate a list of hit-species, and then the list will be used to batch-download specified genomes from NCBI')
## create argparse

parser.add_argument('-input',
                    help = 'blastp ourput, .xml')
## blast_output.xml

#parser.add_argument('-output',
#					help = 'output file name')
## create argument using

#parser.add_argument('-length',
#					help = 'assigned length')
args = parser.parse_args()

##################################################

tree = ET.parse(args.input)
## args.input becomes a file handle for ET.parse

root = tree.getroot()
## gather root information

print (root[8][0][4][0][2].tag) 
print (root[8][0][4][0][2].text) 
## check and see locate the content I need from this file

elem_list = []
## create an empty list for all element tags
for elem in root.iter():
    elem_list.append(elem.tag)
    ## collect all element tags into a list
    #print(elemlist)
N = elem_list.count('Hit')
print (N)
## count the occurrences of 'Hit' tag in the list
## use the number to determine range

target_list = [ ]
## create an empty list for genome names collection

for idx in range(N):
    target_list.append(root[8][0][4][idx][2].text)
    ## collect all Hit_def contents into a list
	
print (target_list[0])
## take a look of the content
## should match the the one shown before 

species_list = []
for idx in range(N):
    left  = target_list[idx].find('[')
    right = target_list[idx].find(']')
    species_list.append(target_list[idx][left+1:right])
#print (species_list)
## collect only the species names inside of '[ ]'	

genus_list = []
for idx in range(N):
    space = species_list[idx].find(' ')
    genus_list.append(species_list[idx][:space])
## collect only the genus names

newlist_g = []
for genus in genus_list:
    if genus not in newlist_g:
        newlist_g.append(genus)
## remove reduntant genuses names in the list

newlist_sp = []
for species in species_list:
    if species not in newlist_sp:
        newlist_sp.append(genus)
## remove reduntant genuses names in the list        
print (len(newlist_g))
print (len(newlist_sp))


file_g = open('genus_list.txt','w') 
## generate genus_list in txt file
for item_g in newlist_g:
    file.write(item_g + ',') 
file_g.close() 

file_sp = open('species_list.txt','w') 
## generate genus_list in txt file
for item_sp in newlist_sp:
    file.write(item_sp + ',') 
file_sp.close() 



