# Игра: Тропы России — 16 народов
# Полная версия с эмоциями, очками и концовками

define e = Character("Преподаватель Вера Павловна", who_color="#c0c0c0")
define r = Character("Бабушка Марфа", who_color="#d3d3d3")
define t = Character("Бабушка Гульшат", who_color="#90ee90")
define ch = Character("Старейшина Аслан", who_color="#ffcc99")
define b = Character("Акберди", who_color="#b0c4de")
define y = Character("Айхал", who_color="#e0ffff")
define cv = Character("Тетя Светлана", who_color="#f0e68c")
define bu = Character("Баир", who_color="#87ceeb")
define a = Character("Магомед", who_color="#f5deb3")
define k = Character("Очир", who_color="#fffacd")
define ka = Character("Миккел", who_color="#d8bfd8")
define m = Character("Сана", who_color="#c1ffc1")
define ck = Character("Рынтыргин", who_color="#b0e0e6")
define n = Character("Ненецкий шаман", who_color="#ffdab9")
define ev = Character("Верба", who_color="#ffe4e1")
define ke = Character("Старый Керек", who_color="#e6e6fa")
define it = Character("Ительмен Итэль", who_color="#ffdead")

default points = 0
default vocab = ""

label start:
    scene black
    show text "ТРОПЫ РОССИИ — 16 НАРОДОВ" with dissolve
    pause 1.0
    hide text

    scene bg classroom
    show teacher happy
    e "Ты студент-этнограф. Твоё задание — посетить 16 народов России и узнать их традиции."
    e "За каждый правильный ответ ты получишь балл и слово в словарь."
    e "Если соберёшь максимум — я буду впечатлена. Поехали!"

    call russian
    call tatars
    call chechens
    call bashkirs
    call yakuts
    call chuvash
    call buryats
    call avars
    call kalmyks
    call karelians
    call mordvins
    call chukchi
    call nenets
    call evens
    call kereks
    call itelmens

    jump final

# ============================================
# НАРОД 1: РУССКИЕ
# ============================================
label russian:
    scene bg russian
    show babushka neutral
    r "Мир вашему дому, гость дорогой! Присаживайся."
    r "Скажи, что символизирует 'хлеб-соль' при встрече гостя?"

    menu:
        "Пожелание богатства":
            $ points += 0
            show babushka angry
            r "Нет, хлеб-соль не только про деньги."
        "Признание гостя посланником Бога":
            $ points += 1
            $ vocab += " Хлеб-соль"
            show babushka happy
            r "Верно! Хлеб — жизнь, соль — душа. Ты молодец!"
        "Охрана дома от злых духов":
            $ points += 0
            show babushka neutral
            r "Это часть правды, но не всё. Ладно."
    return

# ============================================
# НАРОД 2: ТАТАРЫ
# ============================================
label tatars:
    scene bg kazan
    show gulchat neutral
    t "Әйдә, кер! Что ты знаешь о 'тастымал' — свадебном полотенце?"

    menu:
        "Чтобы вытирать руки":
            $ points += 0
            show gulchat angry
            t "Нет, это не просто полотенце!"
        "Символ чистоты и новой жизни":
            $ points += 1
            $ vocab += " Тастымал"
            show gulchat happy
            t "Молодец! Тастымал — начало нового пути."
        "Для защиты от сглаза":
            $ points += 0
            show gulchat neutral
            t "Близко, но не точно. В следующий раз угадаешь."
    return

# ============================================
# НАРОД 3: ЧЕЧЕНЦЫ
# ============================================
label chechens:
    scene bg chechen
    show aslan neutral
    ch "Ассаламу алейкум! Что такое 'къонахалла'?"

    menu:
        "Гостеприимство":
            $ points += 0
            show aslan angry
            ch "Нет! Къонахалла — это не просто угостить."
        "Кодекс чести мужчины":
            $ points += 1
            $ vocab += " Къонахалла"
            show aslan happy
            ch "Верно! Защита слабых, щедрость, верность слову."
        "Помощь соседям":
            $ points += 0
            show aslan neutral
            ch "Это только часть. Ты старался."
    return

# ============================================
# НАРОД 4: БАШКИРЫ
# ============================================
label bashkirs:
    scene bg bashkir
    show akberdi neutral
    b "Һаумыһығыҙ! Что означает обычай 'язы'?"

    menu:
        "Коня закапывали рядом":
            $ points += 0
            show akberdi angry
            b "Нет! Это не так."
        "Ритуал с веткой берёзы для духа коня":
            $ points += 1
            $ vocab += " Язы"
            show akberdi happy
            b "Эйее! Ветка берёзы — чтобы душа поднялась к духам."
        "Коня приносили в жертву и съедали":
            $ points += 0
            show akberdi neutral
            b "Нет, мясо коня в такие дни не едят."
    return

