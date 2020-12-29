#payloads для всего
payloads = {
    #open keyboards
    "get_tasks_list": {     #Открытие списка предметов по скилам
        "type": "open_keyboard",
        "name": "get_tasks_list"
    },
    #программирование
    "get_progers_types": {  #Открытие типов задач программирования
        "type": "open_keyboard",
        "name": "get_progers_types"
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
        "name": "get_eltech_types"
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
        "name": "get_physics_types"
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
        "name": "get_math_types"
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
    "get_roles_list": {  # Открытие ролей
        "type": "send_info_message",
        "name": "get_roles_list"
    },
}