# Remove-Last-Duplicate-Entries

>28th May 2021 01:31 AM

This question uses a dictionary and honestly I can't figure out any other way to do it. I had to look up the solution but before submitting I wanna sort of understand the dictionary solution so I'm typing this out before submitting the question.

***Question: Given a list of integers nums, find all duplicate numbers and delete their last occurrences.***

Tbvh I was kinda frustrated after looking at the solutions because it was stuff I didn't know but well I guess that's what I'm here for - to learn stuff I didn't know.

So with this question there's a thing called a Python Counter. Basically what it does is:

``Python Counter takes in input a list, tuple, dictionary, string, which are all iterable objects, and it will give you output that will have the count of each element.``

So if we have a list `[1,3,4,1,3,5]` then using Counter on this list will return ``Counter({1: 2, 3: 2, 4: 1, 5: 1})``

Basically the key is the element in the list and the value attached to it is how many times it appears in the list. Also in order to make this work you have to `` from collections import Counter``.

The loop is a little weird but the first if statement is sort of a way to complete the circle. Because there's no way in the beginning any ``c[val]`` will be 0. So we move on with the iteration. Or else we append the value to a new list called res and decrease the value for that key by 1. After that we enter another if statement that says if the count of that value is 1 then set the the count of that value to 0. 

So let's work with our example list.

``{1: 2, 3: 2, 4: 1, 5: 1}``

***Step 1:*** The "val" attached to 1 is not 0 so I skip the first if statement and go to the else. I append the actual element in the list to the resulting list and decrease it's count by 1. 


So at this point I have ``res = [1]`` and ``c = {1: 1, 3: 2, 4: 1, 5: 1}``. 

When I enter the next if statement the value attached to 1 is actually 1 so I change it to 0. 

And now I have ``c = {1: 0, 3: 2, 4: 1, 5: 1}``


***Step 2:*** The same process happens for 3 and 3 gets appended to the resulting list once. 

***Step 3:*** When we come to 4; the value attached to it is not 0 and so it just moves to the else too and gets appended to the resulting list. 