# ============================================
# НАРОД 5: ЯКУТЫ
# ============================================
label yakuts:
    scene bg yakut
    show aykhal neutral
    y "Дорообо! Что такое 'алгыс'?"

    menu:
        "Песня шамана для духов":
            $ points += 1
            $ vocab += " Алгыс"
            show aykhal happy
            y "Верно! Алгыс — благословение духам природы."
        "Оберег из шкуры":
            $ points += 0
            show aykhal angry
            y "Нет, алгыс — это действие, а не вещь."
        "Танец вокруг костра":
            $ points += 0
            show aykhal neutral
            y "Танец — осуохай, а алгыс — слова шамана."
    return

# ============================================
# НАРОД 6: ЧУВАШИ
# ============================================
label chuvash:
    scene bg chuvash
    show svetlana neutral
    cv "Салам! Зачем чуваши закапывали монеты на углах нового дома?"

    menu:
        "Чтобы дом был богатым":
            $ points += 0
            show svetlana angry
            cv "Нет! Это не главная причина."
        "Чтобы задобрить духа земли 'Йĕрĕх'":
            $ points += 1
            $ vocab += " Йĕрĕх"
            show svetlana happy
            cv "Верно! Сначала просишь разрешения у хозяина земли."
        "Чтобы откупиться от воров":
            $ points += 0
            show svetlana neutral
            cv "Нет, но ты попытался."
    return

# ============================================
# НАРОД 7: БУРЯТЫ
# ============================================
label buryats:
    scene bg buryat
    show bair neutral
    bu "Амар мэндэ! Что такое 'обоо'?"

    menu:
        "Алтарь для молений":
            $ points += 0
            show bair angry
            bu "Нет! Обоо — это не алтарь."
        "Каменная куча с синими хадаками":
            $ points += 1
            $ vocab += " Обоо"
            show bair happy
            bu "Правильно! Жилище хозяина местности."
        "Палатка для жертв":
            $ points += 0
            show bair neutral
            bu "Нет, это груда камней."
    return

# ============================================
# НАРОД 8: АВАРЦЫ
# ============================================
label avars:
    scene bg avar
    show magomed neutral
    a "Баркала! Зачем кладут ножницы, сахар и иглу перед ребёнком?"

    menu:
        "Чтобы выбрать профессию":
            $ points += 1
            $ vocab += " Первый шаг"
            show magomed happy
            a "Молодец! Что схватит — тем и будет заниматься."
        "Для защиты от духов":
            $ points += 0
            show magomed angry
            a "Нет! Это ритуал выбора."
        "Для веселья гостей":
            $ points += 0
            show magomed neutral
            a "Обычай серьёзный, не для забавы."
    return

# ============================================
# НАРОД 9: КАЛМЫКИ
# ============================================
label kalmyks:
    scene bg kalmyk
    show ochir neutral
    k "Мендвт! Что делали с 'молоком волчицы'?"

    menu:
        "Кропили юрту для духа Окон-Тенгри":
            $ points += 1
            $ vocab += " Окон-Тенгри"
            show ochir happy
            k "Зөв! Окон-Тенгри — бог-воин."
        "Пили, чтобы стать храбрым":
            $ points += 0
            show ochir angry
            k "Нет! Это легенда."
        "Кормили собак":
            $ points += 0
            show ochir neutral
            k "Нет, собаки здесь ни при чём."
    return

# ============================================
# НАРОД 10: КАРЕЛЫ
# ============================================
label karelians:
    scene bg karelian
    show mikkel neutral
    ka "Terveh! Зачем вешали лапоть на берёзу при стройке бани?"

    menu:
        "Чтобы духи не трогали":
            $ points += 0
            show mikkel angry
            ka "Нет! Это не так."
        "Чтобы обмануть лешего":
            $ points += 1
            $ vocab += " Лапоть обман"
            show mikkel happy
            ka "Мудрый гость! Леший думал, что хозяин ушёл."
        "Для отпугивания медведей":
            $ points += 0
            show mikkel neutral
            ka "Нет, мишки любопытны."
    return

# ============================================
# НАРОД 11: МОРДВА
# ============================================
label mordvins:
    scene bg mordovian
    show sana neutral
    m "Шумбрат! Что символизировала свеча на свадьбе?"

    menu:
        "Символ чистоты, гасили для духов предков":
            $ points += 1
            $ vocab += " Озкс"
            show sana happy
            m "Верно! Свеча — огонь новой семьи."
        "Чтобы не сгорел дом":
            $ points += 0
            show sana angry
            m "Нет, это ритуал, а не пожарная безопасность."
        "Знак бога Солнца":
            $ points += 0
            show sana neutral
            m "Солнце — отдельный обряд."
    return

