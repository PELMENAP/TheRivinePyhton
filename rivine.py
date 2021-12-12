from threading import Thread
from playsound import playsound
from tkinter import *
from tkinter import messagebox as mb
from tkinter.ttk import Notebook
from json import dump, loads
from PIL import Image, ImageTk
from time import sleep
from random import randint, randrange
import os
import sys
import webbrowser

sys.setrecursionlimit(10000)

a = {
    "Здоровье": 90,
    "Усталость": 90,
    "Голод": 90,
    "Жажда": 90,
    "Внимательность": 0,
}
a_value = {
    "Здоровье": {10: "На грани смерти", 20: "Просто помираю", 40: "Не очень хорош", 60: "Ну жить можно", 80: "Побаливает кое-где", 1000: "Как огурчик"},
    "Усталость": {10: "Нет больше сил", 20: "Часик бы подремать", 40: "Глаз дёргается", 60: "Ноги точно устали", 80: "Скучно всё это", 1000: "Переполнен энергией"},
    "Голод": {10: "Мои пальцы выглядят аппетитно", 20: "Неуклонно стервенею", 40: "Супчика бы навернуть", 60: "Перекусить чё-нидь", 80: "Приятная лёгкость", 1000: "Больше не влезет"},
    "Жажда": {10: "Снова мираж", 20: "Можно пить слёзы?", 40: "И вот в пустыне я живу", 60: "В горле пересохло", 80: "Чаёв бы погонять", 1000: "Я есть вода"},
    "Внимательность": {10: "Слеподырая корова", 20: "", 40: "", 60: "", 80: "", 100: "Соколинный глаз"},
}
a_max = {
    "Здоровье": 100,
    "Усталость": 100,
    "Голод": 100,
    "Жажда": 100,
    "Внимательность": 10,
    "Вес": 10000,
}
opportunities = ["жизнь", "идти", "использовать"]
use_arguments = ["предмет", "окружение", "готовить", "выбросить"]
skill = {
    "атака": 5,
    "блок": 3,
    "уворот": 30,
    "сбежать": 20,
}
weapon = {
    "рука": 0,
    "палка": 4,
    "палка с ядом": 5,
    "стакан": 7,
    "ржавая коса": 24,
    "коса": 30,
    "ржавый топор": 19,
    "ПМ": 25,
}
stuff = {
    "стакан с отравленной водой": 2,
    "стакан с мутной водой": 0,
    "стакан с фильтром": 0,
    "стакан с водой": 0,
    "стакан": 0,
    "заплесневелые тряпки": 0,
    "ржавая игла": 0,
    "вонючий пух": 0,
    "карандаш": 0,
    "старый сухарь": 0,
    "упаковка газет": 0,
    "палка": 0,
    "палка с ядом": 0,
    "рука": 1,
    "вороний глаз": 0,
    "крапива": 0,
    "иван-чай": 0,
    "одуванчик": 0,
    "земляника": 0,
    "коса": 0,
    "ржавая коса": 0,
    "ржавый топор": 0,
    "спички": 0,
    "сено": 0,
    "отмычка": 0,
    "белый гриб": 0,
    "подберёзовик": 0,
    "рыжик": 0,
    "черника": 0,
    "дрова": 0,
    "спальный мешок": 0,
    "лесной чай": 0,
    "грибное рагу в стакане": 0,
    "сухарь": 0,
    "тушёнка из говядины": 0,
    "белое вино": 0,
    "ПМ": 0,
    "металлолом мал": 0,
    "пат 9х18": 0,
    "картошка": 0,
    "картошка в пепле": 0,
}
weight = {
    "стакан с отравленной водой": 330,
    "стакан с мутной водой": 320,
    "стакан с фильтром": 380,
    "стакан с водой": 300,
    "стакан": 200,
    "заплесневелые тряпки": 50,
    "ржавая игла": 2,
    "вонючий пух": 1,
    "карандаш": 8,
    "старый сухарь": 40,
    "упаковка газет": 80,
    "палка": 400,
    "палка с ядом": 410,
    "вороний глаз": 10,
    "крапива": 20,
    "иван-чай": 40,
    "одуванчик": 10,
    "земляника": 1,
    "коса": 6000,
    "ржавая коса": 5800,
    "ржавый топор": 3900,
    "спички": 2,
    "сено": 100,
    "отмычка": 50,
    "белый гриб": 50,
    "подберёзовик": 50,
    "рыжик": 50,
    "черника": 1,
    "дрова": 1000,
    "спальный мешок": 1500,
    "лесной чай": 320,
    "грибное рагу в стакане": 450,
    "сухарь": 50,
    "тушёнка из говядины": 400,
    "белое вино": 1200,
    "ПМ": 1500,
    "металлолом мал": 100,
    "пат 9х18": 40,
    "картошка": 80,
    "картошка в пепле": 60,
}
eat = [
    "стакан с отравленной водой",
    "стакан с мутной водой",
    "стакан с водой",
    "старый сухарь",
    "земляника",
    "черника",
    "лесной чай",
    "грибное рагу в стакане",
    "сухарь",
    "тушёнка из говядины",
    "белое вино",
    "картошка в пепле",
]
myweight = 0
kraft = {}
dish = {}
map = []
stuff_clearing_at_the_dugout = {
    "small_haystack_crude": 0,
    "small_haystack_dry": 0,
}
burn_down_dugout = False
lock_door_dugout = False
catch_nightstand = {}
catch_hole = {"сухарь": 30, "тушёнка из говядины": 10, "белое вино": 4}
time_to_burn_down = 0
day_to_burn_down = 0
exlimit = 10
ex = 0
level = 0
tim = [0, 8, 0, 0]
locations = "basic_room_bed"
locations_till = "hell"
location_prepare_for_fire = "hell"
location_of_fire = "hell"
count = {
    "count_bed": 0,
    "count_nightstand": 0,
    "count_door": 0,
    "count_edge_of_forest": 0,
    "count_birch_forest": 0,
    "count_food": 0,
    "count_water": 0,
}
record = []
hard_play_2 = False
fight_with_near_weller = False
improvement = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0}
task_1 = 0
click = False
energy = False
ticket = False
frame_destroy = False
e = 0


def update_live(a):
    live = ""
    for i in a_value:
        for j in a_value[i]:
            if a[i] <= j and a[i] > 0:
                live += i + " : " + a_value[i][j] + "\n"
                break
    helpl.config(text=live)


def update_text(text, type=True):
    if type == True:
        delta = 10
        delay = 0
        for i in range(len(text) + 1):
            s = text[:i]

            def update(s=s):
                return txt.config(text=s)
            txt.after(delay, update)
            delay += delta
    else:
        txt['text'] = text


def update_image(path):
    img = ImageTk.PhotoImage(Image.open(path))
    im.configure(image=img)
    im.image = img


class Rec:
    def __init__(self):
        self.already_called = False

    def __call__(self, number):
        global ex
        if not self.already_called:
            if number == 2:
                if 2 in record:
                    self.already_called = True
                else:
                    print(
                        "Хера, стакан. И с водой, не заметил по началу. Повезло, повезло. Немного мутной но ничего\n"
                        "ПОЛУЧЕН ТРЕДМЕТ :стакан с мутной водой:"
                    )
                    stuff["стакан с мутной водой"] += 1
                    ex += 1
                    tim[3] += 2
                    record.append(2)
            elif number == 3:
                update_live(a)
                ex += 1
                tim[3] += 2
                print(
                    " Вы проснулись на месте, окружены страхом к неизвестному.\n"
                    " Вас не покидали мысли о жажде жить, да и о простой жажде желание было сильно. \n Немного покорячившись вы собрались с духом и приподнялись."
                    " Пред вами открылся незамысловатый пейзаж,\n будто вы не чудом выживший путешественник неизведанного мира, а алкаш с соседнего подъезда.\n"
                    " Все же страх одолел вами и сердце застучало так громко, что старые стены затрещали от внезапных ударов.\n"
                    " Почерневшая от плесении кровать, сломаная тумбочка, разбитое вдребезги окно и дверь... \n Самое главное что от неё шёл слабый ручеёк света, вероятно, исходяший не от родной звезды\n"
                    " Справа вы увидите необходимые параметры. Жмакните там что-нибудь внизу"
                )
            elif number == 4:
                if 3 in record:
                    self.already_called = True
                else:
                    print(
                        " Стоять, это не свет. Ааа... Тьфу ты. Картина. Ну и дела, а впрочем даже красивая\n"
                        " (заглянув за дверь вы разглядели картину похуже)\n"
                        " Это в прямом смысле этого слова пиздец. Такого количество грязи и дерьма не наблюдалось даже в сельском туалете\n"
                        ' (в скобку будут заключены мысли и важные заметки (не все), прочитать их снова можно командой "дневник")\n'
                    )
                    tim[3] += 5
                    ex += 2
                    record.append(3)
            elif number == 5:
                if 4 in record:
                    self.already_called = True
                else:
                    print(
                        "(На тумбочке лежал школьный дневник и вы сочли правильным записывать туда выжные заметки)\n"
                        "ПОЛУЧЕН ТРЕДМЕТ :школьный дневник:\n"
                        "\n"
                        "В ДНЕВНИКЕ ПОЯВИЛАСЬ ЗАПИСЬ 1\n"
                        " Блять, а это я зачем вспоминаю? Только хуже становиться\n"
                    )
                    stuff["школьный дневник"] = 1
                    tim[3] += 2
                    ex += 8
                    record.append(4)
            elif number == 6:
                if 5 in record:
                    self.already_called = True
                else:
                    print(
                        "Неплохо так. Я про обстановочку. Это землянка оказывается и чё я так много времени просидел там?\n"
                        "Тааак, что тут у нас? Опушка, ввероятно со вкусностями, судя по кружащим стаям птиц. И дорожка, протоптаная ещё давно\n"
                        "Впринципе и такая жизнь меня больше устраивает, чем в городе. Адреналин как-никак, и много чего неизвестного. А вот с компом был бы вообще шик\n"
                        "Один, один в хижине. Странно что ещё не один медведь меня не сожрал, и даже не поинтересовался, соли не попросил\n"
                        "(землянка была обитаема, это заметно сразу.)\n"
                        "О чёрт, а зачем хозяину сия строяния я? (Тут по неволе вам становиться жутко) Думаю лесник меня бы наоборот отправил в город. А тут\n"
                        "(думать придётся быстро, так как уже в гуще леса послышался треск сухих веток)\n"
                        "КТО-ТО ИДЁТ БЛЯТЬ. Если лось то спрячюсь в будке. А если хозяин, а если не он? Сообразить надо побыстрее\n"
                    )
                    hard_play(1)
                    ex += 2
                    record.append(5)
            elif number == 7:
                if 6 in record:
                    self.already_called = True
                else:
                    print(
                        "Как же тут хорошо, ни суеты, ни движения. Только изредка покрикивают вороны, да поёт соловей\n"
                        "Ух ты, сколько ягод. Думаю, таких запасов не на одну зиму хватит\n"
                        "(Рядом стояла коса, вы её конечно же подобрали)"
                    )
                    stuff["ржавая коса"] += 1
                    ex += 1
                    record.append(6)
            elif number == 8:
                if 7 in record:
                    self.already_called = True
                else:
                    if tim[1] >= 21 or tim[1] <= 4:
                        print(
                            "Вау, ещё удивляет как я в такой темноте нашёл карту\n"
                            "(ПОЛУЧЕН ПРЕДМЕТ :карта ЛесХоз 'Берёзка':)"
                        )
                        map.append("ЛесХоз 'Берёзка'")
                        stuff["карта 'ЛесХоз Берёзка' "] = 1
                        ex += 5
                        record.append(7)
            elif number == 9:
                if 8 in record:
                    self.already_called = True
                else:
                    print(
                        "Рядом с колодцем стоит стакан, неплохо, заскучал навеное уже стоять"
                    )
                    print(
                        "Ну-ка мечи стаканы на стол, Ну-ка мечи стаканы на стол, Ну-ка мечи стаканы на стол, и прочюю посуду"
                    )
                    print("(ПОЛУЧЕН ПРЕДМЕТ :стакан:)")
                    stuff["стакан"] += 1
                    ex += 2
                    record.append(8)
            elif number == 10:
                if 9 in record:
                    self.already_called = True
                else:
                    if tim[1] >= 21 or tim[1] <= 4:
                        print("Лось, ебать")
                        fight("moose")
                    print("ВАУ! Колобок, 6 спичек насчитал")
                    print("(ПОЛУЧЕН ПРЕДМЕТ :спички:)")
                    stuff["спички"] += 6
                    ex += 3
                    record.append(9)
            elif number == 11:
                if 10 in record:
                    self.already_called = True
                else:
                    print(
                        " Ох как тяжело. Кровать конечно замечательная, ничего не скажешь, но продвигаться куда-то нужно\n"
                        " Тем более руки уже онемели от такого прордолжительного отлёживания и полусонного дрёмa\n"
                        " Честное слово, ну произнесите хоть кто-нибуд: что здесь происходит?\n"
                        " Задрали. Ну и поделом. Может и я уже конфузился и начал нести всякую чушь\n"
                        " Нихера. Нихера не понятно. По крайней мере можно доковылять до тумбочки или к двери"
                    )
                    tim[3] += 2
                    ex += 4
                    record.append(10)
            elif number == 12:
                print(
                    "(Впредь, после такой бяки можно много бонусов заработать, медленно отнимающих жизнь)"
                )
            elif number == 13:
                print(
                    " (Укол ржавой иглой не сулит ничего хорошего.)\n"
                    " (Позже, с помощью иных средств, вы сможете выявлять заражение и преждевременно его устранять)"
                )
                ex += 1
            elif number == 14:
                if 11 in record:
                    self.already_called = True
                else:
                    print("ПОЛУЧЕН ПРЕДМЕТ :РЖАВЫЙ ТОПОР:")
                    stuff["ржавый топор"] += 1
                    ex += 2
                    record.append(11)
            elif number == 15:
                if 12 in record:
                    self.already_called = True
                else:
                    stuff["отмычка"] -= 1
                    print(
                        "Поковыряв входную дверь отмычкой, через несколько минут она всё-же поддалась\n"
                        "Это оказался погреб, с ещё сохранившимися вкусностями и, самое главное, с ОРУЖИЕМ\n"
                        "ПОЛУЧЕН ПРЕДМЕТ :ПМ:"
                    )
                    stuff["ПМ"] += 1
                    ex += 6
                    record.append(12)
            elif number == 16:
                if 13 in record:
                    self.already_called = True
                else:
                    print(
                        "А местечко само посебе неплохое, четыре дороги срастаются всместе у общего указателя\n"
                        "В отличие от всего произошедшего, эта картина поражает больше всего, даже понятия не имею почему\n"
                        "(шелест кустов)\n"
                        "- Кто там! Знай, я палкой махать умею. Выходи, или проваливай с моего пути!\n"
                        "- Ты кто? (тихий голос)\n"
                        "- Взаимно\n"
                        "- Я вот путешествую\n"
                        "- А я вот хочу знать, где путешествую. Грёбаный яндекс навигатор\n"
                        "- Впервые не трарь какая-то, повезло (из оврага вылезает нечто, полу человек - полу филин, как человек на маскараде. Да вот нет, не человек)\n"
                        "Меня Тэн зовут, через Порог у двух ворот на Воробьёвы горы хочу попасть, говорят там жить - сказка одна. Такое живописное место, ты просто представить не можешь\n"
                        "- Ты что такое? Как ты вообще оказалось в нашем мире?\n"
                        "- А МОЖЕТ ТЫ, НЕ В ТОМ МИРЕ ОКАЗАЛСЯ? Да ладно, я вот лагерь неподалёку разбил, хожу теперь, вкусности собираю. Ты заходи, не бойся. Знанием не обижу (уходит)\n"
                        "Чё это сейчас было? А может я и вправду не дома, и в принципе, не на Земле\n"
                        "Ой, наприходит чушь всякая, потом спать не могу. Ладно, чего у нас тут\n"
                        "\n"
                    )
                    ex += 1
                    record.append(13)
            elif number == 17:
                if 14 in record:
                    self.already_called = True
                else:
                    print(
                        "Да, ну и пейзаж. Почти до тла выжженые дома и висельницы на каждом углу с уже просохшими насквозь мумиями\n"
                        "Незнаю что тут и делать? Может порыскать чего\n"
                    )
                    ex += 4
                    record.append(14)
            elif number == 18:
                if 15 in record:
                    self.already_called = True
                else:
                    print(
                        "Выйдя на двор перед неплохо отделанным зданием лесничества, вы в первую очередь обратили внимание на автомобиль, стоящий под внешней террасой, смотрящей прямо в сторону асфальной дороги\n"
                        "А само двухэтажное здание могло похвастаться многообразием комнат, вероятно, со всяческими ценностями\n"
                        "По правилу 34 в близлежащей записке необходимо было зайти сбоку сдания, чтобы не попасться в цепкие лапы сигнализационных систем\n"
                        "ПОЛУЧЕН ПРЕДМЕТ :планировка здания №34:\n"
                    )
                    stuff["планировка здания №34"] = 1
                    map.append("Здание №34")
                    ex += 5
                    record.append(15)
            self.already_called = True


