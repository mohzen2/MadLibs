#This is a madlib as we already learned before, but slightly more intricate 
#def madlib():

def madlib():
    noun1 = input("Noun: ")
    noun2 = input("Noun: ")
    noun3 = input("Noun: ")
    occup = input("Occupation: ")
    verb1 = input("Verb: ")
    place1 = input("Place: ")
    verb2 = input('Verb ending in "ED": ')
    noun4 = input("Noun: ")
    verb3 = input('Verb ending in "ING": ')
    noun5 = input('Noun (Plural): ')
    noun6 = input("Noun: ")
    emo = input("Emotion: ")

    madlib = f"It was during the battle of {noun1} when I was running through a {noun2} when a {noun3} went off right next to my platoon. \
Our {occup} yelled for us to {verb1} to the nearest {place1} we could find. When we got to the {place1} we {verb2} to start a fire.\
 As we were starting the fire the enemy saw the {noun4} from the fire and started {verb3} {noun5} at us. We all quickly ducked behind the \
{noun6} at the {place1} and returned fire. We quickly eliminated the enemy and were {emo} that we had won the battle."

    print(madlib)

madlib()

#Remember to call the function at the end of the code in case it is not executing correctly that took me awhile to catch.