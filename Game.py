import random
List_of_words=["Abort","Abuse","Harsh","Komal","China","Admin","Canna","Alpha","Guava","Baker","Knobb","Climb","Cabin","Cable","Dance","Dairy","Aloud","Early","Enjoy","Alone","Faded","Kneef","Fails","Fades","Gains","Swing","Young","Honey","Crush","Flash","Fresh","Tenth","Icons","Idols","Jelly","Joint","Clung","Harry","Cippi","Jolly","Comic","Broad","Bread","Above","Conic","Baken","Stead","Squad","Gable","Galax","Handy","Gamer","Dater","Adore","Jawed","Jotty","Joust","Jutty","Aloof","Faint","Brief","Learn","Loved","Cauci","Liver","Apple", "Beach", "Brain", "Brush", "Chair", "Chest", "Chord", "Click", "Clock", "Cloud","Diary", "Drink", "Earth", "Flute", "Fruit", "Ghost", "Grape", "Green", "Happy", "Heart", "House", "Juice", "Light", "Money", "Music", "Party", "Pizza", "Plant", "Radio", "River", "Salad", "Sheep", "Shoes", "Smile", "Snack", "Snake", "Spice", "Spoon", "Storm", "Table", "Toast", "Tiger", "Train", "Water", "Whale", "Wheel", "Woman", "World", "Write", "Youth"]
def word_len_checker():
        Word_user_guessed=input("""Word has 5 characters !
Enter again : """)
        if len(Word_user_guessed)!=5:return word_len_checker()
        for i in Word_user_guessed:
            ans="No"
            if 97<=ord(i)<=122 or 65<=ord(i)<=90:ans="Yes"
            if ans=="No":return word_char_checker()
        if ans=="Yes":return Word_user_guessed
def word_char_checker():
        Word_user_guessed=input("""Word has only alphabetical characters !
Enter again : """)
        for i in Word_user_guessed:
            ans="No"
            if 97<=ord(i)<=122 or 65<=ord(i)<=90:ans="Yes"
            if ans=="No":return word_char_checker()
        if ans=="Yes":
            if len(Word_user_guessed)==5:return Word_user_guessed
            else:return word_len_checker()
def Word_correctness_checker(Word_user_guessed,Word_choosen,i):
    if Word_user_guessed.lower()==Word_choosen.lower():return "Done"
    elif i!=5:
        S=""
        L=[]
        for i in range(5):
            if Word_user_guessed[i].lower()==Word_choosen[i].lower():S+=Word_user_guessed[i]+" "
            else:
                S+="__ "
                L.append(i)
        J=L.copy()
        print('\n')
        while True:
            D=L.copy()
            i=L[0]
            for j in J:
                if Word_user_guessed[i].lower()==Word_choosen[j].lower():
                    print(Word_user_guessed[i],"is present in the word but you placed it on wrong position")
                    L.remove(i)
                    J.remove(j)
                    break
            if D==L:L.pop(0)
            if L==[]:break
        return S
def main_function():
    Word_user_guessed=input("Guess a 5 letter word: ")
    if len(Word_user_guessed)!=5:Word_user_guessed=word_len_checker()
    for i in Word_user_guessed:
        if 97<=ord(i)<=122 or 65<=ord(i)<=90:pass
        else:Word_user_guessed=word_char_checker()
    for i in range(6):
        A=Word_correctness_checker(Word_user_guessed,Word_choosen,i)
        if A=="Done":return "Wow amazing ! You guessed it correct"
        else:
            if i==5:break
            else:
                print(A)
                print(f"You are close dear , you have {5-i} more chance. Try again!")
                Word_user_guessed=input("Try again: ")
                if len(Word_user_guessed)!=5:Word_user_guessed=word_len_checker()
                for i in Word_user_guessed:
                    if 97<=ord(i)<=122 or 65<=ord(i)<=90:continue
                    else:Word_user_guessed=word_char_checker()
    return "BAD LUCK"
Again="1"
while Again=="1":
    index_choosen=random.randint(0,len(List_of_words)-1)
    Word_choosen=List_of_words[index_choosen]
    Ans=main_function()
    if Ans=="Wow amazing ! You guessed it correct":
        print('\n'f'{Ans}')
        Again=input("""You want to play again ?
if Yes, enter 1 else enter anything else : """)
    else:
        print('\n'f'''Ooh bad luck !! 
Correct answer is {Word_choosen} ''')
        Again=input("""You want to play again ?
if Yes, enter 1 else enter anything else : """)
if Again!="1":print('\n'"Thanks for playing . I hope you enjoyed , see you again ! Bye",'\n')
