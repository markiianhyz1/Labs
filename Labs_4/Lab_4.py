a , countl_z , count_and  =  False , 0 , 0

while  a  !=  Правда :
    file  =  open ( input ( 'Введіть puth to file: ' ), 'r' )
    count_lines  =  файл . readlines ()
    empty_lines  = [ рядок  за  рядком  у  count_lines  if  line  ==  ' \n ' ]
    z_lines  = [ рядок  за  рядком  у  count_lines  , якщо  'z'  у  рядку ]
    count_z  =  len ( z_lines )
    count_z_lines  = [ рядок  за  рядком  у  count_lines  для  z  у  рядку  , якщо  z  ==  'z' ]
    and_lines  = [ рядок  за  рядком  у  count_lines ]
    для  line  in  and_lines :
        якщо  'і'  в  рядку : count_and  +=  1
    print ( f'загальна кількість рядків: { len ( count_lines ) } \n порожні рядки: { len ( порожні_рядки ) } \n ' )
    print ( f'рядки з "z": { count_z } \n ' )
    print ( f'"z" count": { len ( count_z_lines ) } \n рядки з "and": { count_and } \n ' )

    key  =  str ( input ( 'Exit(x) | Analize new file(f) \n Enter char:' ))
    a  =  True  , якщо  ключ  ==  'x'  else  False  , якщо  ключ  ==  'y'  else  True
