with open("dairy.txt","w",encoding="utf-8")as f:
    f.write("15-01-2024: was day buzi \n16-01-2024: learn on files at python \n17-01-2024: complet my first file")
    print("dairy make in succsefuli ")
with open("dairy.txt","r")as f:
    file1=f.read()
    print(file1)
# חלק ב
def add_entry(filename, date, content):
    with open(filename,"a",encoding="utf8") as file:
        file.write(f"{date}:{content}")
add_entry("dairy.txt","\n18-01-2024: ","wonderful day")
def search_diary(filename, keyword):
    list_of_lines=[]
    with open(filename,"r")as file:
        for line in file:
            if keyword in line:
                list_of_lines.append(line.strip())
        print(list_of_lines)
# בונוס
def safe_read_diary(filename):
    try:
        with open(filename,"r")as file:
            file.read()
    except FileNotFoundError:
        print("file not exist")