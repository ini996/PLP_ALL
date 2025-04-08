def read_and_modify_file():
    
    filename = input("Enter the filename you want to read: ")
    try:
        with open(filename, 'r') as file:
            content = file.read()

        modified_content = content.upper()
        output_filename = 'modified_' + filename

        with open(output_filename, 'w') as new_file:
            new_file.write(modified_content)

        print (f"Modified content save to '{output_filename}'.")
        
    except FileNotFoundError:
        print("The file was not found")
    except PermissionError:
        print ("You don't have permission to access this file")
    except Exception as e:
        print(f"An unexpected error: {e}")

#run the function
read_and_modify_file()
