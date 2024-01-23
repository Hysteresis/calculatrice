import tkinter as tk

result = []


def on_key_press(event):
    addition = 0
    current_text = entry.get()
    try:
        result = eval(current_text)
        if event.keysym == "Return":
            print(result)
            entry_result.delete(0, tk.END)
            entry_result.insert(0, str(result))

    except SyntaxError:
        pass





def clear_char():
    current_text = entry.get()
    if current_text:
        entry.delete(len(current_text))
        print(entry)


    return entry


if __name__ == "__main__":
    root = tk.Tk()

    display = tk.Entry(root, bg="#98FB98")
    display.grid(row=0, column=0, columnspan=3)

    root.bind('<Key>', on_key_press)

    entry = display

    entry_result = tk.Entry(root, bg="#98FB98")
    entry_result.grid(row=1, column=0, columnspan=3)

    root.mainloop()
