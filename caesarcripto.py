letras = ['''abcdefghijklmnopqrstuvwyzàáãâéêóôõíúç ABCDEFGHIJKLMNOPQRSTUVWYZ1234567890ÀÁÃÂÉÊÓÕÍÚÇ/*-+!@#$%&*()'"_=§¹²³£¢¬´[]~;/ªº°:?}^{`\|''',
     '''LSém4r¬íÂ/³oõVnáÊ#¢ADKÓh/qUÃJ%g²=°@ÉYp-jº k´RãOi_e`;Tà£ªâóçdyz§N1^b(*M$úu76À':ECs5{2vW*|0lFa}ôê?fc&)IÇ89t3+ÕÁ~wÚBQ![GP"¹Í\ZH]''',
     '''mw²?à§éÉ1NCn@^)ÇI=5|y~ráJ/úódG uP$qÓFW\çâÁjEbotf4ã³eDc3;6Ú-¹Â9Yl8êzk¬gAi{QZ0ª2°`V/õ¢LUv_*ô(ÊSÕOÀ}7!H*Mh]pÍ£'así"K[ºB+:&#´R%ÃT''',
     '''làiÕégÓÚpwNÂ?ãÊú]erb*n5Wí|ÀBU`/âZ:#Tªç0K_ &Gó3\¢fa1oy'@j°EáLF-DRõdºÃS4mO$AtêôQ§({Pu%Mh=+[V9~*7´¹/s¬I^v£HJYC)!Éc8ÍÇ"²26}k;zÁ³q''',
     '''%\*7:*Á ²6¹cYÓ1Deu(=|bEá/Í')o@úqRC;Ç4LJ&"ÃÂHpQªdéK-º}À9ôTP³/gU8Éê{m0!`[¢lfvBs¬°VnO]zàGAÊ$kZ5hF£§tõ~MíÕÚj´aNS#ãWy+I3_?wr2óiâç^''',
     '''QB:M§AºsláÓÃHã¬_$õyvC'&G´[e £U*08)q1`2p?³WfuÁ|â(D=Én;/kÂ6i]óçZ+àmcL!oOúíR*²SÕ°¹ªh~JK3E9wb}F5Êj¢-Í4"\Iédêt#{/NÇrz@7^ÀTÚôaV%gYP''',
     '''/9@s\Íw#À|VmcáY}+n%5Z¹NbõíéK3qf(S`-16!dÚgkêtyzj8E0=Lª*"¬ºÉhI^*C2e[UBo4)WTóD_ú'FQ]O7¢MuPi$ÕâA?;pav°´ç&²àÃ³H/ £RÓJÇ:ôÊãÂÁr§~G{l''',
     '''qY%Ó"m$+õíi:ZGnAâédO9PºÉBóKpD18/FTr¢6^N|ªz&E!vÕQR=;7kSC*ÊçV{aLeÁ#3I[êw}H*)y_´st]-¹ô`Ãu\àb£ÚW2(³ UMÀ@h0Ç'§4¬lúã~gÍ?J/j°ocá²5Âf''',
     '''àY{íd&ÓWi£Bm~6Eãú¹D/g`Fe¬7êoÚ°9Õ=TõMfV3³%ó:*LÀ]4)n|ªaqCNéJÍv#jcÃ§Éy"²wº;^t´káU5OK*$@hSÊçR82Á[QAp+_¢ô0/?szu H!'Z(râ1\-GÂ}lPÇIb''',
     '''5§0dS-a'GIwÚiªlJu|MHRã :eAOEÇ61%=°@¹(3}7cgs²Á4´víb*YptWQ\){m]ôÃâVj&ÓÕqnró¢ÍàhÊºZ/Uk/LÀ`;#N£F³"!8_y¬Â9^çú+áÉzé[oKfCDõB$2~*TPê?''',
     '''KH¢VSÇ~p ÊGóc`²4ú*=$z/ê9Y´Tuwm;àíbÍJ{i°QÁ%o"Ãd(3-ás'Â6MtOL¬Faeé0NÚI[UBE+}|A:P&ÓD§É\âgZ@£5#l^õrjv2/¹f)8qºyÀç!nôk?ã1_7hÕªR*C³]W''',
     '''l¢$/ã+ÉB8vDº¹úàõa7êÇ9*6z³hg^`FGOcÊUâ=Õ|Qí2¬j£JôZY):/ÚÁ;°-WV{NAML"}dsRwP@oEÓ530f]pÂTÍH§ç~´kÃ'\%ub(I1eÀt#!éKnSmóª &[*á_qr²y?iC4''',
     '''$Àdt:C¢ON]T§&qB[L'ê-´õk0/ârs³Ã6Õô)S!v¬ÍY2z@4á1Jàóúy_lfQí\ç| ÂéÉ²n3aPKMu7°Ç5e{R£I`V~ª+hZ(/#Wã*EgG;mUc8wb%D¹^AoÊjiFº=*H"9Á}ÚpÓ?''',
     '''UTqéóuD8n#í0'?@Ã/LÕ£k!p*IÚ°çjâ}"fSZÍôÊde%mº_JÁg(;¬WÇyàCaáªR³Â¹2-~]É54ãY69&tMcQN`lbw¢²Pr ÀhV^´+§oz=E:*Ó1Aõ$HBK|sOú3{/v)iêF7G\[''',]
def senha(senha_o):
    chave = 0
    for k in senha_o:
        chave += ord(k) % 10
    return chave


def criptografar(frase, senha_o):
    x = 0
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

