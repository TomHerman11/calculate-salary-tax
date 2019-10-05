# The following calculation was made following the information supplied here:
# Validity date of rates: October 5th, 2019.
# - https://www.kolzchut.org.il/he/%D7%9E%D7%93%D7%A8%D7%92%D7%95%D7%AA_%D7%9E%D7%A1_%D7%94%D7%9B%D7%A0%D7%A1%D7%94
# - https://www.kolzchut.org.il/he/%D7%93%D7%9E%D7%99_%D7%91%D7%99%D7%98%D7%95%D7%97_%D7%9C%D7%90%D7%95%D7%9E%D7%99_%D7%9C%D7%A2%D7%95%D7%91%D7%93_%D7%A9%D7%9B%D7%99%D7%A8

# define GLOBALS:
INCOME_TAX_RATES = [0.1, 0.14, 0.2, 0.31, 0.35, 0.47, 0.5]
INCOME_TAX_LIMITS = [[0, 6310], [6311, 9050], [9051, 14530], [14531, 20200], [20201, 42030], [42031, 54130], [54130, 1000000]]
TAX_POINTS = 2.25  # deduction from income tax. Israeli citizen is entitled to have 2.25 Tax Points
TAX_POINT_VALUE = 218  # worth of one tax point FOR A MONTH, by: https://www.kolzchut.org.il/he/%D7%9E%D7%A1_%D7%94%D7%9B%D7%A0%D7%A1%D7%94


def calculate_and_print_income_tax_brackets_and_total(initial_salary):
    # brackets are in precentage. e.g. 10% == 0.1

    # can use binary search to find the max bracket for the salary
    # fix size of brackets - 7. will go over brackets by iterations.
    max_bracket_level = 0
    while INCOME_TAX_LIMITS[max_bracket_level][1] <= initial_salary:
        max_bracket_level += 1

    # start calculate tax amounts:
    i = 0
    cur_level_tax = 0
    total_tax = 0

    print("***** INCOME TAX ******")
    while i <= max_bracket_level:
        if i < max_bracket_level:
            cur_level_tax = INCOME_TAX_RATES[i] * INCOME_TAX_LIMITS[i][1]
        else:  # calculate for the last bracket of tax:
            cur_level_tax = INCOME_TAX_RATES[i] * (initial_salary - INCOME_TAX_LIMITS[i][0])

        print("Income Tax Brackets:", INCOME_TAX_LIMITS[i], "Income Tax Rate:", INCOME_TAX_RATES[i], "Amount deducted:", cur_level_tax)
        total_tax += cur_level_tax
        i += 1

    # reduce tax points value from total tax:
    print("Substract from Income tax the following Tax Points value:", TAX_POINTS * TAX_POINT_VALUE)
    total_tax -= (TAX_POINTS * TAX_POINT_VALUE)

    print("Total Income Tax deducted:", total_tax)
    print("")
    return total_tax


# define GLOBALS:
SOCIAL_SECURITY_TAX_RATES = [0.004, 0.07]
HEALTH_TAX_RATES = [0.031, 0.05]
SOCIAL_SECURITY_AND_HEALTH_TAX_LIMITS = [[0, 6146], [6147, 43890]]


def calculate_and_print_social_security_and_health_tax_brackets_and_total(initial_salary):
    # social secutiry and health tax apply for maximum income of SOCIAL_SECURITY_AND_HEALTH_TAX_LIMITS[1][1].
    taxable_salary = initial_salary if (initial_salary <= SOCIAL_SECURITY_AND_HEALTH_TAX_LIMITS[1][1]) else (SOCIAL_SECURITY_AND_HEALTH_TAX_LIMITS[1][1])

    max_bracket_level = 0
    if SOCIAL_SECURITY_AND_HEALTH_TAX_LIMITS[max_bracket_level][1] <= taxable_salary:
        max_bracket_level = 1

    # start calculate tax amounts:
    i = 0
    cur_health_level_tax = 0
    cur_social_security_level_tax = 0

    health_total_tax = 0
    social_securiy_total_tax = 0

    print("***** SOCIAL SECURITY AND HEALTH TAX ******")
    while i <= max_bracket_level:
        if i < max_bracket_level:
            cur_health_level_tax = HEALTH_TAX_RATES[i] * SOCIAL_SECURITY_AND_HEALTH_TAX_LIMITS[i][1]
            cur_social_security_level_tax = SOCIAL_SECURITY_TAX_RATES[i] * SOCIAL_SECURITY_AND_HEALTH_TAX_LIMITS[i][1]
        else:  # calculate for the last brackets of tax:
            cur_health_level_tax = HEALTH_TAX_RATES[i] * (taxable_salary - SOCIAL_SECURITY_AND_HEALTH_TAX_LIMITS[i][0])
            cur_social_security_level_tax = SOCIAL_SECURITY_TAX_RATES[i] * (taxable_salary - SOCIAL_SECURITY_AND_HEALTH_TAX_LIMITS[i][0])

        print("Social Security and Health Brackets:", SOCIAL_SECURITY_AND_HEALTH_TAX_LIMITS[i])
        print("    - Health Tax Rate:", SOCIAL_SECURITY_TAX_RATES[i], "Amount deducted:", cur_health_level_tax)
        print("    - Social Security Tax Rate:", HEALTH_TAX_RATES[i], "Amount deducted:", cur_social_security_level_tax)
        print("")
        health_total_tax += cur_health_level_tax
        social_securiy_total_tax += cur_social_security_level_tax
        i += 1

    total_tax = health_total_tax + social_securiy_total_tax
    print("Total Social Security and Health Tax deducted:", total_tax)
    print("    - Total Health Tax deducted:", health_total_tax)
    print("    - Total Social Security Tax deducted:", social_securiy_total_tax)
    print("")
    return total_tax


def main():
    initial_salary = int(input("Please enter your *monthly* gross salary: "))
    total_tax = 0
    total_tax += calculate_and_print_income_tax_brackets_and_total(initial_salary)
    total_tax += calculate_and_print_social_security_and_health_tax_brackets_and_total(initial_salary)

    net_salary = initial_salary - total_tax
    net_salary_precentage = (net_salary * 100) / initial_salary

    print("Toal tax deducted:", total_tax)
    print("Net Income is:", initial_salary - total_tax, "Precentage of Gross Income:", str(net_salary_precentage)+"%")


# call main function with cli command: "py main.py":
if __name__ == "__main__":
    main()
