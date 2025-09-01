todo_list: list[str] = []

def add_item() -> None:
    item_to_add: str = input("Enter the task you would like to add: ")
    item: str = str(len(todo_list)) + " - " + item_to_add
    todo_list.append(item)

def delete_item() -> None:
    active: bool = True

    while (active == True):
        item_to_delete: int = int(input("Please enter the index of the item you would like to delete: "))
        try:
            todo_list.pop(item_to_delete)
            active = False
        except IndexError:
            print("Whoops! Couldn't find that item.")

def main() -> None:
    running: bool = True

    while running == True:
        print("1. Add item to list")
        print("2. Delete item from list")
        print("3. Show list")
        print("4. Exit program")

        action = int(input("Enter the action you would like to perform: "))

        match action:
            case 1:
                add_item()
            case 2:
                delete_item()
            case 3:
                print(todo_list)
            case 4:
                running = False
            case _:
                print("Whoops! Invalid input.")

if __name__ == "__main__":
    main()