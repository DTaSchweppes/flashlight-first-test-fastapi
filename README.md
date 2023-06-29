# flashlight-first-test-fastapi
Completing a test assignment for an interview

Запуск из:

[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=python+main.py)](https://git.io/typing-svg)

там и установка зависимостей и запуск сервера:

![image](https://github.com/DTaSchweppes/flashlight-first-test-fastapi/assets/45369246/a49b823b-cb94-456e-b3b2-5ba37db42753)

**По первой задаче был вопрос**

![image](https://github.com/DTaSchweppes/flashlight-first-test-fastapi/assets/45369246/61d7812a-8ec4-4184-a970-ee171b591f54)

отсюда не ясно. Мы пишим колиент фонаря (а "сервер" представляем, что он есть и передает JSON) или что-то иначе.
>Задал вопрос через рекрутера получил ответ:

![image](https://github.com/DTaSchweppes/flashlight-first-test-fastapi/assets/45369246/39693eb8-03d1-4f36-9d5c-32a6103c9c43)

но в самом ТЗ:

![image](https://github.com/DTaSchweppes/flashlight-first-test-fastapi/assets/45369246/b3c3b0b0-5f14-4aea-ac70-8c52209c655b)


[Вариант который я сделал как понял по ответу от рекрутера (Серверную часть) [FastApi] [Asyncio]](https://github.com/DTaSchweppes/flashlight-first-test-fastapi/blob/master/app/flashlight_two.py)

[Вариант реализации по пунктам из ТЗ, но при этом на FastApi подключение поверх подключения и т.д.](https://github.com/DTaSchweppes/flashlight-first-test-fastapi/blob/master/app/flashlight_first.py)
>Так как нет сервера фонаря чтобы протестировать и подключиться по IP из ТЗ, тестов нет


**Работа приложения (1 вариант):**

Отправляется команда, обрабатывается и приходит ответ

![image](https://github.com/DTaSchweppes/flashlight-first-test-fastapi/assets/45369246/a2e09d99-4e39-48ec-b7ce-64ab3adf1d4c)

ответ в JSON:

![image](https://github.com/DTaSchweppes/flashlight-first-test-fastapi/assets/45369246/4d3d71ad-343d-4624-b5c4-01f92cd951be)

Есть проверка не был ли включен фонарь ранее:

![image](https://github.com/DTaSchweppes/flashlight-first-test-fastapi/assets/45369246/5ad66298-d949-444b-bba3-83606400644c)


По замене цвета так же:

![image](https://github.com/DTaSchweppes/flashlight-first-test-fastapi/assets/45369246/f3a8dbdb-645c-4abe-9b45-3861be45915e)
