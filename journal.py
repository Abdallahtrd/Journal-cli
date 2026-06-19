
def entry_cumulator():
    entry_cumulator_collector = ""
    entry = input("You can write here... " + '\n')

    entry_cumulator_collector = entry
    return entry_cumulator_collector 

def entry_writting(entry_cumulator_collector):
    with open("entries.txt",'a') as file:
        file.write(entry_cumulator_collector + '\n') 

def view_entry_history():
    with open("entries.txt", 'r') as file:
        entry_history = file.read()
        print(entry_history)

def main():
    
    print("Hey There welcome... Don't be shy to talk (I don't judge)")
    
    temp_entry = entry_cumulator()
    entry_writting(temp_entry)
    


    

while True:
    run_choice = input("Would you like to Write(W), close(C), or view your past entry(E)? ").lower()
    if run_choice == 'w':
        main()
        
    elif run_choice == 'e':
        view_entry_history()

    elif run_choice == 'c':
        break
    else:
        print("Please Pick a choice")
