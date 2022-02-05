from django.http import response

from django.shortcuts import render, HttpResponse
from .functions import *

def indexpage(request):
    return render(request, template_name='index.html')

def results(request):    
    try:
        Sit = request.POST['ressalto']
        Acab = request.POST['acabamento']
        d = request.POST['d_inicial']
        D = request.POST['d_vizinha']
        a = request.POST['l_canal']
        t = request.POST['p_canal']
        dinside = request.POST['p_sulco']
        r_entalhe1 = request.POST['r_entalhe1']
        r_entalhe2 = request.POST['r_entalhe2']
        r_entalhe3 = request.POST['r_entalhe3']
        Temp = request.POST['temperatura']
        conf = request.POST['confiabilidade']
        carga = request.POST['carga']
        eq = request.POST['equilibrio']
        Mat = request.POST['material']
        nseg = request.POST['n_seg']
        decide = request.POST['decide']
        Sut = request.POST['Sut']
        Sy = request.POST['Sy']

        alt_momento1 = request.POST['alt_momento1']
        media_torque2 = request.POST['media_torque2']
        alt_momento3 = request.POST['alt_momento3']
        media_torque3 = request.POST['media_torque3']
        media_momento4 = request.POST['media_momento4']
        alt_momento4 = request.POST['alt_momento4']
        media_torque5 = request.POST['media_torque5']
        alt_torque5 = request.POST['alt_torque5']
        media_momento6 = request.POST['media_momento6']
        alt_momento6 = request.POST['alt_momento6']
        media_torque6 = request.POST['media_torque6']
        alt_torque6 = request.POST['alt_torque6']

        #Ma
        if alt_momento1:
            Ma = float(alt_momento1)
        elif alt_momento3:
            Ma = float(alt_momento3)
        elif alt_momento4:
            Ma = float(alt_momento4)
        elif alt_momento6:
            Ma = float(alt_momento6)
        else:
            Ma = float(0)

        #Mm
        if media_momento4:
            Mm = float(media_momento4)
        elif media_momento6:
            Mm = float(media_momento6)
        else:
            Mm = float(0)

        #Ta
        if alt_torque5:
            Ta = float(alt_torque5)
        elif alt_torque6:
            Ta = float(alt_torque6)
        else:
            Ta = float(0)

        #Tm
        if media_torque2:
            Tm = float(media_torque2)
        elif media_torque3:
            Tm = float(media_torque3)
        elif media_torque5:
            Tm = float(media_torque5)
        elif media_torque6:
            Tm = float(media_torque6)
        else:
            Tm = float(0)

        Sit = int(Sit)
        Acab = int(Acab)
        d = float(d)
        D = float(D)
        a = float(a)
        t = float(t)
        dinside = float(dinside)
        Temp = int(Temp)
        conf = int(conf)
        carga = int(carga)
        eq = int(eq)
        Mat = int(Mat)
        nseg = float(nseg)
        decide = int(decide)

        #r
        if r_entalhe1:
            r = float(r_entalhe1)
        elif r_entalhe2:
            r = float(r_entalhe2)
        elif r_entalhe2:
            r = float(r_entalhe3)
        else:
            r = 0.02*d

        if Sit == 1:
            in1 = D/d
            in2 = r/d
        elif Sit == 2:
            in1 = d/(d - 2*dinside)
            in2 = r/(d - 2*dinside)
            D = d
        elif Sit == 3:
            in1 = r/t
            in2 = a/t
        elif Sit == 4:
            in1 = 3000
            in2 = 3000

        # Valores de tensão de acordo com o material escolhido

        if Mat == 1:
            Sut = 420
            Sy = 350
        elif Mat == 2:
            Sut = 525
            Sy = 440
        elif Mat == 3:
            Sut = 585
            Sy = 515
        elif Mat == 4:
            Sut = 585
            Sy = 450
        elif Mat == 5:
            Sut = 620
            Sy = 485
        elif Mat == 6:
            Sut = 965
            Sy = 585
        elif Mat == 7:
            Sut = 560
            Sy = 460
        elif Mat == 8:
            Sut = 655
            Sy = 415
        elif Mat == 9:
            Sut = 580
            Sy = 425
        elif Mat == 10:
            Sut = 745
            Sy = 470
        elif Mat == 11:
            Sut = 138
            Sy = 97
        elif Mat == 12:
            Sut = 276
            Sy = 194
        elif Mat == 13:
            Sut = 414
            Sy = 276
        elif Mat == 14:
            Sut = 410
            Sy = 270
        elif Mat == 15:
            Sut = 550
            Sy = 375
        elif Mat == 16:
            Sut = 820
            Sy = 620
        else:
            Sut = float(Sut)
            Sy = float(Sy)

        # Obtendo informações dos dados de entrada

        info_ressalto = Ressalto(Sit)
        info_acabamento = Acabamento(Acab)
        info_temperatura = Temperatura(Temp)
        info_confiabilidade = Confiabilidade(conf)
        info_carga = Carga(carga)
        info_equilibrio = Equilibrio(eq)
        info_funcao = Funcao(decide)
        info_diametro = Diametro(d)
        info_fator = Fator(nseg)
        info_material = Material(Mat)

        # Cálculos básicos

        q1 = q(Sut, r)
        qs1 = qs(Sut, r)
        Kt1 = Kt(Sit, in1, in2)
        Kts1 = Kts(Sit, in1, in2)
        Kf1 = Kf(Sut, r, Sit, in1, in2)
        Kfs1 = Kfs(Sut, r, Sit, in1, in2)
        σa1 = σa(Kf1, Ma, d)
        σm1 = σm(Kf1, Mm, d)
        τa1 = τa(Kfs1, Ta, d)
        τm1 = τm(Kfs1, Tm, d)
        σal1 = σal(σa1, τa1)
        σml1 = σml(σm1, τm1)
        σmax1 = σmax(σa1, σm1, τa1, τm1)
        Sel1 = Sel(Sut)
        ka1 = ka(Sut, Acab)
        kb1 = kb(d)
        kc1 = kc(carga)
        kd1 = kd(Temp)
        ke1 = ke(conf)
        Se1 = Se(Sut, Acab, d, carga, conf, Temp)
        ηvm1 = ηvm(σmax1, Sy)
        AGerber1 = AGerber(Kf1, Ma, Kfs1, Ta)
        BGerber1 = BGerber(Kf1, Mm, Kfs1, Tm)
    
        # Resultado final

        result = resultado(decide, Sit, Se1, Sy, Sut, r, D, d, a, t, Kf1, Kfs1, Ma, Mm, Ta, Tm, σal1, σml1, ηvm1, AGerber1, BGerber1, nseg, info_material)
        return render(request, "results.html", {"info_ressalto": info_ressalto, "info_acabamento": info_acabamento, "info_temperatura": info_temperatura, "info_confiabilidade": info_confiabilidade, "info_carga": info_carga, "info_equilibrio": info_equilibrio, "info_funcao": info_funcao, "info_diametro": info_diametro, "info_fator": info_fator, "info_material": info_material, "result": result})

    # Tratamento de exceção

    except:
        return render(request, "error.html")