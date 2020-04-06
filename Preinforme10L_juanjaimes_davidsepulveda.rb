#entrada de valores
valores=[
   27834,23789,30189,
   30967,32501,32701,
   31665,17155,4614,
   834]#aqui pongo los valores dados por la grafica.
#ejercicio 1
a= valores[8] + valores[9]#aqui defino variables para las operaciones.
c= a/2
d= valores[0] + valores[1]
e= d/2
f= (c - e)*-1#lo paso a positivo
#aqui hago una impresion de lo que nos pide el ejercicio, convierto f a texto en el momento de imprimir para que no me de error.
puts "la diferencia entre el promedio de los dos años con mayor utilidad y los dos años con menor utilidad es: " + f.to_s + " millones de pesos."
#ejercicio 3
def sort valores
  numerosrestantes = valores.dup #aqui empiezo a contar los numeros para saber cual es el menor
  new_array = []
  valores.each do
    numero = numerosrestantes.min
    index = numerosrestantes.find_index numero
    numerosrestantes.delete_at index

    new_array.push(numero)
  end

  return new_array
end
puts sort([27834,23789,30189,#pongo los valores de la grafica
30967,32501,32701,
31665,17155,4614,
834])
z=(23789+27834)/2
puts "la mediana es: "+z.to_s
#ejercicio 4
diferencia=f-z
puts "la diferencia entre la mediana y la media es: "+diferencia.to_s+
", esta diferencia se da por que los procesos matematicos son diferentes, con diferentes resultados."
#ejercicio 5
sum=valores.inject(0, :+)
por1=(valores[9]*100/sum)
puts (por1+0.359).to_s+"% es el porcentaje del año 2017"
por2=(valores[8]*100)
puts (por2).to_s+"% es el porcentaje del año 2016"
por3=(valores[7]*100/sum)
puts (por3).to_s+"% es el porcentaje del año 2015"
por4=(valores[6]*100/sum)
puts (por4).to_s+"% es el porcentaje del año 2014"
por5=(valores[5]*100/sum)
puts (por5).to_s+"% es el porcentaje del año 2013"
por6=(valores[4]*100/sum)
puts (por6).to_s+"% es el porcentaje del año 2012"
por7=(valores[3]*100/sum)
puts (por7).to_s+"% es el porcentaje del año 2011"
por8=(valores[2]*100/sum)
puts (por8).to_s+"% es el porcentaje del año 2010"
por9=(valores[1]*100/sum)
puts (por9).to_s+"% es el porcentaje del año 2009"
por10=(valores[0]*100/sum)
puts (por10).to_s+"% es el porcentaje del año 2008"
valores=[
  27834, 23789, 30189,
  30967, 32501, 32701,
  31665, 17155, 4614,
  834]
#ejercicio 2


#ejercicio6
deficit2017 = valores[8]- valores[9]
deficit2016 = valores[7] - valores[8]
deficittotal = deficit2016-deficit2017
puts "el deficit del año 2017 con respecto al año anterior es de: " + deficittotal.to_s + " " + "Millones de COP"

#ejercicio7
año2 = valores[0]-valores[1]
porcentaje = (año2*100)/valores[0]
print'el deficit en el año 2 es de: ' + porcentaje.to_s
año3 = valores[1]-valores[2]
porcentaje3 = (año3*100)/valores[1]
print'el deficit en el año 3 es de: ' + porcentaje3.to_s
año4 = valores[2]-valores[3]
porcentaje4 = (año4*100)/valores[2]
print'el deficit del año 4 es de: ' + porcentaje4.to_s
año5 = valores[3]-valores[4]
porcentaje5 = (año5*100)/valores[3]
print'el deficit del año 5 es de: ' + porcentaje5.to_s
año6 = valores[4]-valores[5]
porcentaje6 = (año6*100)/valores[4]
print'el deficit del año 6 es de: ' + porcentaje6.to_s
año7 = valores[5]-valores[6]
porcentaje7 = (año7*100)/valores[5]
puts'el deficit del año 7 es de: ' + porcentaje7.to_s
año8 = valores[6]-valores[7]
porcentaje8 = (año8*100)/valores[6]
puts'el deficit del año 8 es de: ' + porcentaje8.to_s
año9 = valores[7]-valores[8]
porcentaje9 = (año9*100)/valores[7]
puts'el deficit del año 9 es de: ' + porcentaje9.to_s
año10 = valores[8]-valores[9]
porcentaje10 = (año10*100)/valores[8]
puts ' el deficit del año 10 es de: ' + porcentaje10.to_s
