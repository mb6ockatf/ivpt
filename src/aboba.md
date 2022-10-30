# Интерактивная периодическая таблица химических элементов
## План
### База данных
Необходимо сделать несколько классов, которые будут обеспечивать работу с базой данных.  Весь
код, связаный с СУБД, будет лежать в каталоге src/database Будет использоваться sqlite3.  Модуль 
для работы с ней включён в стандартную библиотеку python с версии 2.5, поэтому она не потянет  
за собой лишние зависимости

Таблицы:
```SQL
CREATE TABLE IF NOT EXISTS basic_info (
	number          INTEGER UNSIGNED    NOT NULL,
	abbreviation    TEXT    UNIQUE      NOT NULL,
	CONSTRAINT number_pk PRIMARY KEY (number));
```
```SQL
CREATE TABLE IF NOT EXISTS basic_params (
	number  INTEGER UNSIGNED UNIQUE NOT NULL,
	name    TEXT             UNIQUE NOT NULL,
	weight  REAL             UNIQUE NOT NULL
	group   TEXT CHECK group IN ('alkal-metal', 'alkaline-earth-metal', 'metalloid', 
		'reactive-nonmetal', 'transitiom-metals', 'noble-gas', post-transition-metal', 'actinoid',
		'lanthanoid', NULL),
	period  INTEGER UNSIGNED,
	CONSTRAINT fk_element_number
		FOREIGN KEY (number)
		REFERENCES basic_info(number));
```
```SQL
CREATE TABLE IF NOT EXISTS congregation (
	number        INTEGER UNSIGNED UNIQUE NOT NULL,
	metal         INTEGER UNSIGNED DEFAULT 0,
	amphoteric    INTEGER UNSIGNED DEFAULT 0,
	energy_levels INTEGER UNSIGNED,
	period        INTEGER UNSIGNED,
	gas           INTEGER UNSIGNED DEFAULT 0,
	semiconductor INTEGER UNSIGNED DEFAULT 0,
	CONSTRAINT fk_element_number
		FOREIGN KEY (number)
		REFERENCES basic_info(number));
```
```SQL
CREATE TABLE IF NOT EXISTS links (
	number    INTEGER,
	wiki_link TEXT
	CONSTRAINT fk_element_number
		FOREIGN KEY (number)
		REFERENCES basic_info(number));
```
И ещё две таблицы с переводами
(одна - для перевода названий елементов, другая - для всего остального)
### Интерфейс
Будет одно основное окно (т.е. сама таблица).
При выборе элемента будет открываться окно поменьше с информацией по этому конкретному элементу.
### Структура
1. БД
   1. Класс, который будет обслуживать подключение к БД и работе с ней.
   2. Тесты для БД. Будет использоваться фреймворк unittest, встроенный в Python с версии 2.1
   3. Парсер для получения информации о хим. элементах из интернета.
Будет использована библиотека Beautiful Soup со встроенным в python парсером html-документов.
Также, модуль requests для получения страницы
2. Интерфейс
   1. Класс окна основного окна `MainWindow`
      - При инициализации в нём будет отрисовываться таблица с элементами.
Будут видны только номер элемента и его обозначение
      - Нажатие на элемент будет создавать окно `ElementWindow`
      - ~~Внизу окна будет кнопка для добавления нового элемента.
Нажатие на неё будет создавать окно `NewElementWindow`~~ *не будет реализовано*
      - Элемент интерфейса для смены языка _(второстепенная задача)_
      - ~~Кнопка сброса базы данных (и закрытия программы)~~ _(не будет реализовано)_
      - Возможно, будет реализован функционал для проведения стехиометрических расчётов
      - Информация о языке будет храниться в файле `~/IVPT/lang.toml`
   2. Класс окна элемента `ElementWindow`
В нём будет отображена подробная информация об элементе (полное название, группа, период, атомная 
масса, принадлежность к металлам / неметаллам, группа элемента по ~~электронным~~ энергетическим 
уровням и т.д.), ссылка на статью в интернете.
~~Так же, здесь можно будет удалть элемент~~ _(не будет реализовано)_
   3. Окно, обрабатывающее исключения _(второстепенная задача)_
   ~~4. Окно добавления нового элемента `NewElementWindow`.
Можно будет указать подробные параметры (см. пункт про `ElementWindow`).
Они будут разделены по группам чтобы избежать лишних запросов к БД (например, если не было указано 
ни одного параметра для таблицы `congregation`)~~ _не будет реализовано_
3. Получение данных.
Для получения пути к базе данных и сопутствующей информации  будет использоваться файл 
`~/IVPT/config.toml`. 
В программе будет жёстко определён путь к `config.toml`, а всё остальное можно будет настроить в 
самом файле  
```ascii
IVPT
│   README.md
│
└───src
    │   main.py
    │   test.py
    │
    ├───database
    └───interface
```
IVPT = interactive visual periodic table, название проекта

------

Thu 27 Oct 2022 05:22:54 PM MSK
