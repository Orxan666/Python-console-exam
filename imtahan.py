# Imtahan sistemi

questions = [
    {
        'question': 'Asagidakilardan hansi bitkiler alemine aiddir?',
        'options': ['Ordek', 'Gobelek', 'At', 'Sam agaci'],
        'answer': 3
    },
    {
        'question': 'Bunlardan hansi saitdir',
        'options': ['b', 'a', 'c', 'd'],
        'answer': 1
    },
    {
        'question': 'En boyuk materik hansidir',
        'options': ['Antarktika', 'Avstraliya', 'Avrasiya', 'Simali Amerika'],
        'answer': 2
    },
    {
        'question': 'Azerbaycan Respublikasi ne vaxt yaranib?',
        'options': ['1928', '1918', '1500', '1930'],
        'answer': 1
    },
    {
        'question': 'Quvvetin vahidi?',
        'options': ['Newton', 'Vold', 'Watt', 'Metr'],
        'answer': 0
    },
    {
        'question': 'Asagidakilardan hansi radioaktivdir?',
        'options': ['Plutonium', 'Cive', 'Lithium', 'Cupper'],
        'answer': 0
    },
    {
        'question': 'Bextiyar Vahabzedenin ilk seiri',
        'options': ['Leyli ve Mecnun', 'Latin dili', 'Ana ve Sekil', '20 yanvar'],
        'answer': 2
    },
    {
        'question': 'sin90 nece edir?',
        'options': ['1', '2', '3', '4'],
        'answer': 0
    },
]

# eq = {'a': 0, 'b': 1, 'c': 2, 'd': 3}
# qe = {eq[key]: key for key in eq}


# i = 0
# counter = 0
# for question in questions:
#     print(questions[i]['question'])
#     print("A)", questions[i]['options'][0],  "\nB)", questions[i]['options'][1], "\nC)", questions[i]['options'][2], "\nD)", questions[i]['options'][3])
#     cavab = input("\nCavabi girin: ")
#     if eq[cavab] != questions[i]['answer']:
#         print(">>>Cavab sehvdir", ' - ', qe[0])
#     else:
#         counter +=1
#     i+= 1

# print("Duzgun cavablarin sayi: ", counter)



result = {
    'correct_count': 0,
    'wrong_count': 0,
    'total_count': len(questions),
    'quiz_result': []
}
for i in range(len(questions)):
    question_info = questions[i]
    question, options, answer = question_info.values()
    print(str(i+1)+'.', question)
    print(*[chr(65+i) + ')' + options[i] for i in range(len(options))], sep='\n')
    user_answer = input('Sualin cavabini girin: ').lower()
    if ord(user_answer) - 97 == answer:
        print('Cavab duzdur!')
    else:
        print('Cavab', chr(answer+65), 'olmalidir!')
    result['quiz_result'].append(
        {'order': i+1, 'user_answer': user_answer.upper(), 'current_answer': chr(answer+65)}
    )

print()
print()
for qresult in result['quiz_result']:
    print(str(qresult['order'])+'.', end=' ')
    print(qresult['user_answer'], end='')
    print('+' if qresult['user_answer'] == qresult['current_answer'] else '-' + qresult['current_answer'])

