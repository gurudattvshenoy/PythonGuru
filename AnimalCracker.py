#ANIMAL CRACKERS: Write a function takes a two-word string and returns True
#if both words begin with same letter
#animal_crackers('Levelheaded Llama') --> True
#animal_crackers('Crazy Kangaroo') --> False

def animal_crackers(s):
    res = s.lower().split()
    return res[0][0] == res[1][0]

print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))
