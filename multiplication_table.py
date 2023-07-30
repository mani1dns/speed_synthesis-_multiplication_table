import pyttsx3

print("-----Speed Synthesis Multiplication Table-----")
n = input("Enter a number: ")
# 9
# one nines are nine
dic = {
    "1": "ones",
    "2": "twos",
    "3": "threes",
    "4": "fours",
    "5": "fives",
    "6": "sixes",
    "7": "sevens",
    "8": "eights",
    "9": "nines",
    "10": "tens"
}
txt = ""

for i in range(1,11):
    # one nines are nine
    # two nines are eighteen
    mul = i * int(n)
    txt += str(i) + " " + dic[n] + " are " + str(mul) + "\n"
engine = pyttsx3.init()
engine.say(txt)
engine.runAndWait()