##  Set Items
        --Set items are unordered, unchangeable, and do not allow duplicate values.

##  Unordered
    --Unordered means that the items in a set do not have a defined order.

    --Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

##  Unchangeable
    --Set items are unchangeable, meaning that we cannot change the items after the set has been created.

    --Once a set is created, you cannot change its items, but you can remove items and add new items.

##  Duplicates Not Allowed
    --Sets cannot have two items with the same value.


##  Python Collections (Arrays)
    --There are four collection data types in the Python programming language:

    --List is a collection which is ordered and changeable. Allows duplicate members.
    --Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    --Set is a collection which is unordered, unchangeable*, and index. No duplicate members.
    --Dictionary is a collection which is ordered** and changeable. No duplicate members.


##  Set Methods
    --Python has a set of built-in methods that you can use on sets.

##          Method	               ----         Description

    --add()	                        --      Adds an element to the set  
    --clear()	                    --      Removes all the elements from the set
    --copy()	                    --      Returns a copy of the set
    --difference()                  --	    Returns a set containing the difference between two or more sets
    --difference_update()           --	    Removes the items in this set that are also included in another, specified set
    --discard()	                    --      Remove the specified item
    --intersection()	            --      Returns a set, that is the intersection of two other sets
    --intersection_update()         --	    Removes the items in this set that are not present in other, specified set(s)
    --isdisjoint()	                --      Returns whether two sets have a intersection or not
    --issubset()	                --      Returns whether another set contains this set or not
    --issuperset()	                --      Returns whether this set contains another set or not
    --pop()	                        --      Removes an element from the set
    --remove()	                    --      Removes the specified element
    --symmetric_difference()        --	    Returns a set with the symmetric differences of two sets
    --symmetric_difference_update() --	    inserts the symmetric differences from this set and another
    --union()	                    --      Return a set containing the union of sets
    --update()	                    --      Update the set with the union of this set and others