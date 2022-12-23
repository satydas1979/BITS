# import os library
import os

# infinite while loop
while True:
    print("Choose a +ve integer from below menu items :-")
    print("1. Input into Array Queue from File (Multiple elements)")
    print("2. Input into Array Queue from command line (Single Element)")
    print("3. Remove element from Array Queue (Single Element)")
    print("4. Input into List Queue from File")
    print("5. Input into List Queue from command line")
    print("6. Remove element from List Queue")
    print("7. Input into Sorted List from File")
    print("8. Input into Sorted List from command line")
    print("9. Find element in Sorted List")
    print("10. Remove element in Sorted List")
    print("11. Input into BST from File")
    print("12. Input into BST from command line")
    print("13. Find element in BST")
    print("14. Remove element From BST")
    print("15. Print BST in order")
    print("16. Quit")

    # take input from user
    choice = raw_input()

    if (0 == choice.isdigit()):
        print("Invalid choice")
        continue

    choice = int(choice)

    if (1 == choice):
        print("Selected 1")
    elif (2 == choice):
        print("Selected 2")
    elif (3 == choice):
        print("Selected 3")
    elif (4 == choice):
        print("Selected 4")
    elif (5 == choice):
        print("Selected 5")
    elif (6 == choice):
        print("Selected 6")
    elif (7 == choice):
        print("Selected 7")
    elif (8 == choice):
        print("Selected 8")
    elif (9 == choice):
        print("Selected 9")
    elif (10 == choice):
        print("Selected 10")
    elif (11 == choice):
        print("Selected 11")
    elif (12 == choice):
        print("Selected 12")
    elif (13 == choice):
        print("Selected 13")
    elif (14 == choice):
        print("Selected 14")
    elif (15 == choice):
        print("Selected 15")
    elif (16 == choice):
        print("Thank you!")
        break
    else :
        print("Invalid choice")