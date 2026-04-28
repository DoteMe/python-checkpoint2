lista_emails_brutos = [
    "  teste@gmail.com  ",
    "TESTE@GMAIL.COM",
    "teste @gmail.com",
    "teste@gmail",
    "teste.com",
    "  user123@hotmail.com",
    "user.name@yahoo.com ",
    "user@@gmail.com",
    "user gmail.com",
    "user@ gmail.com",
    "user@gmail .com",
    "valido@email.com",
    "outro.valido@empresa.org",
    "invalido@",
    "@gmail.com",
]

lista_nascimento_brutos = [
    "17/03/2006",
    "01/11/2006",
    "19/07/2014",
    "14/08/2018",
    " 10/10/2000 ",
    "31/02/2005",
    "29/02/2004",
    "15-05-2003",
    "2001/12/20",
    "abc",
    "12/12/2010",
    "05/09/1990",
    "7/7/2007",
    "",
    "01/01/2027",
]

lista_emails_limpos = []
lista_nascimento_limpos = []

ano_atual = 2026

for i in range(len(lista_emails_brutos)):

    email = lista_emails_brutos[i]
    nascimento = lista_nascimento_brutos[i]

    email_tratado = email.strip().replace(" ", "").lower()

    if "@" in email_tratado and "." in email_tratado:

        nascimento_tratado = nascimento.strip()

        if "/" in nascimento_tratado:

            partes_data = nascimento_tratado.split("/")

            if len(partes_data) == 3:

                dia, mes, ano = partes_data

                if ano.isdigit():

                    ano_nascimento = int(ano)
                    idade = ano_atual - ano_nascimento

                    if idade >= 18:
                        lista_emails_limpos.append(email_tratado)
                        lista_nascimento_limpos.append(nascimento_tratado)
                    else:
                        print(f"Menor de idade: {email_tratado}")

                else:
                    print(f"Ano inválido: {nascimento_tratado}")

            else:
                print(f"Formato de data inválido: {nascimento_tratado}")

        else:
            print(f"Data sem '/': {nascimento_tratado}")

    else:
        print(f"Email inválido: {email_tratado}")

print("\nEmails válidos e maiores de idade:")
print(lista_emails_limpos)

print("\nDatas correspondentes:")
print(lista_nascimento_limpos)