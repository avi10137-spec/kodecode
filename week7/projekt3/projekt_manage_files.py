tasks="1|pending|learn python\n2|done|exisrise 1\n3|pending|final project"
def load_tasks(filename):
    listi=[]
    try:
        with open(filename,"r")as file:
            for l in file:
                l=l.strip().split("|")
                listi.append({"id":l[0],"status":l[1],"description":l[2]})

    except FileNotFoundError:
        print("file not exist")
    return listi
def save_tasks(filename, tasks):
    try:
        with open(filename,"w")as fil:
            tasks=tasks.split("\n")
            for item in tasks:
                fil.write(f"{item}\n")
    except FileNotFoundError:
        print("file not exist")
# save_tasks("tasks.txt",tasks)
def add_task(filename,description):
    try:
        with open(filename,"r+")as fil:
            lines=fil.readlines()
            last_line=len(lines)
            fil.write(f"{int(last_line)+1}|pending|{description}\n")
    except FileNotFoundError:
        print("file not exist")

# add_task("tasks.txt","good job")
def complete_task(filename, task_id):
    try:
        new_file=[]
        with open(filename,"r+")as fil:

            lines=fil.readlines()
            booli=False
            for line in lines:
                line = line.strip().split("|")
                if int(line[0]) == task_id:
                   line[1]="done"
                   booli=True
                new_file.append("|".join(line)+"\n")
            if not booli:
                print(f"the {task_id} not exist")
            with open(filename,"w")as fil:
                fil.writelines(new_file)
    except FileNotFoundError:
        print("file not exsist")
# complete_task("tasks.txt",3)
def list_tasks(filename):
    try:
        with open(filename,"r")as fil:
            lines = fil.readlines()
            print(len(lines))
            if len(lines) ==1:
                print([])
            else:
                for line in lines:
                    line = line.strip().split("|")
                    if line[1] == "done":
                        print(f"{" ".join(line)}[✔️]")
                    else:
                        print(f"{" ".join(line)}[]")
    except FileNotFoundError:
        print("file not exist")
# list_tasks("tasks.txt")
def main():
    filename = "tasks.txt"
    while True:
        print("\n=== to do list manager ====")
        print("1. sow tasks")
        print("2.add task")
        print("mark on make")
        print("4. exit")
        choise=input("enter your choise :")
        if choise == "1":
            list_tasks(filename)
        elif choise =="2":
            desc=input("enter description")
            add_task(filename,desc)
            print("the task add in sec")
        elif choise =="3":
            task_id=int(input("number task"))
            complete_task(filename,task_id)
        elif choise =="4":
            print("good by")
            break
        else:
            print("yor chois is invalid")

if __name__ == '__main__':
    main()












