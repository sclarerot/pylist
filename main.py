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

def show_list() -> None:
    print(todo_list)

def main() -> None:

if __name__ == "__main__":
    main()