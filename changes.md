# List of changes/updates to the programs
*(this list was started 07/10/2021 at 23:02 BST)*
Most recent changes at the top

## MATS23101 - Mechanics of Materials
### 08102021.1407 - Implemented basic tensor operations
 - Tensor components can now be called through 'Tensor[i]', using 0 indexing
 - Fixed bug whereby 1st order tensors could not be created
 - Introduced vector dot product and 2nd order tensor double contraction (amount of components between the different tensors has to be equal)
 -  Introduced calculation of the principal tensor, and its rotation angle and matrix (in 2D)
 -  Introduced tensor rotation given a rotation matrix
 -  Introduced invariants for 1st and 2nd order tensors

### 07102021.2302 - Increased tensor flexibility
 - Tensors can now theoretically be of the 52nd rank/order (although such a tensor, with a maximum index of 3 would have over 6 septillion components)
 - Default tensor is a 2nd order 3x3 tensor of 0s
 - Tensors are still limited to have all indices of equal length, i.e. if *i=1,2,3*, *j=1,2,3*, *k=1,2,3*, etc...
