# testing_service
Микросервис по тестированию.

Демо: http://157.90.153.122:8000/

-Login: admin\
-Password: admin


### Возможности

  Функциональные части сервиса:
  
    * Регистрация пользователей
    * Авторизация пользователей
    * Зарегистрированные пользователи могут проходить любой из тестов
    * Одним запросом отправляются ответы на тест (нужно проверить, что на все вопросы дан ответ)
    * После завершения теста отдавать результат тестирования, количество правильных/неправильных ответов, процент правильных ответов
 
  Система управления. Стандартная админка Django. Разделы:
  
    * Стандартный раздел пользователей
    * Раздел с тестами
    * Возможность на странице набора тестов добавлять вопросы/ответы и отмечать правильный вариант вопроса
    * Результаты тестирования - отобразить, какой пользователь прошел тест, какой тест, какой результат тестирования    

 

### Установка
  1) Склонируйте репозиторий
  ```https://github.com/Stevinel/testing_service```
  2) Установите виртуалуное окружение и активируйте его
  3) Выполните миграции python manage.py migrate и установите зависимости pip install -r requirements.txt
  4) Создайте администратора 
     ```python manage.py createsuperuser```
  5) Запустите сервер 
     ```python manage.py runserver```
  6) Зайдите на страницу 
     ```http://127.0.0.1:8000/```


### Проект выполнен в качестве тестового задания.
  
