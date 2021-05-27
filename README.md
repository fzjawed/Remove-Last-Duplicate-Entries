# Remove-Last-Duplicate-Entries

>28th May 2021 01:31 AM

This question uses a dictionary and honestly I can't figure out any other way to do it. I had to look up the solution but before submitting I wanna sort of understand the dictionary solution so I'm typing this out before submitting the question.

***Question: Given a list of integers nums, find all duplicate numbers and delete their last occurrences.***

We're initialising two dictionaries. Namely ``seen{} and d{}`` 

We iterate through the list and add each value to dictionary ``d{}`` where the key is the number in the list and the value attached to it is the number of times it has been encountered. If the number is not in the dictionary it is added to the dictionary with a value of 1, however if it already exists in the dictionary the value related to it is increased by 1. 

``For example if the list is nums = [1, 3, 4, 1, 3, 5]``

`` '1' would be a key with the value 2, '3' would be a key with value 2, '4' would be a key with value 1 and '5' would be a key with value 1``

Now the weird part.

We initialise a variable i = 0.

With a while loop we're technically iterating through the list. When we initialise ``n = d[nums[i]]`` we're saying n takes the value of the key from dictionary ``d{}``.

So for the first iteration ``n = d[nums[i]] = d[nums[0]] = d[1] = 2``.

Since ``nums[i]`` which in this case is 1 is not in the ``seen{}`` dictionary we add it to the dictionary with the value 1. Meaning this value has now been seen once. If the n value is the same as the key for nums[i] in seen and the n value is greater than 1. That index is removed from nums. 

-- stopping this here because I ran the solution I found and it don't work 🔪😌 -- 
boutta kms
