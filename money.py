def add_expense(category: str, amount: float):
    with open("./ATLA/expense.txt", "a") as file:
        file.write(f"{category}:{amount}\n")



def load_expenses() -> list[tuple[str, float]]:
    with open("./ATLA/expense.txt", "r") as file:
        the_List = []
        for line in file: 
            category, amount = line.replace("\n", "").split(":")
            the_List = category = amount 
        return the_List

add_expense("coffee", 15)

        
