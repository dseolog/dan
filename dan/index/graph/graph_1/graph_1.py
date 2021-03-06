import os
import matplotlib.pyplot as plt

def graph_1(SITE):
    '''
    x = [1, 2, 3, 4, 5, 6, 7]
    y_1 = [1, 3, 2, 7, 5, 6, 8]
    y_2 = [1, 2, 3, 5, 7, 13, 21]
    plt.plot(x, y_1, color='#ff0000', label='График 1')
    print(plt.plot(x, y_2, color='#00ffff', label='График 2'))
    plt.title('Результат 1', fontdict={'fontsize':20})
    plt.xlabel('Ось Х')
    plt.ylabel('Ось Y')
    plt.grid(True)
    plt.legend()  # Выводит лейблы графиков

    # plt.xticks(range(0, 20, 4))  # Выводить по оси х отметки с 0 до 20 с интервалом 4

    # path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '1.png')  # Место исполняемого файла
    # os.remove('media/graph/graph_1/1.png')
    plt.savefig('media/graph/graph_1/1.png')  # Сохраняем график
    '''
    # Make some fake data.
    x = [1, 2, 3, 4, 5, 6, 7]
    y_1 = [1, 18, 2, 7, 5, 6, 8]
    y_2 = [1, 2, 3, 5, 7, 13, 21]
    y_3 = [20, 15, 12, 8, 7, 11, 5]

    # Create plots with pre-defined labels.
    fig, ax = plt.subplots()
    ax.plot(x, y_1, color='#ff0000', label='График 1')
    ax.plot(x, y_2, color='#00ff00', label='График 2')
    ax.plot(x, y_3, color='#0000ff', label='График 3')

    # legend = ax.legend(loc='upper left', fontsize='12')
    legend = ax.legend()
    fig.savefig('media/graph/graph_1/1.png')  # Сохраняем график  

    
    print('FUNCTION -> graph > graph_1')
    SITE.content += '<h1>График</h1>'
    SITE.content += '<img src="/media/graph/graph_1/1.png" alt="График">'
