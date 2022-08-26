import re #need this to strip non alphabetical characters

def main():
    sorted = False
    while True:
        choice = input("Welcome to the word occurrences program, enter what you would like to do: ")
        if choice.upper() == "COUNT":
            try:
                filename = input("\nEnter the name of the text file you would like to count (case sensitive): ")
                f = open(filename+".txt","r") #opens the file with the name the user entered, then reads the data and closes it.
                data = f.read()
                f.close()
                word_counts = count_words(data) #gets a list of [the words, their counts].
                sorted_list = sort_words(word_counts) #sorts the list of [the words, their counts].
                sorted = True
                print("Counting complete, returning to main menu...\n")
            except:
                print("This file does not exist, returning to main menu...\n")

        elif choice.upper() == "DISPLAY":
            if sorted:
                display_sorted(sorted_list) #displays the sorted list to the user.
                print("Display complete, returning to main menu...\n")
            else:
                print("You have not counted a file yet, returning to main menu...\n")

        elif choice.upper() == "SAVE":
            if sorted:
                save_to_file(sorted_list,filename) #saves the sorted list to a file.
                print("File has been written to, returning to main menu...\n")
            else:
                print("You have not counted a file yet, returning to main menu...\n")

        elif choice.upper() == "EXIT":
            print("Now exiting the program...\n")
            break #breaks out of the loop to exit.

        elif choice.upper() == "HELP":
            print("Your available options are:\n- COUNT: Count the number of unique word occurences in a text file. Must be run before DISPLAY or SAVE.\n- DISPLAY: Display each unique word in order of occurence. Can only be used after a file has been counted.\n- SAVE: Save the data of unique word occurences to a seperate text file. Can only be used after a file has been counted.\n- EXIT: Exits from the program.\n- HELP: Displays this menu.\n")

        else:
            print("That is not a valid option. For a list of options, enter 'HELP'.\n")

def count_words(text):
    text = text.strip()
    text = re.sub("[^a-zA-Z ]+","",text) #substitutes characters in the text which aren't a-z, A-Z, or a space, with nothing. borrowed from the internet.
    text = text.split()
    words = [] #contains a list of each unique word.
    counts = [] #contains a list of numbers which correspond to each unique word.
    for word in text:
        word=word.lower() #this is to make it so capitalisation is irrelevant.
        if word in words:
            index = words.index(word)
            counts[index] = counts[index]+1 #if the word is already in the words list, increase the count for that word by 1.
        else:
            words.append(word)
            counts.append(1) #if the word is not in the words list, append it to it and create a count of '1' for its first occurence.
    word_counts = [words,counts]
    return word_counts

def sort_words(unsorted_list):
    words = unsorted_list[0]
    counts = unsorted_list[1]
    for i in range(len(words)): #bubble sort implementation using the counts list, but when counts are swapped the corresponding words are swapped in the same indexes.
        for j in range(len(words)-1):
            if counts[j] < counts[j+1]:
                counts[j], counts[j+1] = counts[j+1], counts[j] #swap the counts around so the larger one comes first.
                words[j], words[j+1] = words[j+1], words[j] #swap the words around so the more common one comes first.
    sorted_list = [words,counts]
    return sorted_list

def display_sorted(sorted_list):
    words = sorted_list[0]
    counts = sorted_list[1]
    for i in range(len(words)): #iterates through the list and prints each word and its count.
        print(f"{words[i]}: Occurred {counts[i]} times.")

def save_to_file(sorted_list,filename):
    words = sorted_list[0]
    counts = sorted_list[1]
    f = open(filename+"_WO.txt","w")
    for i in range(len(words)): #iterates through the list and saves each word and its count.
        f.write(words[i]+": "+str(counts[i])+"\n")
    f.close()

main()
