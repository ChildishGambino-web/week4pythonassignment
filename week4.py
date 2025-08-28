import os

def process_file_with_errors(input_filename: str, output_filename: str):
    """
    Reads content from a file, modifies it, and writes the result to a new file.
    
    This function includes robust error handling for common file-related issues.

    Args:
        input_filename (str): The path to the file to be read.
        output_filename (str): The path to the new file where modified content will be written.
    """
    try:
        # Step 1: Attempt to open and read the input file using a 'with' statement.
        # This is the safest way as it automatically closes the file, even if errors occur.
        with open(input_filename, 'r') as infile:
            original_content = infile.read()
        
        print(f"✅ Successfully read content from '{input_filename}'.")
        
        # Step 2: Modify the content (in this case, converting it to uppercase).
        modified_content = original_content.upper()
        
        # Step 3: Write the modified content to the new output file.
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
            
        print(f"✅ Modified content written successfully to '{output_filename}'.")
        print("---")
        print("The original content was:")
        print(original_content)
        print("\n---")
        print("The modified content is:")
        print(modified_content)
        
    # Step 4: Handle specific errors.
    # This block catches the error if the input file does not exist.
    except FileNotFoundError:
        print(f"❌ Error: The file '{input_filename}' was not found.")
        print("Please check the filename and try again.")
        
    # This block catches other I/O-related errors, such as permission issues.
    except IOError as e:
        print(f"❌ An I/O error occurred while processing the file: {e}")
        
    # The 'else' block executes only if the 'try' block completes without any exceptions.
    else:
        print("\n🎉 All operations completed successfully!")
        
    # The 'finally' block executes no matter what, whether an error occurred or not.
    # In this case, it serves to confirm the process has concluded.
    finally:
        print("\nProgram finished.")


# --- Main part of the program ---
if __name__ == "__main__":
    print("Welcome to the File Processor!")
    print("This program will read a file, convert its contents to uppercase,")
    print("and save it to a new file.")
    print("---")
    
    # Prompt the user for the filenames.
    user_input_file = input("Enter the name of the file to read (e.g., 'my_text.txt'): ")
    user_output_file = input("Enter the name for the new file (e.g., 'my_text_modified.txt'): ")
    
    # Call the function to perform the file operations.
    process_file_with_errors(user_input_file, user_output_file)
