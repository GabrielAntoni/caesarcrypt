def senha(senha_o):
    chave = 0
    for k in senha_o:
        chave += ord(k) % 10
        return chave

def criptografar(frase, senha_o):
    x = 0
    letras = ['abcdefghijklmnopqrstuvwyzàáãâéêóôõíúç ABCDEFGHIJKLMNOPQRSTUVWYZ1234567890ÀÁÃÂÉÊÓÕÍÚÇ',
     'okqnõpiúôl eêçzhíbsmdaácjfóàwtâéyvurãgOKQNÕPIÚÔLEÊÇZHÍBSMDAÁCJFÓÀWTÂÉYVURÃG1234567890',
     'hzptúujõlnóvíasbkqrôyâcidmãfoegwáàéêçHZPTÚUJÕLNÓVÍASBKQRÔYÂ CIDMÃFOEGWÁÀÉÊÇ1234567890',
     '2â0tgEÕnfNcMqA hSÔBCJÂDáPã1zõGeÍ5çLZF9ÇsyrêkíUÊÁuôÓ4pI3úRv7OàKÉYmÃÀQdiw68aVlbÚTóHoéWj',
     'êW6í9qfJnVKIÕàvÀdG7EhÚjuOÓã8LMHNm0AsPU5Q4YÁâéSÔtrkôRÂÊblT3eÍZpÃÉõBCFçó z1aDgcáw2oyÇiú',
     'pRszvA62éÇÕuq0rVdÔOátêmWEcLâQIób õ1j7Fà4N8úÁÀeÃDJPfClGô5gÊçKTHyÍíwBZaÂhY9o3ÓkÚÉMãUSin']
    nova_frase = ''
    for c in frase:
        if x >= len(letras):
            x = 0
        index = letras[x].find(c)
        if index == -1:
            nova_frase += c
        else:
            chave = senha(senha_o)
            new_index = index + chave
            new_index = new_index % len(letras[x])
            nova_frase += letras[x][new_index:new_index+1]
            x += 1
    return nova_frase
def descriptografar(frase, senha_o):
    x = 0
    letras = ['abcdefghijklmnopqrstuvwyzàáãâéêóôõíúç ABCDEFGHIJKLMNOPQRSTUVWYZ1234567890ÀÁÃÂÉÊÓÕÍÚÇ',
     'okqnõpiúôl eêçzhíbsmdaácjfóàwtâéyvurãgOKQNÕPIÚÔLEÊÇZHÍBSMDAÁCJFÓÀWTÂÉYVURÃG1234567890',
     'hzptúujõlnóvíasbkqrôyâcidmãfoegwáàéêçHZPTÚUJÕLNÓVÍASBKQRÔYÂ CIDMÃFOEGWÁÀÉÊÇ1234567890',
     '2â0tgEÕnfNcMqA hSÔBCJÂDáPã1zõGeÍ5çLZF9ÇsyrêkíUÊÁuôÓ4pI3úRv7OàKÉYmÃÀQdiw68aVlbÚTóHoéWj',
     'êW6í9qfJnVKIÕàvÀdG7EhÚjuOÓã8LMHNm0AsPU5Q4YÁâéSÔtrkôRÂÊblT3eÍZpÃÉõBCFçó z1aDgcáw2oyÇiú',
     'pRszvA62éÇÕuq0rVdÔOátêmWEcLâQIób õ1j7Fà4N8úÁÀeÃDJPfClGô5gÊçKTHyÍíwBZaÂhY9o3ÓkÚÉMãUSin']
    nova_frase = ''
    for c in frase:
        if x >= len(letras):
            x = 0
        index = letras[x].find(c)
        if index == -1:
            nova_frase += c
        else:
            chave = senha(senha_o)
            new_index = index - chave
            new_index = new_index % len(letras[x])
            nova_frase += letras[x][new_index:new_index+1]
            x += 1
    return nova_frase

