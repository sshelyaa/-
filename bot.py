import random
import math
from colorama import Fore
import sys
import re
import datetime


d = datetime.datetime.now().strftime("(%Y-%m-%d %H.%M.%S)")


def logger(text):
    with open('Діалог' + d + '.txt', 'a', encoding='utf-8') as f:
        f.write(str(re.sub('\033\[[^m]*m', '', str(text)) + '\n'))
    return text


reactions = [
            "Цікавий вибір!",
            "Моя улюблена тема!",
            "Тривіальний вибір",
            "Цікаво!"
        ]


class Physics:

    def __init__(self):
        print(logger(Fore.MAGENTA + 'Доступні теми:'
              '\n1. Рівняння Гейзенберга\n'
              '2. Закон Стефана-Больцмана\n3. Виведи Сталу Планка.\n'
              'Введіть Назад для повернення до вибору предмета'))
        i = logger(input(logger(Fore.GREEN + 'Виберіть тему: \n')))
        if i == '1':
            self.heisenberg_equation()
        elif i == '2':
            self.bolcman()
        elif i == '3':
            self.planck_constant()
        elif i == 'Назад':
            Bot()
        else:
            print(logger('Неправильне введення.'))
        Physics()

    def heisenberg_equation(self):
        print(logger(Fore.MAGENTA + '''Рівняння, що описує еволюцію квантової спостережуваної гамільтонової системи,
    отримане Вернером Гейзенбергом в 1925 році. Має вигляд: Δx * Δp >= h/2π,де Δx - похибка у визначенні положення 
    частинки, а Δp - похибка у вимірюванні імпульсу частинки. Отже, рівняння описує обернену пропорційність 
    похибок вимірювання положення та імпульсу частинки, адже їх добуток має бути більшим або дорівнювати сталій.'''))
        Physics()

    def bolcman(self):
        try:
            area = float(logger(input(logger(Fore.GREEN + 'Введіть площу поверхні тіла: \n'))))
            temperature = float(logger(input(logger(Fore.GREEN + 'Введіть абсолютну температуру тіла: \n'))))
            power = 5.67e-8 * area * temperature ** 4
            print(logger(Fore.MAGENTA + str(power)))
        except ValueError:
            print(logger('Неправильне значення'))
            Physics.bolcman(self)

    def planck_constant(self):
        planck_constant = 6.62607015e-34
        print(logger(Fore.MAGENTA + "Стала Планка:" + str(planck_constant)))
        Physics()


