from django.shortcuts import render
import copy

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'pancakes': {
        'Молоко, мл': 700,
        'Яйца куриные, шт': 3,
        'Масло растительное, ст. ложки': 3,
        'Мука, г': 300,
        'Сахар, ст. ложки': 2,
        'Соль, щепотки': 2,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def recipe(request):
    name = request.GET.get('name')
    servings = int(request.GET.get('servings', 1))
    context = {'recipe': copy.deepcopy(DATA.get(name)),
               }
    for key in context['recipe']:
        context['recipe'][key] = servings*context['recipe'][key]
    return render(request, 'calculator/index.html', context)
