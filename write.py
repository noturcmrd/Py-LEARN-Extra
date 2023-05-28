

with open("data.txt", mode="w", encoding="utf-8") as file:
    file.write("Hello, World1")

with open("data.txt", mode="a", encoding="utf-8") as file:
    file.write("Hello, World2")
with open("data.txt", mode="r+", encoding="utf-8") as file:
    file.write("Hello, World3")
    data = file.read()
    print(data)

