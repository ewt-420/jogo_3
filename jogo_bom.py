import time
import random


vida_base = 1
vida_extra = 0
vida = vida_base + vida_extra
dano_base = 1
defesa = 1
nivel = 1
monstro_0 = 0
defesa_total = 0
dano_extra = 0
moedas = 0
dano = dano_base + dano_extra
nivel_bug = 0
equipar_itens = 0
golden_dragon_0 = 0
golden_dagon = 0
goldendragon = 0
golden_dragon = 0
print ('bem-vindo!')

bug_01 = 0
bug_02 = 0
bug_03 = 0
bug_04 = 0
bug_05 = 0
bug_06 = 0
bug_07 = 0
bug_08 = 0


selecao_1 = 'asd'
selecao_2 = 'asd'
selecao_3 = 'asd'
selecao_4 = 'asd'


espada_do_guerrilheiro = 0
anel_fantasma = 0
totem_das_desgracas = 0
cajado_das_impossibilidades = 0
colar_das_7_almas = 0; almas_no_colar = 0
cartas_de_vidente = 0
espada_do_cavaleiro = 0
escudo_de_madeira = 0


espadadoguerrilheiro = 0
anelfantasma = 0
totemdasdesgracas = 0
cajadodasimpossibilidades = 0
colardas7almas = 0
cartasdevidente = 0
espadadocavaleiro = 0
escudodemadeira = 0


dano_extra = 0
utilizar_itens = 1


