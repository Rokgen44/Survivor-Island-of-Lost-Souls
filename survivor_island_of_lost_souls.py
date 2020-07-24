import random
import time
players = []
og_tribe1 = []
og_tribe2 = []
swappers = []
merged_tribe = []
isle_of_lost_souls = []
out_pre_merge = []
advantages = ["Hidden Immunity Idol", "Vote Blocker", "Self-Vote Locket", "Idol Nullifier", "Walk Out Immunity", "Loss Island Vote", "Loss Island Idol", "The Will It", "The Extortion Twist"]
willops = ["Locket but Self-Vote", "Idol but Auto-Tribal", "Red. Adv. but Loss Auto-Immune", "Idol but Extortion", "Vote Blocker but No Vote"]
jury = []
idols = []
tokens = {}
forfeit_tokens = {}
bootlist = []
token_num = 1
counter = 0
tok_count = 0
forfeit_num = 0
cast = int(input("How many players do you want in the game?"))
menu = {"idol":4, "locket":2, "vote steal":2, "ch. advantage":3, "red. adv":4, "loss island immunity":4, "willop":5, "50/50 coin":4}
swaptype = ["Len","Equal"]

print("Welcome to Survivor: Island of Lost Souls.")

time.sleep(1)

for castaways in range(cast):
    name = input("Please name your castaway.")
    tribe_choice = int(input("What tribe do you want them on (type 1 or 2)?"))
    players.append(name)
    if tribe_choice == 1:
        og_tribe1.append(name)
        print(og_tribe1)
    elif tribe_choice == 2:
        og_tribe2.append(name)
        print(og_tribe2)
    tokens[name] = token_num

time.sleep(1)
print("\n")
print(og_tribe1)
og_tribe1_name = input("What is this tribe's name?")
time.sleep(1)
print(og_tribe2)
og_tribe2_name = input("What is this tribe's name?")
tribes = [og_tribe1_name, og_tribe2_name]

def boot_list():
    global bootlist
    print ('')
    print ('Bootlist:')
    for x in range(0,len(bootlist)):
        print (str(x+1) + '-th person voted out:', bootlist[x])
    return

