## Challenge Summary

write a function that takes in two hashmaps and left joins into one datastructure

### Challenge Description
write a function that takes in two hashmaps and left joins into one datastructure

#### big o(n)


### input && output 

input 1 synonym table = ['fond':enamored, 'wrath':anger] 2 antonym table = ['fond':averse, 'wrath':delight]

output = [ key, 1, 2] [ ['fond', 'enamored', 'averse'], ['wrath', 'anger', 'delight'], ]


### Approach & Efficiency & algorathm
set empty output list for each key in 1 append key:value pair check if 2 has key TRUE append value FALSE append none append row to output return output
