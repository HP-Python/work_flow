from tkinter import Tk, mainloop, Label, Frame, Button
from db_manage import get_script_state
from admin import env

class App:
    def __init__(self):
        # name
        self.state_lbs = {}
        self.name_state = {}
        self.root = Tk()
        self.UI_layout()
        self.root.after(1000, self.update_state)
    def UI_layout(self, ):
        frame = Frame(self.root)
        frame.grid(column=0,row=0,padx=20,pady=20)
        for i in range(len(env.script_names)):
            # name label
            name = env.script_names[i]
            Label(frame, text=name).grid(column=0,row=i)
            # state
            self.state_lbs[name] = Label(frame, width=3)
            self.state_lbs[name].grid(column=1, row=i,padx=10)
    # self.state_lbs[index].config(bg=color)
    # default color #d9d9d9
    def update_state(self):
        state_dict = get_script_state()
        #color_list :[      0,    1]
        color_list = ['#D9D9D9','#FFFF00','#008000','#FF0000']
        for key in state_dict:
            state = int(state_dict[key])
            self.state_lbs[key]['bg'] = color_list[state]
        self.root.after(2000, self.update_state)

if __name__ == '__main__':
    app = App()
    mainloop()


