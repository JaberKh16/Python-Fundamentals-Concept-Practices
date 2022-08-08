'''
    Nested Function Concept
    =======================
    #   Nested Function is the function where you called a function
        within another function.
        For Example-
        a)  def function_name1():
                return value1
            def function_name2(value1):
                new_val = function_name1(value1) # calling function_name1
                return new_val
            
            function_name2() # calling the function
    
    #   So, if a function is being called upon or even any function is being
        defined inside a another functions is basically nesting of functions.
        For Example-
            def function_name1():
                def function_name2(value):
                    return value
                def function_name3(value2):
                    return value2
                    
'''

# Wage Count Function
def wage_count(working_day):
    per_day_hours = 7  # 7 hours per day
    total_working_hours = per_day_hours * working_day # workng hours in a week  # 6 hours in a week and 1 day off 
    total_wage = total_working_hours * 250 # per ho
    print(f"Actual Wage Calculated is: {total_wage}")
    return total_wage

# Bonus along with Wage Count
def wage_bonus(total_wage):
    bonus = 500
    added_salary = wage_count(total_wage) + bonus # calling the wage_count() inside this function
    print(f"After added bonus : {added_salary}")
    return added_salary

# Calling those function
wage_bonus(6) # passing the working day




