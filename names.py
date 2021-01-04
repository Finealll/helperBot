table_name = ["progers", "eltech", "maths", "physics"]
name_of_subject = ["Системка", "Электротехника", "Дискретная математика", "Физика"]
subject_to_table = {
    name_of_subject[0]: table_name[0],
    name_of_subject[1]: table_name[1],
    name_of_subject[2]: table_name[2],
    name_of_subject[3]: table_name[3],
}
table_to_subject = {
    table_name[0]: name_of_subject[0],
    table_name[1]: name_of_subject[1],
    table_name[2]: name_of_subject[2],
    table_name[3]: name_of_subject[3],
}
questions = [
    {'subject': name_of_subject[0], 'attachment': 'doc-201455689_580090252'},
    {'subject': name_of_subject[1], 'attachment': 'doc-201455689_580090282'},
    {'subject': name_of_subject[2], 'attachment': 'doc-201455689_580090267'},
]

id_community = 201455689

faq = "Привет!\nЭтот бот создан для оптимизации работы над приготовлением ответов к сессии.\nБери задания, делай качественно, отправляй и будет тебе счастье"