# Day 7: 30 days of python programming
#Exercise day 7
#Sets
#Exercise level 1
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print('Length of it_companies set: ', len(it_companies))  #length of the set it_companies

it_companies.add('Twitter')  # Addlng Twitter to it_companies
print(it_companies)   

it_companies.update(['Techno','Infinix' 'Samsung','Huawei','Geonee'])  # Inserting multiple it_companies 
print(it_companies)

#it_companies.remove('Infinix')   # we remove one companies from the set 

#discard is throwing element from the set, while remove return error when the element is not in the set

# Exercise Level 2

print('Joining A and B: ', A.union(B))  # Join two sets A and B

print('Intersection of A and B: ', A.intersection(B))  # return intersection A and B

print('A is a subset of B : ', A.issubset(B)) # # A is a subset of B

print('A and B are disjoint: ', A.isdisjoint(B))  # disjoint sets

print('A with B: ', A.union(B)) # they are the same
print('B with A: ', B.union(A))

print('Symmetric difference of A and B: ',A.symmetric_difference(B))  #symmetric difference between A and B

del A
del B
#print(B) # Return Error

#Exercise Level 3
age = [19, 22, 20, 25, 26, 24, 28, 27]

age_st = set(age)
print('age_set is smaller than age: ', len(age_st) < len(age))  

# strings are ordered and unmutable character enclosed by single or double quotation
# list is a collection of similar of different data types. They are iterable ,ordered and mutable
# tuples are like lists but are unmutable
# sets contain unique elements in the collection. They are unordered but mutable. 

statement = 'I am a teacher and I love to inspire and teach people'
print('Unique words in the sentence: ',set(statement.split()))  #split methods 

