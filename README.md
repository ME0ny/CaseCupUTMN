# CaseCupUTMN
Utair case
Команда Meony

Программа принимает на вход один тикет и выдает оценку менеджеру за один диалог

check/main.py/main - эта функция считает конечные баллы

## Участники
* **Артем Ипатов**
* **Павел Крючков**
* **Дарья Соколова**
* **Данил Изотов**
* **Павел Кучин**


https://www.figma.com/proto/1pJZxaUm0Kx2BvH1g24W6D/Utair?node-id=47%3A2&scaling=min-zoom ссылка на протоип сайта

Проект оценки работы техподдержки для компании Utair реализован на языке Python на веб-фреймворке Django

### На данном этапе программа способна проанализировать 1 тикет техподдержки

Главная страница сайта выводит анализ диалога.
### Принцип работы программы:
views.py вызывает функцию main из файла main.py

    main.py считает баллы по формуле
        (балл за орфографию + балл за уместность ответа) * вес за эмоционально окрашенную лексику * 5(для стандартизации данных)
    
    кроме этого отдельно выводится балл за совпадение тем вопроса и ответа
    Программа получает тикет в формате .txt, после чего с помощью txt2dict.py преобразует его в словарь, убирает лишние символы (нормализует) и после этого преобразует его в Python строку, после этого dict2dialog разбивает строку на два словаря: 
    
    сообщения клиента и сообщения оператора.
    
    Максимальная оценка диалога составляет 5 баллов, минимальная - 1.
    
    Важность параметров оценена субъективно.  
    
    Максимальный показатель параметра "орфография" составляет 0.2, а показателя "уместность ответа" - 0.8. В итоге идеальный ответ будет в сумме давать 1 по обоим параметрам.
    
    Первым делом программа анализирует сообщение оператора на орфографические ошибки с помощью spellcheck.py, где используется алгоритм Левенштейна.
    
    Каждая ошибка в сообщении влияет на балл орфографии и при этом исправляет их, для дальнейшего использования сообщения оператора в оценке уместности ответа.
    
    После этого spellcheck.py возвращает 4 значения.
    ```
    1. Исправленный текст
    2. Кол-во слов в сообщении
    3. Кол-во ошибок
    4. Все ошибочные слова( для вывода на странице анализа)
    ```
    
    Потом для подсчёта общего балла всего диалога находится средний балл между всеми парами сообщений (вопрос-ответ)
    Далее сообщение проверяется на наличие эмоционально окрашенных слов(в том числе нецензурных) с помощью словаря, включающим в себя 500 записей.
    
    При наличии "плохого слова" мы умножаем вес слова из словаря на общую оценку, а так же найденные слова заносятся в массив для последующего вывода.
    
    После этого считается уместность выражения с помощью нейронной сети, а именно предобученная модель для NLP "BERT".
    
    subjects.py использует "keras_bert" для определения уместности выражения. Эта модель уже обучения на большом количестве диалогов и понимает, соответствует ли по тематике два слова или два предложения. В эту нейросеть мы передаем первый вопрос и первый ответ, и проверяем, насколько они соответствуют. 
    
    Таким образом мы понимаем, понял ли менеджер ответ.
    
    Следующий параметр это совпадение тематики со скриптом менеджера.
    
    На этом этапе была воспроизведена попытка обучить нейронную сеть на предоставленных данных. Мы использовали так же "BERT", предоставленные данные мы разбили на классы, но информации оказалось недостаточно, поэтому на данный момент этот элемент еще требует доработки.
    
    Эту сеть мы попробовали обучить на других данных, и она показала pipeline с показателем 0.98, что является очень хорошим результатом.
    
    После этого мы эскпортируем данные с нашей сети, где уже проверяем сходство тематик между собой. С помощью этих данных мы высчитываем балл уместности ответов.
    
    На последнем этапе мы все подготовленные данные отправляем на саму страницу сайта для дальнейшего отображения.