rec = Rec()
rec2 = Rec()
rec3 = Rec()
rec4 = Rec()
rec5 = Rec()
rec6 = Rec()
rec7 = Rec()
rec8 = Rec()
rec9 = Rec()
rec10 = Rec()
rec11 = Rec()
rec12 = Rec()
rec13 = Rec()
rec14 = Rec()
rec15 = Rec()
rec16 = Rec()
rec17 = Rec()
rec18 = Rec()
rec19 = Rec()


class diary:
    def __init__(self, number):
        self.number = number

    def record_1(self, number):
        if self.number == 1:
            if number == 1:
                print(
                    " (Где же мой любимый домик с мягкой кроваткой и тёплым камином, а самое главное с мощным компом)\n"
                    " (Помню как во весь стим переиграл, недолго это все было. Наскучило. Но 8 лет из-за компьютера точно не выходил)\n"
                    " (Вот там то и кипит настоящая жизнь с такими замечательными видами, что огого. И люди, да и не только люди там замечательные)\n"
                )
            elif number == 2:
                print(
                    "Этто ббыло нечто. Такого холодного, да ладно УЖАСА вы не испылывали в новейших частях Resident evil, а Outlast вообще превратился в сказочку\n"
                    "Еле пробравшаяся огромная туша шла вам навстречу. Не человек, МУТАНТ, предстал пред вами во всей красе\n"
                    "Кожа, покрытая огромными волдырями и нарывами, бросит в дрожь любого хирурга. В грязных нарывах копошились личинки\n"
                    "Его глаза светились, не то чтобы светом. Страхом. Уродливое лицо обратило на вас взор, честное слово я бы рванул на месте\n"
                    "Мощное тело поплыло мощным потоком прямо на вас\n"
                    "\n"
                )
            elif number == 3:
                print(
                    "Провалившись в люк в полу норки вы очутились в проходе, по ощущению явно не посреди леса\n"
                    "Тоннель, в котором вы оказались, был весь освещён и по его стенам были проложены трубы\n"
                    "Пройдя чуть дальше вы оказались.. В МЕТРО..ПОСРЕДИ ЛЕСА?\n"
                    "Факт не то чтобы испугал, но удивление пробежалось по всему телу\n"
                    "Интересно, но карта показывала совсем другое, да и зачем в такой глуши метро?\n"
                    "Голова была завалена вопросами, а ноги уж сами побрели вглубь\n"
                    "Пройдя метров сто вы очутились в совсем фантастическом месте\n"
                    "Мало того, что это метро было заброшено одной цивилизацией, дак оно ещё и стало домом для другой\n"
                    "Какие-то примитивные дома и склады, освещения кот нарыдал\n"
                    "Ох, вот он! Хозяин всея подземелья, я тебя не забыл"
                )


def save(file="save.txt"):
    global burn_down_dugout
    global ex
    global locations
    global hard_play_2
    global improvement
    global map
    global frame_destroy
    botton_frame_1.destroy()
    with open(file, "w") as file_obj:
        dump(a, file_obj)
        file_obj.write("\n")
        dump(a_max, file_obj)
        file_obj.write("\n")
        dump(skill, file_obj)
        file_obj.write("\n")
        dump(burn_down_dugout, file_obj)
        file_obj.write("\n")
        dump(ex, file_obj)
        file_obj.write("\n")
        dump(tim, file_obj)
        file_obj.write("\n")
        dump(locations, file_obj)
        file_obj.write("\n")
        dump(count, file_obj)
        file_obj.write("\n")
        dump(hard_play_2, file_obj)
        file_obj.write("\n")
        dump(stuff, file_obj)
        file_obj.write("\n")
        dump(improvement, file_obj)
        file_obj.write("\n")
        dump(stuff_clearing_at_the_dugout, file_obj)
        file_obj.write("\n")
        dump(catch_hole, file_obj)
        file_obj.write("\n")
        dump(catch_nightstand, file_obj)
        file_obj.write("\n")
        dump(record, file_obj)
        file_obj.write("\n")
        dump(map, file_obj)
    print("Успешно сохранено")
    game()


def load(file="save.txt"):
    global burn_down_dugout
    global ex
    global locations
    global hard_play_2
    global improvement
    global a
    global a_max
    global skill
    global tim
    global count
    global stuff
    global stuff_clearing_at_the_dugout
    global catch_hole
    global catch_nightstand
    global record
    global map
    global botton_frame_1
    global frame_destroy
    botton_frame_1.destroy()
    for linenum, line in enumerate(open(file)):
        if linenum == 0:
            a = loads(line)
        elif linenum == 1:
            a_max = loads(line)
        elif linenum == 2:
            skill = loads(line)
        elif linenum == 3:
            burn_down_dugout = loads(line)
        elif linenum == 4:
            ex = loads(line)
        elif linenum == 5:
            tim = loads(line)
        elif linenum == 6:
            locations = loads(line)
        elif linenum == 7:
            count = loads(line)
        elif linenum == 8:
            hard_play_2 = loads(line)
        elif linenum == 9:
            stuff = loads(line)
        elif linenum == 10:
            improvement = loads(line)
        elif linenum == 11:
            stuff_clearing_at_the_dugout = loads(line)
        elif linenum == 12:
            catch_hole = loads(line)
        elif linenum == 13:
            catch_nightstand = loads(line)
        elif linenum == 14:
            record = loads(line)
        elif linenum == 15:
            map = loads(line)
    print("Успешно загружено")
    game()


my_diary = diary(1)


def game_over():
    Game.destroy()
    print()
    print("---------------------------------------------")
    print()
    print("Игра окончена")
    sys.exit(0)


def the_end():
    print()
    print(
        "Молодец, ты прошёл версию 2.0.0 Осталось пожелать тебе удачи и попросить по возможности поддержать проект"
    )
    print()
    print()
    print("---------------------------------------------")
    print()
    print("Игра окончена")
    os._exit(0)


def fight(enemy):
    global ex
    enemy_spell = []
    if enemy == "medium_mutant_forester":
        print("\n" "Туша полупрогнившего лестника втала у вас на пути" "\n")
        enemy_heath = 120
        enemy_block = 7
        enemy_atack = 9
        enemy_move_chance = 30
        enemy_lim = 100
    elif enemy == "medium_mutant_forester_damaged":
        print(
            "\n"
            "Туша полупрогнившего лестника, слегка помятого, втала у вас на пути"
            "\n"
        )
        enemy_heath = 100
        enemy_block = 6
        enemy_atack = 8
        enemy_move_chance = 20
        enemy_lim = 90
    elif enemy == "wolf":
        print("\n" "Волк одиночка хочет укусить вас за бочок" "\n")
        enemy_heath = 110
        enemy_block = 2
        enemy_atack = 15
        enemy_move_chance = 50
        enemy_lim = 100
    elif enemy == "moose":
        print("\n" "Вы перегородили дорогу лосю. Или он вам?" "\n")
        enemy_heath = 220
        enemy_block = 6
        enemy_atack = 10
        enemy_move_chance = 10
        enemy_lim = 90
    elif enemy == "moose_mutant":
        print("\n" "Вы перегородили дорогу мутировавшему лосю. Или он вам?" "\n")
        enemy_heath = 420
        enemy_block = 8
        enemy_atack = 20
        enemy_move_chance = 15
        enemy_lim = 80
    elif enemy == "near_weller":
        print("\n" "Пред вами встал уродец без ног" "\n")
        enemy_heath = 320
        enemy_block = 10
        enemy_atack = 13
        enemy_move_chance = 15
        enemy_spell.append("fear")
        enemy_lim = 120
    elif enemy == "rat":
        print("\n" "Злые серые комочки")
        n = randint(1, 11)
        print("Aж " + str(n) + " штук" "\n")
        enemy_heath = 20 * n
        enemy_block = 1
        enemy_atack = 5 * n
        enemy_move_chance = 40
        enemy_lim = 95
    fear = False
    enemy_lock = False
    enemy_move = False
    combo = 0
    poison = 0
    print()
    print("Способности: ")
    for i in skill:
        if i == "атака":
            print(i.upper() + " урон: " + str(skill[i]))
        elif i == "блок":
            print(i.upper() + " можно заблокировать: " +
                  str(skill[i]) + " урона")
        elif i == "уворот":
            print(i.upper() + " с шансом: " + str(skill[i]))
        elif i == "сбежать":
            print(i.upper() + " с шансом: " + str(skill[i]))
    while enemy_heath > 0:
        print()
        print("Противник")
        print("Здоровье " + str(enemy_heath))
        print("Блок " + str(enemy_block))
        print("Атака " + str(enemy_atack))
        print("Шанс уворота " + str(enemy_move_chance))
        print()
        print("Вы")
        print("Здоровье " + str(a["Здоровье"]))
        print("Блок " + str(skill["блок"]))
        print("Атака " + str(skill["атака"]))
        print("Шанс уворота " + str(skill["уворот"]))
        print()
        my_block = False
        my_move = False
        cho = input("Ваш выбор: ")
        if cho == "атака" or cho == "а":
            if fear == False:
                print()
                print("Вы можете атаковать:")
                for i in weapon:
                    if stuff[i] > 0:
                        print(i + " + " + str(weapon[i]), end="    ")
                print()
                cho = input("Ваш выбор: ")
                print()
                for i in weapon:
                    if cho == i:
                        if stuff[i] > 0:
                            if cho == "стакан":
                                stuff["стакан"] -= 1
                                a["Усталость"] -= 2
                                damaged = skill["атака"] + weapon[i]
                                if randint(1, 10) < 8:
                                    if enemy_lock == True:
                                        print("Вроде попал")
                                        enemy_heath -= damaged - enemy_block
                                        print(
                                            "Нанесено "
                                            + str(damaged - enemy_block)
                                            + " урона"
                                        )
                                    elif enemy_move == True:
                                        print(
                                            "Хах, хотел увернуться, а прилетает вот это"
                                        )
                                        enemy_heath -= damaged * 2
                                        print("Нанесено " +
                                              str(damaged * 2) + " урона")
                                    else:
                                        print("В яблочко")
                                        enemy_heath -= damaged
                                        print("Нанесено " +
                                              str(damaged) + " урона")
                                else:
                                    print("Прям перед ухом пролетел")
                            elif cho == "ПМ":
                                if stuff["пат 9х18"] > 0:
                                    stuff["пат 9х18"] -= 1
                                    damaged = skill["атака"] + weapon[i]
                                    if randint(1, 10) < 8:
                                        if enemy_lock == True:
                                            print("Вроде попал")
                                            enemy_heath -= damaged - enemy_block
                                            print(
                                                "Нанесено "
                                                + str(damaged - enemy_block)
                                                + " урона"
                                            )
                                        elif enemy_move == True:
                                            print(
                                                "Хах, хотел увернуться, а прилетает вот это"
                                            )
                                            enemy_heath -= damaged * 2
                                            print(
                                                "Нанесено "
                                                + str(damaged * 2)
                                                + " урона"
                                            )
                                        else:
                                            print("В яблочко")
                                            enemy_heath -= damaged
                                            print("Нанесено " +
                                                  str(damaged) + " урона")
                                    else:
                                        print("Промах")
                                else:
                                    print("Патронов нет")
                            else:
                                damaged = (
                                    skill["атака"] + weapon[i] +
                                    randrange(-2, 2)
                                )
                                if damaged < 0:
                                    damaged = 0
                                if enemy_lock == True:
                                    if cho == "ржавый топор":
                                        print("Разрубил всю его защиту!")
                                        enemy_heath -= damaged * 2
                                        print("Нанесено " +
                                              str(damaged * 2) + " урона")
                                    else:
                                        print("Вроде попал")
                                        damaged_block = damaged - enemy_block
                                        if damaged_block < 0:
                                            damaged_block = 0
                                        enemy_heath -= damaged_block
                                        print(
                                            "Нанесено " +
                                            str(damaged_block) + " урона"
                                        )
                                elif enemy_move == True:
                                    print("Изворотливый гад")
                                    print("Нанесено 0 урона")
                                else:
                                    print("Хороший шлепок")
                                    enemy_heath -= damaged
                                    print("Нанесено " + str(damaged) + " урона")
                                if cho == "палка с ядом":
                                    print("В рану, оставленной палкой, затёк яд")
                                    poison = 3
                        else:
                            print("Да нет у меня такого!")
                        break
            else:
                print("Вы не можете атаковать из-за применённого заклинания")
        elif cho == "блок" or cho == "б":
            print()
            print("В защиту")
            my_block = True
        elif cho == "уворот" or cho == "у":
            if randint(1, 100) <= skill["уворот"]:
                print()
                print("Ебать я змея нахуй")
                my_move = True
            else:
                print()
                print("Чёт как-то не задалось")
        elif cho == "сбежать" or cho == "с":
            if randint(1, 100) <= skill["сбежать"]:
                if enemy == "medium_mutant_forester":
                    print(
                        "Не рызмышляя вы пустились прочь, только пятки засверкали. Даже не смотря под ноги вы упали в глубокий овраг насмерь расшибив себе все, что можно"
                    )
                    game_over()
                elif locations == "hole":
                    print(
                        "Метнувшись, вы упали на пути. И вдруг, откуда не возьмись, из-за поворота поехал поезд"
                    )
                    game_over()
                else:
                    print("Вы растворились у противника на глазах")
                    game()
            else:
                print("Неудачно, он следует за мной")
        else:
            print("Чё? Или я не понял")
        if poison > 0:
            print("Действует яд")
            enemy_heath -= 5
            print("Нанесено 5 урона")
            poison -= 1
        if locations == "camp_on_the_sink" and tim[0] < 10:
            print()
            print("Атака Тэна")
            print("Нанесено 120 урона")
            enemy_heath -= 120
        print()
        fear = False
        enemy_move = False
        enemy_lock = False
        if enemy_heath > 40:
            ran = randint(1, enemy_lim)
        else:
            ran = randint(1, enemy_lim - 10)
        if combo == 1 or combo == 2:
            ran = 5
        if ran <= 50:
            print("Атака противника")
            if enemy == "medium_mutant_forester_damaged":
                ran = 0
            else:
                ran = randrange(-2, 2)
            damaged = enemy_atack + ran
            if damaged < 0:
                damaged = 0
            if my_block == True:
                damaged_block = damaged - skill["блок"]
                if damaged_block < 0:
                    damaged_block = 0
                a["Здоровье"] -= damaged_block
                my_block = False
                print("Противник нанёс " + str(damaged_block) + " урона")
            elif my_move == True:
                print("Удалось увернуться от атаки")
                print("Нанесено 0 урона")
                my_move = False
            else:
                a["Здоровье"] -= damaged
                print("Противник нанёс " + str(damaged) + " урона")
            if combo == 1:
                combo = 2
                a["Здоровье"] -= damaged
                print("Дополнительно " + str(damaged) +
                      " урона - бонус от комбо")
            else:
                combo = 0
        elif ran <= 80 and enemy != "moose":
            print("Противник готовиться защищаться")
            enemy_lock = True
        elif ran <= 100:
            print("Противник хочет увернуться")
            if randint(1, 100) <= enemy_move_chance:
                enemy_move = True
        elif ran < enemy_lim:
            if len(enemy_spell) > 0:
                spl = randint(1, len(enemy_spell))
                if enemy_spell[spl - 1] == "fear":
                    print(
                        "Загнав вас в астрал, противник мучал вас самыми жуткими картинами"
                    )
                    print("Противник применил заклинание :страх:")
                    fear = True
                    if randint(1, 100) <= enemy_move_chance:
                        combo = 1
                        print("Противник бьёт комбо-ударами")
            else:
                print("Противник замешкался")
    print("Фуух, наконец-то я его одолел")
    if enemy == "medium_mutant_forester":
        ex += 5
    elif enemy == "medium_mutant_forester_damaged":
        ex += 3
    elif enemy == "near_weller":
        print("Уродец улетел обратно")
        ex += 8
        the_end()
    else:
        ex += 2
    a["Усталость"] -= 30
    a["Голод"] -= 20
    a["Жажда"] -= 10
    tim[1] += 1


