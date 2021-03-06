import telebot
import random
from datetime import datetime

bot = telebot.TeleBot('*****************************')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
                     'Привет, жабка, как дела жабка? Чтобы получить комплимент от Максика введи "Получить комплимент"')

@bot.message_handler(content_types=['text'])
def calculate_something(message):
    print(f"Time: {datetime.fromtimestamp(message.date)}")
    print(f"Message from {str(message.chat.first_name)} {str(message.chat.last_name)}")
    print(f"Text: {str(message.text)}")
    if message.text.find('Получить комплимент') != -1:
        arr = ['Ты всегда знаешь, как меня удивить.', 'Глядя на тебя, понимаешь, что спорт — это сила',
               'Потрясающая фигура! Тебя легко принять за фитнес-тренера или спортсменку',
               'Прости, засмотрелся на тебя и потерял мысль. Ты не могла бы повторить все еще раз?',
               'Если быть красивой считается преступлением, то тебя объявят виновной.',
               'Я вижу столько тепла в твоих глазах.', 'Не переставай улыбаться, твоя улыбка обворожительна!',
               'Мне нравится твой стиль.', 'Это платье идеально сидит на тебе. Я ему даже завидую.',
               'Ты очень вкусно пахнешь.', 'Твой смех очаровывает!', 'Я очень сильно ценю тебя.',
               'Ты прекрасный слушатель.', 'С тобой гораздо интереснее общаться, чем с моими сверстниками!',
               'Ты очень добра к людям вокруг тебя.', 'У тебя всегда самые лучшие идеи.',
               'Ты очень талантливая и креативная девушка', 'Твой голос очень мелодичный и волнующий.',
               'У тебя безукоризненные манеры.',
               'Ты отлично владеешь искусством оказываться в нужное время в нужном месте!',
               'Как тебе удается находить выход из безвыходных ситуаций?!', 'Я хотел бы встретить тебя еще в детстве.',
               'Ты заслуживаешь объятия прямо сейчас.', 'Ты являешься прекрасным примером для других.',
               'Ты всегда можешь подобрать правильные слова.', 'Мне очень нравятся твои причуды.',
               'Мне нравится гулять с тобой.', 'С тобой я могу говорить обо всем.',
               'С тобой мне всегда очень комфортно.', 'Я благодарен за то, что ты есть.',
               'Ты всегда знаешь, как меня удивить.', 'Даже когда ты рядом, мне кажется, что тебя не хватает.',
               'Ты понимаешь меня настолько хорошо, как будто читаешь мои мысли.',
               'Просто проводить время с умной, интеллигентной девушкой уже приносит незабываемые минуты радости.',
               'Ты классная собеседница. Когда общаюсь с тобой, даже не замечаю, как пролетает время.',
               'Ты невероятна, когда не боишься быть собой.', 'Твоя действия говорят больше, чем слова.',
               'Меня поражает твоя открытость и искренность.', 'Я полностью обезоружен твоим остроумием.',
               'У меня мурашки от тебя.', 'Ты как магнит притягиваешь к себе.',
               'С тобой очень легко и приятно говорить, ты умеешь располагать к себе парней.',
               'Вот смотрю на тебя и понимаю, что в человеке может быть прекрасна душа, тело и мысли.',
               'Ты вдохновила меня на …', 'Это так мило с твоей стороны.',
               'Ты исполняешь эту песню в разы лучше этого исполнителя!', 'Рядом с тобой я могу быть самим собой.',
               'Ты важна для меня',
               'Ты даришь мне вдохновение в жизни, которое ранее меня не посещало. Классно, что я встретил тебя, очаровательная муза!',
               'Благодаря тебе я поверил в то, что действительно бывают родственные души.',
               'Мне очень важно выслушать твое мнение', 'Обожаю твои милые странности', 'Ты потрясающий друг!',
               'Ты – уникальная! В тебя нельзя не влюбиться.', 'Ты – мой антидепрессант!',
               'Всякий раз, когда мне грустно, мысль о тебе сразу поднимает настроение.', 'Доверяю твоей интуиции.',
               'Ты понимаешь меня лучше всех на свете.',
               'Ты даешь мне уверенность в себе и всегда меня поддерживаешь. Ты моя надежда и любовь.',
               'Часто выступаешь публично? У тебя отлично получается!',
               'У тебя огромный творческий потенциал! Ты можешь сотворить шедевр в каждой сфере жизни!',
               'Ты удивительная девушка, которая может служить примером для всех остальных.',
               'Это потрясающе, что ты всегда стремишься к саморазвитию.',
               'Твой творческий потенциал кажется безграничным.', 'Ты на самом деле знаешь кто ты и чего хочешь.',
               'Ты знаешь себе цену.', 'Ты признаешь свои ошибки и пытаешься их исправить.',
               'Ты всегда изучаешь новые вещи и пытаешься развиваться — это потрясающе.',
               'Я не сумел бы завершить это дело без твоей помощи.',
               'Много читаешь? Порекомендуешь что-нибудь? Мне почему-то кажется, что ты сразу же угадаешь книгу, которая мне понравится.',
               'Ты очень хорошо готовишь.', 'Если бы я сейчас поехал в путешествие, то взял бы с собой только тебя.']
        rand = random.choice(arr)
        bot.send_message(message.from_user.id, rand)
        print(f"Response: {str(rand)}")

bot.polling()
