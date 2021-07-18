# Генерация sql для учебной базы данных vk

### Схема базы данных должна быть именно такой, как в файле *_vk_db_creation.sql*

1. Подготовка:<br><br>

Необходимо установить библиотеку lorem-text для генерации случайных слов<br>
https://pypi.org/project/lorem-text/

> pip install lorem-text
<br>

2. Конфигурация:<br><br>

Можно изменить количество полей, меняя config
<br><br>

3. Запуск:<br>

> python main.py
<br>

4. Результат:<br>
   
После запуска в случае успех будет сгенерирован файл **data.sql**, который содержит sql для вставки данных в базу.
Пример полученного результата находится в файле **sample.data.sql**

Любые исправления, изменения, предолжения приветствуются!!!