def dialog():
    global task_1
    if locations == "camp_on_the_sink" and tim[0] < 10:
        print()
        print(
            "- Чего тебе?\n"
            "- Может поменяемся чем-нибудь? Вижу безделушек у тебя полным полно (1)\n"
            "- Раскажи мне что-нибудь (2)\n"
            "- Помочь? (3)\n"
            "- Слыш голубь, ну держись (атаковать) (4)\n"
            "- Пока (5)\n"
        )
        cho = input("Введите номер: ")
        print()
        if cho == "5":
            print("- Бывай")
            game()
        elif cho == "4":
            print(
                "Только вы это произнесли, как огромное напряжение электрического разряда сожгло ваше тело до угольков"
            )
            game_over()
        elif cho == "3":
            if task_1 == 0:
                print(
                    "- Отвяжись. А хотя ты бы мне сильно подсобил, разобравшись с мародёрами в деревне. Наградой не обижу\n"
                    "- Да что ты говоришь, мне бы их взгляд не поймать, а тут такое\n"
                    "- Дак в лестничестве флакон с хлорофилом есть, пусть поспят малёх\n"
                    "- Ну и дела..\n"
                    "НОВОЕ ЗАДАНИЕ:   <МЕНЬШЕ ЗНАЕШЬ - КРЕПЧЕ СПИШЬ>\n"
                )
                task_1 = 1
            elif task_1 == 1:
                print("- Я же тебе уже сказал?")
            elif task_1 == 2:
                print("- Спасибо, больше меня ничего не беспокоит")
        elif cho == "2":
            print(
                "- А по конкретнее?\n"
                "- Где я? (1)\n"
                "- Что здесь вообще происходит? (2)\n"
                "- Что мне теперь делать? (3)\n"
                "- Кто ты и откуда? (4)\n"
            )
            cho = input("Введите номер: ")
            print()
            if cho == "1":
                print(
                    "- Округ Зеленогорска, район Пьеград, Лесное хозяйство 'Берёзка' если быть точнее\n"
                    "- Дак из какой области? Я даже такого города не знаю\n"
                    "- Дурень, долина Рассвета тебе ни о чём не говорит?\n"
                    "- Специально загадками разговариваешь...\n"
                )
            elif cho == "2":
                print(
                    "- Война, сынок, война близится. Все дрожжат и пытаются получше подготовиться, а кто-то и отдаётся на волю судьбе\n"
                    "- Кто поссорился?\n"
                    "- Тебе лучше не знать\n"
                )
            elif cho == "3":
                print(
                    "- Я то откуда знаю. Иди, гуляй, радуйся жизни, веселись с другими такими же мечтателями. Найди себе кого-нибудь\n"
                    "- А война, а ты почему не расслабишься\n"
                    "- Я главное звено в этой войне, хотя меня мало кто видел. Да и до войны ты, скорее всего, не доживёшь\n"
                )
            elif cho == "4":
                print(
                    "- Ох, твоей голове будет сложно это понять. Давай договоримся, что ты меня не видел\n"
                    "- А что там, на воробьёвых горах?\n"
                    "- Рай там, представить сложно, но добраться стоит. Представь крутую игру, фильм, или аниме какое-нибудь. Дак вот на горах тех всего этого полно, даже больше\n"
                    "- Я сапёра представил\n"
                )
            else:
                print("А?")
        elif cho == "1":
            print("Да, ты прав. И некоторые из них мне абсолютно не нужны\n")
            print("Меняю: \n")
            print("10 одуванчик --> 1 пат 9х18 (1)\n")
            print("1 ржавая коса + 5 тушёнка из говядины --> 1 коса (2) \n")
            print("3 сено --> 1 спички (3)\n")
            cho = input("Введите номер: ")
            if cho == "1" and stuff["одуванчик"] >= 10:
                stuff["одуванчик"] -= 10
                stuff["пат 9х18"] += 1
            elif (
                cho == "2"
                and stuff["ржавая коса"] >= 1
                and stuff["тушёнка из говядины"] >= 5
            ):
                stuff["ржавая коса"] -= 1
                stuff["тушёнка из говядины"] -= 5
                stuff["коса"] += 1
            elif cho == "3" and stuff["сено"] >= 5:
                stuff["сено"] -= 5
                stuff["спички"] += 1
            else:
                print("Видимо, чего-то не хватает")
        else:
            print("A?")
        dialog()


def hard_play(num):
    global ex
    global fight_with_near_weller
    global ticket
    global energy
    global locations
    global hard_play_2
    print()
    if num == 1:
        print(
            "Вы можете: спрятаться(1) бежать(2) атаковать(3)\n"
            "В ДНЕВНИКЕ ПОЯВИЛАСЬ ЗАПИСЬ 2\n"
            "ВНИМАНИЕ! Права на ошибку у вас НЕТ"
        )
        cho = input("Введите номер: ")
        print()
        if cho == "1":
            print("РАзумно, но куда?")
            print("землянка(1) крыша землянки(2) между деревьев(3)")
            cho_1 = input("Введите номер: ")
            print()
            if cho_1 == "1":
                print(
                    "Ну да блять, куда же ещё\n"
                    "Вы притаились под кроватью и собрались ждать. Ждали вы недолго. До боли в животе насторожившие звуки неизбежно приближались к вашему бастиону\n"
                    "Дверь открывается и входит оно\n"
                    "(жми enter или пиши всё, что угодно)"
                    "\n"
                )
                s = input()
                my_diary.record_1(2)
                print(
                    "Только наклонившись оно начало сувать к вам свои руки, а затем показалась и рожа"
                )
                print()
                s = input()
                if stuff["ржавая игла"] == 1:
                    print(
                        "Странно, но духом не пали, вытащили свою верную булавочку и как вонзили ему в правый глаз\n"
                        "Тварь от такого взвыла глухим, пронзающим все кости рёвом. Поднялась. И прыгнув на кровать полностью прогнула её.\n"
                        "Но вы же не из робкого десятка, заранее вышмыгнули из засады и помчались на встречу приключениям\n"
                        "Вылетев из жилища вам надо бвло мигом что-то предпринять\n"
                        "скинусь пенёк с крыши(1) бежать в лес(2)"
                    )
                    print()
                    cho_1_1 = input("Введите номер: ")
                    if cho_1_1 == "1":
                        print(
                            "Взабравшись на невысокую крышу вы вооружились пеньком и приготовились в любой момент бросить\n"
                            "А вот и наш счастливый обладатель шишки на голове показался, непромедлительный и жаждущий чужих лбов пенёк полетел прямо в башку этому мерзавцу\n"
                            "Одноглазое исчадье ада получило ещё один бонус, но оставлять это дело так было бы глупо. Так что взяв оттуда же палку вы принялись колотиль несчатного что есть сил\n"
                        )
                        stuff["ржавая игла"] -= 1
                        stuff["палка"] += 1
                        fight("medium_mutant_forester_damaged")
                        a["Усталость"] -= 40
                        a["Голод"] -= 20
                        a["Жажда"] -= 10
                        tim[1] += 1
                    elif cho_1_1 == "2":
                        print(
                            "Не рызмышляя вы пустились прочь, только пятки засверкали. Даже не смотря под ноги вы упали в глубокий овраг насмерь расшибив себе все, что можно"
                        )
                        game_over()
                    else:
                        print(
                            "Не успев хорошенько подумать вы замешкались, и не заметили, как могучий удар со спины раскрошил ваш череп"
                        )
                        game_over()
                elif stuff["ржавая игла"] >= 2:
                    print(
                        "Странно, но духом не пали, вытащили свои верные булавки и как вонзили в его очи\n"
                        "Тварь от такого не успев приподняться обрушилась на постель, полностью прогнула её, а затем раздавила и вас"
                    )
                    game_over()
                else:
                    print(
                        "У вас не оставалось выбора, только пнув тварь ногой. Но тут вам подджидал неприятный сюрприз\n"
                        "С бешенной скоростью мутант перехватил ногу и откусил её своими гнилыми, но очень сильными зубами\n"
                        "Пока вы кричали от боли, от вышей второй ноги остался только кусок\n"
                        "Вскоре, по чуть-чуть вы потеряли сознание и умерли"
                    )
                    game_over()
            elif cho_1 == "2":
                print(
                    "Интересная идея. С этой мыслью вы полезли на крышу хибары и ,притаившись, собрались ждать любого развития событий\n"
                    "ВЖдали вы недолго. До боли в животе насторожившие звуки неизбежно приближались к вашему бастиону\n"
                    "Из-за деревьев появляется оно\n"
                    "(жми enter или пиши всё, что угодно)"
                    "\n"
                )
                s = input()
                my_diary.record_1(2)
                s = input()
                print(
                    "Перестравшись от страху вы, незаметно для себя, кинули прямо в яблочко твари стакан.\n"
                    "Уродец, покосившись, издал злобный крик, после чего мигом помчался к вам\n"
                    "Вы вооружились пеньком и приготовились в любой момент бросить\n"
                    "А вот и наш счастливый обладатель шишки на голове показался, непромедлительный и жаждущий чужих лбов пенёк полетел прямо в башку этому мерзавцу\n"
                    "Исчадье ада получило ещё один бонус, но оставлять это дело так было бы глупо. Так что взяв оттуда же палку вы принялись колотиль несчатного что есть сил\n"
                )
                if stuff["стакан с мутной водой"] > 0:
                    stuff["стакан с мутной водой"] -= 1
                elif stuff["стакан"] > 0:
                    stuff["стакан"] -= 1
                ex += 4
                stuff["палка"] += 1
                fight("medium_mutant_forester_damaged")
                a["Усталость"] -= 50
                a["Голод"] -= 30
                a["Жажда"] -= 20
                tim[1] += 2
            elif cho_1 == "3":
                print(
                    "Ну ладно. Подумали про себя вы и притаились за ближайшей берёзой\n"
                    "Ждать вам пришлось не долго, до тех пор, пока вам в затылок не прилетел тяжёлый удар, вы потеряли сознание"
                )
                game_over()
            else:
                print(
                    "Не успев хорошенько подумать вы замешкались, и не заметили, как могучий удар со спины раскрошил ваш череп"
                )
                game_over()
        elif cho == "2":
            print(
                "Правильно, пора бы уже и свалить. Надоело. И вы со свех ног понеслись прочь\n"
                "Даже не смотря под ноги вы упали в глубокий овраг насмерь расшибив себе все, что можно"
            )
            game_over()
        elif cho == "3":
            print(
                "Всё равно надо быть на стороже. Взяв с земли палку, вы пошли на встречу нежданному гостю\n"
                "(жми enter или пиши всё, что угодно)"
            )
            s = input()
            my_diary.record_1(2)
            stuff["палка"] += 1
            fight("medium_mutant_forester")
        else:
            print("Не время шутить")
            hard_play(1)
    if num == 2:
        if fight_with_near_weller == False:
            my_diary.record_1(3)
            print("Придётся драться насмерть")
            fight("near_weller")
            print("В ДНЕВНИКЕ ПОЯВИЛАСЬ ЗАПИСЬ 3\n")
            fight_with_near_weller = True
        else:
            print("Ладно, давай по новой")
        print(
            "Надпись: Граждане! Проверяйте свои билеты!\n"
            "Вы можете пройти: диспетчерская(1) пути(2) эскалатор(3) склады(4)\n"
        )
        cho = input("Введите номер: ")
        print()
        if cho == "1":
            print(
                "Подойдя к заросшим паутиной пультам управления вы нашли записку, прочитав которую можно понять, что электричество включается где то на путях"
            )
            hard_play(2)
        elif cho == "2":
            if ticket == False:
                print(
                    "Спрыгнув на пути вы отправились до первого поворота, пока вас не сбил мчащийся со всей силой состав\n"
                )
                game_over()
            else:
                print(
                    "Добравшись без приключений до рычага вы активировали свет по всей станции"
                )
                energy = True
                hard_play(2)
        elif cho == "3":
            if energy == False:
                print(
                    "Вы побежали по застывшему эскалатору вверх, в непроглядную мглу, оступились и полетели вниз с менее довольным лицом"
                )
                game_over()
            else:
                print(
                    "Вы шли долговато, но посередине вас ослепило нестерпимым светом и оказались опять в лесу, на той-же дорожке, да вот только по другую сторону от чертополоха"
                )
                locations = "fork"
                tim[0] += 3
                hard_play_2 = True
                game()
        elif cho == "4":
            print("Порыскав на складах вы нашли уелевшим только проездой билетик")
            ticket = True
            hard_play(2)
        else:
            print("Не время шутить")
            hard_play(2)


