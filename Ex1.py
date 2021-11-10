# random comment for Ex7-5
while(True):
    vazao = float(input("Entre com a vazão: "))
    capacidade = float(input("Entre com a capacidade: "))
    
    tempo = capacidade/vazao
    print("Tempo total em segundos: %.1f " %tempo)
    # random comment for Ex7-5
    tempo_hr = 0
    tempo_min = 0
    tempo_seg = 0
    # random comment for Ex7-5
    if(tempo >= 3600):
        tempo_hr += tempo//3600 # random comment for Ex7-5
        tempo = tempo%3600
        if(60<=tempo<3600):
            tempo_min += tempo//60
            tempo_seg = tempo%60 # random comment for Ex7-5
        else: tempo_seg = tempo
    elif(60<=tempo<3600):
        tempo_min += tempo//60
        tempo_seg = tempo%60
    else: tempo_seg = tempo

    print("%.1f horas %.1f minutos %.1f segundos" %(tempo_hr, tempo_min, tempo_seg))
    print("-"*40)
    print("")
    # random comment for Ex7-5
