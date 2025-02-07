kuukausi = input('Anna kuukauden järjestysnumero (1-12): ')
kuukausi_on = kuukausi.lower()
vuodenaika = ()
if kuukausi_on == '12' or kuukausi_on == '1' or kuukausi_on == '2':
    vuodenaika = 'Talvi'

elif kuukausi_on == '3' or kuukausi_on == '4' or kuukausi_on == '5':
    vuodenaika = 'Kevät'

elif kuukausi_on == '6' or kuukausi_on == '7' or kuukausi_on == '8':
    vuodenaika = 'Kesä'

else:
    vuodenaika = 'Syksy'

print(vuodenaika)


