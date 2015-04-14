#pothole.py

import csv

potholes_by_block = { }

def make_block(address):
    '''Rewrite an address to strip address to 1000's (10 blocks)'''
    parts = address.split()
    # For a number like '5412' this makes '5XXX'
    parts[0] = parts[0][:-3] + 'XXX'
    return ' '.join(parts)

f = open('data/potholes.csv')
for row in csv.DictReader(f):
  status = row['STATUS']
  if status == 'Open':
    address = row['STREET ADDRESS']
    # Change address to block ???

    # Tabulate
    block = make_block(address)
    if block not in potholes_by_block:
      # This is the first occurrence of a given address

      potholes_by_block[block] = 1
    else:
      potholes_by_block[block] =+ 1

# Problem how to sort, find most potholes
