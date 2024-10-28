from enum import IntEnum, StrEnum

class RegIndex(IntEnum):
    NAME = 0
    INN = 1
    KPP = 2
    ADDRESS = 3
    SURNAME = 4
    FIRSTNAME = 5
    PATRONYMIC = 6
    ACTIVITY_TYPE = 7
    PHONES = 8
    EMAIL = 9
    REVENUE = 10
    COST = 11
    OKPO = 12
    PF_REG_NUM = 13
    WEBSITE = 14
    OGRN = 15
    OKVED_ACTIVITY_TYPE = 16
    OKATO_TERRITORY = 17

class RegIndexGov(IntEnum):
    NAME = 0
    INN = 1
    KPP = 2
    ADDRESS = 3
    SURNAME = 4
    FIRSTNAME = 5
    PATRONYMIC = 6
    ACTIVITY_TYPE = 7
    PHONES = 8
    EMAIL = 9
    REVENUE = 10
    COST = 11
    IDENTITYFICATOR = 12
    OKPO = 13
    PF_REG_NUM = 14
    WEBSITE = 15
    OGRN = 16
    OKVED_ACTIVITY_TYPE = 17
    OKATO_TERRITORY = 18


class TempCell(StrEnum):
    NAME = 'E6'
    LEGAL_ADDRESS = 'E7'
    POSTMAIL_ADDRESS = 'E8'
    ADMINISTRATOR = 'E9'
    YEAR = 'E10'
    OWNERSHIP_FORM = 'E11'
    OKPO = 'A15'
    OKVED_ACTIVITY_TYPE = 'D15'
    OKATO_TERRITORY = 'N15'
    INN = 'B17'
    KPP = 'J17'
    OGRN = 'X17'

