def main():
    while True: 
        menu = """
-----------------List of Menu Functions--------------------
1.  Phone Book
2.  Messages
3.  Chat
4.  Call Register
5.  Tones
6.  Settings
7.  Call Divert
8.  Games
9.  Calculator
10. Reminder
11. Clock
12. Profiles
13. SIM services
"""
        print(menu)
        try:
            selectOption = int(input("Enter an option: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        # PHONE BOOK
        if selectOption == 1:
            while True:
                phoneBookMenu = """
1. Search
2. Service Nos
3. Add Name
4. Erase
5. Edit
6. Assign tone
7. Send b'card
8. Options
9. Speed dials
10. Voice Tags
11. Back
"""
                print(phoneBookMenu)
                try:
                    selectPhoneBookOption = int(input("Select and enter an option: "))
                except ValueError:
                    print("Invalid input!")
                    continue
                if selectPhoneBookOption == 11:
                    break
                elif selectPhoneBookOption == 1:
                    print("You have selected Search.")
                elif selectPhoneBookOption == 2:
                    print("You have selected Service Nos.")
                elif selectPhoneBookOption == 3:
                    print("You have selected Add Name.")
                elif selectPhoneBookOption == 4:
                    print("You have selected Erase.")
                elif selectPhoneBookOption == 5:
                    print("You have selected Edit.")
                elif selectPhoneBookOption == 6:
                    print("You have selected Assign Tone.")
                elif selectPhoneBookOption == 7:
                    print("You have selected Send b'card'.")
                elif selectPhoneBookOption == 8:
                    while True:
                        optionsMenu = """
8. Options
1. Type of view
2. Memory status
3. Back
"""
                        print(optionsMenu)
                        try:
                            selectOptionsOption = int(input("Enter an option: "))
                        except ValueError:
                            print("Invalid input!")
                            continue
                        if selectOptionsOption == 3:
                            break
                        elif selectOptionsOption == 1:
                            print("You have selected Type of view.")
                        elif selectOptionsOption == 2:
                            print("You have selected Memory status.")
                elif selectPhoneBookOption == 9:
                    print("You have selected Speed dials.")
                elif selectPhoneBookOption == 10:
                    print("You have selected Voice Tags.")

        # MESSAGES
        elif selectOption == 2:
            while True:
                messagesMenu = """
1. Write Messages
2. Inbox
3. Outbox
4. Picture Messages
5. Templates
6. Smileys
7. Message settings
8. Info service
9. Voice mailbox number
10. Service command editor
11. Back
"""
                print(messagesMenu)
                try:
                    messageOption = int(input("Select an option: "))
                except ValueError:
                    print("Invalid input!")
                    continue
                if messageOption == 11:
                    break
                elif messageOption == 1:
                    print("You have selected Write Messages.")
                elif messageOption == 2:
                    print("You have selected Inbox.")
                elif messageOption == 3:
                    print("You have selected Outbox.")
                elif messageOption == 4:
                    print("You have selected Picture Messages.")
                elif messageOption == 5:
                    print("You have selected Templates.")
                elif messageOption == 6:
                    print("You have selected Smileys.")
                elif messageOption == 7:
                    print("You have selected Message settings.")
                elif messageOption == 8:
                    print("You have selected Info Service.")
                elif messageOption == 9:
                    print("You have selected Voice mailbox number.")
                elif messageOption == 10:
                    print("You have selected Service command editor.")

        # CHAT
        elif selectOption == 3:
            print("Chat")

        # CALL REGISTER
        elif selectOption == 4:
            while True:
                callRegisterMenu = """
1. Missed calls
2. Received calls
3. Dialled numbers
4. Erase recent call lists
5. Show call duration
6. Show call costs
7. Call costs settings
8. Prepaid credit
9. Back
"""
                print(callRegisterMenu)
                try:
                    callOption = int(input("Enter an option: "))
                except ValueError:
                    print("Invalid input!")
                    continue
                if callOption == 9:
                    break
                elif callOption == 1:
                    print("You have selected Missed calls.")
                elif callOption == 2:
                    print("You have selected Received calls.")
                elif callOption == 3:
                    print("You have selected Dialled numbers.")
                elif callOption == 4:
                    print("You have selected Erase recent call lists.")
                elif callOption == 5:
                    print("You have selected Show call duration.")
                elif callOption == 6:
                    print("You have selected Show call costs.")
                elif callOption == 7:
                    print("You have selected Call costs settings.")
                elif callOption == 8:
                    print("You have selected Prepaid credit.")

        # TONES
        elif selectOption == 5:
            while True:
                tonesMenu = """
1. Ringing Tone
2. Ringing volume
3. Incoming call alert
4. Composer
5. Message alert tone
6. Keypad tones
7. Warning and game tones
8. Vibrating alert
9. Screen saver
10. Back
"""
                print(tonesMenu)
                try:
                    tonesOption = int(input("Enter an option: "))
                except ValueError:
                    print("Invalid input!")
                    continue
                if tonesOption == 10:
                    break
                elif tonesOption == 1:
                    print("You have selected Ringing Tone.")
                elif tonesOption == 2:
                    print("You have selected Ringing volume.")
                elif tonesOption == 3:
                    print("You have selected Incoming call alert.")
                elif tonesOption == 4:
                    print("You have selected Composer.")
                elif tonesOption == 5:
                    print("You have selected Message alert tone.")
                elif tonesOption == 6:
                    print("You have selected Keypad tones.")
                elif tonesOption == 7:
                    print("You have selected Warning and game tones.")
                elif tonesOption == 8:
                    print("You have selected Vibrating alert.")
                elif tonesOption == 9:
                    print("You have selected Screen saver.")

        # SETTINGS
        elif selectOption == 6:
            while True:
                settingsMenu = """
1. Call settings
2. Phone Settings
3. Security Settings
4. Restore Factory Settings
5. Back
"""
                print(settingsMenu)
                try:
                    settingsOption = int(input("Enter an option: "))
                except ValueError:
                    print("Invalid input!")
                    continue
                if settingsOption == 5:
                    break
                else:
                    print(f"You have selected option {settingsOption}.")

        # CALL DIVERT
        elif selectOption == 7:
            print("You have selected Call Divert.")

        # GAMES
        elif selectOption == 8:
            print("You have selected Games.")

        # CALCULATOR
        elif selectOption == 9:
            print("You have selected Calculator.")

        # REMINDER
        elif selectOption == 10:
            print("You have selected Reminder.")

        # CLOCK
        elif selectOption == 11:
            while True:
                clockMenu = """
1. Alarm clock
2. Clock settings
3. Date settings
4. StopWatch
5. Countdown timer
6. Auto update of date and time
7. Back
"""
                print(clockMenu)
                try:
                    clockOption = int(input("Enter an option: "))
                except ValueError:
                    print("Invalid input!")
                    continue
                if clockOption == 7:
                    break
                else:
                    print(f"You have selected option {clockOption}.")

        # PROFILES
        elif selectOption == 12:
            print("Profiles")

        # SIM SERVICES
        elif selectOption == 13:
            print("SIM Service")

        else:
            print("Invalid option, try again!")


if __name__ == "__main__":
    main()

