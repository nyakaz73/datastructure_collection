# Python datastructure_collection
A DataStructure collection written in Python which helps developers and big-data scientists in implementing fast and efficient algorithms.

### Show some :heart: and :star: to the repo to support the project

## Package
The Pypi [datastructer_collection](https://github.com/nyakaz73/datastructure_collection.git) package can be found [here](https://github.com/nyakaz73/datastructure_collection.git)

## Getting Started
The datastructure_collection has three data structure classes :

* 1. [BinarySearchTree](https://github.com/nyakaz73/datastructure_collection.git)

* 2. [HashMap](https://github.com/nyakaz73/datastructure_collection.git)

* 3. [LinkedList](https://github.com/nyakaz73/datastructure_collection.git)

I Look forward to add more datastructures in the future.

## Installation

Run the following to install package :

```python
pip install datastructure_collection
```
## Usage

[Example](https://github.com/nyakaz73/datastructure_collection/blob/master/tests/datastructure_example.py)

To use this package :

```python
from datastructure_collection import BinarySearchTree

from datastructure_collection import HashMap

from datastructure_collection import LinkedList
```

### Binary Search Tree
The Binary Search Tree operations and the time complexities are shown in the table below:

| Operation                 | Best Case     |  Worst Case   |  
| -------------             |:-------------:|:-------------:|
| tree = BinarySearchTree() | O(1)          | O(1)          |
|                           |               |               |
| tree.add(key, value)      | O(logN)       | O(N)          | 
| tree.remove(key)          | O(logN)       | O(N)          |
| tree.valueOf(key)         | O(logN)       | O(N)          |
| tree.isEmpty()            | O(1)          | O(1)          |
| tree.minValue()           | O(logN)       | O(N)          |
| tree.maxValue()           | O(logN)       | O(N)          |
| n = len(tree)             | O(1)          | O(1)          |
| x in tree                 | O(logN)       | O(N)          |
| traversal                 | O(N)          | O(N)          |

As seen from the table above the Binary Search Tree has an advantage over a Linear List in terms of its searching mechanism the the tree will be to somewhat sorted where the left elements of a node are less that the elements of a right node, thus giving it a Best case runtime of O(logN) as compared to a List search of O(N).
* **NB** The add,remove,minValue,maxValue and __contains__ ie "in", valueOf operators uses the search mechanism to locate the target.

## Example BinarySearchTree
```python

#import the BinarySearchTree Class
from datastructure_collection import BinarySearchTree

#Instantiate BinarySearchTree object
tree = BinarySearchTree

tree.add(1,"Orange")
tree.add(4,"Banana")
tree.add(7,"Apple")
tree.add(2,"Tomato")


for i in tree:
    print(i) #Prints the sorted List of tuples contaiing the key and value

```


### Pull Requests
I Welcome and i encourage all Pull Requests

## Created and Maintained by
* Author: [Tafadzwa Lameck Nyamukapa](https://github.com/nyakaz73) :
* Email:  [tafadzwalnyamukapa@gmail.com]
* Open for any colleboration and Remote Work!!
* Happy Coding!!

### License
```
BSD 3-Clause License

Copyright (c) 2020, Tafadzwa Lameck Nyamukapa
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

```