while vida > 0:


    compra_01 = 0
    compra_02 = 0
    compra_03 = 0
    compra_04 = 0
    compra_05 = 0
    compra_06 = 0
    compra_07 = 0
    compra_08 = 0


    nivel2 = nivel * 2
    nivel3 = nivel * 3
    dano = dano_base + dano_extra
    utilizar_itenssave = utilizar_itens
    monstro_0 = 0
    listaa = 0
    noloop = 0
    print ('nivel:',nivel,'\t','moedas:',moedas)
    print ()
    time.sleep (0.5)
    print ('               vida','   dano','  defesa')
    time.sleep(0.5)
    print ('player:','\t',vida,'\t',dano,'\t',defesa,'\t')

    if golden_dragon_0 == 1:
        time.sleep (1)
        print ('você encontrou o dragão de ouro!')
        time.sleep (0.5)
        print ('quer enfrentá-lo agora?')
        time.sleep (0.5)
        print ('sim   1')
        time.sleep (0.5)
        print ('não   2')
        golden_dragon_1 = int(input())
        if golden_dragon_1 == 1:
            golden_dragon = 1
            print ('você quer enfrentar o dragão dourado agora!')
        else:
            print ('você não quer enfrentar o dragão agora')

    if nivel_bug != nivel:
        if nivel == 1:
            vidamonstro = 1
            danomonstro = 1
            defesamonstro = 1
        if 2 <= nivel <= 10:
            vidamonstro = random.randint (1,nivel2)
            danomonstro = random.randint (1,nivel)
            defesamonstro = random.randint (1,nivel)
        if nivel > 10 and nivel <= 20:
            vidamonstro = random.randint (nivel,nivel2)
            danomonstro = random.randint (1,nivel2)
            defesamonstro = random.randint (1,nivel2)
        if nivel > 20:
            vidamonstro = random.randint (nivel,nivel3)
            danomonstro = random.randint (1,nivel2)
            defesamonstro = random.randint (1,nivel2)
        if golden_dragon == 1:
            vidamonstro = 200
            danomonstro = 10
            defesamonstro = 30
        nivel_bug = nivel


    time.sleep(0.5)
    print ('monstro:','\t',vidamonstro,'\t',danomonstro,'\t',defesamonstro,'\t')


    guardar_vida = vida


    time.sleep(1)
    print ('digite:')
    time.sleep(0.5)
    comecar_batalha = int(input('1 para começar a batalha\n2 para selecionar itens'))
    time.sleep (1)


    if comecar_batalha == 1:
        while monstro_0 == 0 and vida > 0:


            if comecar_batalha == 1:
                print ('você começa atacando')
                loop_1 = 0
                loop_2 = 0
                totem_das_desgracas_morte = 0
                vida = guardar_vida


                dano = dano_base + dano_extra


            while vida > 0 and monstro_0 == 0:


                loop_3 = 1


                time.sleep (1)
                print ('escolha um número de 1 a',defesamonstro)
                escolha_monstro = random.randint (1,defesamonstro)


                if cartas_de_vidente == 1:
                    visao_1 = random.randint (1,escolha_monstro)
                    visao_2 = random.randint (escolha_monstro,defesamonstro)
                    print ('as cartas te mostraram que o número da defesa está entre',visao_1,'e',visao_2)


                ataque = int(input())
                if ataque == 0:
                    print ('                         vida','   dano','  defesa','  vida max')
                    time.sleep (0.5)
                    print ('          player:','\t',vida,'\t',dano,'\t',defesa,'\t',guardar_vida)
                    time.sleep (0.5)
                    print ('          monstro:','\t',vidamonstro,'\t',danomonstro,'\t',defesamonstro,'\t')
                    time.sleep (0.5)
                    print ('escolha novamente o número do ataque')
                    ataque = int(input())
                distancia_1 = escolha_monstro - ataque
                if distancia_1 < 0:
                    distancia_1 = distancia_1 * -1
                dano_no_monstro = dano - distancia_1
                if dano_no_monstro <= 0:
                    dano_no_monstro = 0
                vidamonstro -= dano_no_monstro
                if vidamonstro <= 0:
                    monstro_0 = 1


                time.sleep (1)
                print ('o número era',escolha_monstro)
                time.sleep (1)
                print ('você causou',dano_no_monstro,'de dano')
                time.sleep (1)


                while loop_3 > 0:
                    loop_3 -= 1


                    if dano_no_monstro == 0 and totem_das_desgracas == 1 and loop_1 == 0:
                       loop_1 = 1
                       print ('mas...')
                       time.sleep (1)
                       print ('o totem te deu mais uma chance')
                       continue


                    print ('o monstro agora está com',vidamonstro,'de vida')
                    time.sleep (1)


                    if monstro_0 == 0:
                       print ('agora o monstro ataca!')
                       escolha_player = random.randint(1,defesa)
                       time.sleep (1)
                       print ('o seu número da defesa é',escolha_player)
                       ataque_monstro = random.randint (1,defesa)
                       time.sleep(1)
                       print ('o monstro escolheu o número...')
                       time.sleep (1)
                       print (ataque_monstro)
                       distancia_2 = escolha_player - ataque_monstro
                       if distancia_2 < 0:
                           distancia_2 = distancia_2 * -1
                       dano_no_player = danomonstro - distancia_2
                       if dano_no_player <= 0:
                           dano_no_player = 0
                       vida = vida - dano_no_player
                       time.sleep (1)
                       print ('o monstro causou',dano_no_player,'de dano')


                       if escolha_player == ataque_monstro and totem_das_desgracas == 1 and loop_2 == 0:
                            loop_2 = 1
                            loop_3 += 1
                            vida += dano_no_player
                            time.sleep (1)
                            print ('mas...')
                            time.sleep (1)
                            print ('o totem te dá mais uma chance')
                            continue


                       if cajado_das_impossibilidades == 1:
                            sorte_do_cajado = random.randint (1,4)
                            if sorte_do_cajado == 1:
                                defesa_total = 1


                       if defesa_total == 1:
                            print ('mas...')
                            time.sleep (1)
                            print ('você desviou de todo o ataque')
                            time.sleep (1)
                            vida = vida + dano_no_player
                            defesa_total = 0


                       if vida <= 0 and totem_das_desgracas == 1 and totem_das_desgracas_morte == 0:
                            totem_das_desgracas_morte = 1
                            print ('você ficou com',vida,'de vida')
                            time.sleep (1)
                            print ('mas...')
                            time.sleep (1)
                            print ('o totem te deixou com 1 de vida')
                            time.sleep (1)
                            vida = 1


                       print ('você está com',vida,'de vida')
                       time.sleep (1)


                       if vida < 0 and anel_fantasma == 1:
                           dano_anel_fantasma = vida * -1
                           vidamonstro = vidamonstro - dano_anel_fantasma
                           print ('você morreu')
                           time.sleep (2)
                           print ('calma...')
                           time.sleep (1.5)
                           print ('você quase morreu!')
                           time.sleep (1.5)
                           print ('você usa o anel para retribuir sua vida negativa em dano no monstro')
                           time.sleep (2)
                           print ('você causa',dano_anel_fantasma,'de dano')
                           time.sleep (1.5)
                           print ('o monstro fica com',vidamonstro,'de vida')
                           time.sleep (1.5)
                           if vidamonstro <= 0:
                               vida = 1
                               print ('o monstro morreu e você se levantou com 1 ponto de vida')
                               monstro_0 = 1
                           if vidamonstro > 0:
                               print ('você tenta se levantar mas não consegue')
                               morreumorrido = 1

                    if vida <= 0:
                        break




            if monstro_0 == 1:


                vida = guardar_vida

                if golden_dragon == 1:
                    golden_dragon = 0
                    goldendragon = 1


                if colar_das_7_almas == 1:
                    almas_no_colar += 1
                    if almas_no_colar == 7:
                       ganho_do_colar1 = random.randint (1,3)
                       ganho_do_colar2 = random.randint (1,3)
                       ganho_do_colar3 = random.randint (1,3)
                       vida += ganho_do_colar1
                       dano += ganho_do_colar2
                       defesa += ganho_do_colar3
                       print ('você coletou 7 almas através do colar')
                       print ('como recompensa, ganhou',ganho_do_colar1,'de vida',ganho_do_colar2,'de dano e',ganho_do_colar3,'de defesa')
                       almas_no_colar = 0


                print ('o monstro morreu')


                recompensa = random.randint (1,100)
                item = random.randint (1,100)


                # VIDA
                if 1 <= recompensa <= 10:   # 20 %
                    vida_base += 1
                    print ('você ganhou 1 ponto de vida')
                if 11 <= recompensa <= 30:   # 20 %
                    vida_base += 2
                    print ('você ganhou 2 pontos de vida')
                if 31 <= recompensa <= 40:   # 20 %
                    vida_base += 3
                    print ('você ganhou 3 pontos de vida')
                # DANO
                if 41 <= recompensa <= 45:   # 10 %
                    dano_base += 1
                    print ('você ganhou 1 ponto de dano')
                if 46 <= recompensa <= 55:   # 10 %
                    dano_base += 2
                    print ('você ganhou 2 pontos de dano')
                if 56 <= recompensa <= 60:   # 10 %
                    dano_base += 3
                    print ('você ganhou 3 pontos de dano')
                # DEFESA
                if 61 <= recompensa <= 65:   # 5 %
                    defesa += 1
                    print ('você ganhou 1 ponto de defesa')
                if 66 <= recompensa <= 75:   # 2 %
                    defesa += 2
                    print ('você ganhou 2 pontos de defesa')
                if 76 <= recompensa <= 80:   # 2 %
                    defesa += 3
                    print ('você ganhou 3 pontos de defesa')
                # TODOS
                if 81 <= recompensa <= 100:   # 1 %
                    if 81 <= recompensa <= 90:
                        vida_base += 1
                        dano_base += 1
                        print ('você ganhou 1 ponto de vida e 1 ponto de dano')
                    if 91 <= recompensa <= 100:
                        vida_base += 1
                        defesa += 1
                        print ('você ganhou 1 ponto de vida e 1 ponto de defesa')

                if goldendragon != 1:
                    if 1 <= item <= 20:
                        if cartasdevidente == 0:
                           cartasdevidente = 1
                           print ('você também ganhou cartas de vidente')
                        else:
                            moedas += 5
                            print ('+5 moedas')
                    if 21 <= item <= 30:
                        if colardas7almas == 0:
                            colardas7almas = 1
                            print ('você também ganhou colar das 7 almas')
                        else:
                            moedas += 5
                            print ('+5 moedas')
                    if 31 <= item <= 45:
                        if espadadoguerrilheiro == 0:
                            espadadoguerrilheiro = 1
                            print ('você também ganhou espada do guerrilheiro')
                        else:
                            moedas += 5
                            print ('+5 moedas')
                    if 46 <= item <= 55:
                        if anelfantasma == 0:
                            anelfantasma = 1
                            print ('você ganhou anel-fantasma')
                        else:
                            moedas += 5
                            print ('+5 moedas')
                    if 56 <= item <= 60:
                        if cajadodasimpossibilidades == 0:
                            cajadodasimpossibilidades = 1
                            print ('você também ganhou cajado das impossibilidades')
                        else:
                            moedas += 5
                            print ('+5 moedas')
                    if 61 <= item <= 75:
                        if totemdasdesgracas == 0:
                           totemdasdesgracas = 1
                           print ('você também ganhou totem das desgraças')
                        else:
                            moedas += 5
                            print ('+5 moedas')
                    if 76 <= item <= 85:
                        if espadadocavaleiro == 0:
                            espadadocavaleiro = 1
                            print ('você também ganhou espada do cavaleiro')
                        else:
                            moedas += 5
                            print ('+5 moedas')
                    if 86 <= item <= 100:
                        if escudodemadeira == 0:
                            escudodemadeira = 1
                            print ('você ganhou escudo de madeira')
                        else:
                            moedas += 5
                            print ('+5 moedas')
                else:
                    moedas += 70


                if nivel % 10 == 0 :
                    time.sleep (1)
                    print ('você encontra um comerciante')
                    time.sleep (1)
                    print ('você tem',moedas,'moedas')
                    time.sleep (1)
                    print ('deseja comprar alguma coisa?')
                    time.sleep (0.5)
                    print ('sim   - 1')
                    time.sleep (0.5)
                    print ('não   - 2')
                    comprinhas = int(input())
                    time.sleep (1)
                    if comprinhas == 2:
                        print ('você não quer comprar nada agora')
                        break
                    if comprinhas == 1:
                        print('você tem',moedas,'moedas')
                        time.sleep (1)
                        print ('você pode comprar estes itens:')
                        time.sleep (0.5)
                        print ('item                          preço        número')
                        time.sleep (0.5)
                        print ('\n')
                        listacomprinhas = [1,2,3,4,5,6,7,8]
                        nivel_10 = int(nivel/10 * 3)
                        listacomprinhas2 = random.sample(listacomprinhas, k = nivel_10)
                        for compras in listacomprinhas2:
                            time.sleep (0.5)
                            if compras == 1 and cartasdevidente == 0:
                                print ('cartas de vidente             $ 015        01')
                                compra_01 = 1
                            if compras == 2 and colardas7almas == 0:
                                print ('colar das 7 almas             $ 015        02')
                                compra_02 = 1
                            if compras == 3 and espadadoguerrilheiro == 0:
                                print ('espada do guerrilheiro        $ 015        03')
                                compra_03 = 1
                            if compras == 4 and anelfantasma == 0:
                                print ('anel-fantasma                 $ 015        04')
                                compra_04 = 1
                            if compras == 5 and cajadodasimpossibilidades == 0:
                                print ('cajado das impossibilidades   $ 015        05')
                                compra_05 = 1
                            if compras == 6 and totemdasdesgracas == 0:
                                print ('totem das desgraças           $ 015        06')
                                compra_06 = 1
                            if compras == 7 and espadadocavaleiro == 0:
                                print ('espada do cavaleiro           $ 015        07')
                                compra_07 = 1
                            if compras == 8 and escudodemadeira == 0:
                                print ('escudo de madeira             $ 015        08')
                                compra_08 = 1


                            time.sleep (0.5)
                        if utilizar_itens < 4:
                            print ('+1 espaço para equipar itens  $ 030        99')
                            equipar_itens = 1
                            time.sleep (0.5)
                        print ('digite 00 se não quiser comprar nada')
                        compra = input()
                        time.sleep (1)
                        if compra == '00':
                            print ('você não comprou nada')
                            break
                        if compra == '01' and compra_01 == 1 and moedas >= 15:
                            cartasdevidente = 1
                            moedas -= 15
                            print ('você comprou cartas de vidente por 15 moedas')
                        if compra == '02' and compra_02 == 1 and moedas >= 15:
                            colardas7almas = 1
                            moedas -= 15
                            print ('você comprou colar das 7 almas por 15 moedas')
                        if compra == '03' and compra_03 == 1 and moedas >= 15:
                            espadadoguerrilheiro = 1
                            moedas -= 15
                            print ('você comprou espada do guerrilheiro por 15 moedas')
                        if compra == '04' and compra_04 == 1 and moedas >= 15:
                            anelfantasma = 1
                            moedas -= 15
                            print ('você comprou anel-fantasma por 15 moedas')
                        if compra == '05' and compra_05 == 1 and moedas >= 15:
                            cajadodasimpossibilidades = 1
                            moedas -= 15
                            print ('você comprou cajado das impossibilidades por 15 moedas')
                        if compra == '06' and compra_06 == 1 and moedas >= 15:
                            totemdasdesgracas = 1
                            moedas -= 15
                            print ('você comprou totem das desgraças por 15 moedas')
                        if compra == '07' and compra_07 == 1 and moedas >= 15:
                            espadadocavaleiro = 1
                            moedas -= 15
                            print ('você comprou espada do cavaleiro por 15 moedas')
                        if compra == '08' and compra_08 == 1 and moedas >= 15:
                            escudodemadeira = 1
                            moedas -= 15
                            print ('você comprou escudo de madeira por 15 moedas')
                        if compra == '99' and equipar_itens == 1 and moedas >= 30:
                            utilizar_itens += 1
                            moedas -= 30
                            print ('você comprou mais um espaço para equipar itens por 30 moedas')
                        equipar_itens = 0

                if nivel > 10 and goldendragon == 0:
                    chance_gold = random.randint (1,100)
                    chance_gold2 = int(moedas/10)
                    if chance_gold2 >= chance_gold:
                        golden_dragon_0 = 1

                nivel += 1


    if comecar_batalha == 2:
       
        dano_extra = 0
        vida_extra = 0


        print ('você possui estes itens:')
        print ('voltar   00')
        if cartasdevidente == 1:
           print ('cartas de vidente   01')
        if colardas7almas == 1:
           print ('colar das 7 almas-',almas_no_colar,'   02')
        if espadadoguerrilheiro == 1:
           print ('espada do guerrilheiro   03')
        if anelfantasma == 1:
           print ('anel-fantasma   04')
        if cajadodasimpossibilidades == 1:
           print ('cajado das impossibilidades   05')
        if totemdasdesgracas == 1:
           print ('totem das desgraças   06')
        if espadadocavaleiro == 1:
            print ('espada do cavaleiro   07')
        if escudodemadeira == 1:
            print ('escudo de madeira   08')
           
        list_selecao = [selecao_1, selecao_2, selecao_3, selecao_4]
        print ('você pode escolher até',utilizar_itens,'itens')
        for listaa in list_selecao:
            utilizar_itens -= 1
            listaa = input('digite a escolha:')
            if listaa == '00':
                break
            if listaa == '01' and cartasdevidente == 1:
                cartas_de_vidente = 1
                bug_01 = 1
                time.sleep (0.5)
                print ('você selecionou cartas de vidente')
            if listaa == '02' and colardas7almas == 1:
                colar_das_7_almas = 1
                bug_02 = 1
                print ('você selecionou colar das 7 almas')
            if listaa == '03' and espadadoguerrilheiro == 1:
                espada_do_guerrilheiro = 1
                bug_03 = 1
                print ('você selecionou espada do guerrilheiro')
            if listaa == '04' and anelfantasma == 1:
                anel_fantasma = 1
                bug_04 = 1
                print ('você selecionou anel-fantasma')
            if listaa == '05' and cajadodasimpossibilidades == 1:
                cajado_das_impossibilidades = 1
                bug_05 = 1
                print ('você selecionou cajado das impossibilidades')
            if listaa == '06' and totemdasdesgracas == 1:
                totem_das_desgracas = 1
                bug_06 = 1
                print ('você selecionou totem das desgraças')
            if listaa == '07' and espadadocavaleiro == 1:
                espada_do_cavaleiro = 1
                bug_07 = 1
                print ('você selecionou espada do cavaleiro')
            if listaa == '08' and escudodemadeira == 1:
                escudo_de_madeira = 1
                bug_08 = 1
                print ('você selecionou escudo de madeira')
            if utilizar_itens == 0:
                break


        if bug_01 == 0:
            cartas_de_vidente = 0
        if bug_02 == 0:
            colar_das_7_almas = 0
        if bug_03 == 0:
            espada_do_guerrilheiro = 0
        if bug_04 == 0:
            anel_fantasma = 0
        if bug_05 == 0:
            cajado_das_impossibilidades = 0
        if bug_06 == 0:
            totem_das_desgracas = 0
        if bug_07 == 0:
            espada_do_cavaleiro = 0
        if bug_08 == 0:
            escudo_de_madeira = 0




        bug_01 = 0
        bug_02 = 0
        bug_03 = 0
        bug_04 = 0
        bug_05 = 0
        bug_06 = 0
        bug_07 = 0
        bug_08 = 0


            # ESPADA DO GUERRILHEIRO
        if espada_do_guerrilheiro == 1:
            dano_extra += 3


            # ESPADA DO CAVALEIRO
        if espada_do_cavaleiro == 1:
            dano_extra += 5


            # ESCUDO DE MADEIRA
        if escudo_de_madeira == 1:
            vida_extra += 3


        noloop = 1


    dano = dano_base + dano_extra

    if vida > 0:
        vida = vida_base + vida_extra
        guardar_vida = vida


    if noloop == 1:
        time.sleep (0.5)
        print ('voltando')
        time.sleep (2)
        utilizar_itens = utilizar_itenssave

time.sleep (0.5)
print ('você morreu')