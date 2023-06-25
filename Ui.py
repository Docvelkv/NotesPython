import Infrastructure as infr


def showWelcome():
    print("Это консольное приложение для создания заметок")


def showMenu():
    print("1\tСоздать заметку\n"
          "2\tПосмотреть всё\n"
          "3\tПосмотреть текст заметок\n"
          "4\tИзменить заметку\n"
          "5\tУдалить заметку\n"
          "6\tЗавершить работу\n")


def hiEnergy():
    print("Работа закончена.\nВсего наилучшего!")


def runOfNotes():
    showWelcome()
    runApp = True
    while (runApp):
        showMenu()
        task = input("Введите цифру для запуска задачи: ")
        if task == "1":
            infr.createNewNote()
        if task == "2":
            infr.showAll()
        if task == "3":
            infr.showContent()
        if task == "4":
            infr.updateNote()
        if task == "5":
            infr.delNote()
        if task == "6":
            hiEnergy()
            runApp = False
