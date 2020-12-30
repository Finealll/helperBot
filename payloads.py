#payloads для всего
payloads = {
    #open keyboards
    "get_main_keyboard": {     # Открытие главной клавы
        "type": "open_keyboard",
        "name": "get_main_keyboard"
    },
    "get_tasks_list": {     #Открытие списка предметов по скилам
        "type": "open_keyboard",
        "name": "get_tasks_list"
    },
    "get_roles_list": {     # Открытие ролей
        "type": "open_keyboard",
        "name": "get_roles_list"
    },
    #программирование
    "get_progers_types": {  #Открытие типов задач программирования
        "type": "open_keyboard",
        "name": "get_progers_types",
        "subtype_1": "get_progers_type1",
        "subtype_2": "get_progers_type2",
        "subtype_3": "get_progers_type3",
    },
    "get_progers_type1": {  #Открытие проверки знаний
        "type": "open_keyboard",
        "name": "get_progers_type1"
    },
    "get_progers_type2": {  #Открытие проверки умений
        "type": "open_keyboard",
        "name": "get_progers_type2"
    },
    "get_progers_type3": {  #Открытие задач
        "type": "open_keyboard",
        "name": "get_progers_type3"
    },
    #Элтех
    "get_eltech_types": {  #Открытие типов задач программирования
        "type": "open_keyboard",
        "name": "get_eltech_types",
        "subtype_1": "get_eltech_type1",
        "subtype_2": "get_eltech_type2",
        "subtype_3": "get_eltech_type3",
    },
    "get_eltech_type1": {  #Открытие проверки знаний
        "type": "open_keyboard",
        "name": "get_eltech_type1"
    },
    "get_eltech_type2": {  #Открытие проверки умений
        "type": "open_keyboard",
        "name": "get_eltech_type2"
    },
    "get_eltech_type3": {  #Открытие задач
        "type": "open_keyboard",
        "name": "get_eltech_type3"
    },
    #Физика
    "get_physics_types": {  #Открытие типов задач программирования
        "type": "open_keyboard",
        "name": "get_physics_types",
        "subtype_1": "get_physics_type1",
        "subtype_2": "get_physics_type2",
        "subtype_3": "get_physics_type3",
    },
    "get_physics_type1": {  #Открытие проверки знаний
        "type": "open_keyboard",
        "name": "get_physics_type1"
    },
    "get_physics_type2": {  #Открытие проверки умений
        "type": "open_keyboard",
        "name": "get_physics_type2"
    },
    "get_physics_type3": {  #Открытие задач
        "type": "open_keyboard",
        "name": "get_physics_type3"
    },
    #Дискретка
    "get_math_types": {  #Открытие типов задач программирования
        "type": "open_keyboard",
        "name": "get_math_types",
        "subtype_1": "get_math_type1",
        "subtype_2": "get_math_type2",
        "subtype_3": "get_math_type3",
    },
    "get_math_type1": {  #Открытие проверки знаний
        "type": "open_keyboard",
        "name": "get_math_type1"
    },
    "get_math_type2": {  #Открытие проверки умений
        "type": "open_keyboard",
        "name": "get_math_type2"
    },
    "get_math_type3": {  #Открытие задач
        "type": "open_keyboard",
        "name": "get_math_type3"
    },
    #Нажатие на кнопку с номером, чтобы взять
    "add_task": {
        "type": "add_task",
        "subject": "",
        "number": "",
        "type_task": 0,
    },
    #Удаление задания
    "delete_task": {
        "type": "delete_task",
        "subject": "",
        "number": "",
    },
    #Отправка задания
    "push_task": {
        "type": "push_task",
        "subject": "",
        "number": "",
    },
    #Обновление задания
    "update_task": {
        "type": "update_task",
        "subject": "",
        "number": "",
    },
    #Отправка сообщений с данными
    "get_now_tasks_list": {  # Открытие своих задач
        "type": "send_info_message",
        "name": "get_now_tasks_list"
    },
    #Роль
    "change_role": {
        "type": "change_info",
        "name": "change_role",
        "role": "",
        "do": ""
    },
    # Отправка документа с заданием
    "get_tasks": {
        "type": "get_doc",
        "name": "get_tasks",
        "subject": "",
    }
}