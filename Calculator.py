import tkinter as tk

class Calculator:

    #Initialize the application
    def __init__(self, root):
        self.root = root #Store the root window reference
        self.root.title("Simple Calculator") #Title
        self.root.geometry("400x500") #Set window size (wxh)
        self.root.resizable(False, False) #Make width and height non resizable
        
         # Initialize the current input (what the user is typing) as empty string
        self.current_input = "" 

        # Initialize the total expression (complete calculation) as empty string
        self.total_expression = ""
        
        # Create display
        self.display = tk.Label(root, #Place in root window
                                text="", #Start with empty text
                                anchor="e", #Right-align text
                                bg="lightgray", #Background
                                font=("Arial", 24), #Font
                                padx=20, #Padding
                                pady=60)
        #Pack the display to fill the available horizontal space
        self.display.pack(fill="x")
        
        #Create buttons in order top to bottom
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '.', '+',
            '='
        ]
        
        #Create a frame for the buttons
        button_frame = tk.Frame(root)

        #Pack the frame to fill available space
        button_frame.pack(expand=True, fill="both")
        
        #Loops through all the buttons and creates them
        for i, text in enumerate(buttons):

            #Create a button with the current text
            btn = tk.Button(button_frame, #Positioned in button frame
                            text=text, #Button text
                            font=("Arial", 14), #Font
                           command=lambda t=text: self.button_click(t)) #When clicked, call button_click with the button's text
            #This part basically helps position the buttons in the calculator
            if text == '=':  # Make equals button wider
                btn.grid(row=4, #Positioned at row 4
                         column=0, #Positioned at column 0, spanning all four columns
                         columnspan=4, 
                         sticky="nsew")
            else: #For the rest of the buttons, sort them using this calculation
                #For example: if we choose '1', i=8, meaning row=2 and column=0
                #Choosing '7' means i=0, meaning row=0 and column=0
                btn.grid(row=i//4, 
                         column=i%4, 
                         sticky="nsew")
            
            # Configure grid weights, making rows and columns expand to fit the screen
            button_frame.grid_rowconfigure(i//4, weight=1)
            button_frame.grid_columnconfigure(i%4, weight=1)
    

    #Handles button clicks
    def button_click(self, value):
        if value == "C": #If C is clicked, clear the calculator
            self.current_input = ""
            self.total_expression = ""
        elif value == "=": #If '=' is clicked
            try:
                #Calculate the result by evaluating total and current expression
                self.current_input = str(eval(self.total_expression + self.current_input))
                self.total_expression = "" # Clear calculation
            except:
                self.current_input = "Error"
        elif value in "+-*/":
            # Add current input and operator to expression
            self.total_expression += self.current_input + value
            self.current_input = ""
        else:
            # Add the pressed digit/decimal to current input
            self.current_input += value
        
        # Update the display with either current input or total expression
        self.display.config(text=self.current_input or self.total_expression)


# Main program entry point
if __name__ == "__main__": 
    root = tk.Tk() #Create the main window
    app = Calculator(root) #Create calculator instance
    root.mainloop() #Start the GUI event loop
    


