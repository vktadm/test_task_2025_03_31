# Тестовое задание - JWT авторизация

### Используемые технологии
- Flask, SQLAlchemy
- Docker
- Redis - хранение blacklist токенов
- SQLite - хранение данных пользователя `username, password, role: admin/user`
- bcrypt - шифрование/дешифрование паролей пользователя

### Структура проекта
```
teast_task.../
| - main.py - точка входа
| - app/
   | - __init__.py - инициализация приложения, подключение endpoints
   | - config.py - конфигурация приложения
   | - content.py - защищеные endpoints: "/admin" - только администраторы "/" - все пользователи
   | - models.py - модель "User" flask-sqlalchemy
   | - auth/
      | - auth.py - endpoints для реализации аутонтефикации/авторизации и регистрации
      | - db_helper.py - CRUD функции
      | - en_de_cryption.py - де/кодирование паролей пользователя
      | - utils_jwt.py - генерация и отзыв jwt токенов
```
### Скриншоты работы
- Попытка авторизоваться с некоректным логином  
![1](inc/1.png)
- Удачная авторизация  
![2](inc/3.png)
- Доступ к защищенному endpoint с **token из whitelist**  
![3](inc/2.png)
- Доступ к защищенному endpoint с **несуществующим token**  
![4](inc/4.png)
- Аннуляция token  
![5](inc/5.png)
- Попытка получить доступ к защищенному контенту с **token из blacklist**  
![6](inc/6.png)
- Регистрация пользователя со статусом - администратор
![7](inc/7.png)
- Авторизация администратора
![8](inc/8.png)
- Доступ **администратора** к защищенному endpoint **доступному для всех ролей**
![9](inc/9.png)
- Доступ **администратора** к защищенному endpoint **доступному только администраторы**
![10](inc/10.png)
- Авторизация обычного пользователя
![11](inc/11.png)
- Доступ **обычного пользователя** к защищенному endpoint **доступному только администраторы**
![12](inc/12.png)