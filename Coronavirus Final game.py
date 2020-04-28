answer = input(" You are outside in the store parking lot, what do you grab? (mask/sunglasses)").lower().strip()
if answer == "mask":
    answer = input("you are protected and walk to the door. You are at the entrance. What do you do? (open door, use hand sanitizer)")
    if answer == "use hand sanitizer":
        answer = input("you are protected and walk into the store.You are now in the store and the greeter wants to say hi, what do you do? (talk to him, ignore him)")
        if answer == "ignore him":
            answer = input("you walk right past him and towards the carts.Standing at the line of shopping carts you see a pack of wipes, what do you grab? (cart/wipes)")
            if answer == "wipes":
                answer = input("you wipe down the cart and start to shop. As you walk down with the cart, you must choose an isle. (electronics/cleaning)")
                if answer == "cleaning":
                    answer = input("You look at the toilet paper part of the isle and it is empty. You decide to look for a worker, but none are in sight. What do you do? (go looking/stay there)")
                    if answer == "stay there":
                        answer = input("As you are standing there, an employee turns the corner. You walk up to him and ask for toilet paper. Do you (demand toilet paper/ask nicely)")
                        if answer == "ask nicely":
                            answer = input("He says he will check in the back to see if any more tp is available. As you are waiting, you see someone without a mask close to you coughing. What do you do? (apply hand sanitizer/ignore them)")
                            if answer == "apply hand sanitizer":
                                answer = input("you kill 99.9 percent of germs and the employee returns with a pack of toilet paper.Now that you have your tp, you decide to see if they have any water bottles. What isle do you look down? (international foods/ alcohol isle)")
                                if answer == "international foods":
                                    answer = input("you find an odd japanese brand, the only water left in the store. As you head to check out you smell the Subway and decide you are hungry, what do you do?(get a sandwich/don't get a sandwich)")
                                    if answer == "don't get a sandwich":
                                        answer = input("You ignore the food and decide theres food at home.As you approach the checkout do you get in line or use self checkout? (line/self checkout)")
                                        if answer == ("self checkout"):
                                            answer = input("you walk up to self checkout with your items.The machine asks you cash or credit, what do you do? (cash/credit)")
                                            if answer == ("cash"):
                                               print("you give the machine cash directly and leave the store safely, you win!")
                                            else:
                                                print("the number pad for your pin gives you the virus, game over.")
                                        else:
                                           print("you came within 6 feet of the cashier and caught the virus, game over.") 
                                    else:
                                        print("the customer before you sneezed on the glass you now have the virus, game over.")
                                else: 
                                    print("you look for water bottles but the only thing left is corona beer, game over.")
                            else:
                                print("They walk up to you anyways and give you the virus, game over.")
                        else:
                            print ("you are rude and got kicked out of the store, game over.")
                    else:
                        print("You walk around all day never finding an employee, game over.")
                else:
                    print("you are looking for toilet paper but instead find the demo PS4 and spend all day there, game over.")
            else:
                print("the cart was carrying the virus, game over.")
        else:
            print("you got closer than 6 ft and caught the virus.")
    else:
        print("without sanitizing the door spread the virus, game over.")
else:
    print("you werent protected and caught the virus, game over.")


