import art

def print_name_in_style(name, style):
    print(art.text2art(name, style))

def main():
    name = input("Enter your name: ")
    while True:
        print("\n1. Block style")
        print("2. Lean style")
        print("3. Universe style")
        print("4. Thinkertoy style")
        print("5. Exit")
        choice = int(input("\nEnter your choice: "))
        if choice == 1:
            print_name_in_style(name, "block")
        elif choice == 2:
            print_name_in_style(name, "lean")
        elif choice == 3:
            print_name_in_style(name, "universe")
        elif choice == 4:
            print_name_in_style(name, "thinkertoy")
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 5.")

if __name__ == "__main__":
    main()