def pre_merge():
    global counter
    global tok_count
    print("The tribes are as follows:")
    print(og_tribe1_name + ":")
    for each in og_tribe1:
        print(each)
    print("\n")
    print(og_tribe2_name + ":")
    for all in og_tribe2:
        print(all)
    print("\n")
    print("And now for today's immunity challenge!")
    ch_winner = random.choice(tribes)
    print(ch_winner, "wins immunity!")

    print(tokens)
    token_help = input("Any token usage today? (type 'yes' or 'no' specifically.")
    if token_help == "yes":
        while True:
            print(tokens)
            choice = input("Type 'give' if someone is giving someone else tokens; 'challenge' if someone volunteeered to compete in a token challenge; 'casino' if someone wants to enter the Survivor Casino; \n 'purchase' if someone is purchasing an item with fire tokens; or 'done' if you're finished with token usage for the day.")
            if choice == "give":
                name = input("Who is giving tokens?")
                much = int(input("How many tokens are being given?"))
                amount = tokens[name]
                if much > amount:
                    print("Can't afford that.")
                else:
                    giving = input("Who are they giving tokens to?")
                    tokens[name] -= much
                    tokens[giving] += much
            elif choice == "challenge":
                if tok_count != 1:
                    challengers = []
                    num = int(input("How many players will be competing?"))
                    for competitors in range(num):
                        name = input("Who shall be competing?")
                        challengers.append(name)
                    print("The winner shall receive a fire token. Loser(s) will lose a fire token. If the loser has no tokens, they will earn a vote at their next tribal council.")
                    win = random.choice(challengers)
                    print(win, "has won a fire token!")
                    tokens[win] += 1
                    challengers.remove(win)
                    for losers in challengers:
                        if tokens[losers] != 0:
                            tokens[losers] -= 1
                        else:
                            print(losers, "has no tokens to lose. Therefore, they will earn a vote at their next tribal council.")
                    tok_count += 1
                else:
                    print("Sorry, no more token challenges today.")
            elif choice == "purchase":
                name = input("Who is buying?")
                print(menu)
                using = input("What are they buying? Please type the item spelled exactly as it appears on the menu.")
                price = menu[using]
                have = tokens[name]
                if price > have:
                    print("Can't afford that.")
                else:
                    print("It's a purchase!")
                    tokens[name] -= price
            elif choice == "casino":
                if counter != 1:
                    s_rate = ["Yes"]
                    risk_taker = input("Who made the first move and decided to take a chance, entering the Survivor Casino?")
                    print(risk_taker, "has entered the Survivor Casino. The way this works is simple. Place a bet of fire tokens. You win, you earn that amount. You lose, lose your bet. Very simple.\n"
                                      "If you want to try, place your bet. If not, type 0 and you won't bet a thing. The higher you bet, the higher the risk.")
                    bet = int(input("What is your bet?"))
                    amount = tokens[risk_taker]
                    if bet > amount:
                        print("Can't afford that.")
                    else:
                        for chance in range(bet):
                            s_rate.append("No")
                        game = random.choice(s_rate)
                        if game == "Yes":
                            print("Congrats, you win", bet, "tokens!")
                            tokens[risk_taker] += bet
                        elif game == "No":
                            print("The risk has failed, you lose", bet, "tokens.")
                            tokens[risk_taker] -= bet
                    counter += 1
                else:
                    print("Sorry, the casino has been used today.")
            elif choice == "done":
                break

    print("Welcome to Tribal Council.")
    if ch_winner == og_tribe1_name:
        print(og_tribe2)
    elif ch_winner == og_tribe2_name:
        print(og_tribe1)
    vote_forfeit = input("Would anyone like to give up their vote for a token?")
    if vote_forfeit == "yes":
        vote_for_num = int(input("How many?"))
        for givers in range(vote_for_num):
            forfeitter = input("Write the name of the person giving up their vote. 'Specifically how it was written originally' ")
            tokens[forfeitter] += 1
    voters = int(input("How many people are voting?"))

    tallies = []
    vote_freq = {}

    idol = input("Did anyone get the idol?")
    if idol == "yes":
        num = int(input("How many people?"))
        for idol in range(num):
            receiver = input("Enter the name.")
            idols.append(receiver)

    for votes in range(voters):
        vote = input("Write the name of the person you will vote out. 'Specifically how it was written originally' ")
        tallies.append(vote)

    for choices in tallies:
        if vote_freq.get(choices) == None:
            vote_freq[choices] = 1
        else:
            vote_freq[choices] += 1

    print(tallies)
    print(vote_freq)

    p_bootee = max(vote_freq, key=vote_freq.get)
    if p_bootee in idols:
        while True:
            print("Any votes against", p_bootee, "will not count.")
            del vote_freq[p_bootee]
            idols.remove(p_bootee)
            p_bootee = max(vote_freq, key=vote_freq.get)
    if p_bootee in og_tribe1:
        og_tribe1.remove(p_bootee)
    elif p_bootee in og_tribe2:
        og_tribe2.remove(p_bootee)


    print(vote_freq)

    print(p_bootee + ",", "the tribe has spoken.")
    isle_of_lost_souls.append(p_bootee)

    will_num = tokens[p_bootee]
    tokens[p_bootee] -= will_num
    del tokens[p_bootee]
    print(tokens)
    will = input("Who is the boot willing tokens to? 'Write it specifically how it was written originally'")
    tokens[will] += will_num
    forfeit_tokens[p_bootee] = forfeit_num
    counter = 0
    tok_count = 0


