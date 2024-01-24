import tkinter as tk
from tkinter import ttk
import pandas as pd

result_history = []
path = "calcul_history.csv"


def on_key_press(event):
    """
    Fonction appelée en réponse à l'événement de pression de touche.

    :param event: L'événement clavier déclenché.
    :return: Aucun.
    """
    current_text = entry.get()
    try:
        if event.keysym == "Return":
            result = eval(current_text)
            label_result.config(text=str(result))
            entry.delete(0, tk.END)
            entry.insert(0, current_text)
            result_history.append({'CALCUL': current_text, 'RESULTAT': result})
            history_df = pd.DataFrame(result_history)
            history_df.to_csv(path, index=False)
            label_error.config(text="")

    except (SyntaxError, ValueError, NameError,ZeroDivisionError) as e:
        label_error.config(text=str(e))


def clear_screen():
    """
    Efface l'écran en réinitialisant les champs d'entrée et de résultat,
    et supprime le message d'erreur affiché.

    :return: Aucun.
    """
    label_error.config(text="")
    entry.delete(0, tk.END)
    label_result.config(text="")


def on_combobox_select(event, combobox, entry, label_result, df):
    """
    Fonction appelée en réponse à la sélection d'un élément dans une combobox.

    :param event: L'événement déclenché.
    :param combobox: La combobox à partir de laquelle l'événement a été déclenché.
    :param entry: Le champ d'entrée à mettre à jour.
    :param label_result: Le champ de résultat à mettre à jour.
    :param df: Le DataFrame contenant les données historiques.
    :return: Aucun.
    """
    selected_calculation = combobox.get()
    selected_result = df.loc[df['CALCUL'] == selected_calculation, 'RESULTAT'].values[0]
    entry.delete(0, tk.END)
    entry.insert(0, selected_calculation)
    label_result.config(text=str(selected_result))


def display_history():
    """
    Affiche l'historique des calculs dans une combobox pour une sélection ultérieure.

    :return: Aucun.
    """
    df = pd.read_csv(path)
    selected_line = df['CALCUL'].tolist()
    combobox = ttk.Combobox(root, values=selected_line, state="readonly")
    combobox.grid(row=2, column=3, sticky="nsew")
    combobox.bind("<<ComboboxSelected>>", lambda event: on_combobox_select(event, combobox, entry, label_result, df))
    combobox.event_generate("<1>")
    if selected_line:
        combobox.set(selected_line[0])
    combobox['state'] = 'normal'


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
    label_result = tk.Label(root, bg="lightgray", anchor="w")
    label_result.grid(row=1, column=0, columnspan=4, sticky="ew")

    # clear the screen
    clear = tk.Button(root, text="Clear", command=clear_screen)
    clear.grid(row=2, column=0)

    # display history
    history = tk.Button(root, text="History", command=display_history)
    history.grid(row=2, column=1)

    # display error
    label_error = tk.Label(root, text="", pady=30)
    label_error.grid(row=3, column=1)

    # configure columns
    for i in range(3):
        root.grid_columnconfigure(i, weight=1)

    root.mainloop()
