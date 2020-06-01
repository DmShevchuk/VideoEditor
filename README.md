# VideoEditor
Приложение для создания видео, редактирования изображений, написания музыки.

# Запуск приложения
В VideoEditor используются следующие библиотеки:
  - os
  - sys
  - sqlite3
  - opencv-python
  - moviepy
  - pygame
  - PyQt5
  - Pillow 
 
(все зависимости в requirements.txt)\
Их необходимо установить и запустить файл ***main.py***.

# Работа с приложением
 ### 1) При запуске выполнить вход или регистрацию
 ### 2) Изображения и музыка
 Можно добавлять уже сохранённые на компьютере изображения или создавать и редактировать свои в фоторедакторе,
 нажав на кнопку в главном окне **[Редактировать изображения]**.
 
 Можно добавлять сохранённую на компьютере музыку или создавать свою - **[Создать музыку]**. Перед созданием необходимо включить
 запись *REC*, а также выбрать английскую раскладку клавиатуры.
 
 Чтобы добавить сохранённую музыку или изображение, нажмите **[Добавить сохранённую музыку]** или **[Добавить сохранённые изображения]**
 соответственно.
 
 ### 3) Редактирование списка добавленной музыки или изображений
 Чтобы удалить элемент из списка, введите ***"-"*** в графе **Удалить**.
 
 Очищение списка сохранённых изображений и музыки происходит с помощью нажатия на кнопку **[с]**.
 
 ### 4) Сохранение видео
 Так как размер изображений может отличаться, выберите:
   - **[Увеличение изображений в соответсвие максимальными размерам]** и цвет заднего фона изображений;
   - **[Уменьшение изображений в соответсвие минимальным размерам]**.
  
 Теперь всё готово, нажмите **[Сохранить]** и наслаждайтесь видео!
