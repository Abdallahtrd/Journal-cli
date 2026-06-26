
def entry_cumulator(): # COLLECTS INPUT FROM USER
    entry_cumulator_collector = "" # ASSIGNS USER'S ENTRY TO COLLECTOR
    entry = input("You can write here... " + '\n') 

    entry_cumulator_collector = entry # ASSIGNS COLLECED INPUT TO THE CUMULATOR
    return entry_cumulator_collector # RETURNS THE ACCUMULATED INPUT

def entry_writting(entry_cumulator_collector): # OPENS AND APPENDS INPUT TO FILE
    with open("entries.txt",'a') as file:
        file.write(entry_cumulator_collector + '\n') 

def view_entry_history(): # ALLOWS USER TO VIEW PREVIOUS ENTRIES
    with open("entries.txt", 'r') as file:
        entry_history = file.read()
        print(entry_history)

def main(): # CALLS FUNCTIONS
    
    print("Hey There welcome... Don't be shy to talk (I don't judge)")
    
    temp_entry = entry_cumulator() # THIS CALLS AND STORES THE CUMULATORS RESULT
    entry_writting(temp_entry) # THIS CALLS THE FUNCTION THAT APPENDS THE ENTRY FROM THE CUMULATOR
    


    

while True: # THIS LOOP KEEPS THE WHOLE PROGRAM RUNNING
    run_choice = input("Would you like to Write(W), close(C), or view your past entry(E)? ").lower()
    if run_choice == 'w': # CALLS MAIN IF CHOICE IS W 
        main()
        
    elif run_choice == 'e': # CALLS VIEW PAST ENTRY FUNCTION WHEN CHOICE IS E 
        view_entry_history()

    elif run_choice == 'c':# CLOSES THE PROGRAM IF CHOICE IS
        break
    else:
        print("Please Pick a choice")
