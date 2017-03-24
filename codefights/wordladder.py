'''
Given two words, beginWord and endWord, and a wordList of approved words, find the length of the shortest transformation
sequence from beginWord to endWord such that:

Only one letter can be changed at a time
Each transformed word must exist in the wordList.

Return the length of the shortest transformation sequence, or 0 if no such transformation sequence exists.

Note: beginWord does not count as a transformed word. You can assume that beginWord and endWord are not empty and are
not the same.

Example

For beginWord = "hit", endWord = "cog", and wordList = ["hot", "dot", "dog", "lot", "log", "cog"], the output should be
wordLadder(beginWord, endWord, wordList) = 5.

The shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog" with a length of 5.

Input/Output

[time limit] 4000ms (py)
[input] string beginWord

Constraints:
1 ≤ beginWord.length ≤ 5.

[input] string endWord

Constraints:
endWord.length = beginWord.length.

[input] array.string wordList

An array containing all of the approved words. All words in the array are the same length and contain only lowercase
English letters. You can assume that there are no duplicates in wordList.

Constraints:
2 ≤ wordList.length ≤ 600,
wordList[i].length = beginWord.length.

[output] integer

An integer representing the length of the shortest transformation sequence from beginWord to endWord using only words
from wordList as described above.


'''

'''wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
beginWord = "hit"
endWord = "cog"'''

'''wordList = ["a", "b","c"]
beginWord = "a"
endWord = "c"'''

'''beginWord = "hot"
endWord = "dog"
wordList = ["hot", "dog",
]'''

beginWord = "teach"
endWord = "place"
wordList = ["peale",
"wilts",
"place",
"fetch",
"purer",
"pooch",
"peace",
"poach",
"berra",
"teach",
"rheum",
"peach"]


def levelOrder(self, root):
    if root is None:
        return
    queue = []
    queue.append(root)
    datalist = []
    while (len(queue) > 0):
        node = queue.pop(0)
        data = node.data
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        datalist.append(data)


def wordLadder(beginWord, endWord, wordList):
    class Node:
        def __init__(self, data, child_list=None):
            self.data = data
            self.child = child_list

        def append(self, node):
            if not self.child:
                self.child = []
            self.child.append(node)
    def countTree(root, endWord, count=1):
        if not root.child and endWord != root.data:
            return 100000
        elif not root.child and endWord == root.data:
            return count + 1
        elif len([n for n in root.child if n.data == endWord]) != 0:
            return (count + 1)
        else:
            return min(countTree(n, endWord, count) for n in root.child) + 1
    if endWord not in wordList:
        return 0
    queue = []
    workingList = wordList
    rootNode = Node(beginWord)
    queue.append(rootNode)
    while (len(queue)):
        dNode = queue.pop(0)
        data = dNode.data
        l = [item for item in workingList
             if len([x for x, y in zip(list(data), list(item)) if x != y]) == 1]
        if l:
            tempList = [it for it in workingList if it not in l and it != beginWord]
            workingList = tempList
            for it in l:
                n = Node(it)
                dNode.append(n)
            queue = queue + dNode.child
    cnt = countTree(rootNode, endWord)
    if cnt < 2 or cnt == 100000:
        return 0
    else:
        return cnt


print wordLadder(beginWord, endWord, wordList)