Abbreviations = [    'АН',    'АО',    'АОЗТ',    'АООТ',    'АП',    'АПК',    'АРА',    'АССР',    'АСУП',    'АЭС',    'БРИЗ',    'ВДНХ',    'ВКП(б)',    'ВЛКСМ',    'ВОГ',    'военкомат',    'ВОИР',    'волисполком',    'ВПО',    'Всекопромсовет',    'ВСНХ',    'ВСХВ',    'ВТЭК',    'ВЦИК',    'ВЦСПС',    'ВЧК',    'г.',    'ГАИ',    'ГАСО',    'гг.',    'ГКО',    'Главюжуралстрой',    'ГО',    'горисполком',    'горком',    'гороно',    'горсовет',    'Госбанк',    'Госплан',    'Госстрах',    'Госстрой',    'ГОСТ',    'ГП',    'ГПУ',    'ГТО',    'ГУ',    'губземотдел',    'губземуправление',    'губисполком',    'губком',    'губпродком',    'губревком',    'ГУЗ',    'ГУП',    'ГЭК',    'Д.',    'дер.',    'ДОК',    'ДП',    'ДСО',    'ЕГЭ',    'ЕЭС',    'ЖБИ',    'ж. д.',    'ЖКО',    'ЖКХ',    'ЖЭК',    'ЗАГС',    'ЗАО',    'здравотдел',    'земотдел',    'исполком',    'и. о.',    'ИТР',    'КИП',    'КИПиА',    'КК',    'КПСС',    'культхоз',    'Л.',    'леспромхоз',    'лесхоз',    'ЛЭП',    'МВД',    'медсанчасть',    'местком',    'ММК',    'МП',    'МТС',    'МУП',    'НИИ',    'НИР',    'НК',    'НКВД',    'НОТ',    'НПО',    'НТД',    'НТИ',    'НТО',    'НЭП',    'ОАО',    'ОАФ',    'обком',    'облздравотдел',    'облземотдел',    'облземуправление',    'облисполком',    'облоно',    'облсовет',    'облсовпроф',    'облфинотдел',    'ОГАЧО',    'ОГПУ',    'окрземуправление',    'окрисполком',    'окрстатбюро',    'окрфинотдел',    'ООО',    'Оп.',    'оп.',    'оргкомитет',    'ОРС',    'ОТК',    'п.',    'партком',    'ПО',    'поссовет',    'промкомбинат',    'промкооперация',    'промотдел',    'промсанитария',    'промфинплан',    'профком',    'п/я',    'р. п.',    'райисполком',    'райком',    'районо',    'райсовет',    'ревком',    'Реввоенсовет',    'РКИ',    'РККА',    'РКП(б)',    'РКСМ',    'РОСТА',    'РСДРП',    'РСУ',    'РСФСР',    'РФ',    'с.',    'С.',    'сберкасса',    'сельсовет',    'Сибревком',    'сл.',    'СМ',    'см.',    'СМИ',    'СМУ',    'СНК',    'СНХ',    'соцкультбыт',    'СПТУ',    'ССР',    'СССР',    'ст.',    'станисполком',    'статбюро',    'статуправление',    'СТО',    'стройфинплан',    'ст-ца',    'США',    'СЭС',    'Т.',    'т. д.',    'т. п.',    'ТАСС',    'техпромфинплан',    'ТОО',    'ТУ',    'ТЭЦ',    'УВД',    'уисполком',    'УПП',    'УралАЗ',    'УралВО',    'УРС',    'Ф.',    'ФГУП',    'ФЗО',    'ФЗУ',    'финотдел',    'ЦАУ',    'ЦЗЛ',    'ЦИК',    'ЦК',    'ЦСУ',    'ЧГПИ',    'ЧГРЭС',    'ЧК',    'ЧМЗ',    'ЧПИ',    'ЧТЗ',    'ЧТПЗ',    'ЧЭМК',    'ЭКОСО',    'ЮУЖД',    'ЮУрГУ']
Abbreviations_Decryption = [    'Академия Наук',    'Акционерное Общество',    'Акционерное Общество Закрытого Типа',    'Акционерное Общество Открытого Типа',    'Арендное Предприятие',    'Агропромышленный Комплекс',    'Американская Организация, Оказывавшая Продовольственную Помощь РСФСР',    'Автономная Советская Социалистическая Республика',    'Автоматические Системы Управления Производством',    'Атомная Электростанция',    'Бюро По Рационализации И Изобретательству',    'Выставка Достижений Народного Хозяйства СССР',    'Всесоюзная Коммунистическая Партия (Большевиков)',    'Всесоюзный Ленинский Коммунистический Союз Молодежи',    'Всероссийское Общество Глухих',    'Военный Комиссариат',    'Всесоюзное Общество Изобретателей И Рационализаторов',    'Волостной Исполнительный Комитет',    'Всесоюзное Производственное Объединение',    'Всесоюзный Совет Промысловой Кооперации',    'Высший Совет Народного Хозяйства',    'Всесоюзная Сельскохозяйственная Выставка',    'Врачебно-Трудовая Экспертная Комиссия',    'Всероссийский Центральный Исполнительный Комитет',    'Всесоюзный Центральный Совет Профессиональных Союзов',    'Всероссийская Чрезвычайная Комиссия По Борьбе С Контрреволюцией И Саботажем',    'Год, Город',    'Государственная Автомобильная Инспекция',    'Государственный Архив Свердловской Области',    'Годы',    'Государственный Комитет Обороны',    'Главное Управление По Строительству В Южно-Уральском Экономическом Районе',    'Гражданская Оборона',    'Городской Исполнительный Комитет',    'Городской Комитет',    'Городской Отдел Народного Образования',    'Городской Совет',    'Государственный Банк',    'Государственная Плановая Комиссия',    'Главное Управление (Правление) Государственного Страхования',    'Госкомитет СМ По Делам Строительства И Архитектуры',    'Государственный Стандарт',    'Государственное Предприятие',    'Государственное Политическое Управление',    'Готов К Труду И Обороне СССР',    'Государственное Учреждение',    'Губернский Земельный Отдел',    'Губернское Земельное Управление',    'Губернский Исполнительный Комитет',    'Губернский Комитет',    'Губернский Продовольственный Комитет',    'Губернский Революционный Комитет',    'Государственное Учреждение Здравоохранения',    'Государственное Унитарное Предприятие',    'Государственная Экзаменационная Комиссия',    'Дело',    'Деревня',    'Деревообрабатывающий Комбинат',    'Дочернее Предприятие',    'Добровольное Спортивное Общество',    'Единый Государственный Экзамен',    'Единая Энергетическая Система',    'Железобетонные Изделия',    'Железная Дорога',    'Жилищно-Коммунальный Отдел',    'Жилищно-Коммунальное Хозяйство',    'Жилищно-Эксплуатационная Контора',    'Запись Актов Гражданского Состояния',    'Закрытое Акционерное Общество',    'Отдел Здравоохранения',    'Земельный Отдел',    'Исполнительный Комитет',    'Исполняющий Обязанности',    'Инженерно-Технические Работники',    'Контрольно-Измерительные Приборы',    'Контрольно-Измерительные Приборы И Автоматика',    'Контрольная Комиссия',    'Коммунистическая Партия Советского Союза',    'Культурное Хозяйство (В Сельском Хозяйстве 20-Х Годов ХХ Века)',    'Лист',    'Лесное Промышленное Хозяйство',    'Лесное Хозяйство',    'Линия Электропередач',    'Министерство Внутренних Дел',    'Медико-Санитарная Часть',    'Местный Комитет',    'Магнитогорский Металлургический Комбинат',    'Муниципальное Предприятие',    'Машинно-Тракторная Станция',    'Муниципальное Унитарное Предприятие',    'Научно-Исследовательский Институт',    'Научно-Исследовательская Работа',    'Народный Комиссариат',    'Народный Комиссариат Внутренних Дел',    'Научная Организация Труда',    'Научно-Производственное Объединение',    'Научно-Техническая Документация',    'Научно-Техническая Информация',    'Научно-Техническое Общество',    'Новая Экономическая Политика',    'Открытое Акционерное Общество',    'Объединенный Архивный Фонд',    'Областной Комитет',    'Областной Отдел Здравоохранения',    'Областной Земельный Отдел',    'Областное Земельное Управление',    'Областной Исполнительный Комитет',    'Областной Отдел Народного Образования',    'Областной Совет',    'Областной Совет Профсоюзов',    'Областной Финансовый Отдел',    'Объединенный Государственный Архив Челябинской Области',    'Объединенное Государственное Политическое Управление',    'Окружное Земельное Управление',    'Окружной Исполнительный Комитет',    'Окружное Статистическое Бюро',    'Окружной Финансовый Отдел',    'Общество С Ограниченной Ответственностью',    'Опись',    'Описи',    'Организационный Комитет',    'Отдел Рабочего Снабжения',    'Отдел Технического Контроля',    'Поселок',    'Партийный Комитет',    'Производственное Объединение',    'Поселковый Совет',    'Промышленный Комбинат',    'Промысловая Кооперация',    'Промышленный Отдел',    'Промышленная Санитария',    'Промышленно-Финансовый План',    'Профсоюзный Комитет',    'Почтовый Ящик',    'Рабочий Поселок',    'Районный Исполнительный Комитет',    'Районный Комитет',    'Районный Отдел Народного Образования',    'Районный Совет',    'Революционный Комитет',    'Революционный Военный Совет',    'Рабоче-Крестьянская Инспекция',    'Рабоче-Крестьянская Красная Армия',    'Российская Коммунистическая Партия (Большевиков)',    'Российский Коммунистический Союз Молодежи',    'Российское Телеграфное Агентство',    'Российская Социал-Демократическая Рабочая Партия',    'Ремонтно-Строительное Управление',    'Российская Советская Федеративная Социалистическая Республика',    'Российская Федерация',    'Село',    'Страница',    'Сберегательная Касса',    'Сельский Совет',    'Сибирский Революционный Комитет',    'Слобода',    'Совет Министров',    'Смотри',    'Средства Массовой Информации',    'Строительно-Монтажное Управление',    'Совет Народных Комиссаров',    'Совет Народного Хозяйства',    'Учреждения Социально-Культурного И Бытового Назначения',    'Сельское Профессионально-Техническое Училище',    'Советская Социалистическая Республика',    'Союз Советских Социалистических Республик',    'Станция',    'Станичный Исполнительный Комитет',    'Статистическое Бюро',    'Статистическое Управление',    'Совет Труда И Обороны',    'Строительно-Финансовый План',    'Станница',    'Соединенные Штаты Америки',    'Санитарно-Эпидемиологическая Станция',    'Том',    'Так Далее',    'Тому Подобное',    'Телеграфное Агентство Советского Союза',    'Технический, Промышленный И Финансовый План',    'Товарищество С Ограниченной Ответственностью',    'Техническое Условие',    'Теплоэнергоцентраль',    'Управление Внутренних Дел',    'Уездный Исполнительный Комитет',    'Учебно-Производственное Предприятие',    'Уральский Автомобильный Завод',    'Уральский Военный Округ',    'Управление Рабочего Снабжения',    'Фонд',    'Федеральное Государственное Унитарное Предприятие',    'Фабрично-Заводское Обучение',    'Фабрично-Заводское Ученичество',    'Финансовый Отдел',    'Центральное Архивное Управление',    'Центральная Заводская Лаборатория',    'Центральный Исполнительный Комитет',    'Центральный Комитет',    'Центральное Статистическое Управление',    'Челябинский Государственный Педагогический Институт',    'Челябинская Государственная Районная Электростанция',    'Чрезвычайная Комиссия По Борьбе С Контрреволюцией, Спекуляцией И Преступлениями По Должности',    'Челябинский Металлургический Завод',    'Челябинский Политехнический Институт',    'Челябинский Тракторный Завод',    'Челябинский Трубопрокатный Завод',    'Челябинский Электрометаллургический Комбинат',    'Экономическое Совещание',    'Южно-Уральская Железная Дорога',    'Южно-Уральский Государственный Университет']