class Math:

    def __init__(self):
        print(logger(Fore.MAGENTA + 'Доступні теми:'
              '\n1. Розв\'яжи квадратне рівняння\n2. Виведи скалярний добуток'
              ' векторів.\n3. Підрахуй площу трикутника\n4. Виведи n-нне число Фібоначчі\n'
              'Введіть Назад для повернення до вибору предмета'))
        i = logger(input(logger(Fore.GREEN + 'Виберіть тему: \n')))
        if i == '1':
            self.quadratic_equation()
        elif i == '2':
            self.scalar_product()
        elif i == '3':
            self.triangle_area()
        elif i == '4':
            self.fib_sequence()
        elif i == 'Назад':
            Bot()
        else:
            print(logger('Неправильне введення.'))
        Math()

    def quadratic_equation(self):
        try:
            a = int(logger(input(logger(Fore.GREEN + 'Введіть коефіцієнт а: '))))
            b = int(logger(input(logger(Fore.GREEN + 'Введіть коефіцієнт b: '))))
            c = int(logger(input(logger(Fore.GREEN + 'Введіть коефіцієнт с: '))))
            try:
                print(logger((-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a))
                print(logger((-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a))
            except ValueError:
                print(logger(Fore.MAGENTA + 'Дискримінант менше нуля'))

        except ValueError:
            print(logger(Fore.MAGENTA + 'Неправильне введення'))

    def triangle_area(self):
        try:
            a = int(logger(input(logger(Fore.GREEN + 'Введіть довжину сторони трикутника: '))))
            h = int(logger(input(logger(Fore.GREEN + 'Введіть довжину висоти яка спирається на сторону: '))))
            print(logger(Fore.MAGENTA + str(0.5 * a * h)))
        except ValueError:
            print(logger(Fore.MAGENTA + 'Неправильне введення'))

    def fib_sequence(self):
        try:
            n = int(logger(input(logger(logger(Fore.GREEN + 'Введи номер числа: ')))))
        except ValueError:
            print(logger(Fore.MAGENTA + 'Неправильне введення'))

        def fibonacci(n):
            if n < 0:
                print(logger(Fore.MAGENTA + "Неправильне введення: "))
            elif n == 0:
                return 0
            elif n == 1 or n == 2:
                return 1
            else:
                return fibonacci(n - 1) + fibonacci(n - 2)

        print(logger(logger(Fore.GREEN + str(fibonacci(n)))))

    def scalar_product(self):
        try:
            a = int(logger(input(logger(Fore.GREEN + 'Введіть довжину першого вектора: '))))
            b = int(logger(input(logger(Fore.GREEN + 'Введіть довжину другого вектора: '))))
            cs = math.cos(int(logger(input(logger(Fore.GREEN + 'Введіть радіанну міру кута між векторами: ')))))
            print(Fore.MAGENTA + logger(a * b * cs))
        except ValueError:
            print(Fore.MAGENTA + 'Неправильне введення')


class Geography:

    def __init__(self):
        print(logger(Fore.MAGENTA + 'Доступні теми:'
              '\n1. Назви 5 найвищих гір в світі та вкажи їх висоти.\n2. Які дві держави мають'
              ' найбільшу кількість кордонів з іншими державами?\n3. Яка держава має найбільшу кількість озер?'
              '\nВведіть "Назад" для повернення до вибору предмета'))
        i = logger(input(logger(Fore.GREEN + 'Виберіть тему, про яку хочете дізнатись: \n')))
        if i == '1':
            self.mountains()
        elif i == '2':
            self.boundaries()
        elif i == '3':
            self.population()
        elif i == 'Назад':
            Bot()
        else:
            print(logger(Fore.MAGENTA + 'Тема вибрана не правильно'))
        Geography()

    def mountains(self):
        print(logger(Fore.MAGENTA + '1. Еверест/Джомолунгма - 8849 (Китай/Непал)\n2. К2/Чоґорі - 8611 (Китай/Індія)\n'
              '3. Канченджанґа - 8586 (Непал/Індія)\n4. Лхоцзе - 8516 (Китай/Непал)\n5. Макалу - 8463 (Непал/Китай)'))

    def boundaries(self):
        print(logger(Fore.MAGENTA + 'Найбільше кордонів мають свиноросія та КНР: по 14.\nСвиноросія межує'
              ' з Норвегією, Фінляндією, Естонією, Латвією, Литвою, Польщею, Білоруссю, Україною, Грузією,\n'
              ' Азербайджаном, Казахстаном, КНР, Монголією, КНДР\nКНР межує з КНДР, свиноросією, Монголією, '
              'Казахстаном, Киргистаном, Таджикистаном, Афганістаном, Пакістаном, Індією, Непалом, Бутаном, М\'янмою,'
              ' Лаосом, В\'єтнамом'))

    def population(self):
        print(logger(Fore.MAGENTA + 'Місце з найбільшою кількістю населення в світі є Шанхай, '
              'приблизна кількість його населення - 24 150 000 осіб.'))


class Philology:
    def __init__(self):
        print(logger(Fore.MAGENTA + 'Доступні теми:'
              '\n1. Як утворити форму множини іменників в українській мові? у \n'
              'Введіть "Назад" для повернення до вибору предмета'))
        i = input(logger(Fore.GREEN + 'Виберіть тему, про яку хочете дізнатись: \n'))
        if i == '1':
            self.quantities()
        elif i == 'Назад':
            Bot()
        else:
            print(logger(Fore.MAGENTA + 'Тема вибрана не правильно'))
        Philology()

    def quantities(self):
        print(logger(Fore.MAGENTA + 'Якщо іменник закінчується на м\'який знак (ь), то він випадає у формі множини.\n'
              'Наприклад: стіл - столи, вікно - вікна.'
              'Якщо іменник закінчується на голосний звук (а, я, о, є, ї, і, у, ю), то до нього додається суфікс'
              ' -й- перед закінченням -и.\nНаприклад: дитина - діти, країна - країни.\n'
              'Якщо іменник закінчується на ж, ш, ч, щ, то до нього додається суфікс -ів- перед закінченням -и.\n'
              'Наприклад: пісня - пісні, книжка - книжки.\n'
              'Якщо іменник закінчується на к, г, х, то до нього додається суфікс -ів- перед закінченням -и.\n'
              'Наприклад: пташка - пташки, доріжка - доріжки.\n'
              'Якщо іменник закінчується на ий, ой, єй, то до нього додається суфікс -їв- перед закінченням -и.\n'                    
              'Наприклад: хлопець - хлопці, горох - горохи.\n'
              'Іменники, які закінчуються на -нь, утворюють форму множини з суфіксом -н- перед закінченням -и.\n'
              'Наприклад: пань - пані, сонячний - сонячні.'))


class Astronomy:

    def __init__(self):
        print(logger(Fore.MAGENTA + 'Доступні теми:'
              '\n1. Які планети Сонячної системи є газовими гігантами?\n'
              '2. Що таке космічне випромінювання\n3. Яка відстань між Землею та Сонцем?\n'
              '4. Як впливає зоряне світло на здоров\'я людини?\n5. Які планети Сонячної системи мають найбільші та '
              'найменші орбіти?\nВведіть "Назад" для повернення до вибору предмета'))
        theme = logger(input(logger(Fore.GREEN + 'Виберіть тему: \n')))
        if theme == '1':
            self.gas_giants()
        elif theme == '2':
            self.cosmic_radiation()
        elif theme == '3':
            self.earth_to_sun_distance()
        elif theme == '4':
            self.starlight()
        elif theme == '5':
            self.largest_and_smallest_orbits()
        elif theme == 'Назад':
            Bot()
        else:
            print(logger(Fore.MAGENTA + 'Тема вибрана не правильно'))
        Astronomy()

    def gas_giants(self):
        print(logger(Fore.MAGENTA + "Газовими гігантами нашої Сонячної системи є Юпітер, Сатурн,"
              " Уран та Нептун, однак останні дві планети "
              "іноді називають крижаними гігантами"))

    def cosmic_radiation(self):
        print(logger(Fore.MAGENTA + "Космічне випромінювання - це потік енергетичних частинок, які походять з"
              " космічного простору, таких як сонячний вітер,\nгалактичні "
              "космічні промені та інші джерела. Це випромінювання "
              "може бути шкідливим для живих організмів, тому космонавти та космічні апарати зазвичай\nзабезпечуються"
              " захисними системами для зменшення впливу випромінювання. На Землі такі системи не потрібні, через"
              " сильне магнітне поле."))

    def earth_to_sun_distance(self):
        print(logger(Fore.MAGENTA + "Відстань між Землею та Сонцем становить приблизно 149,6 мільйонів кілометрів"
              " або 93 мільйони миль.\nЦя відстань в астрономії є стандартом, який називають астрономічною одиницею"))

    def largest_and_smallest_orbits(self):
        print(logger(Fore.MAGENTA + "Найбільша орбіта в Сонячній системі належить Нептуну,а найменша орбіта в Сонячній "
              "системі - Меркурію."))

    def starlight(self):
        print(logger(Fore.MAGENTA + "Зоряне світло впливає на ритми сну та на роботу гормонів у людини, особливо на"
              "мелатонін.\nНадмірне вплив зоряного світла може призвести до порушень сну, а також "
              "збільшити ризик розвитку, пов'язаних зі сном, наприклад, депресії та тривожності."))


class Bot:
    def __init__(self):
        self.topic = None
        self.topic_selection()

    def topic_selection(self):
        print(logger(Fore.MAGENTA + "Ви можете задати мені питання з наступних тем:"))
        print(logger("1. Фізика\n2. Математика\n3. Географія\n4. Астрономія\n5. Філологія\n6. Загальне\n"
                     "Введіть Вихід, щоб закінчити сесію."))
        user_response = logger(input(logger(Fore.GREEN + "Введіть номер або назву теми: \n" + Fore.MAGENTA)))

        if user_response == "1" or user_response.lower() == "фізика":
            self.topic = "фізика"
            print(logger("Обрана тема -" + self.topic))
            Physics()
            print(logger(random.choice(reactions)))
        elif user_response == "2" or user_response.lower() == "математика":
            self.topic = "математика"
            print(logger("Обрана тема -" + self.topic))
            Math()
            print(logger(random.choice(reactions)))
        elif user_response == '3' or user_response.lower() == 'географія':
            self.topic = 'географія'
            print(logger('Обрана тема -' + self.topic))
            Geography()
            print(logger(random.choice(reactions)))
        elif user_response == "4" or user_response.lower() == "астрономія":
            self.topic = "астрономія"
            print(logger("Обрана тема -" + self.topic))
            Astronomy()
            print(logger(random.choice(reactions)))
        elif user_response == '5' or user_response.lower() == 'філологія':
            self.topic = 'філологія'
            print(logger('Обрана тема -' + self.topic))
            Philology()
            print(logger(random.choice(reactions)))
        elif user_response == '6' or user_response.lower() == 'загальне':
            self.topic = 'загальне'
            print(logger(random.choice(reactions)))
            print('Ви обрали тему ' + self.topic)
            self.misc()
        elif user_response == 'Вихід':
            print(logger('Приємно було потеревенити! Бувай!.'))
            sys.exit()
        else:
            print(logger("Неправильне введення"))
            Bot()

    def misc(self):
        print(logger(Fore.MAGENTA + 'Ви можете запитати у мене наступне:'
              '\n1. Як тебе звати?\n2. Заспівай улюблену пісню.\n3. Розкажи анекдот'
              '\n4. Скільки днів у році:\n5. Який зараз рік?\n6. Гра "Вгадай число між 1 та 10".\n7. Котра година?.'
              '\n8. Сказати надихаючу цитату.\nВведіть "Назад" для повернення до вибору теми.\n'))
        i = logger(input(logger(Fore.GREEN + 'Виберіть запитання: \n')))
        if i == '1':
            print(logger(Fore.MAGENTA + 'Мене звати Eve!'))
        elif i == '2':
            n = random.randint(1, 5)
            if n == 1:
                print(logger(Fore.MAGENTA + 'Цей сон! Цей сон\nМені щоночі сниться!\nКрізь сон, крізь сон\n'
                      'Моє лице сміється!\nЦей сон! Цей сон\nМене не покидає!\nЯка краса,\nКоли там підгорає!'))
            elif n == 2:
                print(logger(Fore.MAGENTA + '«Обіцяли роялті від продажі альбому\nА по тєліку вони в брулях лімузинах\n'
                            'Я чекав, минуло більш ніж п\'ять років по тому\n'
                            'Впізнає мене в крамниці тепер тьотя Зіна.\nЯкби мені тоді дали один тільки натяк\n'
                            'Я б не знаю ким би став, куди б, де забіг би\n'
                            'Годі наді мною дослідів, ой, нєнада\nЗупиніть на світлофорі планету - я вийду...'))
            elif n == 3:
                print(logger(Fore.MAGENTA + '«Стоїть на вузліссі фіґурка маленька\nфіґурка маленька,'
                      ' то всьо наробила война\nА Місько наш був комсомолец,\nвін персим сі кинув на цьонк\n'
                      'а цьонк той сі трафив джилізний\nвін наніц нам Міська затовк...'))
            elif n == 4:
                print(logger(Fore.MAGENTA + 'Добре жити у Мадриді,\nЩонеділі на кориді,\nІ в Венеції я б жила,\n'
                      'Щодня на гондолі плила...\nМатадори, гондольєри -\nВсе змішалось до холєри!\n'
                      'Я на мить прикрию очі -\nІ назад до дому хочу!'))
            if n == 5:
                print(logger(Fore.MAGENTA + 'Так!\nЯ полюбляю жарти за столом,\nТак!\nЯ поважаю сало й самогон!\nТак!\n'
                      'Ти знаєш, зять, як поталанило\nТобі з найкращою тещею,\nТещею-мамою на землі!'))
        elif i == '3':
            n = random.randint(1, 5)
            if n == 1:
                print(logger(Fore.MAGENTA + 'Помітила, що з кожним роком я стаю все сильнішою: сумку з продуктами '
                      'на 500 грн стає носити все легше і легше…'))
            elif n == 2:
                print(logger(Fore.MAGENTA + 'Почувши мої бажання, Золота рибка зробила вигляд, що здохла.'))
            elif n == 3:
                print(logger(Fore.MAGENTA + 'Учора вперше ходив на полювання. Після 12-го чи 13-го пострілу качка '
                      'померла від сміху.'))
            elif n == 4:
                print(logger(Fore.MAGENTA + 'У цей непростий для всього світу час, коли руйнується уклад,'
                      ' закриваються кордони, зупиняється транспорт і т.д. Скажіть мені чесно і без паніки:'
                      ' Ви вікна, перед Великоднем мити будете?'))
            if n == 5:
                print(logger(Fore.MAGENTA + 'Коли дитячі психологи були не потрібні…'
                            ' Мама одним пучком кропиви, дієво очищувала карму, відновлювала ауру і знімала негатив.'))
        elif i == '4':
            year = logger(input(logger(Fore.GREEN + 'Введіть бажаний рік:' + Fore.MAGENTA)))
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                days_in_year = 366
            else:
                days_in_year = 365
            print(logger(Fore.MAGENTA + "У році" + year + "є" + str(days_in_year) + "днів."))
        elif i == '5':
            print(logger(Fore.MAGENTA + "Зараз" + str(datetime.datetime.now().year) + "рік."))
        elif i == '6':
            secret_number = random.randint(1, 10)
            print(logger(Fore.MAGENTA + "Привіт! Я загадала число від 1 до 10. Спробуй вгадати!"))

            while True:
                guess = int(logger((input(logger(Fore.GREEN + "Введи свою догадку: ")))))

                if guess == secret_number:
                    print(logger(Fore.MAGENTA + "Вітаю! Ти вгадав число!"))
                    break
                else:
                    print(logger(Fore.MAGENTA + "Невірно! Спробуй ще раз."))
        elif i == '7':
            current_time = datetime.datetime.now()
            hour = current_time.hour
            minute = current_time.minute

            print(logger(Fore.MAGENTA + f"Зараз {hour}:{minute}"))
        elif i == '8':
            n = random.randint(1, 5)
            if n == 1:
                print(logger(Fore.MAGENTA + 'Поки ти тримаєшся за свою «стабільність», хтось поруч втілює в життя твої'
                      ' мрії. Роберт Орбен'))
            elif n == 2:
                print(logger(Fore.MAGENTA + 'Ти повинен займатися тим, що робить тебе щасливим. Забудь про гроші або'
                            ' інші пастки, які заведено вважати успіхом. У тебе всього одне життя. Карл Лагерфельд'))
            elif n == 3:
                print(logger(Fore.MAGENTA + 'Не варто хвилюватися. У світі немає нічого страшнішого за нас самих.'
                      ' Туве Янссон'))
            elif n == 4:
                print(logger(Fore.MAGENTA + 'Існує два способи стати щасливим: поліпшити реальність чи знизити'
                     ' очікування. Джоді Піколт'))
            if n == 5:
                print(logger(Fore.MAGENTA + 'Труднощі не в тому, щоб знайти нові ідеї, а в тому, щоб звільнитися від'
                      ' старих. Джон Мейнард Кейнс'))
        elif i == 'Назад':
            Bot()
        else:
            print(logger('Неправильне введення.'))
        self.misc()


Bot()