print(merged_tribe)
def merge():
    global counter
    global tok_count
    print("The tribes are as follows:")
    print(str((merged_tribe_name + ":")))
    print("\n")
    for them in merged_tribe:
        print(them)
    print("And now for today's immunity challenge!")
    ch_winner = random.choice(merged_tribe)
    print(ch_winner, "wins immunity!")
    tokens[ch_winner] += 1

    print(tokens)
    token_help = input("Any token usage today? Specifically type 'yes' or 'no' ")
    if token_help == "yes":
        while True:
            print(tokens)
            choice = input("Type 'give' if someone is giving someone else tokens; 'challenge' if someone volunteeered to compete in a token challenge; 'casino' if someone wants to enter the Survivor Casino; \n 'purchase' if someone is purchasing an item with fire tokens; or 'done' if you're finished with token usage for the day.")
            if choice == "give":
                name = input("Who is giving tokens?")
                much = int(input("How many tokens are being given?"))
                amount = tokens[name]
                if much > amount:
                    print("Can't afford that.")
                else:
                    giving = input("Who are they giving tokens to?")
                    tokens[name] -= much
                    tokens[giving] += much
            elif choice == "challenge":
                if tok_count != 1:
                    challengers = []
                    num = int(input("How many players will be competing?"))
                    for competitors in range(num):
                        name = input("Who shall be competing?")
                        challengers.append(name)
                    print("The winner shall receive a fire token. Loser(s) will lose a fire token. If the loser has no tokens, they will earn a vote at their next tribal council.")
                    win = random.choice(challengers)
                    print(win, "has won a fire token!")
                    tokens[win] += 1
                    challengers.remove(win)
                    for losers in challengers:
                        if tokens[losers] != 0:
                            tokens[losers] -= 1
                        else:
                            print(losers, "has no tokens to lose. Therefore, they will earn a vote at their next tribal council.")
                    tok_count += 1
                else:
                    print("Sorry, no more token challenges today.")
            elif choice == "purchase":
                name = input("Who is buying?")
                print(menu)
                using = input("What are they buying? Please type the item spelled exactly as it appears on the menu.")
                price = menu[using]
                have = tokens[name]
                if price > have:
                    print("Can't afford that.")
                else:
                    print("It's a purchase!")
                    tokens[name] -= price
            elif choice == "casino":
                if counter != 1:
                    s_rate = ["Yes"]
                    risk_taker = input("Who made the first move and decided to take a chance, entering the Survivor Casino?")
                    print(risk_taker, "has entered the Survivor Casino. The way this works is simple. Place a bet of fire tokens. You win, you earn that amount. You lose, lose your bet. Very simple.\n"
                                      "If you want to try, place your bet. If not, type 0 and you won't bet a thing. The higher you bet, the higher the risk.")
                    bet = int(input("What is your bet?"))
                    amount = tokens[risk_taker]
                    if bet > amount:
                        print("Can't afford that.")
                    else:
                        for chance in range(bet):
                            s_rate.append("No")
                        game = random.choice(s_rate)
                        if game == "Yes":
                            print("Congrats, you win", bet, "tokens!")
                            tokens[risk_taker] += bet
                        elif game == "No":
                            print("The risk has failed, you lose", bet, "tokens.")
                            tokens[risk_taker] -= bet
                    counter += 1
                else:
                    print("Sorry, the casino has been used today.")
            elif choice == "done":
                break
    print(tokens)

    print("Welcome to Tribal Council.")
    print(merged_tribe)
    if len(jury) > 0:
        print("The Jury:", str(jury))
    vote_forfeit = input("Would anyone like to give up their vote for a token?")
    if vote_forfeit == "yes":
        vote_for_num = int(input("How many?"))
        for givers in range(vote_for_num):
            forfeitter = input("Write the name of the person giving up their vote.")
            tokens[forfeitter] += 1
    voters = int(input("How many people are voting?"))

    tallies = []
    vote_freq = {}

    idol = input("Did anyone get the idol?")
    if idol == "yes":
        num = int(input("How many people?"))
        for idol in range(num):
            receiver = input("Enter the name.")
            idols.append(receiver)

    for votes in range(voters):
        vote = input("Write the name of the person you will vote out.")
        tallies.append(vote)

    for choices in tallies:
        if vote_freq.get(choices) == None:
            vote_freq[choices] = 1
        else:
            vote_freq[choices] += 1

    print(tallies)
    print(vote_freq)

    p_bootee = max(vote_freq, key=vote_freq.get)
    if p_bootee in idols:
        while True:
            print("Any votes against", p_bootee, "will not count.")
            del vote_freq[p_bootee]
            idols.remove(p_bootee)
            p_bootee = max(vote_freq, key=vote_freq.get)
    if p_bootee in og_tribe1:
        og_tribe1.remove(p_bootee)
    elif p_bootee in og_tribe2:
        og_tribe2.remove(p_bootee)

    print(vote_freq)

    print(p_bootee + ",", "the tribe has spoken.")
    isle_of_lost_souls.append(p_bootee)
    merged_tribe.remove(p_bootee)

    will_num = tokens[p_bootee]
    tokens[p_bootee] -= will_num
    del tokens[p_bootee]
    print(tokens)
    will = input("Who is the boot willing tokens to?")
    tokens[will] += will_num
    forfeit_tokens[p_bootee] = forfeit_num
    counter = 0
    tok_count = 0

