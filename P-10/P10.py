import tkinter as tk
from tkinter import ttk, messagebox, filedialog, Menu


class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        # 1. Название приложения: ФИО автора
        self.title("Antoshin Anton Andreevich")
        self.geometry("800x600")
        self.minsize(600, 400)

        # Создаем меню
        self.create_menu()

        # Создаем Notebook (вкладки)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)

        # Создаем вкладки
        self.create_calculator_tab()
        self.create_checkboxes_tab()
        self.create_text_tab()

        # Центрируем окно
        self.center_window()

    def center_window(self):
        """Центрирование окна на экране"""
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')

    def create_menu(self):
        """Создание меню приложения"""
        menubar = Menu(self)
        self.config(menu=menubar)

        # Меню Файл
        file_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Файл", menu=file_menu)
        file_menu.add_command(label="Загрузить текст", command=self.load_text_from_file)
        file_menu.add_separator()
        file_menu.add_command(label="Выход", command=self.quit)

        # Меню Справка
        help_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Справка", menu=help_menu)
        help_menu.add_command(label="О программе", command=self.show_about)

    def create_calculator_tab(self):
        """Первая вкладка: простой калькулятор"""
        calc_frame = ttk.Frame(self.notebook)
        self.notebook.add(calc_frame, text="Калькулятор")

        # Заголовок
        title_label = ttk.Label(calc_frame, text="Простейший калькулятор",
                                font=("Arial", 14, "bold"))
        title_label.pack(pady=20)

        # Фрейм для ввода чисел
        input_frame = ttk.Frame(calc_frame)
        input_frame.pack(pady=20)

        # Первое число
        ttk.Label(input_frame, text="Первое число:").grid(row=0, column=0, padx=5, pady=5)
        self.num1_var = tk.StringVar()
        num1_entry = ttk.Entry(input_frame, textvariable=self.num1_var, width=15)
        num1_entry.grid(row=0, column=1, padx=5, pady=5)

        # Выпадающий список операций
        self.operation_var = tk.StringVar(value="+")
        operations = ["+", "-", "*", "/"]
        operation_combo = ttk.Combobox(input_frame, textvariable=self.operation_var,
                                       values=operations, state="readonly", width=5)
        operation_combo.grid(row=1, column=0, columnspan=2, padx=5, pady=10)

        # Второе число
        ttk.Label(input_frame, text="Второе число:").grid(row=2, column=0, padx=5, pady=5)
        self.num2_var = tk.StringVar()
        num2_entry = ttk.Entry(input_frame, textvariable=self.num2_var, width=15)
        num2_entry.grid(row=2, column=1, padx=5, pady=5)

        # Кнопка вычисления
        calc_button = ttk.Button(calc_frame, text="Вычислить", command=self.calculate)
        calc_button.pack(pady=10)

        # Результат
        self.result_var = tk.StringVar(value="Результат: ")
        result_label = ttk.Label(calc_frame, textvariable=self.result_var,
                                 font=("Arial", 12, "bold"), foreground="blue")
        result_label.pack(pady=20)

    def calculate(self):
        """Выполнение вычисления"""
        try:
            num1 = float(self.num1_var.get())
            num2 = float(self.num2_var.get())
            operation = self.operation_var.get()

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    raise ZeroDivisionError("Деление на ноль!")
                result = num1 / num2
            else:
                result = "Неизвестная операция"

            self.result_var.set(f"Результат: {result:.4f}")

        except ValueError:
            messagebox.showerror("Ошибка", "Пожалуйста, введите корректные числа!")
        except ZeroDivisionError as e:
            messagebox.showerror("Ошибка", str(e))
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")

    def create_checkboxes_tab(self):
        """Вторая вкладка: чекбоксы"""
        check_frame = ttk.Frame(self.notebook)
        self.notebook.add(check_frame, text="Выбор варианта")

        # Заголовок
        title_label = ttk.Label(check_frame, text="Выберите вариант(ы)",
                                font=("Arial", 14, "bold"))
        title_label.pack(pady=20)

        # Чекбоксы
        self.checkbox_vars = []
        checkbox_texts = ["Первый", "Второй", "Третий"]

        for i, text in enumerate(checkbox_texts):
            var = tk.BooleanVar()
            self.checkbox_vars.append(var)

            checkbox = ttk.Checkbutton(check_frame, text=text, variable=var)
            checkbox.pack(pady=10)

        # Кнопка
        show_button = ttk.Button(check_frame, text="Показать выбор", command=self.show_selection)
        show_button.pack(pady=20)

    def show_selection(self):
        """Показать выбранные варианты"""
        selected = []
        checkbox_names = ["Первый", "Второй", "Третий"]

        for i, var in enumerate(self.checkbox_vars):
            if var.get():
                selected.append(checkbox_names[i])

        if selected:
            messagebox.showinfo("Ваш выбор", f"Вы выбрали: {', '.join(selected)}")
        else:
            messagebox.showinfo("Ваш выбор", "Вы ничего не выбрали")

    def create_text_tab(self):
        """Третья вкладка: работа с текстом"""
        text_frame = ttk.Frame(self.notebook)
        self.notebook.add(text_frame, text="Работа с текстом")

        # Заголовок
        title_label = ttk.Label(text_frame, text="Загрузка и просмотр текста",
                                font=("Arial", 14, "bold"))
        title_label.pack(pady=10)

        # Фрейм для кнопок
        button_frame = ttk.Frame(text_frame)
        button_frame.pack(pady=10)

        # Кнопки
        load_button = ttk.Button(button_frame, text="Загрузить из файла", command=self.load_text_from_file)
        load_button.pack(side='left', padx=5)

        clear_button = ttk.Button(button_frame, text="Очистить", command=self.clear_text)
        clear_button.pack(side='left', padx=5)

        # Текстовое поле с прокруткой
        text_frame_inner = ttk.Frame(text_frame)
        text_frame_inner.pack(fill='both', expand=True, padx=10, pady=10)

        # Создаем Scrollbar
        scrollbar = tk.Scrollbar(text_frame_inner)
        scrollbar.pack(side='right', fill='y')

        # Создаем Text виджет
        self.text_widget = tk.Text(text_frame_inner, wrap='word', yscrollcommand=scrollbar.set,
                                   font=("Arial", 11))
        self.text_widget.pack(side='left', fill='both', expand=True)

        # Привязываем Scrollbar к Text виджету
        scrollbar.config(command=self.text_widget.yview)

        # Статистика
        self.stats_var = tk.StringVar(value="Статистика: символов: 0, слов: 0")
        stats_label = ttk.Label(text_frame, textvariable=self.stats_var)
        stats_label.pack(pady=5)

    def load_text_from_file(self):
        """Загрузка текста из файла"""
        filetypes = [
            ("Текстовые файлы", "*.txt"),
            ("Все файлы", "*.*")
        ]

        filename = filedialog.askopenfilename(
            title="Выберите текстовый файл",
            filetypes=filetypes
        )

        if filename:
            try:
                with open(filename, 'r', encoding='utf-8') as file:
                    text = file.read()

                self.text_widget.delete(1.0, tk.END)  # Очищаем текущий текст
                self.text_widget.insert(1.0, text)  # Вставляем новый текст

                # Обновляем статистику
                self.update_text_stats()

                messagebox.showinfo("Успех", f"Файл '{filename}' успешно загружен!")

            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось загрузить файл: {str(e)}")

    def clear_text(self):
        """Очистка текстового поля"""
        self.text_widget.delete(1.0, tk.END)
        self.update_text_stats()

    def update_text_stats(self):
        """Обновление статистики текста"""
        text = self.text_widget.get(1.0, tk.END).strip()
        char_count = len(text)
        word_count = len(text.split()) if text else 0
        self.stats_var.set(f"Статистика: символов: {char_count}, слов: {word_count}")

    def show_about(self):
        """Показать информацию о программе"""
        about_text = """Мое приложение
Версия 1.0

Автор: Иванов Иван Иванович

Функционал:
1. Простой калькулятор
2. Выбор вариантов с чекбоксами
3. Загрузка и просмотр текста

© 2024 Все права защищены"""

        messagebox.showinfo("О программе", about_text)


def main():
    app = Application()
    app.mainloop()


if __name__ == "__main__":
    main()