# ============================================
# НАРОД 12: ЧУКЧИ
# ============================================
label chukchi:
    scene bg chukchi
    show ryntyrgin neutral
    ck "Эʼй! Что нельзя делать в яранге?"

    menu:
        "Не свистеть — духи утащат душу":
            $ points += 1
            $ vocab += " Священный рог"
            show ryntyrgin happy
            ck "Верно! Свист — язык душ умерших."
        "Не шуметь":
            $ points += 0
            show ryntyrgin angry
            ck "Нет! Шуметь можно, а свистеть — нет."
        "Не трогать огонь":
            $ points += 0
            show ryntyrgin neutral
            ck "Огонь — живой, но свист страшнее."
    return

# ============================================
# НАРОД 13: НЕНЦЫ
# ============================================
label nenets:
    scene bg nenets
    show nenets_shaman neutral
    n "Тава! Почему нельзя убивать белого оленя без ритуала?"

    menu:
        "Он посланник неба, кожа — врата для духов":
            $ points += 1
            $ vocab += " Белый олень"
            show nenets_shaman happy
            n "Правильно! Белый олень священен."
        "Едят сразу":
            $ points += 0
            show nenets_shaman angry
            n "Нет! Без ритуала грех."
        "Дарят шаману":
            $ points += 0
            show nenets_shaman neutral
            n "Шаману отдают часть, не всё."
    return

# ============================================
# НАРОД 14: ЭВЕНЫ
# ============================================
label evens:
    scene bg even
    show verba neutral
    ev "Торэ! Что запрещено женщинам на 'медвежьем празднике'?"

    menu:
        "Смотреть на кости медведя и перешагивать через оружие":
            $ points += 1
            $ vocab += " Медвежий праздник"
            show verba happy
            ev "Верно! Женщина не может видеть кости — это обесчестит духа зверя."
        "Говорить вслух":
            $ points += 0
            show verba angry
            ev "Нет! Говорить можно, но не всё."
        "Прикасаться к огню":
            $ points += 0
            show verba neutral
            ev "Огонь — женское, тут другое."
    return

# ============================================
# НАРОД 15: КЕРЕКИ
# ============================================
label kereks:
    scene bg kerek
    show stary_kerek neutral
    ke "Йыкы! Что нельзя делать с 'каменной бабой'?"

    menu:
        "Кидать гарпун или плевать":
            $ points += 1
            $ vocab += " Каменная баба"
            show stary_kerek happy
            ke "Правильно! Каменная баба — хозяйка моря."
        "Садиться рядом":
            $ points += 0
            show stary_kerek angry
            ke "Нет! Сидеть можно, если мирно."
        "Красить в белый":
            $ points += 0
            show stary_kerek neutral
            ke "Красить нечем было, запрета нет."
    return

# ============================================
# НАРОД 16: ИТЕЛЬМЕНЫ
# ============================================
label itelmens:
    scene bg itelmen
    show itel neutral
    it "Ксай! Какой ритуал при встрече с мёртвым китом?"

    menu:
        "Поклониться и попросить прощения у духа Митгу":
            $ points += 1
            $ vocab += " Ксай"
            show itel happy
            it "Правильно! Кит — священное животное."
        "Съесть кусок мяса":
            $ points += 0
            show itel angry
            it "Нет! Нельзя, пока дух не успокоишь."
        "Сбежать":
            $ points += 0
            show itel neutral
            it "Тогда удачи не видать."
    return

# ============================================
# ФИНАЛ
# ============================================
label final:
    scene bg classroom
    show teacher happy

    e "Ты прошёл всех 16 народов!"
    e "Твой счёт: [points] из 16."
    e "Твой словарь: [vocab]"

    if points >= 14:
        e "КОНЦОВКА: «Хранитель традиций» — Ты настоящий этнограф!"
        e "Автомат, стипендия и приглашение на этно-форум."
    elif points >= 10:
        e "КОНЦОВКА: «Посол дружбы» — Отличная работа!"
        e "Автомат. Поедешь со мной в экспедицию?"
    elif points >= 6:
        e "КОНЦОВКА: «Уважаемый гость» — Неплохо, но можно лучше."
        e "Автомат, но в следующий раз готовься серьёзнее."
    else:
        e "КОНЦОВКА: «Здравствуйте, я турист» — Ты везде побывал, но ничего не понял."
        e "Экзамен пересдашь."

    e "Россия — это когда в гостях у каждого находишь что-то своё, а уезжаешь с чем-то общим."
    e "Спасибо за игру!"

    return