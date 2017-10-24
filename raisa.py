from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import Filters
import time
import threading
import random

my_token = 'token'

def get_phrase (bot, update):
    looping = True
    global old_phrase_ind
    global old_old_phrase_ind
    while looping:
        phrase_ind = random.randint (0, len (phrases) - 1)
        if old_old_phrase_ind != phrase_ind:
            if old_phrase_ind != phrase_ind:
                phrase = phrases [phrase_ind]
                old_old_phrase_ind = old_phrase_ind
                old_phrase_ind = phrase_ind
                looping = False
                bot.sendMessage (chat_id=update.message.chat_id, text=phrase)

def handle_message (bot, update):
    msg_text = update.message.text
    msg_text = msg_text.lower ()
    if "валентина!" in msg_text:
        for word in words:
            if word in msg_text: 
                bot.sendMessage (chat_id=update.message.chat_id, text="Ой, ну хорошо, уговорили :)")
                get_phrase (bot, update);

words = [
    "стих",
    "стишок",
    "стишк",
    "рифм",
    "стишие",
    "стишье",
    "поэт",
    "поэзи",
    "литератур",
    "строк",
    "строчк",
    "классик",
]
            
phrases = [
    "Ты сказала, что Саади\nЦеловал лишь только в грудь.\nПодожди ты, бога ради,\nОбучусь когда-нибудь!\n\nТы пропела: «За Евфратом\nРозы лучше смертных дев».\nЕсли был бы я богатым,\nТо другой сложил напев.\n\nЯ б порезал розы эти,\nВедь одна отрада мне —\nЧтобы не было на свете\nЛучше милой Шаганэ.\nИ не мучь меня заветом,\nУ меня заветов нет.\nКоль родился я поэтом,\nТо целуюсь, как поэт.",
    "Сыпь, гармоника. Скука… Скука…\nГармонист пальцы льет волной.\nПей со мною, паршивая сука,\nПей со мной.\n\nИзлюбили тебя, измызгали —\nНевтерпеж.\nЧто ж ты смотришь так синими брызгами?\nИль в морду хошь?\n\nВ огород бы тебя на чучело,\nугать ворон.\nДо печенок меня замучила\nСо всех сторон.\n\nСыпь, гармоника. Сыпь, моя частая.\nПей, выдра, пей.\nМне бы лучше вон ту, сисястую, —\nОна глупей.\n\nЯ средь женщин тебя не первую…\nНемало вас,\nНо с такой вот, как ты, со стервою\nЛишь в первый раз.\n\nЧем вольнее, тем звонче,\nТо здесь, то там.\nЯ с собой не покончу,\nИди к чертям.\n\nК вашей своре собачьей\nПора простыть.\nДорогая, я плачу,\nПрости… прости…",
    "Вот они, толстые ляжки\nЭтой похабной стены.\nЗдесь по ночам монашки\nСнимают с Христа штаны.",
    "Не смотри, что рассеян в россыпь,\nчто ломаю и мну себя.\nЯ раздел эту девку — Осень,\nи забылся, ее ебя.\nАх ты сука! Такое тело\nмеж блядьми мне не сыскать!\nСладкой влагой плодов вспотела,\nкольца ягод в твоих сосках.\nРаспахнула! О алый бархат\nгуб и губ! Сумасшедший визг!\nНе могу!!! Позовите Баха!\nон напишет “сонату пизд”.\nАх пора ты моя живая!\nГолова — голова — минет.\nРазрывает меня, сжигает,\nя кончаю… простите мне.",
    "Мне бы женщину — белую, белую\nНу а впрочем какая разница\nЯ прижал бы ее с силой к дереву\nИ в задницу, в задницу, в задницу.",
    "Не тужи, дорогой, и не ахай,\nЖизнь держи, как коня, за узду,\nПосылай всех и каждого на хуй,\nЧтоб тебя не послали в пизду!",
    "Ветер веет с юга\nИ луна взошла,\nЧто же ты, блядюга,\nНочью не пришла?\n\nНе пришла ты ночью,\nНе явилась днем.\nДумаешь, мы дрочим?\nНет! Других ебём!",
    "Я в Париже живу как денди.\nЖенщин имею до ста.\nМой хуй, как сюжет в легенде,\nПереходит из уст в уста.",
    "Мы, онанисты, ребята плечисты!\nНас не заманишь титькой мясистой!\nНе совратишь нас пиздовою плевой!\nКончил правой, работай левой!!!",
    "Эй, онанисты, кричите «Ура!» —\nмашины ебли налажены,\nк вашим услугам любая дыра,\nвплоть до замочной скважины!!!",
    "Лежу на чужой жене,\nпотолок прилипает к жопе,\nно мы не ропщем —\nделаем коммунистов,\nназло буржуазной Европе!\n\nПусть хуй мой как мачта\nтопорщится!\nМне все равно, кто подо мной —\nжена министра или уборщица!",
    "Вы любите розы? а я на них срал!\nстране нужны паровозы, нам нужен металл!\nтоварищ! не охай, не ахай!\nне дёргай узду!\nколь выполнил план,\nпосылай всех в пизду\nне выполнил —сам иди на хуй.",
    "Не те бляди,\nчто хлеба ради\nспереди и сзади\nдают нам ебти,\nБог их прости!\nА те бляди —\nлгущие,\nденьги сосущие,\nебать не дающие —\nвот бляди сущие,\nмать их ети!",
    "Нам ебля нужна\nкак китайцам рис.\nНе надоест хую радиомачтой топорщиться!\nВ обе дырки гляди —\nне поймай сифилис.\nА то будешь\nперед врачами корчиться!",
    "Вам, проживающим за оргией оргию,\nимеющим ванную и теплый клозет!\nКак вам не стыдно о представленных к Георгию\nвычитывать из столбцов газет?\n\nЗнаете ли вы, бездарные, многие,\nдумающие нажраться лучше как,-\nможет быть, сейчас бомбой ноги\nвыдрало у Петрова поручика?..\n\nЕсли он приведенный на убой,\nвдруг увидел, израненный,\nкак вы измазанной в котлете губой\nпохотливо напеваете Северянина!\n\nВам ли, любящим баб да блюда,\nжизнь отдавать в угоду?!\nЯ лучше в баре блядям буду\nподавать ананасную воду!",
    "Накажи, святой угодник,\nКапитана Борозду,\nРазлюбил он, греховодник,\nНашу матушку пизду.\n\nС утра садимся мы в телегу,\nМы рады голову сломать\nИ, презирая лень и негу,\nКричим: пошёл! ебёна мать!",
    "Молчи ж, кума; и ты, как я, грешна,\nА всякого словами разобидишь;\nВ чужой пизде соломинку ты видишь,\nА у себя не видишь и бревна!",
    "Мы пили - и Венера с нами\nСидела, прея, за столом.\nКогда ж вновь сядем вчетвером\nС блядьми, вином и чубуками?",
    "Подойди, Жанета,\nА Луиза - поцелуй,\nВыбрать, так обидишь;\nТак на всех и встанет хуй,\nТолько вас увидишь.",
    "Ты помнишь ли, как были мы в Париже,\nГде наш казак иль полковой наш поп\nМорочил вас, к винцу подсев поближе,\nИ ваших жён похваливал да ёб?",
    "Наконец из Кенигсберга\nЯ приблизился к стране,\nГде не любят Гуттенберга\nИ находят вкус в говне.\nВыпил русского настою,\nУслыхал <<ебёну мать>>,\nИ пошли передо мною\nРожи русские писать.",
    "Когда расступаются тучи\nИ с неба сияет звезда -\nО члене большом и могучем\nВ мечтах молодая пизда.\n\nНе все, что судьба предвещает,\nИмеет достойный конец.\nИ вот уж пизду навещает\nЗажатый в руке огурец!",
    "Один при члене при своем,\nОдин - такое дело.\nА та, что числится при нем,\nСмертельно надоела.\nИ хоть приставлена судьбой,\nНо все ж сказала гнусно:\n<<Я ухожу - и хуй с тобой!>>\nДа, хуй со мной. Но грустно.",
]
  
old_phrase_ind = -1;
old_old_phrase_ind = -1;
    
updater = Updater (token=my_token)
handler = MessageHandler (Filters.text | Filters.command, handle_message)
updater.dispatcher.add_handler (handler)
updater.start_polling ()
