from salesperson import Salesperson
import business_manager_functions as bsf
if __name__ == '__main__':
    s1 = Salesperson('Alessandro', 'Bardi', 1800, trade='Immobiliare')

    print(s1)
    print(s1.thirteenth_month_salary())

    print(bsf.menu())