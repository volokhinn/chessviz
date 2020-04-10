from tkinter import *
import tkinter as tk
from tkinter import ttk
import sqlite3 as lite
import datetime

###################################################################
####################Графическая оболочка###########################
###################################################################

class Main_win: #основное окно
	def __init__(self):
		self.root = tk.Tk()
		self.root.title('ToDo List')
		self.root.geometry("900x600")
		self.root.resizable(False, False)

		toolbar = tk.Frame(bg = 'White', width = 900, height = 100)
		toolbar.place ( x =0, y = 0)



		self.tree = ttk.Treeview(self.root, columns = ('ID','important','task','state','date_start','date_end'),
									   height = 100,
									   show = 'headings')

		self.tree.column('ID', width = 30 , anchor = tk.CENTER)
		self.tree.column('important', width = 60 , anchor = tk.CENTER)
		self.tree.column('task', width = 490 , anchor = tk.CENTER)
		self.tree.column('state', width = 130 , anchor = tk.CENTER)
		self.tree.column('date_start', width = 100 , anchor = tk.CENTER)
		self.tree.column('date_end', width = 100 , anchor = tk.CENTER)

		self.tree.heading('ID', text = 'ID')
		self.tree.heading('important', text = 'Приоритет')
		self.tree.heading('task', text = 'Задание')
		self.tree.heading('state', text = 'Состояние')
		self.tree.heading('date_start', text = 'Дата Начала')
		self.tree.heading('date_end', text = 'Срок сдачи')

		self.tree.place(x=0,y=100)

		self.make_button(toolbar)

		self.db = db
		self.view_records()
	

	def make_button(self, perent):


		self.add=PhotoImage(file='3.png')
		self.change=PhotoImage(file='6.png')
		self.important=PhotoImage(file='4.png')
		self.delete=PhotoImage(file='2.png')
		self.performed=PhotoImage(file='1.png')
		self.delperf=PhotoImage(file='5.png')
		

		btn_open_add = tk.Button(perent,
								text = "Add Task",
								width = 100,
								height = 100,
								image= self.add,
								bd=3,
								command = lambda:self.make_add())
		
		btn_change = tk.Button(perent,
								text = "Change",
								width = 100,
								height = 100,
								image= self.change,
								#command = lambda:self.make_add(),
								
								bd=3)

		btn_important = tk.Button(perent,
								text = "important",
								width = 100,
								height = 100,
								image = self.important,
								#command = lambda:self.make_add(),
								bd=3)

		btn_delete = tk.Button(perent,
								text = "delete",
								width = 100,
								height = 100,
								image = self.delete,
								#command = lambda:self.make_add(),
								bd=3)
		btn_make_performed = tk.Button(perent,
								text = "perfomed",
								width = 100,
								height = 100,
								image = self.performed,
								#command = lambda:self.make_add(),
								bd=3)

		btn_delete_performed = tk.Button(perent,
								text = "del perfomed",
								width = 100,
								height = 100,
								image = self.delperf,
								command = lambda:self.delete_performed(),
								bd=3)
		btn_info = tk.Button(perent,
							 	text = "Информация",
							 	width = 15,
							 	height = 1,
							 	command = lambda:self.info(),
							 	bg = "Grey",
							 	bd=3)
		btn_reference = tk.Button(perent,
							 	text = "Справка",
							 	width = 10,
							 	height = 1,
							 	command = lambda:self.reference(),
							 	bg = "Grey",
							 	bd=3)



		btn_open_add.place 			(x = 5,   y = 0)
		btn_change.place   			(x = 115, y = 0) 
		btn_delete.place			(x = 225, y = 0)	
		btn_important.place 		(x = 335, y = 0)
		btn_make_performed.place 	(x = 445, y = 0)
		btn_delete_performed.place 	(x = 555, y = 0)
		btn_info.place             (x = 735, y = 0)
		btn_reference.place             (x = 660, y = 0)

	def run(self):
		self.root.mainloop()

	def records(self,problem,date_today, date_end,problem_str):
		 self.db.execute_query(problem,date_today, date_end,problem_str)
		 self.view_records()

	def view_records(self):
		self.db.cur.execute('''SELECT * FROM TODO''')
		[self.tree.delete(i) for i in self.tree.get_children()]
		[self.tree.insert('', 'end', values = row) for row in self.db.cur.fetchall()]




	'''def print_problem_add_task(self, result_number, result_status, result_problem, result_date_now, result_date_end):
		number = int(result_number[0][0])
		Label(self.root, text=result_number, font = "Times 16").place(x = 50 , y = 150  + (number - 1) * 50  )
		status_problem = result_problem + '    ' + result_status + '   ' + result_date_now + '   ' + result_date_end #
		Label(self.root, text=status_problem, font = "Times 16").place(x = 90 , y = 150 + (number - 1) * 50)'''


