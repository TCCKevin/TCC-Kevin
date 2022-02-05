import math
import numpy as np
log = np.log

# Informações dos dados de entrada

def Ressalto(Sit):
    if Sit == 1:
        info_Sit = "Arredondamento no ressalto"
    elif Sit == 2:
        info_Sit = "Sulco no ressalto"
    elif Sit == 3:
        info_Sit = "Canal de fundo plano"
    elif Sit == 4:
        info_Sit = "Assento de chaveta de extremidade fresada r/d = 0,02"
    else:
        info_Sit = "Nulo"
    return info_Sit

def Acabamento(Acab):
    if Acab == 1:
        info_Acab = "Retificado"
    elif Acab == 2:
        info_Acab = "Usinado / Laminado a frio"
    elif Acab == 3:
        info_Acab = "Laminado a quente"
    elif Acab == 4:
        info_Acab = "Forjado"
    else:
        info_Acab = "Nulo"
    return info_Acab

def Temperatura(Temp):
    if Temp == 1:
        info_Temp = "20 °C"
    elif Temp == 2:
        info_Temp = "50 °C"
    elif Temp == 3:
        info_Temp = "100 °C"
    elif Temp == 4:
        info_Temp = "150 °C"
    elif Temp == 5:
        info_Temp = "200 °C"
    elif Temp == 6:
        info_Temp = "250 °C"
    elif Temp == 7:
        info_Temp = "300 °C"
    elif Temp == 8:
        info_Temp = "350 °C"
    elif Temp == 9:
        info_Temp = "400 °C"
    elif Temp == 10:
        info_Temp = "450 °C"
    elif Temp == 11:
        info_Temp = "500 °C"
    elif Temp == 12:
        info_Temp = "550 °C"
    elif Temp == 13:
        info_Temp = "600 °C"
    else:
        info_Temp = "Nulo"
    return info_Temp

def Confiabilidade(conf):
    if conf == 1:
        info_conf = "50%"
    elif conf == 2:
        info_conf = "90%"
    elif conf == 3:
        info_conf = "95%"
    elif conf == 4:
        info_conf = "99%"
    elif conf == 5:
        info_conf = "99.9%"
    elif conf == 6:
        info_conf = "99.99%"
    elif conf == 7:
        info_conf = "99.999%"
    elif conf == 8:
        info_conf = "99.9999%"
    else:
        info_conf = "Nulo"
    return info_conf

def Carga(carga):
    if carga == 1:
        info_carga = "Flexão pura"
    elif carga == 2:
        info_carga = "Torção pura"
    elif carga == 3:
        info_carga = "Flexão e torção"
    else:
        info_carga = "Nulo"
    return info_carga

def Equilibrio(eq):
    if eq == 1:
        info_eq = "Sim"
    elif eq == 2:
        info_eq = "Não"
    else:
        info_eq = "Nulo"
    return info_eq

def Funcao(decide):
    if decide == 1:
        info_decide = "Fator de segurança, com diâmetro conhecido"
    elif decide == 2:
        info_decide = "Diâmetro, com fator de segurança conhecido"
    elif decide == 3:
        info_decide = "Lista com o resultado de todos os critérios para fator de segurança"
    elif decide == 4:
        info_decide = "Lista com o resultado de todos os critérios para diâmetro"
    elif decide == 5:
        info_decide = "Validar um fator de segurança, com diâmetro escolhido"
    elif decide == 6:
        info_decide = "Validar um diâmetro, com fator de segurança escolhido"
    else:
        info_decide = "Nulo"
    return info_decide

def Diametro(d):
    if d != 0:
        info_diametro = "%.2f mm" %d 
    else:
        info_diametro = "-"
    return info_diametro

def Fator(nseg):
    if nseg != 0:
        info_fator = nseg
    else:
        info_fator = "-"
    return info_fator

