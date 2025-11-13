# 
# TASK 1
# 
def total_salary(path):
    try:
        with open(path, "r", encoding="UTF-8") as developer:
            salary_list = developer.readlines()
            total_sum = 0
            avg_salary = 0
            for sal_str in salary_list:
                salary = float(sal_str.strip().split(",")[1])
                total_sum = total_sum + salary
            avg_salary = f"{total_sum / len(salary_list):.2f}"
            return (total_sum, avg_salary)
    except FileNotFoundError:
        print(f"Error: File not found at {path}")

# 
# TASK 2
# 
def get_cats_info(path):
    try:
        with open(path, "r", encoding="UTF-8") as cats:
            cats_list = cats.readlines()
            cats_list_result = []
            for cat_str in cats_list:
                cat_list = cat_str.strip().split(",")
                cat = {
                    "id": cat_list[0],
                    "name": cat_list[1],
                    "age": cat_list[2]
                }
                cats_list_result.append(cat)
            return cats_list_result

    except FileNotFoundError:
        print(f"Error: File not found at {path}")