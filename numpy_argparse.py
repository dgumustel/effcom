# This is code for the numpy & argparse assignment 

# imports
import numpy as np
import sys, os
import numpy as np
import pickle
import argparse

# local imports
pth = os.path.abspath('shared')
print('\nAdding the path:')
print(pth + '\n') # the \n adds a line feed
sys.path.append(os.path.abspath('shared'))
import my_module as mymod
from importlib import reload
reload(mymod)

# create output directory if it does not exist
this_dir = os.path.abspath('.').split('/')[-1]
this_parent = os.path.abspath('.').split('/')[-2]
out_dir = '../../' + this_parent + '_output/'
print('Creating ' + out_dir + ', if needed')
mymod.make_dir(out_dir)

# create arrays and do stuff with them
print('\nCreating an array of random floats')
aa = np.array(np.random.randn(16).reshape(4,4))
print('\naa =')
print(aa)
print('\nCreating a copy of aa')
bb = aa.copy()
print('\nbb =')
print(bb)

# try indexing and np.random
print('\nChange the second column in aa to new random values')
aa[:, 1] = np.random.randn(4)
print('\naa =')
print(aa)
print('\nSee difference between aa and bb now')
print('\nbb - aa =')
print(bb-aa)

# try np.sort
aa = np.sort(aa)
print('\nSort each row in aa')
print(aa)
print('\nSee difference between aa and bb again')
print('\nbb - aa =')
print(bb-aa)

# try np.concatenate
print('\nConcatenate aa and bb into a new array called cc')
cc = np.concatenate((aa,bb), axis=1)
print('\ncc =')
print(cc)
print('\nShape of cc =', cc.shape)

# try np.flatten and np.shape
print('\nFlatten cc')
cc = cc.flatten()
print('\ncc =')
print(cc)
print('\nShape of cc =', cc.shape)

print('\n Make a Boolean mask of aa >= 0.5')
mask = aa >= 0.5
print(mask)

print('\n Use the mask to get just those elements of aa: aa[mask]')
print(aa[mask])
print('Note that this returns just a 1-D arrray (flattened)')


# save it as a pickle file
out_fn = out_dir + 'pickled_array.p'
pickle.dump(cc, open(out_fn, 'wb')) # 'wb' is for write binary

# read the array back in
ccc = pickle.load(open(out_fn, 'rb')) # 'rb is for read binary

print('\nThe shape of the loaded object is')
print(ccc.shape)

# Boolean function borrowed from parkermac
def boolean_string(s):
    # this function helps with getting Boolean input
    if s not in ['False', 'True']:
        raise ValueError('Not a valid boolean string')
    return s == 'True' # note use of ==

# create the parser object
parser = argparse.ArgumentParser()

# NOTE: argparse will throw an error if:
#     - a flag is given with no value
#     - the value does not match the type
# and if a flag is not given it will be filled with the default.
parser.add_argument('-a', '--a_string', default='no string', type=str)
parser.add_argument('-v', '--verbose', default=False, type=boolean_string)

# get the arguments
args = parser.parse_args()

# output
print('\nYou entered ' + args.a_string)

if args.verbose:
    print('\nSome basic stats on bb')
    print('\nMean of bb =', bb.mean())
    print('\nStandard deviation of bb =', bb.std())
    print('\nMaximum value in bb =', bb.max())
