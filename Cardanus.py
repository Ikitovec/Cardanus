from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import Combobox
from tkinter import messagebox
import random



def clicked():
    code_text = txt.get("1.0", 'end-1c').lower()
    mask_input=txt2.get("1.0", 'end-1c')
    txt3.delete(1.0, END)
    n=int(spin.get())
    flag=0
    if n%2==1:
        messagebox.showinfo('Ошибка!', f'Сторона решетки должна делиться на 2!')
        flag=1
    elif n<0:
        messagebox.showinfo('Ошибка!', f'Сторона решетки должна быть положительной!')
        flag = 1
    elif len((code_text))>n*n:
        messagebox.showinfo('Ошибка!', f'Выбранная решетка слишком мала для вашего текста! Возьмите размер побольше')
        flag = 1

    if flag==0:
        alphabet='abcdefghijklmnopqrstuvwxyz'
        eng_low_alphabet = 'abcdefghijklmnopqrstuvwxyz'
        rus_low_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        for i in code_text:
            if eng_low_alphabet.find(i,0)!=-1:
                alphabet=eng_low_alphabet
                break
            elif rus_low_alphabet.find(i,0)!=-1:
                alphabet=rus_low_alphabet
                break

        if ((combo2.get() == 'Зашифровать') | (combo2.get() == 'Расшифровать')):

            A = [0] * n
            for i in range(n):
                A[i] = [0] * n

            # левый верхний угол
            l = 0
            for i in range(n // 2):
                for j in range(n // 2):
                    A[i][j] = l
                    l += 1

            # левый нижний угол
            l = 0
            for i in range(0, n // 2):
                for j in range(n - 1, n // 2 - 1, -1):
                    A[j][i] = l
                    l += 1

            # правый нижний угол
            l = 0
            for i in range(n - 1, n // 2 - 1, -1):
                for j in range(n - 1, n // 2 - 1, -1):
                    A[i][j] = l
                    l += 1

            # правый верхний угол
            l = 0
            for i in range(n - 1, n // 2 - 1, -1):
                for j in range(n // 2):
                    A[j][i] = l
                    l += 1

            for i in range(len(A)):
                for j in range(0, len(A[i])):
                    print(A[i][j], end=' ')
                print()

            print('----------------------')
            # сгенерировать случайную решетку
            if len(mask_input)==0:
                mask = [0] * n
                for i in range(n):
                    mask[i] = [0] * n

                random_array = [0] * l * 4
                for i in range(0, len(random_array)):
                    random_array[i] = [0] * 2

                index = 0
                for figure in range(l):
                    for i in range(len(A)):
                        for j in range(len(A[i])):
                            if figure == A[i][j]:
                                random_array[index][0] = i
                                random_array[index][1] = j
                                index += 1

                total_random_array = [0] * l
                for i in range(len(total_random_array)):
                    total_random_array[i] = [0] * 2

                for i in range(l):
                    random_item = random.randrange(0, 4)
                    total_random_array[i][0] = random_array[4 * i + random_item][0]
                    total_random_array[i][1] = random_array[4 * i + random_item][1]
                # print(total_random_array)

                for i in range(len(total_random_array)):
                    mask[total_random_array[i][0]][total_random_array[i][1]] = '!'

                if (combo3.get() == 'С мусором'):
                    delete_number = 0
                    # убираем лишние!
                    missing = n * n - len(code_text)
                    missing_parts = missing // 4
                    print(f'missing parts={missing_parts}')

                    for i in range(0, missing_parts):
                        exitFlag = False

                        for j in range(0, len(mask)):
                            for k in range(0, len(mask[j])):
                                if mask[j][k] == '!':
                                    print(j,k)
                                    delete_number = A[j][k]
                                    for row in range(0, len(A)):
                                        for cols in range(0, len(A[row])):
                                            if A[row][cols] == delete_number:
                                                A[row][cols] = f'{alphabet[random.randrange(0, len(alphabet))]}'
                                    mask[j][k] = 0
                                    exitFlag = True
                                    break
                            if (exitFlag):
                                break






                print('решетка:')
                for i in range(len(mask)):
                    for j in range(0, len(mask[i])):
                        print(mask[i][j], end=' ')
                        txt2.insert(INSERT, mask[i][j])
                    print()
                    txt2.insert(INSERT, '\n')
            else:

                mask = [0] * n
                for i in range(n):
                    mask[i] = [0] * n

                t = 0
                for i in range(0, n):
                    for j in range(0, n):
                        if mask_input[t] == '\n':
                            t += 1
                        mask[i][j] = mask_input[t]
                        t += 1

                print(mask)

            if (combo2.get() == 'Зашифровать'):

                index = 0
                for loops in range(4):

                    print(f'{loops}:')
                    for i in range(n):
                        for j in range(n):
                            if mask[i][j] == '!':
                                if index < len(code_text):
                                    A[i][j] = code_text[index]
                                    index += 1
                                else:
                                    A[i][j] = code_text[random.randrange(0, len(code_text))]

                    print('--------после замены-----------')
                    for i in range(len(A)):
                        for j in range(0, len(A[i])):
                            print(A[i][j], end=' ')
                        print()

                    trans = tuple(zip(*A[::-1]))
                    print('--------транспонирование-----------')

                    for i in range(len(trans)):
                        for j in range(0, len(trans[i])):
                            print(trans[i][j], end=' ')
                        print()

                    for i in range(n):
                        for j in range(n):
                            A[i][j] = trans[i][j]



                for i in range(len(A)):
                    for j in range(len(A[i])):
                        txt3.insert(INSERT, A[i][j])

            elif (combo2.get() == 'Расшифровать'):

                for i in range(0,n):
                    for j in range(0,n):
                        A[i][j]=code_text[i*n+j]

                mask_deshifr = [0] * n
                for i in range(n):
                    mask_deshifr[i] = [0] * n

                t=0
                for i in range(0,n):
                    for j in range(0,n):
                        if mask_input[t]=='\n':
                            t+=1
                        mask_deshifr[i][j] = mask_input[t]
                        t+=1

                index = 0
                for loops in range(4):

                    print(f'{loops}:')
                    for i in range(n):
                        for j in range(n):
                            if mask_deshifr[i][j] == '!':
                                if index < len(code_text):
                                    txt3.insert(INSERT, A[i][j])
                                    print(i,j)
                                    index += 1
                                else:
                                    A[i][j] = code_text[random.randrange(0, len(code_text))]

                    print('--------после замены-----------')
                    for i in range(len(A)):
                        for j in range(0, len(A[i])):
                            print(A[i][j], end=' ')
                        print()

                    trans = tuple(zip(*A[::-1]))
                    print('--------транспонирование-----------')

                    for i in range(len(trans)):
                        for j in range(0, len(trans[i])):
                            print(trans[i][j], end=' ')
                        print()

                    for i in range(n):
                        for j in range(n):
                            A[i][j] = trans[i][j]

        else:
            messagebox.showinfo('Ошибка!', f'Вы неверно ввели действие! (Зашифровать или Расшифровать)')




def swap():
    temp1 = txt3.get("1.0", 'end-1c')
    txt.delete(1.0, END)
    txt.insert(INSERT, temp1)
    txt3.delete(1.0, END)

window = Tk()
window.title("Решето Кардано")
window.geometry('700x500')



lbl = Label(window, text="Ваше сообщение")
lbl.grid(column=0, row=0)

spin = Spinbox(window, from_=0, to=100, width=5)
spin.grid(column=1, row=3)

lbl = Label(window, text="Квадратная матрица со стороной:")
lbl.grid(column=0, row=3)


combo2 = Combobox(window)
combo2['values'] = ("Зашифровать", "Расшифровать")
combo2.current(0)
combo2.grid(column=0, row=7)



combo3 = Combobox(window)
combo3['values'] = ("С мусором", "Без мусора")
combo3.current(0)
combo3.grid(column=2, row=7)



btn = Button(window, text="Получить ответ", command=clicked)
btn.grid(column=0, row=8)
lbl = Label(window)


txt = scrolledtext.ScrolledText(window, width=40, height=1)
txt.grid(column=2, row=0)

lbl = Label(window, text="Решетка:")
lbl.grid(column=0, row=6)
txt2 = scrolledtext.ScrolledText(window, width=40, height=15)
txt2.grid(column=2, row=6)

btn = Button(window, text="преместить", command=swap)
btn.grid(column=2, row=8)
lbl = Label(window)

txt3 = scrolledtext.ScrolledText(window, width=40, height=15)
txt3.grid(column=2, row=9)


window.mainloop()