def search():
    global ex
    global e
    print()
    print("Начать поиски (да\нет)")
    voise = str(input(": "))
    if voise == "да":
        if tim[1] < 22 and tim[1] > 3:
            if a["Усталость"] > 10:
                print()
                print("Ща пощупаем")
                if a["Внимательность"] >= 10:
                    chance = randint(1, 90)
                elif a["Внимательность"] >= 5:
                    chance = randint(1, 95)
                else:
                    chance = randint(1, 100)
                if locations == "basic_room_bed":
                    if count["count_bed"] <= 50:
                        print("На кровати так-то спать надо")
                        sleep(2)
                        count["count_bed"] += 1
                        a["Усталость"] -= 2
                        tim[2] += 1
                        print()
                        if chance <= 7:
                            print(
                                "АЙ БЛЯТЬ, сука иголка. ААА... Стоп а вещица то неплохая"
                            )
                            stuff["ржавая игла"] += 1
                            print("(ПОЛУЧЕН ПРЕДМЕТ :ржавая игла:)")
                            ex += 5
                            rec13(1)
                            a["Здоровье"] -= 1
                            search()
                        elif chance <= 12:
                            print(
                                "Может подушки помучать, вдруг что-нибудь получиться")
                            print("(ПОЛУЧЕН ПРЕДМЕТ :вонючий пух:)")
                            stuff["вонючий пух"] += randint(1, 4)
                            ex += 3
                            search()
                        elif chance <= 46:
                            print("Ладно, хоть немного адекватные тряпки заберу")
                            print("(ПОЛУЧЕН ПРЕДМЕТ :заплесневелые тряпки:)")
                            stuff["заплесневелые тряпки"] += randint(
                                2, 3)
                            search()
                        else:
                            print("О чёрт, ничего не нашёл")
                            search()
                    else:
                        print(
                            "Похоже тут так всё обшарпано вдоль и поперёк, что спать, наверное, будет неудобно"
                        )
                elif locations == "basic_room_nightstand":
                    if count["count_nightstand"] <= 60:
                        count["count_nightstand"] += 1
                        print(
                            "Да тут много чего можно раскопать. Думаю, если полазать тщательней, то добром наживёшься"
                        )
                        sleep(3)
                        a["Усталость"] -= 2
                        tim[2] += 2
                        print()
                        if chance <= 5:
                            print("Ух ты, карандаш, вот щас попишем")
                            stuff["карандаш"] += 1
                            print("(ПОЛУЧЕН ПРЕДМЕТ :карандаш:)")
                            ex += 5
                            if e == 0:
                                print()
                                print(
                                    "(Появилась возможность записывать в дневник, каждые 3 записи карандаш расходуется)"
                                )
                                print()
                                e == 1
                            else:
                                print(
                                    "Карандашом можно писать, а можно насрать. Ну это уже по желанию"
                                )
                            search()
                        elif chance <= 18:
                            print("Вау корочка, не первой свежести но всё же")
                            print("(ПОЛУЧЕН ПРЕДМЕТ :старый сухарь:)")
                            stuff["старый сухарь"] += randint(1, 2)
                            ex += 2
                            search()
                        elif chance <= 49:
                            print("Иных хоронили в упаковке глазёнок")
                            print("(ПОЛУЧЕН ПРЕДМЕТ :упаковка газет:)")
                            stuff["упаковка газет"] += randint(1, 3)
                            search()
                        else:
                            print("О чёрт, ничего не нашёл")
                            search()
                    else:
                        print("Бедная тумба, скрипеть уж начала. Нечего тут рыскать")
                elif locations == "basic_room_door":
                    print("Идиот? Чё я по твоему в двери искать буду?")
                    tim[3] += 1
                    a["Усталость"] -= 2
                    if count["count_door"] <= 30:
                        count["count_door"] += 1
                        if randint(1, 100) <= 15:
                            print(
                                "Отмычка? Видимо до меня эту дверь пытались взломать")
                            stuff["отмычка"] += 1
                    search()
                elif locations == "clearing_at_the_dugout":
                    print("Идиот? Чё я по твоему около землянки найду?")
                    rec14(14)
                    tim[3] += 1
                    a["Усталость"] -= 3
                    if stuff_clearing_at_the_dugout["small_haystack_dry"] > 0:
                        stuff_clearing_at_the_dugout["small_haystack_dry"] -= 1
                        stuff["сено"] += randint(3, 7)
                        print("Хотя вот, сено подсохло")
                elif locations == "edge_of_forest":
                    if count["count_edge_of_forest"] <= 90:
                        count["count_edge_of_forest"] += 1
                        print("Тут ходили наверное тысячу раз, ладно, посмотрю")
                        sleep(3)
                        a["Усталость"] -= 4
                        tim[2] += 4
                        print()
                        if chance <= 4:
                            print("Око врановых, может быть. Всё может быть")
                            stuff["вороний глаз"] += 1
                            print("(ПОЛУЧЕН ПРЕДМЕТ :вороний глаз:)")
                            ex += 6
                            search()
                        elif chance <= 21:
                            print("Зараза, крапива")
                            print("(ПОЛУЧЕН ПРЕДМЕТ :крапива:)")
                            a["Здоровье"] += 1
                            stuff["крапива"] += randint(1, 2)
                            ex += 1
                            search()
                        elif chance <= 32:
                            print("Ваня, за что тебя так")
                            print("(ПОЛУЧЕН ПРЕДМЕТ :иван-чай:)")
                            stuff["иван-чай"] += randint(1, 3)
                            search()
                        elif chance <= 58:
                            print(
                                "Повсюду эти жёлтые глазки"
                            )
                            print("(ПОЛУЧЕН ПРЕДМЕТ :одуванчик:)")
                            stuff["одуванчик"] += randint(1, 3)
                            search()
                        elif chance <= 70:
                            print("Пособирал землянички, так, для перекуса")
                            print("(ПОЛУЧЕН ПРЕДМЕТ :земляника:)")
                            stuff["земляника"] += randint(5, 10)
                            search()
                        else:
                            print("О чёрт, ничего не нашёл")
                            search()
                    else:
                        print(
                            "Кусты так оголели, что ягоды наверное появятся через никогда"
                        )
                elif locations == "birch_forest":
                    if count["count_birch_forest"] <= 120:
                        count["count_birch_forest"] += 1
                        print("Тут ходили наверное тысячу раз, ладно, посмотрю")
                        sleep(3)
                        a["Усталость"] -= 5
                        tim[2] += 4
                        print()
                        if chance <= 3:
                            print("Я ГРИБАБАС - ГРОЗА ГРИБОВ")
                            ran = randint(1, 4)
                            if ran == 1:
                                stuff["белый гриб"] += 1
                                print("(ПОЛУЧЕН ПРЕДМЕТ :белый гриб:)")
                            elif ran == 2:
                                stuff["подберёзовик"] += 1
                                print("(ПОЛУЧЕН ПРЕДМЕТ :подберёзовик:)")
                            else:
                                stuff["рыжик"] += 1
                                print("(ПОЛУЧЕН ПРЕДМЕТ :рыжик:)")
                            ex += 3
                            search()
                        elif chance <= 15:
                            print("Прикололся")
                            print("(ПОЛУЧЕН ПРЕДМЕТ :крапива:)")
                            a["Здоровье"] += 1
                            stuff["крапива"] += randint(2, 7)
                            ex += 1
                            search()
                        elif chance <= 35:
                            print("")
                            print("(ПОЛУЧЕН ПРЕДМЕТ :черника:)")
                            stuff["черника"] += randint(5, 15)
                            search()
                        elif chance <= 45:
                            print("Bалежник брать можно")
                            print("(ПОЛУЧЕН ПРЕДМЕТ :дрова:)")
                            stuff["дрова"] += randint(1, 5)
                            search()
                        elif chance <= 60:
                            print(
                                "Везде валяются палки, если валяются - значит так надо"
                            )
                            print("(ПОЛУЧЕН ПРЕДМЕТ :палка:)")
                            stuff["палка"] += randint(3, 8)
                            search()
                        else:
                            print("О чёрт, ничего не нашёл")
                            search()
                    else:
                        print(
                            "Ведь каждый уголок здесь знаю. И ещё знаю точно, что в тех уголках ничего не осталось"
                        )
                elif locations == "hole":
                    if level >= 5:
                        if hard_play_2 == False:
                            hard_play(2)
                        else:
                            print(
                                "Странно, даже дырки в сыре не могут так внезапно исчезнуть"
                            )
                    else:
                        print("И чё мне тут рыться, всё же на виду")
                elif locations == "village_pogorelovka":
                    if count["count_door"] <= 60:
                        count["count_door"] += 1
                        print("Тут ходили наверное тысячу раз, ладно, посмотрю")
                        sleep(3)
                        a["Усталость"] -= 8
                        tim[2] += 6
                        print()
                        if chance <= 2:
                            print(
                                "Один был опасным парнем, или тем, кто просто любит жизнь"
                            )
                            print("(ПОЛУЧЕН ПРЕДМЕТ :пат 9х18:)")
                            stuff["пат 9х18"] += randint(2, 4)
                            ex += 4
                            search()
                        elif chance <= 15:
                            print("Ух ты, уцелевший огород")
                            print("(ПОЛУЧЕН ПРЕДМЕТ :картошка:)")
                            stuff["картошка"] += randint(2, 7)
                            ex += 2
                            search()
                        elif chance <= 35:
                            print(
                                "Может куски железа от разобранного автомобиля пригодяться"
                            )
                            print("(ПОЛУЧЕН ПРЕДМЕТ :металлолом мал:)")
                            stuff["металлолом мал"] += randint(5, 15)
                            search()
                        elif chance <= 45:
                            print("Огонь до дровенника не добрался")
                            print("(ПОЛУЧЕН ПРЕДМЕТ :дрова:)")
                            stuff["дрова"] += randint(2, 8)
                            search()
                        elif chance <= 60:
                            print("Одна виселица уж слишком хороша, чтобы убивать")
                            print("(ПОЛУЧЕН ПРЕДМЕТ :палка:)")
                            stuff["палка"] += randint(3, 6)
                            search()
                        else:
                            print("О чёрт, ничего не нашёл")
                            search()
                    else:
                        print("Да нет тут ничего, говорю же")
                else:
                    print("Что я тебе тут найду?")
            else:
                print("Сил больше нет")
                game()
        else:
            if a["Усталость"] > 10:
                print("Не видно ж ничего")
            else:
                print("Не знаю как ты, а я бы этой ночью поспал")
            game()
    elif voise == "нет":
        print("Ну как хочешь")
        game()
    else:
        print("Напишете :нет: для другого действия")
        search()


