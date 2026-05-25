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
    with open(filename,"w")as fil:
        tasks=tasks.split("\n")
        for item in tasks:
            fil.write(f"{item}\n")
save_tasks("tasks.txt",tasks)
def add_task(filename,description):
    with open(filename,"r+")as fil:
        lines=fil.readlines()
        last_line=lines[-1][0]
        fil.write(f"{int(last_line)+1}|pending|{description}")

add_task("tasks.txt","good job")
def complete_task(filename, task_id):
    with open(filename,"r+")as fil:
        for line in fil:
            line = line.strip().split("|")
            if int(line[0]) == task_id:
                line[1]="done"
complete_task("tasks.txt",2)






