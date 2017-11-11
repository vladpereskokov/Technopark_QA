# Автоматизация функционального тестирования

Проект [***Одноклассники***](https://www.ok.ru)

## Содержание
  - [Команда](#team)
  - [Jira](#jira)
  - [Стек технологий](#tech-stack)
  - [Чек листы](#check-lists)
    * [Семенов Антон](#check-lists-sa)
    * [Семенова Екатерина](#check-lists-se)
    * [Перескоков Владислав](#check-lists-vp)
   

<a name="team"></a>
## Команда
  - [Семенов Антон](https://github.com/J0kerPanda)
  - [Семенова Екатерина](https://github.com/SemenovaEkaterina)
  - [Перескоков Владислав](https://github.com/vladpereskokov)
  
<a name="jira"></a>
## Jira
[Ссылка](http://st-jira.tech-mail.ru/browse/PARK-82) на [Jira](https://ru.atlassian.com/software/jira)

<a name="tech-stack"></a>
### Стек технологий

  - python 2.7
  — selenium
  - chrome / firefox

<a name="check-lists"></a>
## Чек листы

<a name="check-lists-sa"></a>
### Семенов Антон

|                                Тест                               | Статус |
|:-----------------------------------------------------------------:|:------:|
|       Класс ставится на фотографии на странице пользователя       |   Ok   |
|       Класс снимается с фотографий на странице пользователя       |   Ok   |
|               Класс ставится с фотографий в альбомах              |   Ok   |
|              Класс снимается с фотографий в альбомах              |   Ok   |
|  Класс ставится на удаленные фотографии (без обновления страницы) |   Ok   |
|  Класс снимается с удалённых фотографий (без обновления страницы) |   Ok   |
|         Быстрая простановка и снятие классов на фотографии        |   Ok   |
|      Классы на странице пользователя и в альбомах одинаковые      |   Ok   |
|         Класс ставится на подарки на странице пользователя        |   Ok   |
|        Класс снимается с подарков на странице пользователя        |   Ok   |
|           Класс ставится на подарки на странице подарков          |   Ok   |
|          Класс снимается с подарков на странице подарков          |   Ok   |
|         Быстрая простановка и снятие классов на фотографии        |   Ok   |
| Классы на странице пользователя и на странице подарков одинаковые |   Ok   |
|         Класс ставится на новости на странице пользователя        |   Ok   |
|        Класс снимается с новостей на странице пользователя        |   Ok   |

<a name="check-lists-se"></a>
### Семенова Екатерина

|                                Тест                                | Статус |
|:------------------------------------------------------------------:|:------:|
|           Ставится оценка любого типа на чужие фотографии          |   Ok   |
|                Не ставится неправильная оценка - не                |   Ok   |
|                Не ставятся оценки на свой фотографии               |   Ok   |
|     После выставления оценки есть возможность "Повысить на 5+"     |   Ok   |
|             Посмотреть оценки, проставленные фотографии            |   Ok   |
|               Удалить чужую оценку со свой фотографии              |   Ok   |
|                    Восстановить удаленную оценку                   |   Ok   |
| Поставить новую оценку фотографии, если пользователь удалил старую |   Ok   |
|    Появляется оповещение в событиях о новой проставленной оценке   |   Ok   |
|     Из вкладки события можно посмотреть счетчик текущих оценок     |   Ok   |

<a name="check-lists-vp"></a>
### Перескоков Владислав

|                                Тест                               | Статус |
|:-----------------------------------------------------------------:|:------:|
|                       Добавление комментария                      |   Ok   |
|                        Удаление комментария                       |   Ok   |
|                          Лайк комментария                         |   Ok   |
|                         Репост комментария                        |   Ok   |
|         Статус событий друга после добавления комментариев        |   Ok   |
|              Добавление и сразу удаление комментария              |   Ok   |
|                      Восстановить комментарий                     |   Ok   |
|                 Удалить и восстановить комментарий                |   Ok   |
|                   Оценить удаленный комментарий                   |   Ok   |
|                  Репостнуть удаленный комментарий                 |   Ok   |
|             Добавление комментария к удаленным записям            |   Ok   |
|            Удалить, добавить и восстановить комментарий           |   Ok   |
|                    xss уязвимость в комментарии                   |   Ok   |
