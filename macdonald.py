#OLD MACDONALD: Write a function that capitalizes the first and fourth letters
#of a name
#old_macdonald('macdonald')

def old_macdonald(input):
    return input[0].capitalize() + input[1:3]+ input[3].capitalize()+ input[4:]

print(old_macdonald('macdonald'))
