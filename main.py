def fizz_buzz(a,b):
    result = 0
    
    for i in range(a,b+1):
        
        if i % 3 == 0 and i % 5 == 0:
            result += i
    return result
            
    


print('0-3:', fizz_buzz(0, 3))
print('0-5:', fizz_buzz(0, 5))
print('15-15:', fizz_buzz(15, 15))
print('1000-20000:', fizz_buzz(1000, 20000))

print("POINT2")

def plural_form(num,form1,form2,form3):
    list_yablok = [0,5,6,7,8,9]
    list_yablok2 = [11,12,13,14]
    list_yabloka = [2,3,4]

    if num % 10 in list_yablok:
        return form3
    
    elif num % 10 in list_yabloka:
        return form2

    elif num in list_yablok2:
        return form3
    
    elif num % 10 == 1 and num != 11:
        return form1

    
print(1, plural_form(1, 'яблоко', 'яблока', 'яблок'))
print(3, plural_form(3, 'яблоко', 'яблока', 'яблок'))
print(5, plural_form(5, 'яблоко', 'яблока', 'яблок'))
print(11, plural_form(11, 'яблоко', 'яблока', 'яблок'))
print(121, plural_form(121, 'яблоко', 'яблока', 'яблок'))
print(125, plural_form(125, 'яблоко', 'яблока', 'яблок'))


def html(*args,**kwargs):
    def decorator(func):
        def wrapper(input_value):
            result = func(input_value)
            if kwargs:
                atributes = ''
                final1 = ''
                final2 = ''
             
                for k ,v in kwargs.items():
                    atributes += f'{k}="{v}"'
                for i in args:
                    final1 = f'<{i} {atributes}> '
                    final2 = f'</{i}>'
                result = final1 + input_value + final2 
            else:
                result = f'<{args}> {input_value} </{args}>'   
            return result
        return wrapper
    return decorator


# @html('body')
@html('a', href='https://yandex.ru/')
@html('div', width=200, height=100)
def to_string(input_value):
    return str(input_value)

print(to_string("ссылка на яндекс"))





    

        
    
        