def move():
    global location_prepare_for_fire
    global location_of_fire
    global lock_door_dugout
    global location_of_fire
    global locations
    global burn_down_dugout
    global time_to_burn_down
    global day_to_burn_down
    global myweight
    global ex
    if randint(1, 30) == 1:
        if (
            locations != "basic_room_bed"
            and locations != "basic_room_door"
            and locations != "basic_room_nightstand"
        ):
            print("Заморосило")
            if location_of_fire != "hell":
                location_of_fire = "hell"
                print("Костёр потух")
    nowweight = 0
    for i in weight:
        if stuff[i] > 0:
            nowweight += weight[i] * stuff[i]
    myweight = nowweight
    print()
    if location_prepare_for_fire == locations:
        print("Рядом поленья аккуратно сложены в шалашик")
    elif location_of_fire == locations:
        print("Рядом горит небольшой костерок")
    print()
    move = str(input(": "))
    print()
    if move == "жизнь" or move == "жи":
        live()
    elif move == "идти" or move == "ид":
        move_between_obgect()
    elif (move == "обыск" or move == "об") and level >= 1:
        if tim[1] < 22 and tim[1] > 3:
            if a["Усталость"] > 10:
                search()
            else:
                print("Сил больше нет")
        else:
            if a["Усталость"] > 10:
                print("Не видно ж ничего")
            else:
                print("Не знаю как ты, а я бы этой ночью поспал")
    elif (move == "дневник" or move == "дн") and "школьный дневник" in stuff:
        if stuff["карандаш"] > 0:
            print("Введите номер записи")
            try:
                number = int(input("Введите номер записи: "))
            except ValueError:
                print("Требуется ввести число")
            else:
                print()
                print("ЗАПИСЬ " + str(number))
                print()
                my_diary.record_1(number)
        else:
            print()
            print("А чем я писать то буду?")
    elif (move == "употребить" or move == "уп") and level >= 2:
        print("Вы можете употребить:")
        for i in stuff:
            if stuff[i] != 0 and i in eat:
                print(str(i) + " " + str(stuff[i]), end="    ")
        print()
        f = str(input("Введите название того, чего хотите употребить: "))
        try:
            n = int(input("Количество: "))
        except ValueError:
            print("Требуется ввести число")
        else:
            print()
            if f in eat:
                if stuff[f] > 0:
                    if n <= stuff[f]:
                        if n == 0:
                            print("Пустоту жрать?")
                        elif f == "стакан с отравленной водой":
                            print("Немного горчит")
                            stuff["стакан с отравленной водой"] -= 1 * n
                            stuff["стакан"] += 1 * n
                            if improvement["4"] == 0:
                                a["Здоровье"] -= 1 * n
                            a["Здоровье"] -= 2 * n
                            a["Жажда"] += 10 * n
                            rec12(12)
                        elif f == "стакан с мутной водой":
                            print("Противно конечно, но что поделать")
                            stuff["стакан с мутной водой"] -= 1 * n
                            stuff["стакан"] += 1 * n
                            if improvement["4"] == 0:
                                a["Здоровье"] -= 1 * n
                            a["Жажда"] += 20 * n
                            rec12(12)
                        elif f == "стакан с водой":
                            print("Практически чистейшая")
                            stuff["стакан с водой"] -= 1 * n
                            stuff["стакан"] += 1 * n
                            a["Здоровье"] += 1 * n
                            a["Жажда"] += 30 * n
                        elif f == "старый сухарь":
                            print("Противно конечно, но что поделать")
                            stuff["старый сухарь"] -= 1 * n
                            if improvement["4"] == 0:
                                a["Здоровье"] -= 1 * n
                            a["Голод"] += 7 * n
                            rec12(12)
                        elif f == "земляника":
                            print("Какая сладкая!")
                            stuff["земляника"] -= 1 * n
                            a["Голод"] += 1 * n
                            if n > 10:
                                a["Жажда"] += 1
                            if n > 30:
                                a["Здоровье"] += 1
                        elif f == "черника":
                            print("Прям как лес во рту")
                            stuff["черника"] -= 1 * n
                            a["Голод"] += 1 * n
                            if n > 5:
                                a["Жажда"] += 1
                            if n > 20:
                                a["Здоровье"] += 1
                            if n > 50:
                                a["Внимательность"] += 1
                        elif f == "сухарь":
                            print("Грызть можно")
                            stuff["сухарь"] -= 1 * n
                            a["Голод"] += 10 * n
                        elif f == "лесной чай":
                            print("А какой аромат!")
                            stuff["лесной чай"] -= 1 * n
                            stuff["стакан"] += 1 * n
                            a["Жажда"] += 20 * n
                            a["Усталость"] += 10 * n
                        elif f == "грибное рагу в стакане":
                            print("Теперь то я поверю, что грибы заменяют мясо!")
                            stuff["грибное рагу в стакане"] -= 1 * n
                            stuff["стакан"] += 1 * n
                            a["Здоровье"] += 5 * n
                            a["Голод"] += 30 * n
                            a["Жажда"] += 15 * n
                            a["Усталость"] += 5 * n
                        elif f == "тушёнка из говядины":
                            print("Не мраморная говядина, но всё же")
                            stuff["тушёнка из говядины"] -= 1 * n
                            a["Здоровье"] += 5 * n
                            a["Голод"] += 35 * n
                        elif f == "белое вино":
                            print("Не мраморная говядина, но всё же")
                            stuff["белое вино"] -= 1 * n
                            a["Здоровье"] += 3 * n
                            a["Жажда"] += 10 * n
                            a["Усталость"] -= 10
                            ex += 2
                        elif f == "картошка в пепле":
                            print("Вкус детства")
                            stuff["картошка в пепле"] -= 1 * n
                            a["Голод"] += 10 * n
                        if improvement["4"] == 1:
                            a["Голод"] += 2
                    else:
                        print("Нету у меня столько")
            else:
                print("И куда это мне полезет?")
    elif (move == "спать" or move == "сп") and level >= 1:
        if locations == "basic_room_bed" or locations == "camp_on_the_sink":
            print("Уххх... И хорошо же здесь, хоть и грязновато немного")
            if stuff_clearing_at_the_dugout["small_haystack_crude"] > 0:
                stuff_clearing_at_the_dugout[
                    "small_haystack_dry"
                ] = stuff_clearing_at_the_dugout["small_haystack_crude"]
                stuff_clearing_at_the_dugout["small_haystack_crude"] = 0
            sleep(3)
            chance = randint(1, 5)
            if chance == 1:
                a["Здоровье"] -= 1
                a["Усталость"] += 30
                a["Голод"] -= 10
                a["Жажда"] -= 5
                tim[1] += 4
                print(
                    "Спал ужасно, постоянные скрипы снаружи, сырость кругом и чувсво как-будто кто-то говорит"
                )
                if locations == "basic_room_bed":
                    if randint(1, 3) == 1:
                        if lock_door_dugout == False:
                            fight("near_weller")
                        else:
                            print("Ночью в дверь кто-то стучался")
                elif locations == "camp_on_the_sink":
                    if randint(1, 4) == 1:
                        print("Утро доброе")
                        fight("moose_mutant")
            elif chance == 2:
                a["Здоровье"] += 15
                a["Усталость"] += 80
                a["Голод"] -= 20
                a["Жажда"] -= 15
                tim[1] += 10
                print(
                    "Ох как себя чувствую, будто проспал 30 лет и 3 года, силушки богатырской хоть отбавляй. Хотя не надо. Понадобиться"
                )
            else:
                if a["Здоровье"] >= 20 and a["Здоровье"] <= 80:
                    a["Здоровье"] += 10
                a["Усталость"] += 50
                a["Голод"] -= 15
                a["Жажда"] -= 10
                tim[1] += 6
                print("Ну подремал малёха, не отель но и не мусорка")
        else:
            print("И как я тебе здесь спать буду?")
            print("Понимаю только, что молча")
    elif move == "использовать" or move == "исп":
        for i in use_arguments:
            print(i, end="    ")
        print()
        cho = input("Ваш выбор: ")
        if cho == "окружение" or cho == "окр":
            if locations == "basic_room_bed":
                print("Ну. Я здесь спать могу")
            elif locations == "basic_room_nightstand":
                print("Вы можете спрятать, забрать")
                f = input()
                if f == "спрятать" or f == "спр":
                    print()
                    print("Вы можете спрятать: ")
                    for i in stuff:
                        if (
                            i != "карандаш"
                            and i != "рука"
                            and i != "школьный дневник"
                            and stuff[i] != 0
                        ):
                            print(i + " " + str(stuff[i]), end="  ")
                    print()
                    print()
                    f = input("Введите название того, что хотите спрятать: ")
                    try:
                        n = int(input("Количество: "))
                    except ValueError:
                        print("Требуется ввести число!")
                    else:
                        for i in stuff:
                            if f == i:
                                if n <= stuff[i]:
                                    if i in catch_nightstand:
                                        stuff[i] -= n
                                        catch_nightstand[i] += n
                                    else:
                                        catch_nightstand[i] = 0
                                        stuff[i] -= n
                                        catch_nightstand[i] += n
                                else:
                                    print("Нету у меня столько")
                        a["Усталость"] -= 5
                elif f == "забрать" or f == "заб":
                    print()
                    print("Вы можете забрать: ")
                    for i in catch_nightstand:
                        if catch_nightstand[i] != 0:
                            print(i + " " + str(catch_nightstand[i]), end="  ")
                    print()
                    print()
                    f = input("Введите название того, что хотите забрать: ")
                    try:
                        n = int(input("Количество: "))
                    except ValueError:
                        print("Требуется ввести число!")
                    else:
                        for i in catch_nightstand:
                            if f == i:
                                if n <= catch_nightstand[i]:
                                    stuff[i] += n
                                    catch_nightstand[i] -= n
                                else:
                                    print("Нету тут столько")
                                break
                        a["Усталость"] -= 5
                else:
                    print("А что же ещё?")
            elif locations == "hole":
                print("Вы можете спрятать, забрать")
                f = input()
                if f == "спрятать" or f == "спр":
                    print()
                    print("Вы можете спрятать: ")
                    for i in stuff:
                        if (
                            i != "карандаш"
                            and i != "рука"
                            and i != "школьный дневник"
                            and stuff[i] != 0
                        ):
                            print(i + " " + str(stuff[i]), end="  ")
                    print()
                    print()
                    f = input("Введите название того, что хотите спрятать: ")
                    try:
                        n = int(input("Количество: "))
                    except ValueError:
                        print("Требуется ввести число!")
                    else:
                        for i in stuff:
                            if f == i:
                                if n <= stuff[i]:
                                    if i in catch_hole:
                                        stuff[i] -= n
                                        catch_hole[i] += n
                                    else:
                                        catch_hole[i] = 0
                                        stuff[i] -= n
                                        catch_hole[i] += n
                                else:
                                    print("Нету у меня столько")
                        a["Усталость"] -= 5
                elif f == "забрать" or f == "заб":
                    print()
                    print("Вы можете забрать: ")
                    for i in catch_hole:
                        if catch_hole[i] != 0:
                            print(i + " " + str(catch_hole[i]), end="  ")
                    print()
                    print()
                    f = input("Введите название того, что хотите забрать: ")
                    try:
                        n = int(input("Количество: "))
                    except ValueError:
                        print("Требуется ввести число!")
                    else:
                        for i in catch_hole:
                            if f == i:
                                if n <= catch_hole[i]:
                                    stuff[i] += n
                                    catch_hole[i] -= n
                                else:
                                    print("Нету тут столько")
                    a["Усталость"] -= 5
                else:
                    print("А что же ещё?")
            elif locations == "basic_room_door":
                if lock_door_dugout == False:
                    print("Дверь закрыта")
                    lock_door_dugout = True
                    a["Усталость"] -= 1
                else:
                    print("Дверь открыта")
                    lock_door_dugout = False
                    a["Усталость"] -= 1
            elif locations == "clearing_at_the_dugout":
                if stuff["ржавая коса"] > 0 or stuff["коса"] > 0:
                    print(
                        "Накосив травушки-муравушки вы сложили её в небольшой стог: на просушку"
                    )
                    stuff_clearing_at_the_dugout["small_haystack_crude"] += 1
                    a["Усталость"] -= 20
                    a["Голод"] -= 10
                    a["Жажда"] -= 5
                    tim[2] += 4
                else:
                    print("А чем?")
            elif locations == "well":
                ran = randint(1, 100)
                if ran <= 10:
                    print("Я для этого дебила лифт что-ле")
                    fight("near_weller")
                if stuff["стакан"] > 0:
                    if stuff["стакан"] < 10:
                        stuff["стакан с отравленной водой"] += stuff["стакан"]
                        stuff["стакан"] = 0
                    else:
                        stuff["стакан с отравленной водой"] += 10
                        stuff["стакан"] -= 10
                else:
                    print("А во что набирать?")
            elif locations == "fork":
                print("Похоже сквозь непроглядные буквы вырисовывается странный символ")
                print("ПОЛУЧЕН ??? :ЧЕРНАЯ МЕТКА:")
        elif cho == "предмет" or cho == "пред":
            print("Вы можете использовать: ")
            for i in stuff:
                if stuff[i] > 0:
                    if (
                        i == "спички"
                        or i == "стакан с фильтром"
                        or i == "спальный мешок"
                    ):
                        print(i + " " + str(stuff[i]), end="    ")
            print()
            cho = input("Ваш выбор: ")
            print()
            if cho == "спички":
                if (
                    locations == "basic_room_bed"
                    or locations == "basic_room_door"
                    or locations == "basic_room_nightstand"
                ):
                    print(
                        "Со спички огонь перекинулся на сухие обои, а затем и захватил всю землянку. Вы успели выбежать на поляну"
                    )
                    burn_down_dugout = True
                    locations = "clearing_at_the_dugout"
                    game()
                elif location_prepare_for_fire == locations:
                    if randint(1, 10) < 8:
                        location_of_fire = location_prepare_for_fire
                        location_prepare_for_fire = "hell"
                        time_to_burn_down = tim[1] + 6
                        day_to_burn_down = tim[0]
                        if time_to_burn_down > 24:
                            time_to_burn_down -= 24
                            day_to_burn_down += 1
                    else:
                        print("Чётр, потухла")
                else:
                    print("Кого поджечь?")
            elif cho == "стакан с фильтром":
                if stuff["стакан с мутной водой"] > 0:
                    a["Усталость"] -= 2
                    tim[3] += 4
                    stuff["стакан с фильтром"] -= 1
                    stuff["стакан с мутной водой"] -= 1
                    stuff["стакан"] += 1
                    stuff["стакан с водой"] += 1
                    print("Вода, пройдя через фильтр, очистилась и заблестела")
                else:
                    print("А что цедить?")
            elif cho == "спальный мешок":
                print("Ощущения, конечно, не забываемые")
                if stuff_clearing_at_the_dugout["small_haystack_crude"] > 0:
                    stuff_clearing_at_the_dugout[
                        "small_haystack_dry"
                    ] = stuff_clearing_at_the_dugout["small_haystack_crude"]
                    stuff_clearing_at_the_dugout["small_haystack_crude"] = 0
                sleep(5)
                chance = randint(1, 5)
                if chance == 1:
                    a["Здоровье"] -= 1
                    a["Усталость"] += 20
                    a["Голод"] -= 15
                    a["Жажда"] -= 10
                    tim[1] += 4
                    print("Ужас. Все время думал, что кто-то трогает мою ногу")
                    if randint(1, 10) == 1:
                        print("О, будильник пришёл")
                        fight("wolf")
                elif chance == 2:
                    a["Здоровье"] += 10
                    a["Усталость"] += 60
                    a["Голод"] -= 30
                    a["Жажда"] -= 20
                    tim[1] += 10
                    print(
                        "Ох как себя чувствую, будто проспал 30 лет и 3 года, силушки богатырской хоть отбавляй. Хотя не надо. Понадобиться"
                    )
                else:
                    if a["Здоровье"] >= 20 and a["Здоровье"] <= 80:
                        a["Здоровье"] += 5
                    a["Усталость"] += 40
                    a["Голод"] -= 20
                    a["Жажда"] -= 15
                    tim[1] += 6
                    print("Ну подремал малёха, не отель но и не мусорка")
            else:
                print("A?")
        elif cho == "готовить" or cho == "гот":
            if location_of_fire == locations or (
                locations == "camp_on_the_sink" and tim[0] < 10
            ):
                cho = input("Ваш выбор: ")
                if cho in dish:
                    print()
                    print("Для этого понадобиться / у вас есть")
                    for i, j in dish.items():
                        if cho == i:
                            for f in j:
                                print(
                                    f + " " + str(j[f]) +
                                    " / " + str(stuff[f]),
                                    end="   ",
                                )
                            break
                    print()
                    cho2 = input("Приготовить? (да/нет): ")
                    if cho2 == "да":
                        for f in dish[cho]:
                            if stuff[f] >= j[f]:
                                stuff[f] -= j[f]
                            else:
                                print()
                                print("Видимо чего-то не хватает")
                                break
                        else:
                            if randint(1, 10) == 1:
                                print(
                                    "Ааа.. Как я не уследил? Угольки теперь придётся есть"
                                )
                                print("ПОЛУЧЕН ПРЕДМЕТ :уголь:")
                                stuff["уголь"] += 3
                            else:
                                stuff[cho] += 1
                                print()
                                sleep(3)
                                print("Даже не подгорело")
                    else:
                        if a["Голод"] > 20:
                            print("Ну и правильно, не очень-то и хотелось")
                        else:
                            print("Хотя есть хочеться сильно")
                else:
                    print("Я не знаю такого")
            else:
                print("Было-бы над чем")
        elif cho == "выбросить" or cho == "выб":
            print()
            print("Вы можете выбросить: ")
            for i in stuff:
                if i != "рука" and i != "школьный дневник" and stuff[i] != 0:
                    print(i + " " + str(stuff[i]), end="  ")
            print()
            print()
            f = input("Введите название того, что вам точно не нужно: ")
            try:
                n = int(input("Количество: "))
            except ValueError:
                print("Требуется ввести число!")
                game()
            else:
                for i in stuff:
                    if f == i:
                        if n <= stuff[i]:
                            stuff[i] -= n
                        else:
                            print("Нету у меня столько")
        else:
            print("А?")
    elif (move == "карта" or move == "кар") and level >= 5:
        print("Вы можете посмотреть:")
        for i in range(0, len(map)):
            print(str(map[i]) + " (" + str(i) + ")", end="    ")
        print()
        try:
            b = int(input("Введите номер: "))
        except ValueError:
            print("Требуется ввести число!")
        else:
            if map[b] == "ЛесХоз 'Берёзка'":
                print(
                    "                                            /\ На 'Пьеград'            - -\n"
                    "             Село     П  П                     |    |               - -    - \n"
                    "        Погореловка    П  П        -    -      |    |               -   -   -\n"
                    "        _________        \       -    -  -     |    |    Лесоповал           Село Большое\n"
                    "          __________      |       -    -  -    |    |       _I_              П                  ___________\n"
                    "         _______      ____|_____ -  -  - ______|    |        |______П   П  П                     __________\n"
                    "                     /    |     \_______/      |    |        |       П   П   П                 _____________\n"
                    "    /\  ____________/     |                    |    |_______/              \__Н - Райцентр         Мельница\n"
                    " Землянка     -            \                   |    |       \                                    / \ \n"
                    "  лесника     -  -  -       \  ___             |    |        |       ____________________________|_|\n"
                    "            -  -  - -         /___\            |    |        \______/                                   ____________\n"
                    "            -    -      Лесное хозяйство       |    |              П   П                             _____________\n"
                    "                                               |    |               П П   Село Видное                 ____________\n"
                    "                                      \/ На 'Порог у двух ворот' \n"
                )
            elif map[b] == "Здание №34":
                print(
                    "                    \/ Лесница                                                                            \n"
                    "          ___________________________________________________                                        \n"
                    "         |        | \\     |          |    |        |        |                          \n"
                    "         |        |______/ |         \_____| \______|        |                           \n"
                    "         |                  /             /         |        |                           \n"
                    "         |__/ _____________|               |__/ ____|____ \__|                           \n"
                    "         |       _______   |______/  ______|        |         \                                              \n"
                    "          \     |_______|  /        /      \        |_/ ____/   <--Запасной выход      \n"
                    "           \              /                 \              /                                       \n"
                    "            \____----____/                   \____----____/                                                        \n"
                    "    Конференц-зал /\                                                                \n"
                )
    elif (move == "крафт" or move == "кр") and level >= 4:
        cho = input("Ваш выбор: ")
        if cho in kraft:
            print()
            print("Для этого понадобиться / у вас есть")
            for i, j in kraft.items():
                if cho == i:
                    for f in j:
                        print(f + " " + str(j[f]) +
                              " / " + str(stuff[f]), end="   ")
                    break
            print()
            cho2 = input("Создать предмет? (да/нет): ")
            if cho2 == "да":
                for f in kraft[cho]:
                    if stuff[f] >= j[f]:
                        stuff[f] -= j[f]
                    else:
                        print()
                        print("Видимо чего-то не хватает")
                        break
                else:
                    if cho != "заготовка для костра":
                        if cho == "стакан с фильтром":
                            a["Усталость"] -= 3
                            tim[3] -= 5
                        stuff[i] += 1
                    elif cho == "заготовка для костра":
                        if location_prepare_for_fire == "hell":
                            if location_of_fire == locations:
                                print("Подкинем..")
                                time_to_burn_down += 6
                                if time_to_burn_down > 24:
                                    time_to_burn_down -= 24
                                    day_to_burn_down += 1
                            if location_prepare_for_fire == locations:
                                print("Да есть уже тут, зажечь бы")
                            else:
                                a["Усталость"] -= 5
                                tim[3] -= 7
                                location_prepare_for_fire = locations
                        else:
                            print("Я же где-то уже хотел развести костёр!?")
                    else:
                        print("А?")
                        game()
                    print()
                    sleep(3)
                    print("Предмет успешно создан")
            else:
                print("Правильно, и зачем мне это?")
        else:
            print()
            print("А как это делать?")
    elif move == "сохранить" or move == "сох":
        save()
    elif move == "загрузить" or move == "заг":
        load()
    elif move == "ул" and level >= 3:
        if improvement["1"] == 0:
            print(
                " Дерево прокачки                                                                       \n"
                "                                                             (1) I'm awake and alive (10 ex)                        \n"
                "                                                                     Здоровье макс + 5                                \n"
                "                                                                     Вес макс + 1 кг                                  \n"
                "                                                                     Атака + 1                   \n"
                "                                                                     Усталость макс + 10    \n"
            )
        elif improvement["2"] == 0:
            print(
                " Дерево прокачки                                                                        \n"
                "                                                             (1) I'm awake and alive (10 ex)                        \n"
                "                                                               /     Здоровье макс + 5      \                           \n"
                "                                                              /      Вес макс + 1 кг         \                           \n"
                "                              (2) Лесной повар (18 ex) <-----/       Атака + 1                \----> (3) Cumень (13 ex)      \n"
                "                                    + 3 рецепта                      Усталость макс + 10              Блок + 2           \n"
                "                                   Голод макс + 10                                                   Вес макс + 3 кг         \n"
                "                                                                                                \n"
            )
        elif improvement["2"] == 1:
            print(
                " Дерево прокачки                                                                        \n"
                "                                                             (1) I'm awake and alive (10 ex)                        \n"
                "                                                               /     Здоровье макс + 5      \                           \n"
                "                                                              /      Вес макс + 1 кг         \                           \n"
                "                              (2) Лесной повар (18 ex) <-----/       Атака + 1                \----> (3) Cumень (13 ex)      \n"
                "                     /-----------   + 3 рецепта                      Усталость макс + 10              Блок + 2           \n"
                "                    /              Голод макс + 10                                                   Вес макс + 3 кг         \n"
                "  (4) Крепкий желудок (22 ex)                \                                                                               \n"
                "  мутная вода и просроченная                  \-> (5) Я и из лужи пил (33 ex)                                          \n"
                "  еда не отнимают здоровья                             Возможность пить                                                      \n"
                "+ 2 к насыщению от каждого продукта                    отравленную воду                                                        \n"
            )
        try:
            cho = int(input("Введите номер: "))
        except ValueError:
            print("Требуется ввести число!")
        else:
            if cho == 1:
                if ex >= 10:
                    if improvement["1"] == 0:
                        print(
                            "Я очутился в неисвестном доселе месте, и базовые навыки выживания лишними не станут"
                        )
                        a_max["Здоровье"] += 5
                        a_max["Вес"] += 1000
                        a_max["Усталость"] += 10
                        skill["атака"] += 1
                        ex -= 10
                        improvement["1"] = 1
                    else:
                        print("Модификация уже исследована")
                else:
                    print("Недостаточно опыта")
            elif cho == 2:
                if ex >= 18:
                    if improvement["1"] == 1:
                        if improvement["2"] == 0:
                            print(
                                "Как-то помню в лагере учили меня готовить в полевых условиях, надо бы припомнить"
                            )
                            a_max["Голод"] += 10
                            dish["лесной чай"] = (
                                {"стакан с водой": 1, "иван-чай": 10, "земляника": 3},
                            )
                            dish["грибное рагу в стакане"] = {
                                "стакан с водой": 1,
                                "белый гриб": 1,
                                "подберёзовик": 1,
                                "рыжик": 1,
                                "сухарь": 2,
                                "тушёнка из говядины": 1,
                            }
                            dish["картошка в пепле"] = {"картошка": 1}
                            ex -= 18
                            improvement["2"] = 1
                        else:
                            print("Модификация уже исследована")
                    else:
                        print("Не исследованы предыдущие модификации")
                else:
                    print("Недостаточно опыта")
            elif cho == 3:
                if ex >= 13:
                    if improvement["1"] == 1:
                        if improvement["3"] == 0:
                            print("С каждым днём я становлюсь всё крепче")
                            skill["блок"] += 2
                            a_max["Вес"] += 3000
                            ex -= 13
                            improvement["3"] = 1
                        else:
                            print("Модификация уже исследована")
                    else:
                        print("Не исследованы предыдущие модификации")
                else:
                    print("Недостаточно опыта")
            elif cho == 4:
                if ex >= 22:
                    if improvement["2"] == 1:
                        if improvement["4"] == 0:
                            print("Жить захочешь - и не такое проглотишь")
                            improvement["4"] = 1
                        else:
                            print("Модификация уже исследована")
                    else:
                        print("Не исследованы предыдущие модификации")
                else:
                    print("Недостаточно опыта")
            elif cho == 5:
                if ex >= 33:
                    if improvement["2"] == 1:
                        if improvement["5"] == 0:
                            print("Да вроде-бы и не очень уж отвратительно")
                            improvement["5"] = 1
                        else:
                            print("Модификация уже исследована")
                    else:
                        print("Не исследованы предыдущие модификации")
                else:
                    print("Недостаточно опыта")
            else:
                print("Я не знаю такой модификации")
    elif (move == "говорить" or move == "гов") and level >= 5:
        dialog()
    else:
        print()
        print("Чё?")
        print("Я не знаю такого")
    try:
        game()
    except RecursionError:
        save()
        print("Аварийный выход из игры причина : довольно продолжительный сеанс")
        game_over()


