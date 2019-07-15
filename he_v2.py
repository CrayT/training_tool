#! /usr/bin/env python3
#encoding:utf-8
from wx import *
class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self,None,-1,title="何老师专用小工具",pos=(100,100),size=(400,400))
        self.panel=Panel(self,-1)

        StaticText(self.panel,-1,"输入时间、距离、配速或圈速任意两项:",pos=(20,5))
        StaticText(self.panel,-1,"时间:",pos=(20,40))
        StaticText(self.panel,-1,"时",pos=(88,40))
        StaticText(self.panel,-1,"分",pos=(148,40))
        StaticText(self.panel,-1,"秒",pos=(198,40))
        StaticText(self.panel,-1,"百分秒",pos=(248,40))
        # StaticText(self.panel,-1,"(则默认为0)",pos=(280,40))

        StaticText(self.panel,-1,"距离:",pos=(20,80))
        StaticText(self.panel,-1,"KM",pos=(125,80))

        StaticText(self.panel,-1,"配速:",pos=(20,120))
        StaticText(self.panel,-1,"分",pos= (88,120))
        StaticText(self.panel,-1,"秒",pos=(138,120))
        StaticText(self.panel,-1,"百分秒",pos=(188,120))
        
        StaticText(self.panel,-1,"圈速:",pos=(20,160))
        StaticText(self.panel,-1,"秒",pos= (118,160))

        text_input01 = TextCtrl(self.panel,-1,pos=(60,40),size=(25,20)) #时间 时
        self.__TextBox01 = text_input01 
        text_input02 = TextCtrl(self.panel,-1,pos=(115,40),size=(30,20)) #时间 分
        self.__TextBox02 = text_input02 
        text_input03 = TextCtrl(self.panel,-1,pos=(170,40),size=(25,20)) #时间 秒
        self.__TextBox03 = text_input03 
        text_input04 = TextCtrl(self.panel,-1,pos=(215,40),size=(30,20)) #时间 百分秒
        self.__TextBox04 = text_input04

        text_input1 = TextCtrl(self.panel,-1,pos=(60,80),size=(60,20)) #距离
        self.__TextBox1 = text_input1
        text_input2 = TextCtrl(self.panel,-1,pos=(60,120),size=(25,20)) #配速 分
        self.__TextBox2 = text_input2
        text_input3 = TextCtrl(self.panel,-1,pos=(110,120),size=(25,20)) #配速 秒
        self.__TextBox3 = text_input3
        text_input4 = TextCtrl(self.panel,-1,pos=(160,120),size=(25,20)) #配速 秒
        self.__TextBox4 = text_input4

        text_input5 = TextCtrl(self.panel,-1,pos=(60,160),size=(50,20)) #单圈 秒，自动计算产生。
        self.__TextBox5 = text_input5

        self.button1 = Button(self.panel,-1,"计算",pos=(20,200),size=(70,20))
        self.button2 = Button(self.panel,-1,"重置",pos=(100,200),size=(70,20))
        
        self.button1.Bind(EVT_BUTTON,self.run_file)
        self.button2.Bind(EVT_BUTTON,self.clear_data)

        # StaticText(self.panel,-1,"Version: 2.0",pos=(900,630))
        # StaticText(self.panel,-1,"By: Xu.T",pos=(900,650))

        self.InitUI() 

    def run_file(self,event): 
        flag_time = True
        flag_distance = True
        flag_pace = True
        flag_lap = True

        #时间：
        hour = self.__TextBox01.GetValue()
        minute = self.__TextBox02.GetValue()
        second = self.__TextBox03.GetValue()
        minisecond = self.__TextBox04.GetValue()
        if not hour:
            hour = 0
        if not minute:
            minute = 0
        if not second:
            second = 0
        if not minisecond:
            minisecond = 0

        #距离：
        distance = self.__TextBox1.GetValue()
        if not distance:
            distance = 0
        
        #配速,要输入分秒，百分秒可以不输入，默认0
        pace_minute = self.__TextBox2.GetValue()
        pace_second = self.__TextBox3.GetValue()
        pace_minisecond = self.__TextBox4.GetValue() #百分秒
        if not pace_minute:
            pace_minute = 0
        if not pace_second:
            pace_second = 0
        if not pace_minisecond:
            pace_minisecond = 0
                
        #单圈：
        pace_lap = self.__TextBox5.GetValue()
        if not pace_lap:
            pace_lap = 0

        #判断输入了那两项：
        if (not self.__TextBox01.GetValue()) and (not self.__TextBox02.GetValue()) and (not self.__TextBox03.GetValue()): #没有输入时间
            flag_time = False
        if not self.__TextBox1.GetValue() :
            flag_distance = False
        if (not self.__TextBox2.GetValue()) and (not self.__TextBox3.GetValue()) and (not self.__TextBox4.GetValue()):
            flag_pace = False
        if not self.__TextBox5.GetValue():
            flag_lap = False
        # print(flag_time,flag_distance,flag_pace,flag_lap)
        #判断时间 时分秒 输入正确与否，不输入默认为0
        try:
            time_total = int(hour)*3600 + int(minute)*60 + int(second) + int(minisecond)/100
            # print("总时间:%s"%(time_total))
            time_pace = int(pace_minute)*60 + int(pace_second) + int(pace_minisecond)/100 #配速
            pace_km = float(pace_lap)*2.5
        except Exception as e:
            # print(e)
            string="请输入正确时间！"
            dial=MessageDialog(None,string)
            dial.ShowModal()
        
        if (not flag_time ) and (not flag_distance) and (not flag_pace) and (not flag_lap): #无输入
            string="请输入其中两项数据！"
            dial=MessageDialog(None,string)
            dial.ShowModal()

        if int(flag_distance) + int(flag_lap) +int(flag_pace) + int(flag_time) == 1: #只输入一个数据
            string="至少输入其中两项数据！"
            dial=MessageDialog(None,string)
            dial.ShowModal()

        if int(flag_distance) + int(flag_lap) +int(flag_pace) + int(flag_time) == 3: #输入3个数据
            string="输入三项数据，错误！"
            dial=MessageDialog(None,string)
            dial.ShowModal()

        if int(flag_lap) + int(flag_pace) == 2: #同时输入配速和圈速
            string="配速和圈速不能同时输入！"
            dial=MessageDialog(None,string)
            dial.ShowModal()

        if flag_time and flag_distance and flag_pace and flag_lap: #四项全部输入
            string="不能同时输入四项数据！"
            dial=MessageDialog(None,string)
            dial.ShowModal()

        if flag_time and flag_distance: #根据时间和距离 计算配速和圈速
            pace_tmp = float(time_total/float(distance))
            pace_m = int(pace_tmp/60)
            pace_s = int(pace_tmp%60)
            pace_mi = int((pace_tmp - pace_m*60 - pace_s)*100)
            pace_lap_tmp =int((float(time_total*0.4/float(distance)))*100)/100
            # print(pace_tmp ,pace_lap_tmp, float(time_total*0.4/float(distance)), (float(time_total*0.4/float(distance)))*100/100)
            self.__TextBox2.AppendText(str(pace_m))
            self.__TextBox3.AppendText(str(pace_s))
            self.__TextBox4.AppendText(str(pace_mi))
            self.__TextBox5.AppendText(str(pace_lap_tmp))#计算单圈圈速：

        elif flag_time and flag_pace: #根据时间和配速计算距离和圈速
            distance_tmp = int((time_total/time_pace)*100)/100 
            lap_time = int((time_pace /2.5)*100)/100
            self.__TextBox1.AppendText(str(distance_tmp)) #填充距离
            self.__TextBox5.AppendText(str(lap_time)) #填充圈速

        elif flag_distance and flag_pace: #根据距离和配速计算时间和圈速
            time_tmp = time_pace*float(distance)
            # print(time_tmp)
            hour_tmp = int(time_tmp/3600)
            minute_tmp = int((time_tmp-hour_tmp*3600)/60)
            second_tmp = int((time_tmp-hour_tmp*3600-minute_tmp*60)%60)
            minisecond = int((time_tmp - hour_tmp*3600 - minute_tmp*60 - second_tmp)*100) #白分秒
            # print(time_tmp - hour_tmp*3600 - minute_tmp*60 - second_tmp, minisecond)
            lap_time = int((time_pace /2.5)*100)/100
            self.__TextBox01.AppendText(str(hour_tmp))
            self.__TextBox02.AppendText(str(minute_tmp))
            self.__TextBox03.AppendText(str(second_tmp))
            self.__TextBox04.AppendText(str(minisecond))
            self.__TextBox5.AppendText(str(lap_time)) #填充圈速

        elif flag_time and flag_lap: #根据时间和圈速计算距离和配速
            distance_tmp = int((time_total/pace_km)*100)/100 
            pace_m = int(pace_km/60)
            pace_s = int(pace_km%60)
            pace_mi = int((pace_km - pace_m*60 - pace_s)*100)
            self.__TextBox1.AppendText(str(distance_tmp)) #填充距离
            self.__TextBox2.AppendText(str(pace_m))
            self.__TextBox3.AppendText(str(pace_s))
            self.__TextBox4.AppendText(str(pace_mi))

        elif flag_distance and flag_lap: #根据距离和圈速计算时间和配速
            time_tmp = pace_km*float(distance)
            hour_tmp = int(time_tmp/3600)
            minute_tmp = int((time_tmp-hour_tmp*3600)/60)
            second_tmp = int((time_tmp-hour_tmp*3600-minute_tmp*60)%60)
            minisecond = int((time_tmp - hour_tmp*3600 - minute_tmp*60 - second_tmp)*100) #白分秒
            pace_m = int(pace_km/60)
            pace_s = int(pace_km%60)
            pace_mi = int((pace_km - pace_m*60 - pace_s)*100)
            self.__TextBox01.AppendText(str(hour_tmp))
            self.__TextBox02.AppendText(str(minute_tmp))
            self.__TextBox03.AppendText(str(second_tmp))
            self.__TextBox04.AppendText(str(minisecond))
            self.__TextBox2.AppendText(str(pace_m))
            self.__TextBox3.AppendText(str(pace_s))
            self.__TextBox4.AppendText(str(pace_mi))

    def clear_data(self, event):
        self.__TextBox01.Clear()    
        self.__TextBox02.Clear()
        self.__TextBox03.Clear()
        self.__TextBox04.Clear()
        self.__TextBox1.Clear()
        self.__TextBox2.Clear()    
        self.__TextBox3.Clear()
        self.__TextBox4.Clear()
        self.__TextBox5.Clear()
        

    def InitUI(self):    #自定义的函数,完成菜单的设置  
        menubar = MenuBar()        #生成菜单栏  
        filemenu = Menu()        #生成一个菜单  
        qmi1 = MenuItem(filemenu,1, "help")     #生成一个help菜单项  
        qmi2 = MenuItem(filemenu,2, "Quit")  #quit项，id设为2，在bind中调用
        filemenu.AppendItem(qmi1)            #把菜单项加入到菜单中  
        filemenu.AppendItem(qmi2)  
        menubar.Append(filemenu, "&File")        #把菜单加入到菜单栏中  
        self.SetMenuBar(menubar)            #把菜单栏加入到Frame框架中  
        self.Bind(EVT_MENU, self.OnQuit, id=2)    #给菜单项加入事件处理，id=2  
        self.Bind(EVT_MENU, self.help_window, id=1)  #help窗口
        self.Show(True)        #显示框架  

    def OnQuit(self, e):    #自定义函数　响应菜单项　　  
        self.Close()

    def help_window(self,event): #定义help窗口
        dial = MessageDialog(None,"何老师专用！",pos=(10,10)) #测试用
        dial.ShowModal()

if __name__ == "__main__":
    app = App()    #创建应用的对象
    myframe = MyFrame()    #创建一个自定义出来的窗口
    myframe.Show()    #这两句一定要在MainLoop开始之前就执行    
    app.MainLoop()