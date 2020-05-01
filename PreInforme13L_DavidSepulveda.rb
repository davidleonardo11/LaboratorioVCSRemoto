canasta = {}
more = 'Si'
while more == 'Si'
    item = 'Introduce un artículo: ' + gets()
    name = gets()
    precio = puts 'Introduce el precio de ' , name , ': '
    pre=  gets()
    pr= puts name + pre
    canasta[name] = pre
end
