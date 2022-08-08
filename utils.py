def money_output(value) -> str:
    '''
        A money printing treatment to 2 decimal places output.
            Exemples:
                Integer number: 1000 to 1000.00
                Float number with 1 decimal number after the floating point: 500.7 to 500.70
    '''

    if value == 0 or "." not in str(value):
        
        return f"{value}.00"

    elif '.' in str(value)[-2]:

        return f"{value}0"
    
    return f"{value}"

def float_treatment(value) -> float:
    '''
        A float memory treatment to round float values.
            Exemple: 
                500.96000000000000001 to 500.96
    '''

    if '.' in str(value) and len(str(value)[str(value).find('.'):]) > 3:
        
        new_value = float(str(value)[:str(value).find('.')+3])        
        
        return new_value

    return value