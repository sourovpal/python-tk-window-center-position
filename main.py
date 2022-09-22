import tkinter

root = tkinter.Tk()
root.eval('tk::PlaceWindow . center')

second_win = tkinter.Toplevel(root)
root.eval(f'tk::PlaceWindow {str(second_win)} center')

root.mainloop()

=================================================================


window_width = 400
window_height = 550

root = tk.Tk()

root.title("Hello")

root.resizable(False, False)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
