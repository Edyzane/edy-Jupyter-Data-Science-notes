#elif (one or none)
#if all false...return none @ terminate/end
# seems like this code cannot run because two types 
# of input variable int and string in one conditional
# bugged?? dunno but only integer works
name = 'carol'
x = 3000

if name == 'carol':
    print("hi carol")
elif x < 12:
    print("you are not alice kiddo")
elif x > 100:
    print("you are not alice grannie")
elif x > 2000:
    print("unlike you alice is not a vampire")