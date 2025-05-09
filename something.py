import tkinter as tk

# from PIL import Image, ImageDraw, ImageTk

class container(tk.Canvas):
        def __init__(self, master, **kwargs):
                super().__init__(master, **kwargs)
                self.grid_propagate(False)
                self.grid_columnconfigure([0,1,2], weight=1)
                bacK = tk.Label(self, text="\u2B9C", bg='#181818', fg='white', font=('',16))
                bacK.grid(row=0, column=0, sticky='WE')
                self.thing = smth(self)
                self.thing.grid(row=0, column=1, sticky='WE')
                nexT = tk.Label(self, text="\u2B9E", bg='#181818', fg='white', font=('',16))
                nexT.grid(row=0, column=2, sticky='EW')
                nexT.bind("<Enter>", self.fwscroller)
                bacK.bind("<Enter>", self.bwscroller)
                nexT.bind("<Leave>", self.scrollReset)
                bacK.bind("<Leave>", self.scrollReset)
                nexT.bind("<Button-1>", self.thing.iterNext)
                bacK.bind("<Button-1>", self.thing.iterBack)
                
        def fwscroller(self, event=None, xview=0.1491):
                if xview == 1: return
                self.thing.xview_moveto(xview)
                self.callback = self.after(30, self.fwscroller, None, xview+0.01)
        
        def bwscroller(self, event=None, xview=0.1491):
                if xview == 0: return
                self.thing.xview_moveto(xview)
                self.callback = self.after(30, self.bwscroller, None, xview-0.01)
                
        def scrollReset(self, event):
                self.after_cancel(self.callback)
                self.thing.xview_moveto((0.5 * (285 - 200)) / 285)
        

class smth(tk.Canvas):
        def __init__(self, master, **kwargs):
                super().__init__(master, bg='#181818', width=200, height=30, highlightthickness=0)
                self.grid_propagate(False)
                
                self.items = []
                self.itemFrame = tk.Frame(self, bg='#181818', width=285)
                
                for x in range(5):
                        l = tk.Label(self.itemFrame, text=f"item{x}", font=('',14), bg='#181818', fg='gray')
                        self.items.append(l)
                        l.grid(row=0, column=x)
                        l.bindtags('node')
                        
                self.selection = self.items[len(self.items)//2]
                
                self.configure(scrollregion=(0,0,sum(x.winfo_reqwidth() for x in self.items),30))
                self.create_window(0,0, window=self.itemFrame, height=30, anchor='nw')
                self.xview_moveto((0.5 * (285 - 200)) / 285)
                
                for _ in range(len(self.items)//2):
                        self.iterBack()
                                
                self.bind_class('node', "<Button-1>", self.onClick)
                
                
        def itemManager(self):
                for index in range(len(self.items)):
                        self.items[index].grid_forget()
                        self.items[index].grid(row=0, column=index)
                self.selection.configure(fg='gray')
                self.selection = self.items[len(self.items)//2]
                self.selection.configure(fg='white')
        
        def iterBack(self, *args):
                self.items.insert(0, self.items.pop(-1))
                self.itemManager()

        def iterNext(self, *args):
                self.items.append(self.items.pop(0))
                self.itemManager()
                
        def onClick(self, event):
                times = self.items.index(event.widget) - self.items.index(self.selection)
                if times > 0:
                        for _ in range(times):
                                self.iterNext()
                else:
                        for _ in range(abs(times)):
                                self.iterBack()

        


    
    
root = tk.Tk()

test = container(root, bg='#181818', width=300, height=30, highlightthickness=0)
test.grid()


root.mainloop()