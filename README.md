# Методы и технологии программирования

## Лабораторная работа №1

### Инструкция:

1) Переходим в каталог 'LR 1':
```shell
cd 'LR 1'
```
2) Делаем скрипты `test1.py`, `test2.py` и `test3.py` исполняемыми:
```shell
chmod +x test1.py
```
```shell
chmod +x test2.py
```
```shell
chmod +x test3.py
```
3) Запускаем скрипты:
```shell
./test1.py | ./test2.py 2>> errors.txt | ./test3.py 2>> errors.txt
```

## Лабораторная работа №2

### Инструкция:

1) Переходим в каталог 'LR 2':
```shell
cd 'LR 2'
```
2) Делаем скрипт `test1.py` исполняемым:
```shell
chmod +x test1.py
```

### Примеры использования:

#### Пример 1:

Содержимое файла `names.txt`
```text
lena
Anya
sonya
vika
Maria
Anastasia
vera
lubov
Dim@
Oleg
```

Запускаем:
```shell
./test1.py < names.txt 2> error.txt
```

Результат в терминале:
```text
Nice to see you Anya!
Nice to see you Maria!
Nice to see you Anastasia!
Nice to see you Oleg!
```

Содержимое файла `error.txt`:
```text
Error: Name 'lena' needs to start in uppercase!
Error: Name 'sonya' needs to start in uppercase!
Error: Name 'vika' needs to start in uppercase!
Error: Name 'vera' needs to start in uppercase!
Error: Name 'lubov' needs to start in uppercase!
Error: Name 'Dim@' contains invalid characters!
```

#### Пример 2:

Запускаем:
```shell
./test1.py
```

Результат в терминале:
```text
Hey, what's your name?
Ivan
Nice to see you Ivan!
Hey, what's your name?
Nastya
Nice to see you Nastya!
Hey, what's your name?
Ler@
Error: Name 'Ler@' contains invalid characters!
Hey, what's your name?
artem
Error: Name 'artem' needs to start in uppercase!
Hey, what's your name?
^C
Goodbye!
```
