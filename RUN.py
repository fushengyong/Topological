import sys

def main():
    print("""
    1.Run CLI - Command Line Interface
    2.Run GUI - Graphical User Interface
    3.Help - Display Help Documentation
    4.Exit - Quit Application
    """)
    key = input("Selection: ")
    if key == '1':
        print("\nCLI Launched")
        from CLI import switch
    elif key == '2':
        print("\nGUI Launched")
        from GUI import app
    elif key == '3':
        print("\nHelp Documentation:")
        print(help())
    elif key == '4':
        print("\nGoodbye") 
        sys.exit()
        key = None
    else:
        print("\nNot Valid Choice Try again")
    main()

def help():
    return("""
    View the most up-to-date documentation online at 
    https://github.com/KaiGH/Topological
    For offline users, a readme is distributed with this 
    program and should be within the application directory. 
    Additional help is available within the GUI, such as 
    Tool Tips which are displayed when hovering over buttons. 
    """)

if __name__ == "__main__":
    main()