########Тест чтобы вызвать дочернее окно , потом назначить на кнопку##

	def make_add(self):
		Add(self.root)
	def info(self):
		Info(self.root)
        
	def delete_performed(self):
		DelPerf(self.root)
	def make_performed(self):
		Perf(self.root)
	def reference(self):
		Reference(self.root)

class Add: #дочернее окно
	def __init__(self, perent):
		self.root2 = tk.Toplevel(perent)
		self.root2.title('Add Task')
		self.root2.geometry("350x130")
		self.root2.resizable(False, False)

		self.view = main_win
		self.make_window(self.root2)
		




	def make_window(self, root2):
		btn_add_problem = tk.Button(self.root2,
									text = "Add",
									width = 5,
									height = 1,
									command = lambda:self.view.records(self.problem.get(),
																	   self.date_today,
																	   self.Date_end,
																	   self.problem),
									bg = "Green",
									bd=3)

		btn_add_problem.place (x = 100, y = 100)


		self.problem = Entry(self.root2, width = 40)
		self.problem.place(x = 75, y = 5)
		
		Label(self.root2, text = 'Задача').place(x = 10, y = 5)

		Label(self.root2, text = 'Дата окончания').place(x = 10, y = 35)

		self.date_today = datetime.date.today()

		self.Day = tk.IntVar()
		self.Month = tk.IntVar()
		self.Year = tk.IntVar()

		self.Day.set(self.date_today.day)
		self.Month.set(self.date_today.month)
		self.Year.set(self.date_today.year)

		self.Day_spin = Spinbox(self.root2,
								width=3,
								from_ = 1, to = 31, 
								textvariable=self.Day, 
								command = self.date_less_today)

		self.Day_spin.place(x = 45, y = 65)

		Label(self.root2, text = 'День').place(x = 10, y = 65)

		self.Month_spin = Spinbox(self.root2, 
								  width = 3, 
								  from_=1, 
								  to=12, 
								  textvariable=self.Month, 
								  command = self.date_less_today)

		self.Month_spin.place(x = 135, y = 65)

		Label(self.root2, text = 'Месяц').place(x = 85, y = 65)

		self.Year_spin = Spinbox(self.root2,
								 width = 5,
								 from_= 2020, 
								 to=9999, 
								 textvariable=self.Year, 
								 command = self.date_less_today)
		self.Year_spin.place(x = 195, y = 65)
		Label(self.root2, text = 'Год').place(x = 170, y = 65)


		self.Date_end = datetime.date(self.Year.get(), self.Month.get(), self.Day.get())



		btn_add_destroy = tk.Button(self.root2,
								text = "Close",
								width = 5,
								height = 1,
								command = lambda:self.root2.destroy(),
								bg = "Green",
								bd=3)

		btn_add_destroy.place (x = 190, y = 100)
		self.focuse()


	def focuse(self):
		self.root2.grab_set()
		self.root2.focus_set()
		self.root2.wait_window()

	def date_less_today(self):
		self.Year_t = int(self.Year.get())
		self.Month_t = int(self.Month.get())
		self.Day_t = int(self.Day.get())

		self.change_spin()

	def change_spin(self):
		if(self.Year_t < self.date_today.year or self.Year_t == self.date_today.year):
			if(self.Month_t <  self.date_today.month or self.Month_t == self.date_today.month):
				if(self.Day_t < self.date_today.day):
					self.Day_spin.config(from_ = self.date_today.day)
				self.Month_spin.config(from_= self.date_today.month)
			self.Year_spin.config(from_ = self.date_today.year)

		if(self.Year_t == self.date_today.year and self.Month_t > self.date_today.month):
			self.Day_spin.config(from_ = 1)

		if(self.Year_t > self.date_today.year):
			self.Month_spin.config(from_= 1)
			self.Day_spin.config(from_ = 1)
class Info: 
	def __init__(self, perent):
		self.root3 = tk.Toplevel(perent)
		self.root3.title('Информация')
		self.root3.geometry("300x250")
		self.root3.resizable(False, False)

		Label(self.root3, text = 'На данный момент:').place(relx=.2, rely=.1)

		self.focuse()

	def focuse(self):
		self.root3.grab_set()
		self.root3.focus_set()
		self.root3.wait_window()