def new_merge():
    print("The tribes are as follows:")
    print(str((merged_tribe_name + ":")))
    print("\n")
    for them in merged_tribe:
        print(them)
    print("And now for today's immunity challenge!")
    ch_winner = random.choice(merged_tribe)
    print(ch_winner, "wins immunity!")

    print("Welcome to Tribal Council.")
    print(merged_tribe)
    if len(jury) > 0:
        print("The Jury:", str(jury))
    voters = int(input("How many people are voting?"))

    tallies = []
    vote_freq = {}

    idol = input("Did anyone get the idol?")
    if idol == "yes":
        num = int(input("How many people?"))
        for idol in range(num):
            receiver = input("Enter the name.")
            idols.append(receiver)

    for votes in range(voters):
        vote = input("Write the name of the person you will vote out.")
        tallies.append(vote)

    for choices in tallies:
        if vote_freq.get(choices) == None:
            vote_freq[choices] = 1
        else:
            vote_freq[choices] += 1

    print(tallies)
    print(vote_freq)

    p_bootee = max(vote_freq, key=vote_freq.get)
    if p_bootee in idols:
        while True:
            print("Any votes against", p_bootee, "will not count.")
            del vote_freq[p_bootee]
            idols.remove(p_bootee)
            p_bootee = max(vote_freq, key=vote_freq.get)

    print(vote_freq)

    print(p_bootee + ",", "the tribe has spoken.")
    jury.append(p_bootee)
    merged_tribe.remove(p_bootee)
    bootlist.append(p_bootee)

def swap():
    if (len(tokens)%2) == 0:
        type = random.choice(swaptype)
        if type == "Len":
            init1 = len(og_tribe1)
            init2 = len(og_tribe2)
            for each in og_tribe1:
                swappers.append(each)
            for all in og_tribe2:
                swappers.append(all)
            for each2 in range(init1):
                new_mem = random.choice(swappers)
                swappers.remove(new_mem)
                if new_mem not in og_tribe1:
                    og_tribe2.remove(new_mem)
                    og_tribe1.append(new_mem)
            for all2 in range(init2):
                new_mem = random.choice(swappers)
                swappers.remove(new_mem)
                if new_mem not in og_tribe2:
                    og_tribe1.remove(new_mem)
                    og_tribe2.append(new_mem)
        elif type == "Equal":
            swapped = []
            for each in og_tribe1:
                swapped.append(each)
                og_tribe1.remove(each)
            for all in og_tribe2:
                swapped.append(all)
                og_tribe2.remove(all)
            for twist in range(int((len(swapped))/2)):
                picked = random.choice(swapped)
                og_tribe1.append(picked)
                swapped.remove(picked)
            for twist2 in range(len(swapped)):
                picked = random.choice(swapped)
                og_tribe2.append(picked)
                swapped.remove(picked)
    else:
        init1 = len(og_tribe1)
        init2 = len(og_tribe2)
        for each in og_tribe1:
            swappers.append(each)
        for all in og_tribe2:
            swappers.append(all)
        for each2 in range(init1):
            new_mem = random.choice(swappers)
            swappers.remove(new_mem)
            if new_mem not in og_tribe1:
                og_tribe2.remove(new_mem)
                og_tribe1.append(new_mem)
        for all2 in range(init2):
            new_mem = random.choice(swappers)
            swappers.remove(new_mem)
            if new_mem not in og_tribe2:
                og_tribe1.remove(new_mem)
                og_tribe2.append(new_mem)


def isle_of_lost_souls_voting():
        global bootlist
        if len(isle_of_lost_souls) == 3:
            print("Welcome to the Island of Lost Souls.")
            print(isle_of_lost_souls)
            print(forfeit_tokens)
            forfeit_vote = input("Did anyone forfeit their vote? Type their name if they did or no if no one did.")
            if forfeit_vote != "no":
                forfeit_tokens[forfeit_vote] += 1
            voters = int(input("How many people are voting?"))

            tallies = []
            vote_freq = {}

            for votes in range(voters):
                vote = input("Write the name of the person you will vote out.")
                tallies.append(vote)

            for choices in tallies:
                if vote_freq.get(choices) == None:
                    vote_freq[choices] = 1
                else:
                    vote_freq[choices] += 1

            print(tallies)
            print(vote_freq)

            p_bootee_isle_souls = max(vote_freq, key=vote_freq.get)
            isle_of_lost_souls.remove(p_bootee_isle_souls)

            print(p_bootee_isle_souls + ",", "the tribe has spoken.")
            out_pre_merge.append(p_bootee_isle_souls)
            bootlist.append(p_bootee_isle_souls)
            del forfeit_tokens[p_bootee_isle_souls]

            print(isle_of_lost_souls)
            print("And now, the ultimate test. Who will remain here and who will return to the game?")
            print(forfeit_tokens)
            forfeit_challenge = input("Will anyone forfeit this challenge for 2 tokens? If yes, put their name. If no, put no.")
            if forfeit_challenge != "no":
                forfeit_tokens[forfeit_challenge] += 2
                for competes in isle_of_lost_souls:
                    if competes != forfeit_challenge:
                        red_winner = competes
            else:
                red_winner = random.choice(isle_of_lost_souls)
            print("Congratulations,", red_winner, "you are back in this game.")
            adv_opp = random.choice(advantages)
            print(red_winner, "comes with a", adv_opp, "that they must give to someone on their new tribe.")
            if adv_opp == "The Will It":
                willit = random.choice(willops)
                print("The note is for", willit + ".")
            isle_of_lost_souls.remove(red_winner)
            game_return = random.choice(tribes)
            if game_return == og_tribe1_name:
                og_tribe1.append(red_winner)
            elif game_return == og_tribe2_name:
                og_tribe2.append(red_winner)
            tokens[red_winner] = forfeit_tokens[red_winner]
            del forfeit_tokens[red_winner]