def Material(Mat):
    if Mat == 1:
        info_Mat = "Aço SAE 1020"
    elif Mat == 2:
        info_Mat = "Aço SAE 1030"
    elif Mat == 3:
        info_Mat = "Aço SAE 1040"
    elif Mat == 4:
        info_Mat = "Aço SAE 1045"
    elif Mat == 5:
        info_Mat = "Aço SAE 1060"
    elif Mat == 6:
        info_Mat = "Aço SAE 1080"
    elif Mat == 7:
        info_Mat = "Aço SAE 4130"
    elif Mat == 8:
        info_Mat = "Aço SAE 4140"
    elif Mat == 9:
        info_Mat = "Aço SAE 4320"
    elif Mat == 10:
        info_Mat = "Aço SAE 4340"
    elif Mat == 11:
        info_Mat = "Ferro Fundido ASTM A48 Classe 20"
    elif Mat == 12:
        info_Mat = "Ferro Fundido ASTM A48 Classe 40"
    elif Mat == 13:
        info_Mat = "Ferro Fundido ASTM A48 Classe 60"
    elif Mat == 14:
        info_Mat = "Ferro Fundido ASTM A536 Classe 60-40-18"
    elif Mat == 15:
        info_Mat = "Ferro Fundido ASTM A536 Classe 80-55-06"
    elif Mat == 16:
        info_Mat = "Ferro Fundido ASTM A536 Classe 120-90-02"
    else:
        info_Mat = "-"
    return info_Mat

# Início do código

# Implementação das figuras

def reta(x0, y0, x1, y1, x):
    return (y0 + (y1 - y0)*(x - x0)/(x1 -  x0))

def Fig1(rDd, rrd):
    result109 = 0.8299*(rrd**(-0.165))
    result12 = 0.8013*(rrd**(-0.235))
    result133 = 0.8522*(rrd**(-0.232))
    result2 = 0.8148*(rrd**(-0.2688))
    if (rDd <= 1.09):
        result = result109
    elif (rDd <= 1.2):
        result = reta(1.09, result109, 1.2, result12, rDd)
    elif (rDd <= 1.33):
        result = reta(1.2, result12, 1.33, result133, rDd)
    elif (rDd <= 2):
        result = result = reta(1.33, result133, 2, result2, rDd)
    else:
        result = result2
    return result

def Fig2(rDd, rrd):
    result102 = 0.917*(rrd**(-0.2039))
    result105 = 0.9223*(rrd**(-0.2292))
    result11 = 0.9040*(rrd**(-0.2511))
    result15 = 0.8729*(rrd**(-0.2922))
    result3 = 0.8936*(rrd**(-0.3107))
    if (rDd <= 1.02):
        result = result102
    elif (rDd <= 1.05):
        result = reta(1.02, result102, 1.05, result105, rDd)
    elif (rDd <= 1.1):
        result = reta(1.1, result11, 1.05, result105, rDd)
    elif (rDd <= 1.5):
        result = reta(1.5, result15, 1.1, result11, rDd)
    elif (rDd <= 3):
        result = reta(1.5, result15, 3, result3, rDd)
    else:
        result = result3
    return result

def Fig3(rDd, rrd):
    result102 = 0.9932*(rrd**(-0.2006))
    result105 = 0.9731*(rrd**(-0.2593))
    result15 = 0.9579*(rrd**(-0.3201))
    if (rDd <= 1.02):
        result = result102
    elif (rDd <= 1.05):
        result = reta(1.02, result102, 1.05, result105, rDd)
    elif (rDd <= 1.5):
        result = reta(1.5, result15, 1.05, result105, rDd)
    else:
        result = result15
    return result

def Fig4(rDd, rrd):
    result102 = 0.9872*(rrd**(-0.1196))
    result105 = 0.9632*(rrd**(-0.1587))
    result13 = 0.8667*(rrd**(-0.2522))
    if (rDd <= 1.02):
        result = result102
    elif (rDd <= 1.05):
        result = reta(1.02, result102, 1.05, result105, rDd)
    elif (rDd <= 1.3):
        result = reta(1.3, result13, 1.05, result105, rDd)
    else:
        result = result13
    return result

def Fig5(rrt, rat):
    result003 = -0.8134*log(rat) + 8.6878
    result004 = -0.7040*log(rat) + 7.7962
    result005 = -0.6386*log(rat) + 7.1864
    result007 = -0.5793*log(rat) + 6.3311
    result010 = -0.4445*log(rat) + 5.5212
    result015 = -0.4971*log(rat) + 4.9092
    result020 = -0.4534*log(rat) + 4.5660
    result040 = -0.5045*log(rat) + 3.8376
    result060 = -0.6052*log(rat) + 3.6449
    result1 = -0.7237*log(rat) + 3.5022
    if rrt <= 0.03:
        result = result003
    elif rrt <= 0.04:
        result = reta(0.03,result003,0.04,result004, rrt)
    elif rrt <= 0.05:
        result = reta(0.05,result005,0.04,result004, rrt)
    elif rrt <= 0.07:
        result = reta(0.05,result005,0.07,result007, rrt)
    elif rrt <= 0.10:
        result = reta(0.10,result010,0.07,result007, rrt)
    elif rrt <= 0.15:
        result = reta(0.10,result010,0.15,result015, rrt)
    elif rrt <= 0.2:
        result = reta(0.2,result020,0.15,result015, rrt)
    elif rrt <= 0.4:
        result = reta(0.2,result020,0.4,result040, rrt)
    elif rrt <= 0.6:
        result = reta(0.6,result060,0.4,result040, rrt)
    elif rrt <= 1:
        result = reta(0.6,result060,1,result1, rrt)
    else:
        result = result1
    return result

