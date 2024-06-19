from auth import Auth
from exam import Exam

def main():
    auth = Auth()
    exam = Exam()

    while True:
        print("\nWelcome to the Exam Portal")
        print("1. Register")
        print("2. Login")
        print("3. Create Exam")
        print("4. Take Exam")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            auth.register()
        elif choice == '2':
            auth.login()
        elif choice == '3':
            exam.create_exam()
        elif choice == '4':
            exam.take_exam()
        elif choice == '5':
            print("Thank you for using the Exam Portal!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