class Reference: 
	def __init__(self, perent):
		self.root4 = tk.Toplevel(perent)
		self.root4.title('Справка')
		self.root4.geometry("500x750")
		self.root4.resizable(False, False)
		self.add=PhotoImage(file='3.png')
		self.change=PhotoImage(file='6.png')
		self.important=PhotoImage(file='4.png')
		self.delete=PhotoImage(file='2.png')
		self.performed=PhotoImage(file='1.png')
		self.delperf=PhotoImage(file='5.png')
		Label(self.root4, text = 'Чтобы добавить задачу нажмите кнопку:').place(x=0, y=0)
		img1 = Label(self.root4, image = self.add).place(x = 20, y = 20)
		Label(self.root4, text = 'Чтобы изменить задачу, выделите задачу, затем нажмите кнопку:').place(x=0, y=120)
		img2 = Label(self.root4, image = self.change).place(x=20, y=140)
		Label(self.root4, text = 'Чтобы пометить задачу как важную, выделите задачу, затем нажмите кнопку:').place(x=0, y=240)
		img3 = Label(self.root4, image = self.important).place(x=20, y = 260)
		Label(self.root4, text = 'Чтобы удалить задачу, выделите задачу, затем нажмите кнопку:').place(x=0, y=360)
		img4 = Label(self.root4, image = self.delete).place(x=20, y = 380)
		Label(self.root4, text = 'Чтобы отметить задачу как выполненную, выделите задачу, затем нажмите кнопку:').place(x=0, y=480)
		img4 = Label(self.root4, image = self.performed).place(x=20, y = 500)
		Label(self.root4, text = 'Чтобы удалить все выполненные задачи нажмите кнопку:').place(x=0, y=600)
		img4 = Label(self.root4, image = self.delperf).place(x=20, y = 620)
		self.focuse()

	def focuse(self):
		self.root4.grab_set()
		self.root4.focus_set()
		self.root4.wait_window()
        
class DelPerf: 
	def __init__(self, perent):
		self.root5 = tk.Toplevel(perent)
		self.root5.title('Удалить выполненные задачи')
		self.root5.geometry("350x250")
		self.root5.resizable(False, False)

		Label(self.root5, text = 'Вы уверены, что хотите удалить выполненные задачи?').place(x=23, rely=.1)
		btn_yes = tk.Button(self.root5,
							 	text = "Да",
							 	width = 3,
							 	height = 1,
							 	command = lambda:self.root5.destroy(),
							 	bg = "Green",
							 	bd=3)
		btn_yes.place(relx = .3, rely = .4)
		btn_no = tk.Button(self.root5,
							 	text = "Нет",
							 	width = 3,
							 	height = 1,
							 	command = lambda:self.root5.destroy(),
							 	bg = "Green",
							 	bd=3)
		btn_no.place(relx = .6, rely = .4)
		self.focuse()

	def focuse(self):
		self.root5.grab_set()
		self.root5.focus_set()
		self.root5.wait_window()

class DB:
	def __init__(self):
		self.connection = lite.connect("to_do_list.db")
		self.cur = self.connection.cursor()
		self.cur.execute("""
			CREATE TABLE IF NOT EXISTS TODO (
  			№ INTEGER PRIMARY KEY AUTOINCREMENT,
  			Приоритет TEXT, 
  			Задача TEXT NOT NULL,
 			Статус TEXT ,
 			Дата_добавления DATE,
 			Дата_окончания DATE
			)
			""")

		self.connection.commit()

	def execute_query(self, problem, date_today, Date_end, problem_str):

		priority = 'Нет'
	
		status = 'Не выполнено'
		self.cur.execute('''INSERT INTO TODO(Приоритет,Задача, Статус, Дата_добавления, Дата_окончания) VALUES (?,?,?,?, ?)''',
                       (priority,problem, status, date_today, Date_end))
		self.connection.commit()

		'''self.cur.execute("SELECT № FROM TODO ORDER BY № DESC LIMIT 1;")
		self.result_number = self.cur.fetchall()
		self.cur.execute("SELECT Задача FROM TODO ORDER BY № DESC LIMIT 1;")
		self.result_problem = self.cur.fetchall()
		self.cur.execute("SELECT Статус FROM TODO ORDER BY № DESC LIMIT 1;")
		self.result_status = self.cur.fetchall()
		self.cur.execute("SELECT Дата_окончания FROM TODO ORDER BY № DESC LIMIT 1;")
		self.result_date_end = self.cur.fetchall()
		self.cur.execute("SELECT Дата_добавления FROM TODO ORDER BY № DESC LIMIT 1;")
		self.result_date_now = self.cur.fetchall()
		self.result_status = str(self.result_status[0][0])
		self.result_problem = str(self.result_problem[0][0])
		self.result_date_end = str(self.result_date_end[0][0])
		self.result_date_now = str(self.result_date_now[0][0])
		self.date_end_numeral = [int(x) for x in self.result_date_end.split("-")]
		day_end = int(self.date_end_numeral[2])
		month_end =int(self.date_end_numeral[1])
		year_end = int(self.date_end_numeral[0])
		self.date_end_less = datetime.date(year_end, month_end, day_end)
		print(self.date_end_numeral)
		problem_str.delete(0,'end')
		main_win.print_problem_add_task(self.result_number, self.result_status, self.result_problem, self.result_date_now, self.result_date_end)'''

if __name__ == "__main__":

	db = DB()
	main_win = Main_win()
	main_win.run()
	
