import Note
import json
import os


filePath = "D:/Medium/NotesPython/notes.json"


def showMenu():
    print("1\tСоздать заметку\n \
           2\tПосмотреть всё\n \
           3\tПосмотреть текст заметок\n \
           4\tИзменить заметку\n \
           5\tУдалить заметку\n \
           6\tЗавершить работу\n")


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


def createNewNote():
    key = numOfNotes() + 1
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
    print(f"Добавлена новая заметка с номером {key}")


def showContent():
    if getAllNotes is not None:
        notes = getAllNotes()
        for x in notes:
            print(notes[x]['content'])


def showAll():
    if getAllNotes is not None:
        notes = getAllNotes()
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
        print(f"Заметка с номером {key} изменена")
    else:
        print("Изменять нечего, заметок нет")
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
        print(f"заметка с номером {key} удалена")
    else:
        print("Заметка не найдена")
    showAll()


delNote()
