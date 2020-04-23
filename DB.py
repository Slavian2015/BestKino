
import pandas as pd
import numpy as np

import os

main_path_data = os.path.abspath("./data")



#################################   CREAT NEW FILES   ##########################################

if os.path.isfile(main_path_data + "\\server.csv"):
    pass
else:
    Mid = ['337788']
    poster = ['https://static.hdrezka.ac/i/2013/7/30/hd148876c2399hu76n85x.jpg']
    name = ['Железный человек']
    disc = ['"Тони Старк – миллиардер, филантроп и плейбой, но при этом он еще и гениальный изобретатель. Он ведет беззаботную жизнь, зарабатывая тем, что его компания создает оружие и оборудование для армии США. Однажды Тони отправляется в Афганистан, для демонстрации нового оружия. На конвой, который сопровождал Старка, совершается нападение, а его самого террористы берут в плен. Они требуют, чтобы он собрал для них новейшую разработку его компании – ракету «Иерихон». Тони соглашается, однако на самом деле разрабатывает и конструирует бронированный костюм, при помощи которого впоследствии и сбегает. Плен меняет внутренний мир Старка, по возвращению домой он усовершенствует свой костюм и начинает помогать людям. Теперь он «Железный человек»..."']
    category = ['soon']
    youtube = ['https://youtu.be/nAXX9eRDg4o']
    type = ['2D']
    pic1 = ['https://static.hdrezka.ac/i/2013/7/30/hd148876c2399hu76n85x.jpg']
    pic2 = ['https://static.hdrezka.ac/i/2013/7/30/hd148876c2399hu76n85x.jpg']
    pic3 = ['https://static.hdrezka.ac/i/2013/7/30/hd148876c2399hu76n85x.jpg']
    pic4 = ['https://static.hdrezka.ac/i/2013/7/30/hd148876c2399hu76n85x.jpg']
    pic5 = ['https://static.hdrezka.ac/i/2013/7/30/hd148876c2399hu76n85x.jpg']
    year = ['14 апреля 2008 года']
    country = ['USA']
    ganr = ['Боевики']
    time = ['126 мин']





    dtt = {'Mid': Mid,
           'poster': poster,
           'name': name,
           'disc': disc,
           'category': category,
           'youtube': youtube,
           'type': type,
           'pic1': pic1,
           'pic2': pic2,
           'pic3': pic3,
           'pic4': pic4,
           'pic5': pic5,
           'year': year,
           'country': country,
           'ganr': ganr,
           'time': time}

    # dtt = ['Mid',
    #        'poster',
    #        'name',
    #        'disc',
    #        'category',
    #        'youtube',
    #        'type',
    #        'pic1',
    #        'pic2',
    #        'pic3',
    #        'pic4',
    #        'pic5',
    #        'year',
    #        'country',
    #        'ganr',
    #        'time']



    dftt = pd.DataFrame(data=dtt)
    dftt.to_csv(main_path_data + "\\server.csv", index=False, header=True)
    pass