def Fig6(rrt, rat):
    result003 = -0.0871*log(rat) + 4.6640
    result004 = -0.1608*log(rat) + 4.2970
    result006 = -0.1608*log(rat) + 3.7970
    result010 = -0.2552*log(rat) + 3.2393
    result020 = -0.2244*log(rat) + 2.6760
    if rrt <= 0.03:
        result = result003
    elif rrt <= 0.04:
        result = reta(0.03,result003,0.04,result004, rrt)
    elif rrt <= 0.06:
        result = reta(0.06,result006,0.04,result004, rrt)
    elif rrt <= 0.1:
        result = reta(0.06,result006,0.1,result010, rrt)
    elif rrt <= 0.2:
        result = reta(0.1,result010,0.20,result020, rrt)
    else:
        result = result020
    return result

# Cálculo de q, qs, Kt, Kts, Kf, Kfs

def q(Sut, r):
    Neuber = 0.246 - 0.308e-2*(Sut/6.89) + 0.151e-4*(Sut/6.89)**2 - 0.267e-7*(Sut/6.89)**3
    Neuber *= 25.4**0.5
    return (1/(1 + Neuber/(r**0.5)))
def qs(Sut, r):
    Neuber = 0.190 - 2.51e-3*(Sut/6.89) + 1.35e-5*(Sut/6.89)**2 - 2.67e-8*(Sut/6.89)**3
    Neuber*=25.4**0.5
    return (1/(1 + Neuber/(r**0.5)))

def Kt(Sit, in1, in2):
    if Sit == 1:
        Kt = Fig2(in1, in2)
    elif Sit == 2:
        Kt = Fig3(in1, in2)
    elif Sit == 3:
        Kt = Fig5(in1, in2)
    else:
        Kt = 2.14
    return Kt
def Kts(Sit, in1, in2):
    if Sit == 1:
        Kts = Fig1(in1, in2)
    elif Sit == 2:
        Kts = Fig4(in1, in2)
    elif Sit == 3:
        Kts = Fig6(in1, in2)
    else:
        Kts = 3
    return Kts

def Kf(Sut, r, Sit, in1, in2):
    return (1 + q(Sut,r)*(Kt(Sit, in1, in2) - 1))
def Kfs(Sut, r, Sit, in1, in2):
    return (1 + qs(Sut,r)*(Kts(Sit, in1, in2) - 1))

# Cálculo das tensões

def σa(Kf, Ma, d):
    return (32*Kf*Ma/(np.pi*((d/10)**3)))
def σm(Kf, Mm, d):
    return (32*Kf*Mm/(np.pi*((d/10)**3)))
def τa(Kfs, Ta, d):
    return (16*Kfs*Ta/(np.pi*((d/10)**3)))
def τm(Kfs, Tm, d):
    return (16*Kfs*Tm/(np.pi*((d/10)**3)))
def σal(σa, τa):
    return (σa**2 + 3*τa**2)**0.5
def σml(σm, τm):
    return (σm**2 + 3*τm**2)**0.5
def σmax(σa, σm, τa, τm):
    return ((σm + σa)**2 + 3*(τm + τa)**2)**0.5

# Definição dos coeficientes da equação de Marin 

def ka(Sut, Acab):
    if Acab == 1:
        a = 1.58
        b = -0.085
    elif Acab == 2:
        a = 4.51
        b = -0.265
    elif Acab == 3:
        a = 57.7
        b = -0.718
    elif Acab == 4:
        a = 272
        b = -0.995
    return (a*Sut**b)

def kb(d):
    if d >= 2.79 and d <= 51:
        kb = 1.24*d**-0.107
    elif d >= 51 and d <= 254:
        kb = 1.51*d**-0.107
    return kb

