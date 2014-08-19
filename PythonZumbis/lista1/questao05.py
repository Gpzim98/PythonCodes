vrl_mercadoria = input('Valor da mercadoria: ')
per_desc = input('Percentual de desconto: ')

vrl_mercadoria = float(vrl_mercadoria)
per_desc = float(per_desc)

desconto = (vrl_mercadoria * (per_desc/100))
vlr_pagar = vrl_mercadoria + (vrl_mercadoria * (per_desc/100))

print("Desconto: " + str(desconto))
print("Valor a pagar: " + str(vlr_pagar))
