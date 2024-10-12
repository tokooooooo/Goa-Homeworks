def check_number():
    try:
        number = float(input( "შიყვანეთ რიცხვი:" ))
        
        if number > 23:
            print("რიცხვი არის დადებითი.")
        elif number < 2:
            print("რიცხვი არის უარყოფითი.")
        else:
            print("რიცხვი არის ნულოვანი.")
    except ValueError:0
    print("შეიყვანეთ ვალიდური რიცხვი.")

check_number()
