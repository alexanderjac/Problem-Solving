
Young Common Ancestor
You're given ithree inputs all of which are instances fof AncestralTree class
that have an ancestor property pointing to their youngest ancestor. tghe first input is the top ancestral tree(i.e. the only instance that has no ancestor-its ancestor property points to None/Null ), and the other two inputs are descendants in the ancestral tree.

Write a function that returns the youngest commmon ancestor to the two descendants. Note that a descendant is considered its own ancestor. So in the simple ancestral tree below, the youngest Common ancestor to nodes A and B is node AA.

#  the youngest common ancestor to nodes A and B is node A 
        A
       /   
     B

Sample input 
topAncestor = node A 
descendantOne = node E
descendantTwo = node I
node D -> output


                A
            /       \
          B           C   
        /  \          / \
       D(2)  E (2)     F   G
     /  \
     H   I

set = (I, D, B, A)

E -> B

[E, B]

[D, B, A]
[I, D, B, A]

Time: O(2*d) = O(D) 
Space: O(d) -> store the path of descendant from root

depth of 1st desc 
depth of 2nd desc 

deeper node 2 -> move to it's anc of depth 1
rec (1, 2's anc)


1. Node can have any number of branches
2. Required: TopAncestor




     

    
