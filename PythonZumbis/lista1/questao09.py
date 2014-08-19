dias = input('Digite os dias:  ')
km = input('Digite os kilometros:  ')

vlr_pagar = 60 * int(dias)
vlr_pagar = vlr_pagar + (int(km) * 0.15)

print(str(vlr_pagar))
