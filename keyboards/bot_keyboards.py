from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

class Keyboards:
    @staticmethod
    async def educational_environment_keyboard():
        builder = InlineKeyboardBuilder()
        builder.button(text="Iнфраструктура",url="http://cee.kdu.edu.ua/uk/content/infastruktura")
        builder.button(text="Аудиторний фонд кафдери",url="http://cee.kdu.edu.ua/uk/content/audytornyy-fond-kafedry")
        builder.button(text="Бiблiотечний фонд кафедри",url="http://cee.kdu.edu.ua/uk/content/bibliotechnyy-fond-kafedry")
        builder.button(text="Забезпечення особливих потреб",url="http://cee.kdu.edu.ua/uk/content/zabezpechennya-osoblyvyh-potreb")
        builder.button(text="Повернутись до головної cторiнки",callback_data="back_to_main")
        builder.adjust(1)
        return builder.as_markup()

    @staticmethod
    async def practical_training_keyboard():
        builder = InlineKeyboardBuilder()
        builder.button(text="Бази практик",url="http://cee.kdu.edu.ua/uk/content/bazy-praktyk")
        builder.button(text="Нормативна документацiя",url="http://cee.kdu.edu.ua/uk/content/normatyvna-dokumentaciya")
        builder.button(text="Договори про спiвпрацю",url="http://cee.kdu.edu.ua/uk/content/dogovory-pro-spivpracyu")
        builder.button(text="Залучення практикiв до пiдготовки здобувачiв",url="http://cee.kdu.edu.ua/uk/content/zaluchennya-praktykiv-do-pidgotovky-zdobuvachiv")
        builder.button(text="Вакансії з працевлаштування",url="http://cee.kdu.edu.ua/uk/node/343")
        builder.button(text="Повернутись до головної cторiнки",callback_data="back_to_main")
        builder.adjust(1)
        return builder.as_markup()
    @staticmethod
    async def international_activity_keyboard():
        builder = InlineKeyboardBuilder()
        builder.button(text="Договори про спiвпрацю",url="http://cia.kdu.edu.ua/mignar_zvyazk_partn.php")
        builder.button(text="Закордонi стажування",url="http://cee.kdu.edu.ua/uk/content/zakordonni-stazhuvannya")
        builder.button(text="Мiжнароднi здобутки",url="http://cee.kdu.edu.ua/uk/content/mizhnarodni-zdobutky")
        builder.button(text="Мiжнародний конкурс студентських наукових робiт",url="http://krnukonkurs.kdu.edu.ua/")
        builder.button(text="Повернутись до головної cторiнки",callback_data="back_to_main")
        builder.adjust(1)
        return builder.as_markup()
    @staticmethod
    async def educational_activity_keyboard():
        builder = InlineKeyboardBuilder()
        builder.button(text="План роботи",url="http://cee.kdu.edu.ua/uk/content/plany-vyhovnoyi-roboty")
        builder.button(text="Заходи",url="http://cee.kdu.edu.ua/uk/content/vyhovni-zahody")
        builder.button(text="Нормативна документацiя та методичнi матерiали",url="http://cee.kdu.edu.ua/uk/content/normatyvna-dokumentaciya-ta-metodychni-materialy")
        builder.button(text="Повернутись до головної cторiнки",callback_data="back_to_main")
        builder.adjust(1)
        return builder.as_markup()
    @staticmethod
    async def scientific_activity_keyboard():
        builder = InlineKeyboardBuilder()
        builder.button(text="Науковi здобутки",url="http://cee.kdu.edu.ua/uk/content/naukovi-zdobutky")
        builder.button(text="Теми НДР",url="http://cee.kdu.edu.ua/uk/content/temy-ndr")
        builder.button(text="Науковi заходи",url="http://cee.kdu.edu.ua/uk/content/naukovi-zahody")
        builder.button(text="Наукова дiяльнiсть здобувачiв освiти",url="http://cee.kdu.edu.ua/uk/content/naukova-diyalnist-zdobuvachiv-osvity")
        builder.button(text="Повернутись до головної cторiнки",callback_data="back_to_main")
        builder.adjust(1)
        return builder.as_markup()
    @staticmethod
    async def education_keyboard():
        builder = InlineKeyboardBuilder()
        builder.button(text="Освiтнi програми", callback_data="list_education")
        builder.button(text="Розклад", url="http://193.189.127.179:5010/")
        builder.button(text="Якiсть освiти", url="http://cee.kdu.edu.ua/uk/content/yakist-osvity")
        builder.button(text="Неформальна i дуальна освiта", callback_data="casual_dual_education")
        builder.button(text="Вiртуальний оcвiтнiй простiр", url="http://krnu.org/course/index.php?categoryid=18")
        builder.button(text="Подiї", url="http://cee.kdu.edu.ua/uk/informal-dual-education")
        builder.button(text="Повернутись до головної cторiнки",callback_data="back_to_main")
        builder.adjust(1)
        return builder.as_markup()

    @staticmethod
    async def to_the_entrant_keyboard():
        builder = InlineKeyboardBuilder()
        builder.button(text="Iнформацiя про освiтнi програми", url="http://cee.kdu.edu.ua/uk/content/informaciya-pro-osvitni-programy")
        builder.button(text="Правила прийому", url="http://www.kdu.edu.ua/new/priyom.php")
        builder.button(text="Програма вступних випробувань", url="http://cee.kdu.edu.ua/uk/content/programy-vstupnyh-vyprobuvan")
        builder.button(text="Iноземним студентам", url="http://cee.kdu.edu.ua/uk/content/inozemnym-studentam")
        builder.button(text="Контакти щодо вступу", url="http://www.kdu.edu.ua/new/contact_pk.php")
        builder.button(text="Повернутись до головної cторiнки",callback_data="back_to_main")
        builder.adjust(1)
        return builder.as_markup()

    @staticmethod
    async def about_the_departament_keyboard():
        builder = InlineKeyboardBuilder()
        builder.button(text="Iсторiя", url="http://cee.kdu.edu.ua/uk/content/istoriya-kafedry-kompyuternoyi-inzheneriyi-ta-elektroniky")
        builder.button(text="Склад кафедри", url="http://cee.kdu.edu.ua/uk/employees-cee")
        builder.button(text="Ліцензії i сертифiкати", url="http://cee.kdu.edu.ua/uk/content/licenziyi-i-sertyfikaty")
        builder.button(text="Пiдсумки рейтингування", url="http://cee.kdu.edu.ua/uk/content/pidsumky-reytynguvannya")
        builder.button(text="Випускники", url="http://cee.kdu.edu.ua/uk/content/vypusknyky")
        builder.button(text="Повернутись до головної cторiнки",callback_data="back_to_main")
        builder.adjust(1)
        return builder.as_markup()

    @staticmethod
    async def start_keyboard():
        builder = InlineKeyboardBuilder()
        builder.button(text="Про кафедру", callback_data="Про кафедру")
        builder.button(text="Вступнику", callback_data="Вступнику")
        builder.button(text="Освiта", callback_data="Освiта")
        builder.button(text="Наукова дiяльнiсть", callback_data="Наукова дiяльнiсть")
        builder.button(text="Виховна дiяльнiсть", callback_data="Виховна дiяльнiсть")
        builder.button(text="Мiжнародна дiяльнiсть",callback_data="Мiжнародна дiяльнiсть")
        builder.button(text="Практична пiдготовка", callback_data="Практична пiдготовка")
        builder.button(text="Освітнє середовище", callback_data="Освітнє середовище")
        builder.button(text="Контакти", url="http://cee.kdu.edu.ua/uk/content/de-nas-znayty")
        builder.adjust(1)
        return builder.as_markup()
