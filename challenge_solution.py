file_name = "alpha.txt"

def get_last_tip_number():
    with open(file_name) as f:
        last_line = f.readlines()[-1]
        return int(last_line.split(")")[0])

last_tip = get_last_tip_number()
with open(file_name, "a") as f:
    new_tip_number = last_tip + 1
    f.write("\n")

    f.write(f"{new_tip_number}) This is a dynamic addition to that file, that is amazing!")
    print(f"You just wrote tip number {new_tip_number}")



