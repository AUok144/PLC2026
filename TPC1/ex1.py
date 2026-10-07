import re 
# Expressão: 1*(0|01)*
#
# A substring proibida é "011".
# Para evitar "011", depois de aparecer um 0 nunca podem aparecer
# dois 1 seguidos.
#
# 1* -> no início podemos ter qualquer quantidade de 1s,
#            porque ainda não existe nenhum 0 antes deles.
#
# (0|01)* -> depois disso, a string é formada por blocos:
#            "0"  ou  "01".
#            Assim, sempre que aparece um 1 depois de um 0,
#            nunca pode aparecer imediatamente outro 1.
#
# ^ e $ garantem que a expressão corresponde à string inteira.

# Exemplos: 
# "011011": rejeita
# "10111": rejeita
# "1101": aceita
# "101010": aceita
# "0000": aceita
# "111": aceita

exp = r"^1*(0|01)*$"

exs = ["011011", "10111", "1101", "101010", "0000", "111"]
for s in exs: 
    print(s, "aceita" if re.match(exp, s) else "rejeita")