def kc(carga):
    if carga == 1:
        kc = 1
    elif carga == 2:
        kc = 0.59
    elif carga == 3:
        kc = 1
    return kc

def kd(Temp):
    if Temp == 1:
        kd = 1
    elif Temp == 2:
        kd = 1.01
    elif Temp == 3:
        kd = 1.02
    elif Temp == 4:
        kd = 1.025
    elif Temp == 5:
        kd = 1.02
    elif Temp == 6:
        kd = 1
    elif Temp == 7:
        kd = 0.975
    elif Temp == 8:
        kd = 0.943
    elif Temp == 9:
        kd = 0.9
    elif Temp == 10:
        kd = 0.843
    elif Temp == 11:
        kd = 0.768
    elif Temp == 12:
        kd = 0.672
    elif Temp == 13:
        kd = 0.549
    return kd
    
def ke(conf):
    if conf == 1:
        ke = 1
    elif conf == 2:
        ke = 0.897
    elif conf == 3:
        ke = 0.868
    elif conf == 4:
        ke = 0.814
    elif conf == 5:
        ke = 0.753
    elif conf == 6:
        ke = 0.702
    elif conf == 7:
        ke = 0.659
    elif conf == 8:
        ke = 0.62
    return ke

kf = 1

def Sel(Sut):
    if Sut <= 1400:
        Sel = 0.5*Sut
    else:
        Sel = 700
    return Sel

# Equação de Marin

def Se(Sut, Acab, d, carga, conf, Temp):
    return Sel(Sut)*ka(Sut, Acab)*kb(d)*kc(carga)*ke(conf)*kd(Temp)

# Fator de segurança para cada critério

def Goodman(σal, σml, Se, Sut):
    return (σal/Se + σml/Sut)**-1
def ηvm(σmax, Sy):
    return Sy/σmax
def Soderberg(σal, σml, Se, Sy):
    return (σal/Se + σml/Sy)**-1
def ASME(d, Kf, Ma, Se, Kfs, Ta, Mm, Tm, Sy):
    return (1/1000)*((16/(np.pi*d**3))*(4*(Kf*Ma/Se)**2 + 3*(Kfs*Ta/Se)**2 + 4*(Kf*Mm/Sy)**2 + 3*(Kfs*Tm/Sy)**2)**(1/2))**(-1)
def AGerber(Kf, Ma, Kfs, Ta):
    return (4*(Kf*Ma)**2 + 3*(Kfs*Ta)**2)**0.5
def BGerber(Kf, Mm, Kfs, Tm):
    return (4*(Kf*Mm)**2 + 3*(Kfs*Tm)**2)**0.5
def Gerber(AGerber, BGerber, d, Se, Sut):
    return (1/1000)*((8*AGerber/(np.pi*Se*d**3))*(1 + (1 + (2*BGerber*Se/(AGerber*Sut))**2)**0.5))**(-1)

# Escolha do fator de segurança

def fatordeseg(σal, σml, Se, Sut, σmax, Sy):
    if Goodman(σal, σml, Se, Sut) <= ηvm(σmax, Sy):
        η = Goodman(σal, σml, Se, Sut)
    else:
        η = Soderberg(σal, σml, Se, Sy)
    return η

# Diâmetro para cada critério

def dGoodman(η, Kf, Ma, Kfs, Ta, Mm, Tm, Se, Sut):
    return 10*(((1/Se)*(4*(Kf*Ma)**2 + 3*(Kfs*Ta)**2)**0.5 + (1/Sut)*(4*(Kf*Mm)**2 + 3*(Kfs*Tm)**2)**(1/2))*(16*η/np.pi))**(1/3)
def dSoderberg(η, Kf, Ma, Kfs, Ta, Mm, Tm, Se, Sy):
    return 10*(((1/Se)*(4*(Kf*Ma)**2 + 3*(Kfs*Ta)**2)**0.5 + (1/Sy)*(4*(Kf*Mm)**2 + 3*(Kfs*Tm)**2)**(1/2))*(16*η/np.pi))**(1/3)
def dvm(η, Kf, Ma, Kfs, Ta, Mm, Tm, Sy):
    return (((1/((np.pi*(Sy/η))**2))*((32*Kf*(Mm+Ma))**2 + 3*(16*Kfs*(Tm+Ta))**2))**(1/6))*10
