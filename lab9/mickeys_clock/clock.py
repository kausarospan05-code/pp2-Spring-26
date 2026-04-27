from datetime import datetime

def get_time_angles():
    now = datetime.now()

    seconds = now.second
    minutes = now.minute
    hours = now.hour % 12#Сағат форматын 24-тен 12-ге айналдырады. Себебі циферблатта 24 емес, 12 сағат қана бар.


    second_angle = -(seconds * 12)#Математикасы: Толық шеңбер — $360^\circ$. Бір минутта 60 секунд бар. Демек, 1 секунд = $360 / 60 = 6^\circ$.Неге минус (-)?: 
    #Pygame-де бұрыштар сағат тіліне қарсы бағытта есептеледі (математикалық тригонометриядағыдай). Сағат тілімен оңға қарай жылжуы үшін біз оны минусқа көбейтеміз.
    

    minute_angle = -(minutes * 6 + seconds * 0.1)#Ол минут тілінің тегіс (smooth) қозғалуын қамтамасыз етеді. Минут тілі бір минут біткенде "секіріп" кетпей, секундтар өткен сайын ақырындап жылжиды.
    

    hour_angle   = -(hours * 30 + minutes * 0.5)

    return hour_angle, minute_angle, second_angle