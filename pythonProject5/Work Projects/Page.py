import tkinter as tk
import tkinter_page as tkp

window = tk.Tk()

base_frame = tk.Frame(window)

# First we creat three child pages
# We can creat a pack way for a page
def pack_way1():
	print("Use function to define pack way.")
	label1.pack(fill='x',side='bottom')
child1 = tkp.Page(base_frame,pack_way=pack_way1)
label1 = tk.Label(base_frame,text="child1",width=10,height=2)
child1.add_component(label1)

def pack_way2():
	print("Auto pack way is like this.")
	label2.pack()
child2 = tkp.Page(base_frame,pack_way=pack_way2)
label2 = tk.Label(base_frame,text="child2",width=10,height=2)
child2.add_component(label2)

# We can also use auto pack way(do not need a pack way func)
child3 = tkp.Page(base_frame)
label3 = tk.Label(base_frame,text="child3",width=10,height=2)
child3.add_component(label3)

# make child page list
child_page = [child1,child3]
child_page_name = ['page1','page3']

# construct father page - load child page at init
page1 = tkp.Page(base_frame,show_child=True,\
	flip="Combobox",child_page=child_page,\
	child_page_name=child_page_name,current=0,\
	log=False)
label0 = tk.Label(base_frame,text="Combobox Flipway Page",width=20,height=2,\
	font=('Times', '15', 'bold'))
page1.add_component(label0)
# construct father page - add child page at certain place
page1.set_child_page(child2,name='page2',mode='ADD',place=1)

# Pack Father Page
# you can also use
# page1.pack(show_child=True)
# to auto show the current child page
base_frame.pack(fill='both',expand=1)
page1.pack()

window.mainloop()