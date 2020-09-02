from tkinter import *
from PIL import Image,ImageTk,ImageDraw  #pip install Pillow
from datetime import *
import time
import sys
import os
import cv2
import pickle
from math import *
import csv
import requests as req
#import pymysql
from tkinter import messagebox,ttk
from facenet.part1 import main_train
from facenet.part3 import main_test
import pandas as pd
print("hello")
filename = "class_records.csv"
namefield = [["name","enrollment","time"]]
with open("D:\\FR\\facenet\\"+filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(namefield) 

# if __name__ == "__main__":
#     with open("D:\\FR\\facenet\\test_part3.pkl", 'rb') as test:
#         test_part3 = pickle.load(test)
class Login_window:
     
    def __init__(self,root):
        
        self.photos_list = []
        self.photos_name = []
        self.root=root
        self.root.title("Attendance System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")
        # with open("D:\\FR\\facenet\\model_part.pkl", 'rb') as file:
        #     self.model_part1 = pickle.load(file)
        
        
        
        
         #=======background colors==================================
        self.bg=ImageTk.PhotoImage(file="D:/FR/images/bg1.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        
        #left_lbl=Label(self.root,bg="#08A3D2",bd=0)
        #left_lbl.place(x=0,y=0,relheight=1,width=600)
        #self.bg=ImageTk.PhotoImage(file="D:/FR/images/b1.jpg")
        #bg=Label(self.root,image=self.bg).place(x=0,y=0,width=1000,height=500)
        
        #right_lbl=Label(self.root,bg="#031F3C",bd=0)
        #right_lbl.place(x=600,y=0,relheight=1,relwidth=1)
         #========frames1===================================
        
        login_frame=Frame(self.root,bg="white")
        login_frame.place(x=250,y=100,width=800,height=500)
        
        title=Label(login_frame,text="ATTENDANCE SYSTEM",font=("times new roman",30,"bold"),bg="white",fg="#08A3D2").place(x=250,y=50)
        
        #uname=Label(login_frame,text="USER NAME",font=("times new roman",18,"bold"),bg="white",fg="gray").place(x=250,y=150)
        #self.txt_uname=Entry(login_frame,font=("times new roman",15),bg="lightgray")
        #self.txt_uname.place(x=250,y=180,width=375,height=35)
        
        #enroll=Label(login_frame,text="ENROLLMENT NUMBER",font=("times new roman",18,"bold"),bg="white",fg="gray").place(x=250,y=250)
        #self.txt_enroll=Entry(login_frame,font=("times new roman",15),bg="lightgray")
        #self.txt_enroll.place(x=250,y=280,width=375,height=35)
        
        #btn_reg=Button(login_frame,cursor="hand2",command=self.register_window,text="Register New Account?",font=("times new roman",14),bg="white",bd=0,fg="#B00857").place(x=250,y=320)
        #btn_forget=Button(login_frame,cursor="hand2",command=self.forget_password_window,text="Forget Password?",font=("times new roman",14),bg="white",bd=0,fg="red").place(x=450,y=320)
        #btn_login=Button(login_frame,text="Login",command=self.login,font=("times new roman",20,"bold"),fg="white",bg="#B00857",cursor="hand2").place(x=250,y=380,width=180,height=40)
        #btn_datacollect=Button(login_frame,text="Data Collect",command=self.datacollect_window,font=("times new roman",20,"bold"),fg="black",bd=0,bg="lightblue",cursor="hand2",overrelief='sunken').place(x=400,y=120,width=180,height=40)
        #btn_train=Button(login_frame,text="Train",command=self.train,font=("times new roman",20,"bold"),fg="black",bd=0,bg="lightblue",cursor="hand2",overrelief='sunken').place(x=400,y=170,width=180,height=40)
        #btn_test=Button(login_frame,text="Test",command=self.test,font=("times new roman",20,"bold"),fg="black",bd=0,bg="lightblue",cursor="hand2",overrelief='sunken').place(x=400,y=220,width=180,height=40)
        #btn_csvsubmit=Button(login_frame,text="CSV Submit",command=self.csvsubmit,font=("times new roman",20,"bold"),fg="black",bd=0,bg="lightblue",cursor="hand2",overrelief='sunken').place(x=400,y=270,width=180,height=40) 
        #btn_department=Button(login_frame,text="Select Depart.",command=self.department,font=("times new roman",20,"bold"),fg="black",bd=0,bg="lightblue",cursor="hand2",overrelief='sunken').place(x=400,y=320,width=180,height=40)
        #btn_login=Button(login_frame,text="Login",command=self.login,font=("times new roman",20,"bold"),fg="black",bd=0,bg="lightblue",cursor="hand2",overrelief='sunken').place(x=400,y=370,width=180,height=40)
        self.btn_datacollect=ImageTk.PhotoImage(file="D:/FR/images/icons8-data-recovery-80.png")
        btn=Button(login_frame,image=self.btn_datacollect,cursor="hand2",bd=0,overrelief='sunken',command=self.datacollect_window).place(x=350,y=160)
        
        self.btn_traine=ImageTk.PhotoImage(file="D:/FR/images/icons8-training-96.png")
        btn=Button(login_frame,image=self.btn_traine,bd=0,cursor="hand2",overrelief='sunken',command=self.call_model).place(x=550,y=160)
        
        self.btn_test=ImageTk.PhotoImage(file="D:/FR/images/icons8-test-passed-96.png")
        btn=Button(login_frame,image=self.btn_test,bd=0,cursor="hand2",overrelief='sunken',command=self.test_model).place(x=350,y=280)
        
        self.btn_csvsubmit=ImageTk.PhotoImage(file="D:/FR/images/icons8-submit-resume-96.png")
        btn=Button(login_frame,image=self.btn_csvsubmit,bd=0,cursor="hand2",overrelief='sunken',command=self.csvsubmit).place(x=550,y=280)
        
        # self.btn_department=ImageTk.PhotoImage(file="D:/FR/images/icons8-department-96.png")
        # btn=Button(login_frame,image=self.btn_department,bd=0,cursor="hand2",overrelief='sunken',command=self.department_window).place(x=350,y=320)
        
        # self.btn_login=ImageTk.PhotoImage(file="D:/FR/images/icons8-enter-96.png")
        # btn=Button(login_frame,image=self.btn_login,bd=0,cursor="hand2",overrelief='sunken').place(x=550,y=320)
        
        
        #=======clock==================================
        #self.lbl = Label(self.root,text="\n BEC CLOCK",font=("Book Antiqua",25,"bold"),fg="white",compound=BOTTOM,bg="#081923",bd=0)
        self.lbl = Label(self.root,bg="#081923",bd=0)
        self.lbl.place(x=90,y=120,height=450,width=350)
        #self.clock_image()
        self.working()
        #========frames2===================================
    def call_model(self):
        main_train()
    def test_model(self):
        main_test()
    def csvsubmit(self):
        data = pd.read_csv("D:\\FR\\facenet\\class_records.csv")
        record = []
        
        for i in data.index:
            url = "http://127.0.0.1:8000/api/studentlist/?search={:d}".format(data["enrollment"][i])
            response = req.get(url)
            record.append(response.json())
        
        for j in record:
            data_post = {'enrollment':j[0]["enrollment"],'sem':j[0]["semester"]}
            data_update = {'total_attendance':j[0]["total_attendance"]+1}
            req.post("http://127.0.0.1:8000/api/attendancelist/",data_post)
            req.patch("http://127.0.0.1:8000/api/student/update/{:d}/".format(j[0]["id"]), data_update)
        
    def department(self):
        pass
    def login(self):
        pass

        
    def write(self):
        
        directory = self.txt_uname.get()+"_"+self.txt_enroll.get()
        parent_dir = os.getcwd()+"\\facenet\\5-celebrity-faces-dataset\\train"
        path = os.path.join(parent_dir, directory) 
        os.mkdir(path)
        # data = {'ERN': ern, 'NAME': name, 'IMAGE':file_name_path}
        # self.dataset  = self.dataset .append(data, ignore_index=True)
        # self.dataset.to_excel('data.xlsx', index=False)
        for photo, name in zip(self.photos_list,self.photos_name):
            cv2.imwrite(os.path.join(path , name), img=photo)
        
        # self.list_data()
    def take_photo(self):
            
            global key, webcam
            key = cv2. waitKey(1)
            webcam = cv2.VideoCapture(0)
            for i in range(5):
                while True:
                    try:
                        global frame
                        check, frame = webcam.read()
                        cv2.imshow("Capturing", frame)
                        key = cv2.waitKey(1)
                        if key == ord('s'):
                            global counter
                            global file_name_path
                            file_name_path = self.txt_enroll.get()+'_'+self.txt_uname.get()+'_'+str(i+1)+'.jpg'
                            
                            
                            #self.image_name.setText(file_name_path)
                            
                            self.photos_list.append(frame)
                            self.photos_name.append(file_name_path)
                            # webcam.release()
                            # img_ = cv2.imread(file_name_path, cv2.IMREAD_ANYCOLOR)
                            print(i)
                            
                            break
                        elif key == ord('q'):
                            webcam.release()
                            cv2.destroyAllWindows()
                            break
                    except(KeyboardInterrupt):
                        print("Turning off camera.")
                        webcam.release()
                        print("Camera off.")
                        print("Program ended.")
                        cv2.destroyAllWindows()
                        break
            print(self.photos_name)
            print(self.photos_list)
            webcam.release()
            cv2.destroyAllWindows()
    def datacollect_window(self):
   
       
        self.root2=Toplevel()
        self.root2.title("Data Collection")
        self.root2.geometry("520x430+490+150")
        self.root2.config(bg="white")##d3d3d3
        self.root2.focus_force()
        self.root2.grab_set()
        #login_frame1=Frame(self.root2,bg="white")
        #login_frame1.place(x=250,y=100,width=800,height=500)
        #self.left=ImageTk.PhotoImage(file="D:/FR/images/side.jpg")
        #left=Label(self.root2,image=self.left).place(x=490,y=150,width=520,height=430)
        
  
        title=Label(self.root2,text="Data Collection",font=("times new roman",30,"bold"),bg="white",fg="#08A3D2").place(x=130,y=50)
        
        uname=Label(self.root2,text="USER NAME",font=("times new roman",18,"bold"),bg="white",fg="black").place(x=100,y=120)
        self.txt_uname=Entry(self.root2,font=("times new roman",15),bg="lightgray")
        self.txt_uname.place(x=100,y=150,width=350,height=35)
        
        enroll=Label(self.root2,text="ENROLLMENT NUMBER",font=("times new roman",18,"bold"),bg="white",fg="black").place(x=100,y=220)
        self.txt_enroll=Entry(self.root2,font=("times new roman",15),bg="lightgray")
        self.txt_enroll.place(x=100,y=250,width=350,height=35)
        
        
        #btn_reg=Button(login_frame,cursor="hand2",command=self.register_window,text="Register New Account?",font=("times new roman",14),bg="white",bd=0,fg="#B00857").place(x=250,y=320)
        #btn_forget=Button(login_frame,cursor="hand2",command=self.forget_password_window,text="Forget Password?",font=("times new roman",14),bg="white",bd=0,fg="red").place(x=450,y=320)
        #btn_login=Button(login_frame,text="Login",command=self.login,font=("times new roman",20,"bold"),fg="white",bg="#B00857",cursor="hand2").place(x=250,y=380,width=180,height=40)
        #btn_opencam=Button(self.root2,text="OpenCam",command=self.opencam,font=("times new roman",20,"bold"),fg="black",bd=0,bg="#08A3D2",cursor="hand2",overrelief='sunken').place(x=130,y=360,width=160,height=40)
        #btn_save=Button(self.root2,text="Save",command=self.save,font=("times new roman",20,"bold"),fg="black",bd=0,bg="#08A3D2",cursor="hand2",overrelief='sunken',underline=3).place(x=330,y=360,width=160,height=40)
        self.btn_opencam=ImageTk.PhotoImage(file="D:/FR/images/icons8-camera-96 - Copy.png")
        btn=Button(self.root2,image=self.btn_opencam,bd=0,cursor="hand2",overrelief='sunken',command=self.take_photo).place(x=170,y=330)
        self.btn_save=ImageTk.PhotoImage(file="D:/FR/images/25536-4-save-button-photos-thumb - Copy.png")
        btn=Button(self.root2,image=self.btn_save,bd=0,cursor="hand2",overrelief='sunken',command=self.write).place(x=270,y=310)
        #self.btn_img=ImageTk.PhotoImage(file="D:/FR/images/icons8-login-100.png")
        #btn=Button(self.root2,image=self.btn_img,bd=0,cursor="hand2",overrelief='sunken').place(x=600,y=360)
        #btn_settings=Button(login_frame,text="settings",command=self.settings_window,font=("times new roman",20,"bold"),fg="white",bg="blue",cursor="hand2").place(x=600,y=50,width=180,height=40)
        
        #=======clock==================================
        #self.lbl = Label(self.root,text="\n BEC CLOCK",font=("Book Antiqua",25,"bold"),fg="white",compound=BOTTOM,bg="#081923",bd=0)
        #self.lbl = Label(self.root2,bg="#081923",bd=0)
        #self.lbl.place(x=90,y=120,height=450,width=350)
        #self.clock_image()
        #self.working()
    def department_window(self):
       
        self.root2=Toplevel()
        self.root2.title("Select Department & College")
        self.root2.geometry("520x430+490+150")
        self.root2.config(bg="white")##d3d3d3
        self.root2.focus_force()
        self.root2.grab_set()
        #login_frame1=Frame(self.root2,bg="white")
        #login_frame1.place(x=250,y=100,width=800,height=500)
        #self.left=ImageTk.PhotoImage(file="D:/FR/images/side.jpg")
        #left=Label(self.root2,image=self.left).place(x=490,y=150,width=520,height=430)
        
  
        title=Label(self.root2,text="Select Department & College",font=("times new roman",20,"bold"),bg="white",fg="#08A3D2").place(x=100,y=50)
        
        cname=Label(self.root2,text="COLLEGE NAME",font=("times new roman",18,"bold"),bg="white",fg="black").place(x=100,y=120)
        self.txt_cname=Entry(self.root2,font=("times new roman",15),bg="lightgray")
        self.txt_cname.place(x=100,y=150,width=350,height=35)
        
        depart=Label(self.root2,text="DEPARTMENT",font=("times new roman",18,"bold"),bg="white",fg="black").place(x=100,y=220)
        self.txt_depart=Entry(self.root2,font=("times new roman",15),bg="lightgray")
        self.txt_depart.place(x=100,y=250,width=350,height=35)
        
        self.btn_ok=ImageTk.PhotoImage(file="D:/FR/images/137-1378237_round-error-warning-button-clip-art-at-clkercom - Copy.png")
        btn=Button(self.root2,image=self.btn_ok,bd=0,cursor="hand2",overrelief='sunken').place(x=210,y=300)
        
    def train(self):
        pass
    def test(self):
        pass
    def scan(self):
        self.root.destroy()
        import DE
    def settings_window(self):
        self.root3=Toplevel()
        self.root3.title("Settings")
        self.root3.geometry("350x400+495+150")
        self.root3.config(bg="white")
        self.root3.focus_force()
        self.root3.grab_set()
    
    
        t=Label(self.root3,text="Settings",font=("times new roman",20,"bold"),bg="white",fg="blue").place(x=0,y=10,relwidth=1)
        btn_scan=Button(self.root3,text="scan to login",command=self.scan,bg="green",fg="white",font=("times new roman",15,"bold")).place(x=90,y=340)
                    
    def reset(self):
        self.cmb_quest.current(0)
        self.txt_new_pass.delete(0,END)
        self.cmb_quest2.current(0)
        self.txt_pass_.delete(0,END)
        self.txt_email.delete(0,END)
    def forget_password(self):
        if self.cmb_quest.get()=="select" or self.cmb_quest2.get()=="" or self.txt_new_pass.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root2)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="studentreg")
                cur=con.cursor()
                cur.execute("select * from student where email=%s and branch=%s and semester=%s ",(self.txt_email.get(),self.cmb_quest.get(),self.cmb_quest2.get()))
                row=cur.fetchone()
                if row==None:
                     messagebox.showerror("Error","Please select the correct branch / enter semester",parent=self.root2)
                else:
                    cur.execute("update student set password=%s where email=%s",(self.txt_new_pass.get(),self.txt_email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","your password has been reset,Please login with new password",parent=self.root2)
                    self.reset()    
                    self.root2.destroy()
                    
            except Exception as es:
                messagebox.showerror("Error",f"Error Due To: {str(es)}",parent=self.root)        
        
        
        
    def forget_password_window(self):
        if self.txt_email.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset your password",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="studentreg")
                cur=con.cursor()
                cur.execute("select * from student where email=%s",self.txt_email.get())
                row=cur.fetchone()
                if row==None:
                     messagebox.showerror("Error","Please enter the valid email address to reset your password",parent=self.root)
                else:
                    con.close()
                    self.root2=Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("350x400+495+150")
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()
                    
                    t=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),bg="white",fg="red").place(x=0,y=10,relwidth=1)
                    
                    
                    #-------------------------------------------------------------------------------forget password
                    
                    branch=Label(self.root2,text="Branch",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
                    
                    
                    self.cmb_quest = ttk.Combobox(self.root2,font=("times new roman",13),state='readonly',justify=CENTER)
                    self.cmb_quest['values']=("Select","Computer","Electrical","Mechanical","Civil")
                    self.cmb_quest.place(x=50,y=130,width=250)
                    self.cmb_quest.current(0)
                    
                    
                    
                    semester=Label(self.root2,text="Semester",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=180)
        
        
                    self.cmb_quest2 = ttk.Combobox(self.root2,font=("times new roman",13),state='readonly',justify=CENTER)
                    self.cmb_quest2['values']=("Select","Sem1","Sem2","Sem3","Sem4","Sem5","Sem6","Sem7","Sem8")
                    self.cmb_quest2.place(x=50,y=210,width=250)
                    self.cmb_quest2.current(0)
                    #answer=Label(self.root2,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=180)
                    #self.txt_answer = Entry(self.root2,font=("times new roman",15),bg="lightgray")
                    #self.txt_answer.place(x=50,y=210,width=250)
                    
                    new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=260)
                    self.txt_new_pass = Entry(self.root2,font=("times new roman",15),bg="lightgray")
                    self.txt_new_pass.place(x=50,y=290,width=250)
                    
                    btn_change_password=Button(self.root2,text="Reset Password",command=self.forget_password,bg="green",fg="white",font=("times new roman",15,"bold")).place(x=90,y=340)
                    
                    
                    
            except Exception as es:
                messagebox.showerror("Error",f"Error Due To: {str(es)}",parent=self.root)
        
           
        
    #def register_window(self):
        #self.root.destroy()
        #import Register
    
    def opencam(self):
        if self.txt_uname.get()=="" or self.txt_enroll.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="studentreg")
                cur=con.cursor()
                cur.execute("select * from student where uname=%s and enroll=%s",(self.txt_uname.get(),self.txt_enroll.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Username & enrollmentnumber",parent=self.root)
                else:
                    messagebox.showinfo("Success","Welcome",parent=self.root)
                    self.root.destroy()
                    import AS
                    con.close()
            except Exception as es:
                messagebox.showerror("Error",f"Error Due To: {str(es)}",parent=self.root)
        
    def save(self):
        pass
        
        
        
        
    def clock_image(self,hr,min_,sec_):
        clock = Image.new("RGB",(400,450),(0,0,0))
        draw = ImageDraw.Draw(clock)
        #====for clock image==========
        bg = Image.open("images/c.png")
        bg = bg.resize((300,300),Image.ANTIALIAS)
        clock.paste(bg,(50,50))
        #=====formula to rotate the anticlock====
        #angle_in_radians = angle_in_degress * math.pi / 180
        #line_length = 100
        #center_x = 250
        #center_y = 250
        #end_x = center_x + line_length * math.cos(angle_in_radians)
        #end_y = center_y - line_length * math.sin(angle_in_radians)
        
        
        #====hour line image==========
        #          x1 ,y1 ,x2  ,y2
        origin = 200,200
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="#DF005E",width=4)
        #====min line image==========
        draw.line((origin,200+80*sin(radians(min_)),200-80*cos(radians(min_))),fill="white",width=3)
        #====sec line image==========
        draw.line((origin,200+100*sin(radians(sec_)),200-100*cos(radians(sec_))),fill="yellow",width=2) 
        draw.ellipse((195,195,210,210),fill="black")
        clock.save("images/clock_new.png")
        
    def working(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second
        
        hr=(h/12)*360
        min_=(m/60)*360
        sec_=(s/60)*360
        #print(h,m,s)
        #print(hr,min_,sec_)
        self.clock_image(hr,min_,sec_)
        
        self.img=ImageTk.PhotoImage(file="images/clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200, self.working)

root = Tk()
obj = Login_window(root)
root.mainloop()
    
    