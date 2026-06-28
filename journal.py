
def entry_cumulator(): # COLLECTS INPUT FROM USER  

    entry_cumulator_collector = "" # ASSIGNS USER'S ENTRY TO COLLECTOR
    
    while True:
       entry = input("You can write here... use lower case letters to type done " ) 
       if entry == 'done':
           break
       else:
            entry_cumulator_collector += '\n' + entry

    return entry_cumulator_collector


   

def entry_writting(entry_cumulator_collector,date_andtime): # OPENS AND APPENDS INPUT TO FILE
    
    with open("entries.txt",'a') as file:
        file.write(f"Date and time is: {date_andtime}\n")
        file.write(entry_cumulator_collector + '\n\n') 

def view_entry_history(): # ALLOWS USER TO VIEW PREVIOUS ENTRIES
    with open("entries.txt", 'r') as file:
        entry_history = file.read()
        print(entry_history)

def main(): # CALLS FUNCTIONS
    import datetime
    current_datetime = datetime.datetime.now()
    print("Hey There welcome... Don't be shy to talk (I don't judge)")
    
    date_andtime = str(current_datetime)
    temp_entry = entry_cumulator() # THIS CALLS AND STORES THE CUMULATORS RESULT
    entry_writting(temp_entry,date_andtime) # THIS CALLS THE FUNCTION THAT APPENDS THE ENTRY FROM THE CUMULATOR
   


    

while True: # THIS LOOP KEEPS THE WHOLE PROGRAM RUNNING
    run_choice = input("Would you like to Write(W), close(C), or view your past entry(H)? , delete past entries(E) ").lower()
    if run_choice == 'w': # CALLS MAIN IF CHOICE IS W 
        main()
        
    elif run_choice == 'h': # CALLS VIEW PAST ENTRY FUNCTION WHEN CHOICE IS E 
        view_entry_history()

    elif run_choice == 'c':# CLOSES THE PROGRAM IF CHOICE IS
        break
    elif run_choice == 'e':
        with open ("entries.txt", 'w') as file:
            pass
    else:
        print("Please Pick a choice")
