def create_grades_file(filename):
    stdents = [
        ("Dan", [85, 90, 78]),
        ("MOMO", [92, 88, 95]),
        ("Yoni", [70, 65, 80]),
        ("Avi", [100, 95, 98]),
        ("Sara", [60, 72, 68]),
    ]

    with open(filename,"w",encoding="utf-8")as file:
        for s in stdents:
            s=list(s)
            # print(s[1])
            last_s=" ".join(str(s[1]).strip("[]"))
            final=s[0].strip("[]")+", "+last_s.strip("")
            print(final)
            file.write(f"{final}\n")
create_grades_file("grade.txt")

def calculate_averages(filename):
    with open(filename,"r")as file:
        avarage={}
        lines=file.readlines()
        for line in lines:
            sumi=0
            line= line.strip().split(",")
            line1=line[1:]
            print(line1)
            for item in line1:
                sumi+=int(item.replace(" ",""))
            avarage[line[0]]=sumi/len(line1)
        return avarage
result=calculate_averages("grade.txt")
for name, avg in result.items():
    print(f'{name}: {avg:.1f}')

sorted_grades = dict(sorted(result.items(),key=lambda item: item[1],reverse=True))
for name, avg in sorted_grades.items():
    print(f'{name}: {avg:.1f}')







