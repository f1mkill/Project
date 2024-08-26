
from tkinter import *
from functools import partial
from tkinter.messagebox import *
import re



a="Авторизируйтесь"
b="Вход в приложение"
c="Пожайлуста введите данные:"
d="Вы зарагистрированны?"
e="Придумайте надежный логин и пароль"
f="Регистрация"


#Логины
namelist = ["ilia"]
#Пароли
passwdlist= ["2" "1"]

window = Tk()
window.title(a)


text1=Label(text=b)
text1.pack(fill=BOTH, expand=True)

text2=Label(text=c)
text2.pack(fill=BOTH, side=LEFT, expand=True)

entryLOGIN = Entry()
entryLOGIN.insert(0,"Логин")
entryLOGIN.pack(fill=BOTH, side=LEFT, expand=True)


entryPASS = Entry()
entryPASS.pack(fill=BOTH, side=LEFT, expand=True)
entryPASS.insert(0,"Пароль")


i=0


#Оценка стойкости пароля
def ChekDATA(entryEPASS,entryELOGIN,namelist,passwdlist):
	passw=entryEPASS.get()
	name=entryELOGIN.get()
	fl=0
	a=0
	while True:
		if (len(passw)<8):
			fl=-1
			break
		elif not re.search("[a-z]",passw):
			fl=-1
			break
		elif not re.search ("[A-Z]",passw):
			fl=-1					
			break	
		elif not re.search("[0-9]",passw):
			fl=-1	
			break	
		elif re.search("\s",passw):
			fl=-1
			break
	if fl==0:
		passwdlist.append(passw)
		a=a+1
	while True:
		if (len(name)<8):

			fl=-1
			break
		elif not re.search("[a-z]",name):
			fl=-1
			break
		elif not re.search ("[A-Z]",name):
			fl=-1					
			break	
		elif not re.search("[0-9]",name):
			fl=-1	
			break	
		elif re.search("\s",name):
			fl=-1
			break
	if fl==0:
		namelist.append(name)
		a=a+1
	if a==2:
		avt(passwdlist,namelist,a,b,c,d,e,f,window)
	else:
		showinfo("Информация","Пароль ненадежн повторите попытку")
		reg(window)	



#Приложение регистрации
def reg(window):
	window.destroy()
	Regw= Tk()
	Regw.title(f)

	text1E=Label(text=e)
	text1E.pack(fill=BOTH, expand=True)

	text2E=Label(text=c)
	text2E.pack(fill=BOTH, side=LEFT, expand=True)

	entryELOGIN = Entry()
	entryELOGIN.insert(0,"Логин")
	entryELOGIN.pack(fill=BOTH, side=LEFT, expand=True)


	entryEPASS = Entry()
	entryEPASS.pack(fill=BOTH, side=LEFT, expand=True)
	entryEPASS.insert(0,"Пароль")

	buttonREG = Button(text="Ввести",command=partial
	(
	ChekDATA,
	entryPASS,
	entryLOGIN,
	namelist,
	passwdlist
	))
	buttonREG.pack(fill=BOTH, side=BOTTOM, expand=True) 
	

def avt(passwdlist,namelist,a,b,c,d,e,f,window):	
	#Приложение авторизации
	window.destroy()
	window = Tk()
	window.title(a)


	text1=Label(text=b)
	text1.pack(fill=BOTH, expand=True)

	text2=Label(text=c)
	text2.pack(fill=BOTH, side=LEFT, expand=True)

	entryLOGIN = Entry()
	entryLOGIN.insert(0,"Логин")
	entryLOGIN.pack(fill=BOTH, side=LEFT, expand=True)


	entryPASS = Entry()
	entryPASS.pack(fill=BOTH, side=LEFT, expand=True)
	entryPASS.insert(0,"Пароль")


	i=0
	#Функция авторизации и проверки паролей на подлинность
	def increase(namelist,passwdlist,entryLOGIN,entryPASS,i):
		p=entryPASS.get()
		name=entryLOGIN.get()
		
		while i<10:
			if name in namelist:
				print("имя есть")
				if p in passwdlist:
					print(a)
					window.destroy()
					main(name)
				else:
					
					entryPASS.delete(0,END)
					i=+1
			else :
				showerror(
			"Ошибка","Введен неверный логин"
			)	
				enrtyLOGIN.delete(0,END)
				i=+1
		else:
			showerror(
			"Ошибка","Попытки кончились"
			)
			


	buttonVXOD = Button(
				master=window,
				text="Войти",
				command=partial(increase,
				namelist,
				passwdlist,
				entryLOGIN,
				entryPASS,
				i
			)
		)
	buttonVXOD.pack(fill=BOTH, side=BOTTOM, expand=True) 





	#Вопрос о том зарегистрирован ли пользователь
def check():
	answer = askyesno(
	title="Вопрос", 
	message=d
	)
	if answer:
		avt(passwdlist,namelist,a,b,c,d,e,f,window)
	else:
		reg(window)
	     
		
check()









window.mainloop()
