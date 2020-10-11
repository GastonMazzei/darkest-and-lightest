import sys

import numpy as np

from PIL import Image
from copy import deepcopy

# Load the image
#
try:
  name = sys.argv[1]
  print(f'\nUsing the following image: {name}\n')
except:
  print('\nPlease input your images\' name')
  name = input('\nYour answer: ')
  print('\n')
img = np.asarray(Image.open(name))

# Define two dictionaries for iterations
#
R_G_B = {'R':[],'G':[], 'B':[]}
cases = {'light_index':[np.argmin, deepcopy(R_G_B)],
       'dark_index':[np.argmax, deepcopy(R_G_B)]}

# Find out the indexes of the darkest and 
# lightest color
#
for x in cases.keys():
  cases[x][0] = cases[x][0](np.mean(img,2))

# evalute the R,G,B vectors in said indexes
#
for x in cases.keys():
  for i,color in enumerate(['R','G','B']):
    cases[x][1][color].append(img[:,:,i].flatten()[cases[x][0]])
  print(f'The {x.split("_")[0]}est color is: ',
         '#{:02x}{:02x}{:02x}'.format(
                          cases[x][1]['R'][0],
                          cases[x][1]['G'][0],
                          cases[x][1]['B'][0],).upper())
print('\n')

