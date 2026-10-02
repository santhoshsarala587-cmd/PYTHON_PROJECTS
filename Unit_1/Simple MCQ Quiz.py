print("======================================")
print("      SIMPLE MCQ QUIZ APPLICATION")
print("======================================")

name = input("Enter your name: ")
score = 0

print("\nWelcome", name, "Let's start the quiz!\n")

# -------- QUESTIONS --------

print("1. Chemical symbol of Water is?")
print("A. O2")
print("B. CO2")
print("C. H2O")
print("D. H2")
ans = input("Answer: ")
if ans == "C" or ans == "c":
    score += 1

print("\n2. Atomic number of Hydrogen?")
print("A. 1")
print("B. 2")
print("C. 8")
print("D. 0")
ans = input("Answer: ")
if ans == "A" or ans == "a":
    score += 1

print("\n3. Which gas is used for respiration?")
print("A. Nitrogen")
print("B. Oxygen")
print("C. Carbon dioxide")
print("D. Hydrogen")
ans = input("Answer: ")
if ans == "B" or ans == "b":
    score += 1

print("\n4. pH value of pure water is?")
print("A. 5")
print("B. 6")
print("C. 7")
print("D. 8")
ans = input("Answer: ")
if ans == "C" or ans == "c":
    score += 1

print("\n5. Chemical symbol of Sodium?")
print("A. Na")
print("B. So")
print("C. Sn")
print("D. Sd")
ans = input("Answer: ")
if ans == "A" or ans == "a":
    score += 1

print("\n6. Who is the main character of Jujutsu Kaisen?")
print("A. Gojo Satoru")
print("B. Megumi Fushiguro")
print("C. Yuji Itadori")
print("D. Sukuna")
ans = input("Answer: ")
if ans == "C" or ans == "c":
    score += 1

print("\n7. Who is known as the strongest sorcerer?")
print("A. Yuji")
print("B. Gojo")
print("C. Nanami")
print("D. Todo")
ans = input("Answer: ")
if ans == "B" or ans == "b":
    score += 1

print("\n8. Sukuna is known as?")
print("A. Curse King")
print("B. Demon Lord")
print("C. Shadow King")
print("D. Fire God")
ans = input("Answer: ")
if ans == "A" or ans == "a":
    score += 1

print("\n9. Megumi uses which technique?")
print("A. Fire")
print("B. Shadow")
print("C. Ice")
print("D. Wind")
ans = input("Answer: ")
if ans == "B" or ans == "b":
    score += 1

print("\n10. Gojo's special ability is?")
print("A. Sharingan")
print("B. Six Eyes")
print("C. Bankai")
print("D. Rasengan")
ans = input("Answer: ")
if ans == "B" or ans == "b":
    score += 1

print("\n11. 10 + 20 = ?")
print("A. 20")
print("B. 25")
print("C. 30")
print("D. 40")
ans = input("Answer: ")
if ans == "C" or ans == "c":
    score += 1

print("\n12. 15 x 2 = ?")
print("A. 30")
print("B. 25")
print("C. 20")
print("D. 35")
ans = input("Answer: ")
if ans == "A" or ans == "a":
    score += 1

print("\n13. Square of 5?")
print("A. 10")
print("B. 20")
print("C. 25")
print("D. 30")
ans = input("Answer: ")
if ans == "C" or ans == "c":
    score += 1

print("\n14. 50 ÷ 5 = ?")
print("A. 5")
print("B. 10")
print("C. 15")
print("D. 20")
ans = input("Answer: ")
if ans == "B" or ans == "b":
    score += 1

print("\n15. 7 x 8 = ?")
print("A. 54")
print("B. 56")
print("C. 64")
print("D. 48")
ans = input("Answer: ")
if ans == "B" or ans == "b":
    score += 1

print("\n16. Value of pi is approximately?")
print("A. 2.14")
print("B. 3.14")
print("C. 4.13")
print("D. 3.41")
ans = input("Answer: ")
if ans == "B" or ans == "b":
    score += 1

print("\n17. Which is an even number?")
print("A. 3")
print("B. 5")
print("C. 7")
print("D. 8")
ans = input("Answer: ")
if ans == "D" or ans == "d":
    score += 1

print("\n18. HCl is an example of?")
print("A. Base")
print("B. Salt")
print("C. Acid")
print("D. Metal")
ans = input("Answer: ")
if ans == "C" or ans == "c":
    score += 1

print("\n19. 100 - 45 = ?")
print("A. 55")
print("B. 65")
print("C. 45")
print("D. 50")
ans = input("Answer: ")
if ans == "A" or ans == "a":
    score += 1

print("\n20. Which one is NOT a programming language?")
print("A. Python")
print("B. Java")
print("C. HTML")
print("D. C")
ans = input("Answer: ")
if ans == "C" or ans == "c":
    score += 1

print("\n======================================")
print("Quiz Completed!")
print("Final Score:", score, "/ 20")

if score >= 15:
    print("Excellent Performance ")
elif score >= 10:
    print("Good Job ")
else:
    print("Keep Practicing ")
