@авторизация @авторизация.feature
Функция: Авторизация в приложении

@critical @positive
Сценарий: Я авторизуюсь с существующим логином и паролем
Пусть я открываю сайт "qa-testing.ru"
И заполняю форму логина валидными данными:
| элемент      | значение               |
| логин Email  | test1user@testmail.com |
| логин Пароль | "BAw23f5m"             |
И нажимаю "кнопку Войти"
Тогда я понимаю, что авторизован, так как вижу "профиль Пользователя"

@critical @negative
Сценарий: Я не зарегистрирован, авторизуюсь с несуществующими логином и паролем
Пусть я открываю сайт "qa-testing.ru"
И заполняю форму логина невалидными данными:
| элемент      | значение               |
| логин Email  | cat1user@testmail.com  |
| логин Пароль | "12bN2398"             |
И нажимаю "кнопку Войти"
Тогда я понимаю, что не авторизован, так как вижу сообщение "Такой пользователь не найден"

@critical @negative
Сценарий: Я авторизуюсь с существующим логином и паролем поменяв их местами
Пусть я открываю сайт "qa-testing.ru"
И в поле "Email" ввожу "логин Пароль", а в поле "Пароль" ввожу "логин Email":
| элемент      | значение               |
| логин Email  | "BAw23f5m"             |
| логин Пароль | test1user@testmail.com |
И нажимаю "кнопку Войти"
Тогда я понимаю, что не авторизован, так как вижу сообщение "Введите корректные Email и Пароль"

@critical @negative
Сценарий: Я авторизуюсь с незаполненными логином и паролем
Пусть я открываю сайт "qa-testing.ru"
И не заполняю форму логина:
| элемент      | значение               |
| логин Email  |                        |
| логин Пароль |                        |
И нажимаю "кнопку Войти"
Тогда я понимаю, что не авторизован, так как вижу сообщение "Введите корректные Email и Пароль"

@critical @negative
Сценарий: Я авторизуюсь с пробелами вместо логина и пароля
Пусть я открываю сайт "qa-testing.ru"
И в поля "Email" и "Пароль" ввожу пробелы:
| элемент      | значение               |
| логин Email  | " "                    |
| логин Пароль | " "                    |
И нажимаю "кнопку Войти"
Тогда я понимаю, что не авторизован, так как вижу сообщение "Введите корректные Email и Пароль"

@critical @negative
Сценарий: Я авторизуюсь только с существующим логином
Пусть я открываю сайт "qa-testing.ru"
И в поле "Email" ввожу "логин Email", а поле "Пароль" оставляю пустым:
| элемент      | значение               |
| логин Email  | test1user@testmail.com |
| логин Пароль | "BAw23f5m"             |
И нажимаю "кнопку Войти"
Тогда я понимаю, что не авторизован, так как вижу сообщение "Введите корректные Email и Пароль"

@critical @negative
Сценарий: Я авторизуюсь только с существующим паролем
Пусть я открываю сайт "qa-testing.ru"
И поле "Email" оставляю пустым, а в поле "Пароль" ввожу "логин Пароль":
| элемент      | значение               |
| логин Email  | test1user@testmail.com |
| логин Пароль | "BAw23f5m"             |
И нажимаю "кнопку Войти"
Тогда я понимаю, что не авторизован, так как вижу сообщение "Введите корректные Email и Пароль"






