from unittest import result


name = input('Name:')
kg = float(input('Weight:'))
meter = float(input('Height:'))

result = (kg / meter**2)

print(f'Underweight:{0<result<18.4}' + ' '+ str(result))
print(f'Normalweight:{18.5<result<24.9}' +' '+ str(result))
print(f'Over-weight:{25.0<result<29.9}' +' '+ str(result))
print(f'Fat(Obese):{30<result<34.9}' +' '+ str(result))