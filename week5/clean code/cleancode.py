# 1.
# def mens_is_exept(origin_list):
#     names_of_exept = []
#     for men in origin_list:
#         if men[1] >= 18 and men[2] == "True":
#             names_of_exept.append(men[0])
#     return names_of_exept

# list_mens_with_age_and_stat= [
#     ["Dan", 25, "True"],
#     ["Noa", 16, "True"],
#     ["Yael", 30, "False"],
# ]

# print(mens_is_exept(list_mens_with_age_and_stat))
# 2.
# def chak_imail(user_email):
#     if not user_email:
#         print("Invalid user")
#         return None


# def chak_quantity(quantity, stock):
#     if quantity <= 0 or quantity > stock:
#         print("Invalid quantity")
#         return None


# def chak_discount_according_quantity(quantity, product_price):
#     price = product_price * quantity
#     if quantity >= 10:
#         price *= 0.9
#     if quantity >= 50:
#         price *= 0.8
#     return price


# def handle_purchase(user_email, product_name, product_price, stock, quantity):
#     chak_imail(user_email)
#     chak_quantity(quantity, stock)

#     price = chak_discount_according_quantity(quantity, product_price)

#     stock -= quantity

#     order_user = user_email
#     order_product = product_name
#     order_quantity = quantity
#     order_total = price
#     order_status = "confirmed"
#     print(f"Order {order_status}: {order_user} bought {order_quantity} of {order_product} for ${order_total}")
#     return order_user, order_product, order_quantity, order_total, order_status


# handle_purchase("avi10137", "apple",10 , 30, 10)
# 3.
# validation
def is_valid(new_name,new_grade):
    if not new_name or len(new_name) < 2:
        print("Error: invalid name")
        return False
    if new_grade < 0 or new_grade > 100:
        print("Error: grade must be 0-100")
        return False
    return True
    # add student
def add_student(grades,new_grade):
    grades.append(new_grade)
    return grades

          # calculate stats
def calculate_stat(grades):
    total = sum(grades)
    average = total / len(grades)
    top_count = sum(1 for g in grades if g >= 90)
    failing_count = sum(1 for g in grades if g < 56)
    return total,average,top_count,failing_count
# print report
def printer(nanes,grades,average,top_count,failing_count):
    print("=== Student Report ===")
    for i in range(len(names)):
        print(f"  {names[i]}: {grades[i]}")
    print(f"Average: {average:.1f}")
    print(f"Top students: {top_count}")
    print(f"Failing: {failing_count}")
    # save to file
def save_to_file(names,grades):
    with open("students.txt", "w") as f:
        for i in range(len(names)):
            f.write(f"{names[i]},{grades[i]}\n")

    return names, grades






     
        
def manage_students(names, grades, new_name, new_grade):
    is_valid(new_name,new_grade)
    add_student(new_grade,grades)
    calculate_stat(grades)
    printer(calculate_stat)
    save_to_file(names,grades)
manage_students(["avi","yosi"],[80,90],"kobi",55)



    


    

    
    

  
  

    
    

    
    
manage_students(["avi","yosi"],[80,90],"kobi",70)

    
# 4.
# def chak_validition(name,email):
#     if not name or len(name) < 2:
#         raise ValueError("Invalid name")
#     if "@" not in email:
#         raise ValueError("Invalid email")
# def create_new_user(name, email):
#     chak_validition(name,email)
#     return name, email, "admin", "2024-01-01", True
# 5.