def return_to(loc, fatigue, min):
    global locations
    global click
    global botton_frame_1
    botton_frame_1.destroy()
    if locations == "clearing_at_the_dugout":
        if loc == "basic_room_door" and burn_down_dugout:
            pass
    count["count_food"] += 1
    count["count_water"] += 1
    a["Усталость"] -= fatigue
    tim[3] += min
    locations = loc
    game()


def basic_room_bed():
    print()
    rec3(3)
    update_image("resources\\BED.png")
    if tim[1] >= 16:
        rec2(2)
    if tim[1] >= 5 and tim[1] <= 12:
        update_text(
            "Всё такая-же грязненькая кроватка. На которой можно немного подремать \n \n"
            "Почевальня или портал в мир грёз"
        )
    elif tim[1] >= 13 and tim[1] <= 18:
        update_text(
            "Всё такая-же грязненькая кроватка. На которой можно немного подремать \n \n"
            "В полдень, особенно после плотного обеда, кроватка стала ещё привлекательнее"
        )
    elif tim[1] >= 19 or tim[1] <= 4:
        update_text(
            "Всё такая-же грязненькая кроватка. На которой можно немного подремать \n \n"
            "В непроглядной мгле так и кажется, что кровать - единственное безопасное место"
        )
    move_between_obgect()


