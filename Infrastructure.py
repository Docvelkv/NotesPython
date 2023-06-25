import Note
import json
import os


filePath = "D:/Medium/NotesPython/notes.json"


def getAllNotes():
    if os.stat(filePath).st_size != 0:
        with open(filePath, 'r+', encoding="utf-8") as file:
            data = json.load(file)
            return data
    else:
        return None


def numOfNotes():
    if getAllNotes is not None:
        with open(filePath, 'r+', encoding="utf-8") as file:
            data = json.load(file)
            num = len(data)
    else:
        num = 0
    return num


def checkingExistenceOfKey(key):
    notes = getAllNotes()
    listKeys = list(notes.keys())
    for i in listKeys:
        if int(i) == key:
            key = key + 1
    return key


def createNewNote():
    key = checkingExistenceOfKey(numOfNotes() + 1)
    title = input("Введите заголовок: ")
    content = input("Введите текст: ")
    note = Note.Note(title, content)
    if os.stat(filePath).st_size != 0:
        with open(filePath, 'r+', encoding="utf-8") as file:
            data = json.load(file)
            file.seek(0)
            data.update({key: note.__dict__})
        with open(filePath, "w", encoding="utf-8", ) as file:
            json.dump(data, file, indent=0, ensure_ascii=False)
    else:
        data = {key: note.__dict__}
        with open(filePath, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=0, ensure_ascii=False)
    print(f"***\nДобавлена новая заметка с номером {key}\n***")


def showContent():
    if getAllNotes is not None:
        notes = getAllNotes()
        print("***")
        for x in notes:
            print(notes[x]['content'])
    print("***")


def showAll():
    if getAllNotes() is not None:
        notes = getAllNotes()
        print("***")
        for x in notes:
            print("№: ", x)
            for y in notes[x]:
                if y == 'title':
                    st = "Тэг: "
                if y == 'dateTime':
                    st = "Дата: "
                if y == 'content':
                    st = "Текст: "
                print(st, notes[x][y])
    print("***")


def updateNote():
    key = input("Введите номер заметки: ")
    title = input("Введите заголовок: ")
    content = input("Введите текст: ")
    note = Note.Note(title, content)
    if os.stat(filePath).st_size != 0:
        with open(filePath, 'r+', encoding="utf-8") as file:
            data = json.load(file)
            file.seek(0)
            data.update({key: note.__dict__})
        with open(filePath, "w", encoding="utf-8", ) as file:
            json.dump(data, file, indent=0, ensure_ascii=False)
        print(f"***\nЗаметка с номером {key} изменена\n***")
    else:
        print("***\nИзменять нечего, заметок нет\n***")
    showAll()


def delNote():
    nNote = numOfNotes()
    print(f"Всего заметок: {nNote}")
    key = input("Введите номер заметки: ")
    notes = getAllNotes()
    if key in notes:
        del notes[key]
        with open(filePath, "w", encoding="utf-8") as file:
            json.dump(notes, file, indent=0, ensure_ascii=False)
        print(f"***\nзаметка с номером {key} удалена\n***")
    else:
        print("***\nЗаметка не найдена\n***")
    showAll()
