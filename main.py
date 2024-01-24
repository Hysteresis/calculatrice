import tkinter as tk
from tkinter import ttk
import pandas as pd

# result = []
result_history = []
path = "calcul_history.csv"


def on_key_press(event):
    current_text = entry.get()
    try:
        if event.keysym == "Return":
            result = eval(current_text)
            print(result)
            entry_result.delete(0, tk.END)
            entry_result.insert(0, str(result))
            entry.delete(0, tk.END)
            entry.insert(0, current_text)
            result_history.append({'CALCUL': current_text, 'RESULTAT': result})
            history_df = pd.DataFrame(result_history)
            history_df.to_csv(path, index=False)
            label_error.config(text="...")

    except (SyntaxError, ValueError, NameError,ZeroDivisionError) as e:
        label_error.config(text=str(e))


def clear_char(event):
    current_text = entry.get()
    if current_text:
        entry.delete(len(current_text))
        print(entry)
    return entry


def clear_screen():
    label_error.config(text="")
    entry.delete(0, tk.END)
    entry_result.delete(0,tk.END)


def on_combobox_select(event, combobox, entry, entry_result, df):
    selected_calculation = combobox.get()
    selected_result = df.loc[df['CALCUL'] == selected_calculation, 'RESULTAT'].values[0]
    entry.delete(0, tk.END)
    entry.insert(0, selected_calculation)
    entry_result.delete(0, tk.END)
    entry_result.insert(0, selected_result)


def display_history():
    df = pd.read_csv(path)
    selected_line = df['CALCUL'].tolist()
    combobox = ttk.Combobox(root, values=selected_line)
    combobox.grid(row=2, column=3, sticky="nsew")
    combobox.bind("<<ComboboxSelected>>", lambda event: on_combobox_select(event, combobox, entry, entry_result, df))


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Calculatrice")
    root.geometry("300x300")

    # 1st screen: The user enters their calculations
    entry = tk.Entry(root, bg="#98FB98")
    entry.grid(row=0, column=0, columnspan=4, sticky="ew")

    # bind the key pressed
    root.bind('<Key>', on_key_press)

    # 2nd screen: display the result
    entry_result = tk.Entry(root, bg="#98FB98")
    entry_result.grid(row=1, column=0, columnspan=4, sticky="ew")

    # clear the screen
    clear = tk.Button(root, text="Clear", command=clear_screen)
    clear.grid(row=2, column=0)

    # display history
    history = tk.Button(root, text="History", command=display_history)
    history.grid(row=2, column=1)

    # display error
    label_error = tk.Label(root, text="...", pady=30)
    label_error.grid(row=3, column=1)


    # configure columns
    for i in range(3):
        root.grid_columnconfigure(i, weight=1)

    root.mainloop()
