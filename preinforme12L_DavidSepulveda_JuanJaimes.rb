listapromedio=[110.06,107.89,108.45,108.49,109.03,110.11,109.87,119.38,119.35,116.34,117.73,120.01,118.19,119.53,117.09,118.03,118.65,117.47,117.49,109.65,110.44,110.51,107.38,109.26,106.18,109.36,106.61,105.16,110.11,105.48,108.37,107.59,108.91,108.35,109.57,122.56,124.44,125.97,121.03,121.22,122.41,122.15,124.52,123.35,125.76,121.08,122.29,105.42,110.67,107.73,105.76,107.85]
listapromedio2=listapromedio.sort


def mayor_menor (listapromedio)
    minlisp=listapromedio.min
    maxlisp=listapromedio.max
    diferencia=maxlisp-minlisp
    puts "La diferencia entre las utilidades fue: #{diferencia}"
end
mayor_menor(listapromedio)


def media (listapromedio)
    longitudlista=listapromedio.length
    suma=listapromedio.sum
    media=(suma)/(longitudlista)
    return media
end

puts "La media de las presiones: #{media(listapromedio)}"


def mediana (listapromedio2)
    long=listapromedio2.length
    mediana=listapromedio2[long/2]+listapromedio2[(long/2)-1]
    mediana=mediana/2
    puts "La mediana de las presiones es: #{mediana}"
end
mediana(listapromedio2)

x= media(listapromedio)
y= mediana(listapromedio2)
diferencia= x-y
puts diferencia.to_s