def basic_room_door():
    print()
    rec4(4)
    update_image("resources\\DOOR.png")
    if tim[1] >= 5 and tim[1] <= 12:
        if lock_door_dugout:
            update_text(
                "Теперь вам её уже нельзя приоткрыть, зато подслушать - запросто! \n\n Нисего такая дверца"
            )
        else:
            update_text(
                "Подойдя к двери вы приоткрыли её, что-бы удостовериться в безопастности \n\n Нисего такая дверца"
            )
    elif tim[1] >= 13 and tim[1] <= 20:
        if lock_door_dugout:
            update_text(
                "Теперь вам её уже нельзя приоткрыть, зато подслушать - запросто! \n\n Стоишь. Только мешаешь"
            )
        else:
            update_text(
                "Подойдя к двери вы приоткрыли её, что-бы удостовериться в безопастности \n\n Стоишь. Только мешаешь"
            )
    elif tim[1] >= 21 or tim[1] <= 4:
        if lock_door_dugout:
            update_text(
                "Теперь вам её уже нельзя приоткрыть, зато подслушать - запросто! \n\n Думаю закрыть дверь будет наилучшим решением"
            )
        else:
            update_text(
                "Подойдя к двери вы приоткрыли её, что-бы удостовериться в безопастности \n\n Думаю закрыть дверь будет наилучшим решением"
            )
    move_between_obgect()


def basic_room_nightstand():
    print()
    rec5(5)
    update_image("resources\\NIGHTSTAND.png")
    if tim[1] >= 5 and tim[1] <= 12:
        if tim[0] <= 3:
            update_text(
                "Всё ещё работающий будильник помогает ориентироваться во времени \n\n Время "
                + str(tim[1])
                + " : "
                + str(tim[2])
                + str(tim[3])
                + " \n\nБудка как будка. Ничего нового, но и ничего старого"
            )
        else:
            update_text(
                "Будильник разрядился \n\n Будка как будка. Ничего нового, но и ничего старого"
            )
    elif tim[1] >= 13 and tim[1] <= 20:
        if tim[0] <= 3:
            update_text(
                "Всё ещё работающий будильник помогает ориентироваться во времени \n\n Время "
                + str(tim[1])
                + " : "
                + str(tim[2])
                + str(tim[3])
                + " \n\nПейзаж в рамке чей-то, не разглядеть."
            )
        else:
            update_text(
                "Будильник разрядился \n\n Пейзаж в рамке чей-то, не разглядеть."
            )
    elif tim[1] >= 21 or tim[1] <= 4:
        if tim[0] <= 3:
            update_text(
                "Всё ещё работающий будильник помогает ориентироваться во времени \n\n Время "
                + str(tim[1])
                + " : "
                + str(tim[2])
                + str(tim[3])
                + " \n\nНа картине появились тёмные фигуры, странно, раньше не замечал их"
            )
        else:
            update_text(
                "Будильник разрядился \n\n На картине появились тёмные фигуры, странно, раньше не замечал их"
            )
    move_between_obgect()


def clearing_at_the_dugout():
    global burn_down_dugout
    if randint(1, 10) == 1:
        rec6(6)
    if burn_down_dugout:
        update_image("resources\\DUGOUT_BURN_DOWN.png")
    else:
        update_image("resources\\DUGOUT.png")
    if tim[1] >= 5 and tim[1] <= 12:
        if burn_down_dugout:
            update_text(
                "Травка зеленеет, а вот птички что-то разлетелись. \n\n Роса до сих пор не испарилась"
            )
        else:
            update_text(
                "Травка зеленеет, птички поют. \n\n Роса до сих пор не испарилась"
            )
    elif tim[1] >= 13 and tim[1] <= 20:
        if burn_down_dugout:
            update_text(
                "Травка зеленеет, а вот птички что-то разлетелись. \n\n Крепость!"
            )
        else:
            update_text(
                "Травка зеленеет, птички поют, угольки бегут. \n\n Крепость!")
    elif tim[1] >= 21 or tim[1] <= 4:
        if burn_down_dugout:
            update_text(
                "Мгла и только \n\n Я уж посчитал что берлога какая-то")
        else:
            update_text(
                "Ну травка то зелёная, в этом я не сомневаюсь \n\n Я уж посчитал что берлога какая-то"
            )
    move_between_obgect()


def edge_of_forest():
    print()
    rec7(7)
    print("Травка зеленеет, птички поют.")
    print(
        "         \            /  \n"
        "| \   |  |  |  O  |  |  |\n"
        "  |    |  \    |   |  I  | |  |\n"
        "|  |  o   |  |    T    /    | |\n"
        "  |   |    |   |  I |   |  \n"
    )
    if tim[1] >= 5 and tim[1] <= 12:
        print("Полёт шмеля")
    elif tim[1] >= 13 and tim[1] <= 20:
        print("Огромный ястреб кружит в поисках назойливых мышей")
    elif tim[1] >= 21 or tim[1] <= 4:
        print("Вдалеке провыл волк")
    move()


def birch_forest():
    print()
    rec8(8)
    print("Прекрасный лесочек заводит своей тропинкой из мха")
    print(
        "__|   |       |   |      /  |  | |   \n"
        "  \   |       |   |      |  |  | |     \n"
        "  |   |       |   |      |  | /  |  \n"
        "  |   |     \ |   |      |  |/  /   \n"
        "  | \ |     O |   |  O   |  |  / \n"
        "  |   |  \  | |   |  I   |    | \n"
        "  __     o    |   |    T |/   |\n"
        "          _--_|   |  I         \n"
    )
    if tim[1] >= 5 and tim[1] <= 12:
        print("Просыпается, и уже активно ищет приключения лесная природа")
    elif tim[1] >= 13 and tim[1] <= 20:
        print("Пора бы чем-нибудь перекусить")
    elif tim[1] >= 21 or tim[1] <= 4:
        print("Такое чувство, что все кусты шуршат не из-за ветра")
        if randint(1, 100) <= 10:
            print("Волк. Не дав")
            fight("wolf")
    move()


def well():
    print()
    rec9(9)
    print("Вода на вид не очень, а что поделать")
    print(
        "     ____________\n"
        "    |///_/__////_|===_\n"
        "    | _|________ |   | \n"
        "    |/ |        \|   L\n"
        "    |  |         |\n"
        "    |\__________/|\n"
        "    ||          ||\n"
        "    \|__________|/\n"
    )
    if tim[1] >= 5 and tim[1] <= 12:
        print("Колодец, колодец, дай воды напиться. Колодец, колодец, дай неба глоток")
    elif tim[1] >= 13 and tim[1] <= 20:
        print("Просто колодец, прикольно")
    elif tim[1] >= 21 or tim[1] <= 4:
        print("Ух.. Я думал кто-то стоит")
        print(
            "Подойдя к колодцу, вы заметили, что из дна кто-то пристально наблюдает за вами \n"
            "Ах ёп.. ЭТА ХЕРНЯ КАРАБКАЕТСЯ КО МНЕ. Тут то вы не сразу сообразили, а драться с хозяином придётся"
        )
        fight("near_weller")
    move()


def dashing_path():
    print()
    rec10(10)
    print("Тропиночка, ничего удивительного")
    print(
        "  |      \ |   |        |/\n"
        "   \ |     O    |  O   |  |  |\n"
        "         |       ________________\n"
        "________________/        l\n"
        "       o         ________________\n"
        "________________/\n"
        "  |   |       |   |  I   |  |\n"
    )
    if tim[1] >= 5 and tim[1] <= 12:
        print("Переливающие от утренней зари камушки только украшают тропинку")
        ran = randint(1, 100)
        if ran <= 5:
            print("Лось, ебать")
            fight("moose")
    elif tim[1] >= 13 and tim[1] <= 20:
        print("УУуууУУ")
    elif tim[1] >= 21 or tim[1] <= 4:
        print("Откуда-то взлетела стая ворон")
        ran = randint(1, 100)
        if ran <= 20:
            print("Волк. Не дав")
            fight("wolf")
    move()


def hole():
    print()
    rec15(15)
    print("И чего я суда полез?")
    print("(-_-)")
    move()


def fork():
    print()
    rec16(16)
    print(
        "Ещё раз взглянув на указатель вы прочли полустёртые буквы: < Погореловка /\ Трасса А32 > Лестничество \/ Хижина Павла Ивановича"
    )
    print(
        "  |      \ |   |      |   |/\n"
        "   \ |     O   |  ___ |  |  |  |\n"
        "         |     | |___||________________\n"
        "_______________|   |    l\n"
        "       o           |   ________________\n"
        "________________      |        \n"
        "  |   |        |      |  I   |  |\n"
        "               |      |             \n"
    )
    if tim[1] >= 5 and tim[1] <= 12:
        print("Солнце мешает разглядывать полустёртые буквы")
        ran = randint(1, 100)
        if ran <= 5:
            print("Лось, ебать")
            fight("moose")
    elif tim[1] >= 13 and tim[1] <= 20:
        print("Пролетела красивая бабочка")
    elif tim[1] >= 21 or tim[1] <= 4:
        print("В овраге, кажеться, кто-то сидит")
        ran = randint(1, 100)
        if ran <= 20:
            print("Волк. Не дав")
            fight("wolf")
    move()


def village_pogorelovka():
    print()
    rec17(17)
    print("Завораживающий вид")
    print(
        "  | ___  ___ | |      |  | |_|   /\n"
        " \| |_|  |_| | |      |  |________|  |\n"
        "  |__________| |      |________________\n"
        "_______________|        l\n"
        "       o               ________________\n"
        "________________      |        \n"
        "  |   |        |      |  I   |  |\n"
        "      \        |      |             \n"
    )
    if tim[1] >= 5 and tim[1] <= 12:
        print("Где-то всё ещё идёт дым")
    elif tim[1] >= 13 and tim[1] <= 20:
        print("Интересно - на запах мяса никто не сбежиться?")
    elif tim[1] >= 21 or tim[1] <= 4:
        print("Мерещиться свет в окнах")
        ran = randint(1, 100)
        if ran <= 20:
            print("Волк. Не дав")
            fight("wolf")
    move()


def the_yard_before_forestry():
    print()
    rec18(18)
    print("Здание! Ничего себе")
    print(
        "   /             /           \               \      \n"
        "   |  ___\ |     |           |  ___    ___   |   /\n"
        "   |  | |  O  |  |  ___      |  | |    | |   |  |\n"
        "___|________--___|__|_|______|_______________|\n"
        "                         ;         l            \n"
        "       o                                       \n"
        "                0      h                               \n"
        "  |          |                     I   |  |\n"
    )
    if tim[1] >= 5 and tim[1] <= 12:
        print("Неплохой асфальтик")
    elif tim[1] >= 13 and tim[1] <= 20:
        print("Душно стоять на таком-то солнцепёке")
    elif tim[1] >= 21 or tim[1] <= 4:
        print("Наглая мышь пробежала практически у ног")
        ran = randint(1, 100)
        if ran <= 20:
            print("Серая стая")
            fight("rat")
    move()


def camp_on_the_sink():
    print()
    rec19(19)
    if tim[0] < 10:
        print("Палатка, а рядом костерок, ещё и от дождя укрыт")
        print(
            "          /         / ________         \n"
            "         /\        /  |     | \_   \n"
            "        /  \      /   |_____|  |   \n"
            "       / /\ \    /   /_--___-\ |   \n"
            "      / /  \ \  /    \-__---_/             \n"
            "     /_/    \_\/                     \n"
        )
        if tim[1] >= 5 and tim[1] <= 12:
            print("Тэн решил поподкидывать дрова")
        elif tim[1] >= 13 and tim[1] <= 20:
            print("Тэн копошиться в какой-то электронике")
        elif tim[1] >= 21 or tim[1] <= 4:
            print("Тэн предлагает отдохнуть у него")
    else:
        print("Надпись у палатки: Не ищи меня, мне пора")
    move()


def Time():
    global time_to_burn_down
    global day_to_burn_down
    global location_of_fire
    if tim[0] >= day_to_burn_down:
        if tim[1] >= time_to_burn_down:
            location_of_fire = "hell"
    for i in a:
        if i == "Здоровье" or i == "Голод" or i == "Жажда" or i == "Усталость":
            if a[i] > a_max[i]:
                a[i] = a_max[i]
            elif a[i] <= 0:
                a["Здоровье"] -= 1
                a[i] = 0
    if tim[1] >= 24:
        while tim[1] >= 24:
            tim[1] -= 24
            tim[0] += 1
    elif tim[2] >= 6:
        while tim[2] >= 6:
            tim[2] -= 6
            tim[1] += 1
    elif tim[3] >= 10:
        while tim[3] >= 10:
            tim[3] -= 10
            tim[2] += 1
    if count["count_food"] % 4 == 0:
        a["Голод"] -= 1
        count["count_food"] += 1
    if count["count_water"] % 6 == 0:
        a["Жажда"] -= 1
        count["count_water"] += 1


def Ex():
    global ex
    global exlimit
    global level
    global locations
    global stuff
    if ex >= exlimit:
        level += 1
        exlimit = int(exlimit * 1.5)
        print()
        print("Новый уровень " + str(level))
        print("До следующего уровня требуестя " + str(exlimit) + " опыта")
        print()
        if level == 1:
            print("Новая возможность: обыск, дневник, спать")
            print("Новое блюдо: :стакан с мутной водой:")
            dish["стакан с мутной водой"] = {"стакан с отравленной водой": 1}
            opportunities.append("обыск")
            opportunities.append("дневник")
            opportunities.append("спать")
        elif level == 2:
            print("Новая возможность: употребить")
            print("Новый крафт: :стакан с фильтром:")
            opportunities.append("употребить")
            kraft["стакан с фильтром"] = {
                "стакан": 1,
                "крапива": 4,
                "заплесневелые тряпки": 2,
                "упаковка газет": 3,
            }
        elif level == 3:
            print("Новая возможность: ул (прокачка)")
            print("Новый крафт: :заготовка для костра:")
            print("Новый крафт: :спальный мешок:")
            opportunities.append("ул")
            kraft["заготовка для костра"] = {
                "дрова": 4, "палка": 6, "вонючий пух": 20}
            kraft["спальный мешок"] = {
                "заплесневелые тряпки": 20,
                "сено": 10,
                "ржавая игла": 1,
            }
        elif level == 4:
            print("Новая возможность: крафт")
            print("Новый крафт: :палка с ядом:")
            opportunities.append("крафт")
            kraft["палка с ядом"] = {"палка": 1, "вороний глаз": 3}
        elif level == 5:
            print("Новая возможность: карта, говорить")
            opportunities.append("говорить")
            opportunities.append("карта")
        print(":", end=" ")
    if a["Здоровье"] <= 0:
        print("Я чувсвую свет! Тьфу, это все-го лишь сон")
        tim[1] = 8
        if ex < 10:
            ex = 0
        else:
            ex -= 10
        for i in stuff:
            stuff[i] = 0
        for i in a:
            if i != "Внимательность":
                a[i] = 100
        locations = "basic_room_bed"