def dASME(η, Kf, Ma, Se, Kfs, Ta, Mm, Tm, Sy):
    return 10*((16*η/np.pi)*(4*(Kf*Ma/Se)**2 + 3*(Kfs*Ta/Se)**2 + 4*(Kf*Mm/Sy)**2 + 3*(Kfs*Tm/Sy)**2)**0.5)**(1/3)
def dGerber(AGerber, BGerber, η, Se, Sut):
    return 10*((8*η*AGerber/(np.pi*Se))*(1 + (1 + (2*BGerber*Se/(AGerber*Sut))**2)**0.5))**(1/3)

# Escolha do diâmetro

def diameter(η, Kf, Ma, Kfs, Ta, Mm, Tm, Se, Sy, Sut):
    if dGoodman(η, Kf, Ma, Kfs, Ta, Mm, Tm, Se, Sut) >= dvm(η, Kf, Ma, Kfs, Ta, Mm, Tm, Sy):
        d = dGoodman(η, Kf, Ma, Kfs, Ta, Mm, Tm, Se, Sut)
    else:
        d = dSoderberg(η, Kf, Ma, Kfs, Ta, Mm, Tm, Se, Sy)
    return d

# Cálculo do resultado de acordo com a opção escolhida pelo usuário

def resultado(decide, Sit, Se, Sy, Sut, r, D, d, a, t, Kf, Kfs, Ma, Mm, Ta, Tm, σal, σml, ηvm, AGerber, BGerber, nseg, info_material):
    if decide == 1:
        nGoodman = Goodman(σal, σml, Se, Sut)
        nSoderberg = Soderberg(σal, σml, Se, Sy)
        if nGoodman <= ηvm:
            if nGoodman >= 1:
                resposta = "O fator de segurança de %.2f foi escolhido pelo critério de Goodman. O fator de falha por escoamento no primeiro ciclo de von Mises (%.2f) é maior ou igual a este valor." % (nGoodman, ηvm)
            else:
                resposta = "O fator de segurança de %.2f foi escolhido pelo critério de Goodman. Contudo, este valor é inferior a 1, e portanto a sua utilização não é recomendada. Algumas sugestões para aumentar o fator de segurança são: Aumentar o diâmetro do eixo; Selecionar um material mais resistente; Alterar o tipo de acabamento superficial." % (nGoodman)
        else:
            if nSoderberg >= 1:
                resposta = "O fator de segurança de %.2f foi escolhido pelo critério de Soderberg. Goodman (%.2f) falhou na checagem de falha por escoamento no primeiro ciclo, segundo o critério de von Mises (%.2f)." % (nSoderberg, nGoodman, ηvm)
            else:
                resposta = "O fator de segurança de %.2f foi escolhido pelo critério de Soderberg. Contudo, este valor é inferior a 1, e portanto a sua utilização não é recomendada. Algumas sugestões para aumentar o fator de segurança são: Aumentar o diâmetro do eixo; Selecionar um material mais resistente; Alterar o tipo de acabamento superficial." % (nSoderberg)
        return resposta

    elif decide == 2:
        if Sit == 1 or Sit == 2:
            Kfa = Kf(Sut, r, Sit, D/d, r/d)
            Kfsa = Kfs(Sut, r, Sit, D/d, r/d)
        elif Sit == 3:
            Kfa = Kf(Sut, r, Sit, r/t, a/t)
            Kfsa = Kfs(Sut, r, Sit, r/t, a/t)
        else:
            Kfa = Kf
            Kfsa = Kfs
        dGoodmann = dGoodman(nseg, Kfa, Ma, Kfsa, Ta, Mm, Tm, Se, Sut)
        dSoderbergg = dSoderberg(nseg, Kfa, Ma, Kfsa, Ta, Mm, Tm, Se, Sy)
        dvmm = dvm(nseg, Kfa, Ma, Kfsa, Ta, Mm, Tm, Sy)
        if dGoodmann >= dvmm:
            if nseg >= 1:
                resposta = "O diâmetro de %.2f mm foi escolhido pelo critério de Goodman. A falha por escoamento no primeiro ciclo foi checada pelo critério de von Mises (%.2f mm)." % (dGoodmann, dvmm)
            else:
                resposta = "O diâmetro de %.2f mm foi escolhido pelo critério de Goodman. Porém, como seu fator de segurança escolhido é inferior a 1, a sua utilização não é recomendada. Para eixos de transmissão, a literatura recomenda valores de fatores de segurança entre 2 e 3." % (dGoodmann)
        else:
            if nseg >= 1:
                resposta = "O diâmetro de %.2f mm foi escolhido pelo critério de Soderberg. Há risco de falha por escoamento no primeiro ciclo com Goodman (%.2f mm) segundo o critério de von Mises (%.2f mm)." % (dSoderbergg, dGoodmann, dvmm)
            else:
                resposta = "O diâmetro de %.2f mm foi escolhido pelo critério de Soderberg. Porém, como seu fator de segurança escolhido é inferior a 1, a sua utilização não é recomendada. Para eixos de transmissão, a literatura recomenda valores de fatores de segurança entre 2 e 3." % (dSoderbergg)
        return resposta

    elif decide == 3:
        nGoodman = Goodman(σal, σml, Se, Sut)
        nSoderberg = Soderberg(σal, σml, Se, Sy)
        nGerber = Gerber(AGerber, BGerber, d, Se, Sut)
        nASME = ASME(d, Kf, Ma, Se, Kfs, Ta, Mm, Tm, Sy)
        if (nGoodman >= 1) and (nSoderberg >= 1) and (nGerber >= 1) and (nASME >= 1):
            resposta = "Os fatores de segurança calculados por todos os critérios foram: Goodman = %.2f, Soderberg = %.2f, von Mises = %.2f, Gerber = %.2f, ASME = %.2f." % (nGoodman, nSoderberg, ηvm, nGerber, nASME)
        else:
            resposta = "Os fatores de segurança calculados por todos os critérios foram: Goodman = %.2f, Soderberg = %.2f, von Mises = %.2f, Gerber = %.2f, ASME = %.2f. Note que não é recomendada a utilização de fatores de segurança inferiores a 1. Algumas sugestões para aumentar os valores de fatores de segurança são: Aumentar o diâmetro do eixo; Selecionar um material mais resistente; Alterar o tipo de acabamento superficial." % (nGoodman, nSoderberg, ηvm, nGerber, nASME)
        return resposta

    elif decide == 4:
        if Sit == 1 or Sit == 2:
            Kfa = Kf(Sut, r, Sit, D/d, r/d)
            Kfsa = Kfs(Sut, r, Sit, D/d, r/d)
        elif Sit == 3:
            Kfa = Kf(Sut, r, Sit, r/t, a/t)
            Kfsa = Kfs(Sut, r, Sit, r/t, a/t)
        else:
            Kfa = Kf
            Kfsa = Kfs
        dGoodmann = dGoodman(nseg, Kfa, Ma, Kfsa, Ta, Mm, Tm, Se, Sut)
        dSoderbergg = dSoderberg(nseg, Kfa, Ma, Kfsa, Ta, Mm, Tm, Se, Sy)
        dvmm = dvm(nseg, Kfa, Ma, Kfsa, Ta, Mm, Tm, Sy)
        dASMEE = dASME(nseg, Kfa, Ma, Se, Kfsa, Ta, Mm, Tm, Sy)
        dGerberr = dGerber(AGerber, BGerber, nseg, Se, Sut)
        if nseg >= 1:
            resposta = "Os diâmetros calculados por todos os critérios foram: Goodman = %.2f mm, Soderberg = %.2f mm, von Mises = %.2f mm, Gerber = %.2f mm, ASME = %.2f mm." % (dGoodmann, dSoderbergg, dvmm, dGerberr, dASMEE)
        else:
            resposta = "Os diâmetros calculados por todos os critérios foram: Goodman = %.2f mm, Soderberg = %.2f mm, von Mises = %.2f mm, Gerber = %.2f mm, ASME = %.2f mm. Porém, como seu fator de segurança escolhido é inferior a 1, a sua utilização não é recomendada. Para eixos de transmissão, a literatura recomenda valores de fatores de segurança entre 2 e 3." % (dGoodmann, dSoderbergg, dvmm, dGerberr, dASMEE)
        return resposta

    elif decide == 5:
        if nseg >= 1:
            if Goodman(σal, σml, Se, Sut) <= ηvm:
                η = Goodman(σal, σml, Se, Sut)
                if nseg >= η:
                    resposta = "Seu fator de segurança de %.2f foi aprovado de acordo com o critério de Goodman. O fator de segurança de Goodman calculado foi de %.2f." % (nseg, η)
                else:
                    η = Soderberg(σal, σml, Se, Sy)
                    if nseg >= η:
                        resposta = "Seu fator de segurança de %.2f foi aprovado de acordo com o critério de Soderberg. O fator de segurança de Soderberg calculado foi de %.2f." % (nseg, η)
                    else:
                        ηGoodman = Goodman(σal, σml, Se, Sut)
                        ηSoderberg = Soderberg(σal, σml, Se, Sy)
                        if info_material != "-":
                            resposta = "Seu fator de segurança de %.2f NÃO foi aprovado de acordo com os critérios de Goodman e Soderberg. O fator de segurança pelo critério de Goodman é de %.2f, e pelo critério de Soderberg é de %.2f. Para manter esse mesmo diâmetro, é sugerido que um material mais resistente do que o " % (nseg, ηGoodman, ηSoderberg) + info_material + " seja selecionado, com tensão de escoamento superior a %.2f e tensão última superior a %.2f.  Você também pode alterar o tipo de acabamento superficial do material." % (Sy, Sut)
                        else:
                            resposta = "Seu fator de segurança de %.2f NÃO foi aprovado de acordo com os critérios de Goodman e Soderberg. O fator de segurança pelo critério de Goodman é de %.2f, e pelo critério de Soderberg é de %.2f. Para manter esse mesmo diâmetro, é sugerido que um material mais resistente seja selecionado, com tensão de escoamento superior a %.2f e tensão última superior a %.2f.  Você também pode alterar o tipo de acabamento superficial do material." % (nseg, ηGoodman, ηSoderberg, Sy, Sut)
            else:
                η = Soderberg(σal, σml, Se, Sy)
                if nseg >= η:
                    resposta = "Seu fator de segurança de %.2f foi aprovado de acordo com o critério de Soderberg. O fator de segurança de Soderberg calculado foi de %.2f." % (nseg, η)
                else:
                    ηGoodman = Goodman(σal, σml, Se, Sut)
                    ηSoderberg = Soderberg(σal, σml, Se, Sy)
                    if info_material != "-":
                        resposta = "Seu fator de segurança de %.2f NÃO foi aprovado de acordo com os critérios de Goodman e Soderberg. O fator de segurança pelo critério de Goodman é de %.2f e não foi aprovado pelo critério de von Mises (%.2f), e o fator de segurança pelo critério de Soderberg é de %.2f. Para manter esse mesmo diâmetro, é sugerido que um material mais resistente que o " % (nseg, ηGoodman, ηvm, ηSoderberg) + info_material + " seja selecionado, com tensão de escoamento superior a %.2f e tensão última superior a %.2f. Você também pode alterar o tipo de acabamento superficial do material." % (Sy, Sut)
                    else:
                        resposta = "Seu fator de segurança de %.2f NÃO foi aprovado de acordo com os critérios de Goodman e Soderberg. O fator de segurança pelo critério de Goodman é de %.2f e não foi aprovado pelo critério de von Mises (%.2f), e o fator de segurança pelo critério de Soderberg é de %.2f. Para manter esse mesmo diâmetro, é sugerido que um material mais resistente seja selecionado, com tensão de escoamento superior a %.2f e tensão última superior a %.2f. Você também pode alterar o tipo de acabamento superficial do material." % (nseg, ηGoodman, ηvm, ηSoderberg, Sy, Sut)
        else:
            resposta = "Seu fator de segurança de %.2f NÃO foi aprovado, pois seu valor é inferior a 1. Para eixos de transmissão, a literatura recomenda valores de fatores de segurança entre 2 e 3." % (nseg)
        return resposta
        
    elif decide == 6:
        if Sit == 1 or Sit == 2:
            Kfa = Kf(Sut, r, Sit, D/d, r/d)
            Kfsa = Kfs(Sut, r, Sit, D/d, r/d)
        elif Sit == 3:
            Kfa = Kf(Sut, r, Sit, r/t, a/t)
            Kfsa = Kfs(Sut, r, Sit, r/t, a/t)
        else:
            Kfa = Kf
            Kfsa = Kfs
        dGoodmann = dGoodman(nseg, Kfa, Ma, Kfsa, Ta, Mm, Tm, Se, Sut)
        dSoderbergg = dSoderberg(nseg, Kfa, Ma, Kfsa, Ta, Mm, Tm, Se, Sy)
        dvmm = dvm(nseg, Kfa, Ma, Kfsa, Ta, Mm, Tm, Sy)
        if nseg >= 1:
            if dGoodmann >= dvmm:
                if d >= dGoodmann:
                    resposta = "Seu diâmetro de %.2f mm foi aprovado de acordo com o critério de Goodman. O diâmetro calculado pelo critério de Goodman é de %.2f mm." % (d, dGoodmann)
                elif d >= dSoderbergg:
                    resposta = "Seu diâmetro de %.2f mm foi aprovado de acordo com o critério de Soderberg. O diâmetro calculado pelo critério de Soderberg é de %.2f mm." % (d, dSoderbergg)
                else:
                    resposta = "Seu diâmetro de %.2f mm NÃO foi aprovado de acordo com os critérios de Goodman e Soderberg. O diâmetro calculado pelo critério de Goodman é de %.2f mm, e o diâmetro pelo critério de Soderberg é de %.2f mm. É necessário aumentar o diâmetro do eixo ou selecionar um material mais resistente para manter o mesmo fator de segurança." % (d, dGoodmann, dSoderbergg)
            else:
                if d >= dSoderbergg:
                    resposta = "Seu diâmetro de %.2f mm foi aprovado de acordo com o critério de Soderberg. O diâmetro calculado pelo critério de Soderberg é de %.2f mm." % (d, dSoderbergg)
                else:
                    resposta = "Seu diâmetro de %.2f mm NÃO foi aprovado de acordo com os critérios de Goodman e Soderberg. O diâmetro calculado pelo critério de Goodman é de %.2f mm e não foi aprovado pelo critério de von Mises (%.2f mm), e o diâmetro pelo critério de Soderberg é de %.2f mm. Para manter o mesmo fator de segurança, é necessário aumentar o diâmetro do eixo ou selecionar um material mais resistente." % (d, dGoodmann, dvmm, dSoderbergg)
        else:
            if dGoodmann >= dvmm:
                if d >= dGoodmann:
                    resposta = "ATENÇÃO! Seu fator de segurança escolhido é inferior a 1, não sendo recomendada a sua utilização. Para eixos de transmissão, a literatura recomenda valores de fatores de segurança entre 2 e 3. Contudo, seu diâmetro de %.2f mm foi aprovado de acordo com o critério de Goodman. O diâmetro calculado pelo critério de Goodman é de %.2f mm." % (d, dGoodmann)
                elif d >= dSoderbergg:
                    resposta = "ATENÇÃO! Seu fator de segurança escolhido é inferior a 1, não sendo recomendada a sua utilização. Para eixos de transmissão, a literatura recomenda valores de fatores de segurança entre 2 e 3. Contudo, seu diâmetro de %.2f mm foi aprovado de acordo com o critério de Soderberg. O diâmetro calculado pelo critério de Soderberg é de %.2f mm." % (d, dSoderbergg)
                else:
                    resposta = "ATENÇÃO! Seu fator de segurança escolhido é inferior a 1, não sendo recomendada a sua utilização. Para eixos de transmissão, a literatura recomenda valores de fatores de segurança entre 2 e 3. De qualquer forma, seu diâmetro de %.2f mm NÃO foi aprovado de acordo com os critérios de Goodman e Soderberg. O diâmetro calculado pelo critério de Goodman é de %.2f mm, e o diâmetro pelo critério de Soderberg é de %.2f mm." % (d, dGoodmann, dSoderbergg)
            else:
                if d >= dSoderbergg:
                    resposta = "ATENÇÃO! Seu fator de segurança escolhido é inferior a 1, não sendo recomendada a sua utilização. Para eixos de transmissão, a literatura recomenda valores de fatores de segurança entre 2 e 3. Contudo, seu diâmetro de %.2f mm foi aprovado de acordo com o critério de Soderberg. O diâmetro calculado pelo critério de Soderberg é de %.2f mm." % (d, dSoderbergg)
                else:
                    resposta = "ATENÇÃO! Seu fator de segurança escolhido é inferior a 1, não sendo recomendada a sua utilização. Para eixos de transmissão, a literatura recomenda valores de fatores de segurança entre 2 e 3. De qualquer forma, seu diâmetro de %.2f mm NÃO foi aprovado de acordo com os critérios de Goodman e Soderberg. O diâmetro calculado pelo critério de Goodman é de %.2f mm e não foi aprovado pelo critério de von Mises (%.2f mm), e o diâmetro pelo critério de Soderberg é de %.2f mm. Para manter o mesmo fator de segurança, é necessário aumentar o diâmetro do eixo ou selecionar um material mais resistente." % (d, dGoodmann, dvmm, dSoderbergg)
        return resposta