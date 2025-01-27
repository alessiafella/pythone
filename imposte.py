reddito =int(input ("inserisci il tuo reddito: "))

prima_aliquota= 0.23
seconda_aliquota= 0.35
terza_aliquota= 0.43


if reddito <= 28000 :
  aliquote_uno = prima_aliquota*(reddito)
  totale_da_pagare = reddito-(aliquote_uno)

elif 28001 <= reddito <= 50000 :
  aliquote_uno = prima_aliquota*(28000)
  aliquote_due= seconda_aliquota*(reddito-28001) 
  totale_da_pagare = reddito - ( aliquote_uno + aliquote_due)

else  :
  aliquote_uno = prima_aliquota*(28000)
  aliquote_due = seconda_aliquota*(21999) 
  aliquote_tre = terza_aliquota*(reddito-50000)
  totale_da_pagare = reddito - ( aliquote_uno + (aliquote_due)+ aliquote_tre)
  

print ("dovrai pagare" , int(totale_da_pagare) , "euro")