def game():
    global locations
    update_live(a)
    Time()
    Ex()
    call = globals()[locations]
    call()


def live():
    global ex
    global myweight
    print()
    print("Ваше состояние")
    for i in a:
        if a[i] > 0:
            print(i + " " + str(a[i]), end="    ")
    print()
    print()
    print("Ваши навыки")
    for i in skill:
        if skill[i] != 0:
            print(str(i) + " " + str(skill[i]), end="    ")
    print()
    print()
    print("Ваши возможности")
    for i in opportunities:
        print(i, end="    ")
    print()
    print()
    print("У вас есть")
    for i in stuff:
        if stuff[i] != 0 and i != "рука":
            print(str(i) + " " + str(stuff[i]), end="    ")
    print()
    print("Вы можете сделать: ")
    for i, j in kraft.items():
        print(i, end="   ")
    print()
    print("Вы можете приготовить")
    for i, j in dish.items():
        print(i, end="   ")
    print()
    print()
    print("Вес: " + str(myweight // 1000) +
          " кг " + str(myweight % 1000) + " г")
    print()
    print("Опыт: " + str(ex))
    print()
    print("С начала игры прошло " + str(tim[0]) + " суток")
    print()
    game()


def move_between_obgect():
    global locations
    global locations_till
    global burn_down_dugout
    global myweight
    global botton_frame_1
    global frame_destroy
    botton_frame_1 = Frame(BOTTON_FRAME, bg="black")
    botton_frame_1.pack()
    if myweight <= a_max["Вес"]:
        if a["Усталость"] > 5:
            if locations == "basic_room_bed":
                rec11(11)
                Label(
                    botton_frame_1,
                    text="Да уж засиделся, пора в путь. Далёкий путь",
                    bg="black",
                    fg="white",
                ).pack(side=TOP)
                Button(
                    botton_frame_1,
                    width=20,
                    height=2,
                    text="Дверь",
                    command=lambda: return_to("basic_room_door", 2, 1),
                ).pack(side=LEFT)
                Button(
                    botton_frame_1,
                    width=20,
                    height=2,
                    text="Тумбочка",
                    command=lambda: return_to(
                        "basic_room_nightstand", 1, 1),
                ).pack(side=LEFT)
            elif locations == "basic_room_door":
                Label(
                    botton_frame_1, text="Интересно, что там?", bg="black", fg="white"
                ).pack(side=TOP)
                Button(
                    botton_frame_1,
                    width=20,
                    height=2,
                    text="Кровать",
                    command=lambda: return_to("basic_room_bed", 2, 1),
                ).pack(side=LEFT)
                Button(
                    botton_frame_1,
                    width=20,
                    height=2,
                    text="Тумбочка",
                    command=lambda: return_to(
                        "basic_room_nightstand", 1, 1),
                ).pack(side=LEFT)
                Button(
                    botton_frame_1,
                    width=20,
                    height=2,
                    text="Просека у землянки",
                    command=lambda: return_to(
                        "clearing_at_the_dugout", 2, 1),
                ).pack(side=LEFT)
            elif locations == "basic_room_nightstand":
                Label(
                    botton_frame_1,
                    text="Ох, и спина вся затекла",
                    bg="black",
                    fg="white",
                ).pack(side=TOP)
                Button(
                    botton_frame_1,
                    width=20,
                    height=2,
                    text="Кровать",
                    command=lambda: return_to("basic_room_bed", 1, 1),
                ).pack(side=LEFT)
                Button(
                    botton_frame_1,
                    width=20,
                    height=2,
                    text="Дверь",
                    command=lambda: return_to("basic_room_door", 1, 1),
                ).pack(side=LEFT)
            elif locations == "clearing_at_the_dugout":
                Label(
                    botton_frame_1, text="Траву уже всю примял", bg="black", fg="white"
                ).pack(side=TOP)
                Button(
                    botton_frame_1,
                    width=20,
                    height=2,
                    text="Дверь",
                    command=lambda: return_to("basic_room_door", 1, 2),
                ).pack(side=LEFT)
                Button(
                    botton_frame_1,
                    width=20,
                    height=2,
                    text="Опушка леса",
                    command=lambda: return_to("edge_of_forest", 2, 6),
                ).pack(side=LEFT)
                Button(
                    botton_frame_1,
                    width=20,
                    height=2,
                    text="Лихая тропа",
                    command=lambda: return_to("dashing_path", 1, 3),
                ).pack(side=LEFT)
                Button(
                    botton_frame_1,
                    width=20,
                    height=2,
                    text="Колодец",
                    command=lambda: return_to("well", 1, 1),
                ).pack(side=LEFT)
            elif locations == "edge_of_forest":
                print("Хорошее поле, обязательно вернусь")
                print()
                print(
                    "Вы можете пройти к: просека у землянки (1) березняк (2) лихая тропа (3)"
                )
                move = input("Введите номер: ")
                if move == "1":
                    locations = "clearing_at_the_dugout"
                    a["Усталость"] -= 2
                    tim[3] += 6
                elif move == "2":
                    locations = "birch_forest"
                    a["Усталость"] -= 2
                    tim[3] += 6
                elif move == "3":
                    if "ЛесХоз 'Берёзка'" in map:
                        locations = "dashing_path"
                        a["Усталость"] -= 1
                        tim[3] += 2
                        print("Вот с картой самое то")
                    else:
                        print("Ссыковато так рано уходить")
            elif locations == "birch_forest":
                print("Так свежо кругом")
                print()
                print("Вы можете пройти к: опушка леса (1) нора (2) колодец (3)")
                move = input("Введите номер: ")
                if move == "1":
                    locations = "edge_of_forest"
                    a["Усталость"] -= 2
                    tim[3] += 6
                elif move == "2":
                    if hard_play_2 == False:
                        if stuff["отмычка"] > 0:
                            locations = "hole"
                            a["Усталость"] -= 1
                            tim[3] += 3
                        else:
                            print(
                                "Думаю туда лучше не лезть, тем более дверь заперта")
                    else:
                        locations = "hole"
                        a["Усталость"] -= 1
                        tim[3] += 3
                elif move == "3":
                    locations = "well"
                    a["Усталость"] -= 1
                    tim[3] += 1
            elif locations == "well":
                print("Отходить от источника жизни не очень то хочется")
                print()
                print("Вы можете пройти к: просека у землянки (1) березняк (2)")
                move = input("Введите номер: ")
                if move == "1":
                    locations = "clearing_at_the_dugout"
                    a["Усталость"] -= 1
                    tim[3] += 1
                elif move == "2":
                    locations = "birch_forest"
                    a["Усталость"] -= 1
                    tim[3] += 1
            elif locations == "dashing_path":
                print("Так кружит. Интересно, куда она меня заведёт?")
                print()
                print(
                    "Вы можете пройти к: опушка леса (1) просека у землянки (2) развилка (3)"
                )
                move = input("Введите номер: ")
                if move == "1":
                    locations = "edge_of_forest"
                    a["Усталость"] -= 1
                    tim[3] += 1
                elif move == "2":
                    locations = "clearing_at_the_dugout"
                    a["Усталость"] -= 1
                    tim[3] += 3
                elif move == "3":
                    if hard_play_2 == False:
                        print(
                            "Густые заросли чертополоха загромодили путь. Нет, не пройти"
                        )
                    else:
                        locations = "fork"
                        a["Усталость"] -= 3
                        tim[2] += 2
            elif locations == "hole":
                print("Неплохо-бы увидеть солнце")
                print()
                if hard_play_2 == True:
                    print("А где=же тот люк?")
                print("Вы можете пройти к: березняк (1)")
                move = input("Введите номер: ")
                if move == "1":
                    locations = "birch_forest"
                    a["Усталость"] -= 1
                    tim[3] += 3
            elif locations == "fork":
                print("Четыре полосы разьехались кто куда")
                print()
                print(
                    "Вы можете пройти к: лихая тропа (1) Село Погореловка (2) Шоссе (3) Лесное хозяйство (4) Лагерь у обочины (5)"
                )
                move = input("Введите номер: ")
                if move == "1":
                    locations = "dashing_path"
                    a["Усталость"] -= 3
                    tim[3] += 2
                elif move == "2":
                    locations = "village_pogorelovka"
                    a["Усталость"] -= 4
                    tim[3] += 6
                elif move == "3":
                    print("Не, без машины там делать нечего")
                elif move == "4":
                    print("И чего я там забыл?")
                    locations = "the_yard_before_forestry"
                    a["Усталость"] -= 7
                    tim[3] += 11
                elif move == "5":
                    locations = "camp_on_the_sink"
                    a["Усталость"] -= 3
                    tim[3] += 4
            elif locations == "village_pogorelovka":
                print("Свалить бы отсюда побыстрее")
                print()
                print("Вы можете пройти к: развилка (1) жилой дом (2)")
                move = input("Введите номер: ")
                if move == "1":
                    locations = "fork"
                    a["Усталость"] -= 4
                    tim[3] += 6
                elif move == "2":
                    print(
                        "Только подойдя к привлёкшей вас машине, вы увидели свет в окнах единственного уцелевшего дома\n"
                        "Это были мародёры, и они явно не будут рады моему приходу, грохнуть надо их, только чуть позже\n"
                    )
        else:
            mb.showinfo('Nap', "Без сил вы упали прямо посреди локации")
            chance = randint(1, 1)
            if chance == 1:
                mb.showerror('Game over', "Видимо это ваш последний сон")
                game_over()
            else:
                sleep(3)
                if a["Здоровье"] >= 20 and a["Здоровье"] <= 80:
                    a["Здоровье"] += 10
                a["Усталость"] += 40
                a["Голод"] -= 15
                a["Жажда"] -= 10
                tim[1] += 6
                mb.showinfo('Nap', "Думал, засну навеки")
    else:
        print("Перевес")


def music():
    mus = randint(2, 2)
    if mus == 1:
        playsound("fon1.mp3", True)
        playsound("fon1.mp3", False)
    elif mus == 2:
        playsound("fon2.mp3", True)
        playsound("fon2.mp3", False)
    sleep(3)
    music()


def go_to_chat():
    webbrowser.open_new_tab("https://vk.com/im?sel=c59")


def start_single_game():
    global helpl
    global txt
    global face_image
    global im
    global mmm
    global botton_frame_1
    global BOTTON_FRAME
    global Game
    global frame_destroy
    main.destroy()
    sleep(1)
    Game = Tk()
    Game.title("The Rivine")
    Game.configure(background="black")
    mainmenu = Menu(Game, bg="black")
    Game.config(menu=mainmenu)
    filemenu = Menu(mainmenu, tearoff=0)
    filemenu.add_command(label="Сохранить", command=save)
    filemenu.add_command(label="Загрузить", command=load)
    filemenu.add_command(label="Справка", command=go_to_chat)
    mainmenu.add_cascade(label="Игра", menu=filemenu)

    tabs = Notebook(Game)
    tabs.pack(fill=BOTH, expand=True)

    main_tab = Frame(tabs, bg="black")
    level_up_tab = Frame(tabs, bg="black")

    main_tab.pack(fill='both', expand=True)
    level_up_tab.pack(fill='both', expand=True)

    TOP_FRAME = Frame(main_tab, bg="black")
    img_frame = Frame(TOP_FRAME, bg="black")
    help_frame = Frame(TOP_FRAME)
    help_frame.pack(side=RIGHT)
    helpl = Label(help_frame, text="", width=35,
                  height=37, bg="black", fg="white")
    helpl.pack(side=TOP)
    help_frame.pack(side=RIGHT)
    mmm = PhotoImage(file="resources\\BED.png")
    im = Label(img_frame, image=mmm)
    im.pack()
    txt = Label(img_frame, width=100, height=10,
                text="", bg="black", fg="white")
    txt.pack()
    TOP_FRAME.pack()
    img_frame.pack(side=LEFT)

    BOTTON_FRAME = Frame(main_tab, bg="black")
    botton_frame = Frame(BOTTON_FRAME)
    BOTTON_FRAME.pack()
    botton_frame.pack()

    LEVEL_FRAME = Frame(level_up_tab)
    tree = Label(LEVEL_FRAME, width=100, height=10,
                 text="ynfdbg", bg="white", fg="white")
    LEVEL_FRAME.pack()
    tree.pack()
    tabs.add(main_tab, text="Главная")
    tabs.add(level_up_tab, text="Древо улучшений")
    Button(
        botton_frame,
        width=20,
        height=2,
        text="Использовать",
    ).pack(side=LEFT)
    Thread(target=music, daemon=True).start()
    game()
    Game.mainloop()


def go_to_group():
    webbrowser.open_new_tab("https://vk.com/public197287702")


def main_menu():
    global main
    main = Tk()
    main.title("The Rivine")
    TOP_FRAME = Frame(main).pack()
    img_frame = Frame(TOP_FRAME).pack()
    face_image = PhotoImage(file=r"resources\\RIVER.png")
    im = Label(img_frame, image=face_image)
    but = Button(
        img_frame,
        width=20,
        height=2,
        text="Новая игра",
        bg="#567",
        fg="White",
        activebackground="White",
        activeforeground="#567",
        relief="flat",
        font=("Yu Gothic", 9),
        command=start_single_game,
    )
    but1 = Button(
        img_frame,
        width=20,
        height=2,
        text="Сообщество",
        bg="#567",
        fg="White",
        activebackground="Gray",
        activeforeground="#567",
        command=go_to_group,
    )
    but2 = Button(
        img_frame,
        width=20,
        height=2,
        text="Мультиплеер",
        bg="#567",
        fg="White",
        activebackground="White",
        activeforeground="#567",
        relief="groove",
        font=("Yu Gothic", 9),
    )
    news = Label(
        img_frame,
        width=40,
        height=10,
        bg="#567",
        text="Список изменений 2.0.0 \n - графическое оформление\n  - дизайн кнопок и инструментов",
        anchor=NW,
    )
    im.pack()
    but.place(in_=im, x=60, y=10)
    but1.place(in_=im, x=100, y=60)
    but2.place(in_=im, x=140, y=110)
    news.place(in_=im, x=700, y=580)
    main.mainloop()


if __name__ == "__main__":
    main_menu()