def isle_souls_jury_phase():
        global bootlist
        if len(isle_of_lost_souls) == 3:
            print("Welcome to the Island of Lost Souls.")
            print(isle_of_lost_souls)
            print(forfeit_tokens)
            forfeit_vote = input("Did anyone forfeit their vote? Type their name if they did or no if no one did.")
            if forfeit_vote != "no":
                forfeit_tokens[forfeit_vote] += 1
            voters = int(input("How many people are voting?"))

            tallies = []
            vote_freq = {}

            for votes in range(voters):
                vote = input("Write the name of the person you will vote out.")
                tallies.append(vote)

            for choices in tallies:
                if vote_freq.get(choices) == None:
                    vote_freq[choices] = 1
                else:
                    vote_freq[choices] += 1

            print(tallies)
            print(vote_freq)

            p_bootee_isle_souls = max(vote_freq, key=vote_freq.get)
            isle_of_lost_souls.remove(p_bootee_isle_souls)

            print(p_bootee_isle_souls + ",", "the tribe has spoken.")
            jury.append(p_bootee_isle_souls)
            bootlist.append(p_bootee_isle_souls)
            del forfeit_tokens[p_bootee_isle_souls]

            print(isle_of_lost_souls)
            print("And now, the ultimate test. Who will remain here and who will return to the game?")
            print(forfeit_tokens)
            forfeit_challenge = input("Will anyone forfeit this challenge for 2 tokens? If yes, put their name. If no, put no.")
            if forfeit_challenge != "no":
                forfeit_tokens[forfeit_challenge] += 2
                for competes in isle_of_lost_souls:
                    if competes != forfeit_challenge:
                        red_winner = competes
            else:
                red_winner = random.choice(isle_of_lost_souls)
            print("Congratulations,", red_winner, "you are back in this game.")
            adv_opp = random.choice(advantages)
            print(red_winner, "comes with a", adv_opp, "that they must give to someone on their new tribe.")
            isle_of_lost_souls.remove(red_winner)
            merged_tribe.append(red_winner)
            tokens[red_winner] = forfeit_tokens[red_winner]
            del forfeit_tokens[red_winner]
            return
def finale():
    print("Finalists:", str(merged_tribe))
    print("The Jury:", str(jury))
    voters = int(input("How many people are voting?"))
    tallies = []
    vote_freq = {}
    for votes in range(voters):
        vote = input("Write the name of the person you will vote to win.")
        tallies.append(vote)
    for choices in tallies:
        if vote_freq.get(choices) == None:
            vote_freq[choices] = 1
        else:
            vote_freq[choices] += 1
    print(tallies)
    print(vote_freq)
    p_winner = max(vote_freq, key=vote_freq.get)
    print("The winner of Survivor: Island of Lost Souls,", p_winner)
    return
while True:
    pre_merge()
    isle_of_lost_souls_voting()
    swapping = input("Would you like a tribe swap? 'Specifically type 'yes' or 'no'")
    if swapping == "yes":
        swap()
    elif swapping == "no":
        merging = input("Would you like to merge? 'Specifically type 'yes' or 'no' ")
        if merging == "yes":
            merged_tribe = og_tribe1 + og_tribe2
            merged_tribe_name = input("What is the merged tribe's name?")
            break
while True:
    merge()
    end = input("Island of Lost Souls End? 'Specifically type 'yes' or 'no' ")
    if end == "yes":
        break
    else:
        isle_souls_jury_phase()
while True:
    for remaining in isle_of_lost_souls:
        jury.append(remaining)
        bootlist.append(remaining)
        isle_of_lost_souls.remove(remaining)
    official_end = input("Finale time? 'Specifically type 'yes' or 'no' ")
    if official_end == "yes":
        break
    else:
        new_merge()
finale()
boot_list()
