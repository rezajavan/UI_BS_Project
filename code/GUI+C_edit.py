import struct
import os
import time
import math
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk

import view
from ctypes import *
import shutil
import os

on_srs = False

root = Tk()
root.title('Input for LTE signal')
root.geometry('1500x300')
#define variable
padx = 3
pady = 5
width_btn = 30
width_Entry = 10

#scrol
main_frame = Frame(root)
main_frame.pack(fill=BOTH,expand=1)

canvas = Canvas(main_frame,bg='gray25')
canvas.pack(fill=BOTH,side=LEFT,expand=1)

scr_x = ttk.Scrollbar(main_frame,orient = HORIZONTAL,command = canvas.xview)
scr_y = ttk.Scrollbar(main_frame,orient = VERTICAL,command = canvas.yview)
scr_x.pack(side= BOTTOM,fill=X)
scr_y.pack(side=RIGHT,fill=Y)


canvas.configure(yscrollcommand = scr_y.set,xscrollcommand = scr_x.set)

canvas.bind('<Configure>', lambda e:canvas.configure(scrollregion = canvas.bbox("all") ))

frame_in_canvas = Frame(canvas,bg = 'LightSkyBlue4')

canvas.create_window((0,0),window=frame_in_canvas)


Change_CFO = True
Change_TFO = True
Change_IQ = True
Change_PN = True
Change_Doppler = True
Change_IIP3 = True
Change_multipath = True




v_CFO_carrier = StringVar()
v_TFO_delay = StringVar()
v_TFO_SamplingRate = StringVar()
v_IQ_Ampitude = StringVar()
v_IQ_Phase = StringVar()
v_PN_Var = StringVar()
v_PN_offset = StringVar()
v_PN_SamplingRate = StringVar()
v_multipath = StringVar()
v_mul_SamplingRate = StringVar()
v_Doppler = StringVar()
v_IIP3_0 = StringVar()
v_IIP3_1 = StringVar()
v_IIP3_2 = StringVar()
v_IIP3_3 = StringVar()

#define var_mul_delay
var_mul_custom_delay0 = StringVar()
var_mul_custom_delay1 = StringVar()
var_mul_custom_delay2 = StringVar()
var_mul_custom_delay3 = StringVar()
var_mul_custom_delay4 = StringVar()
var_mul_custom_delay5 = StringVar()
var_mul_custom_delay6 = StringVar()
#and set

#define var_mul_gain_A
var_mul_custom_gainA0 = StringVar()
var_mul_custom_gainA1 = StringVar()
var_mul_custom_gainA2 = StringVar()
var_mul_custom_gainA3 = StringVar()
var_mul_custom_gainA4 = StringVar()
var_mul_custom_gainA5 = StringVar()
var_mul_custom_gainA6 = StringVar()
#define var_mul_gain_P
var_mul_custom_gainP0 = StringVar()
var_mul_custom_gainP1 = StringVar()
var_mul_custom_gainP2 = StringVar()
var_mul_custom_gainP3 = StringVar()
var_mul_custom_gainP4 = StringVar()
var_mul_custom_gainP5 = StringVar()
var_mul_custom_gainP6 = StringVar()
v_fx = StringVar()
def set_default_variable():
    v_mul_SamplingRate.set('0')
    v_multipath.set('Custom')
    v_CFO_carrier.set('0')
    v_TFO_delay.set('0')
    if (on_srs):
        v_TFO_SamplingRate.set('7.68')
    else:
        v_TFO_SamplingRate.set('0')

    v_IQ_Ampitude.set('0')
    v_IQ_Phase.set('0')
    v_PN_Var.set('0')
    v_PN_offset.set('10')
    v_PN_SamplingRate.set('0')
    v_Doppler.set('0')
    v_IIP3_0.set('0')
    v_IIP3_1.set('0')
    v_IIP3_2.set('1')
    v_IIP3_3.set('0')
    v_fx.set('900')
    #set mul_delay
    var_mul_custom_delay0.set('0')
    var_mul_custom_delay1.set('0')
    var_mul_custom_delay2.set('0')
    var_mul_custom_delay3.set('0')
    var_mul_custom_delay4.set('0')
    var_mul_custom_delay5.set('0')
    var_mul_custom_delay6.set('0')
    #set mul_gain_A
    var_mul_custom_gainA0.set('0')
    var_mul_custom_gainA1.set('0')
    var_mul_custom_gainA2.set('0')
    var_mul_custom_gainA3.set('0')
    var_mul_custom_gainA4.set('0')
    var_mul_custom_gainA5.set('0')
    var_mul_custom_gainA6.set('0')
    #set mul_gain_P
    var_mul_custom_gainP0.set('0')
    var_mul_custom_gainP1.set('0')
    var_mul_custom_gainP2.set('0')
    var_mul_custom_gainP3.set('0')
    var_mul_custom_gainP4.set('0')
    var_mul_custom_gainP5.set('0')
    var_mul_custom_gainP6.set('0')




set_default_variable()


def reset_Chage_state():
    global Change_TFO
    global Change_CFO
    global Change_IQ
    global Change_IIP3
    global Change_PN
    global Change_multipath
    global Change_Doppler

    Change_CFO = False
    Change_TFO = False
    Change_IQ = False
    Change_PN = False
    Change_Doppler = False
    Change_IIP3 = False
    Change_multipath = False











#create Frame
frame_btn = LabelFrame(frame_in_canvas,padx=padx,pady=pady,text="")

#frame_btn.grid(row=0,column=0,padx=padx,pady=pady)
#frame_btn.pack(side='top',anchor=NW,padx=padx,pady=pady)
padx_frame = padx
pady_frame = pady

padx_b_frame = 4*padx
pady_b_frame = 3*pady
width_frame = 1500
height_mul = 210
height_other = 120
frame_1 = LabelFrame(frame_in_canvas,padx=padx,pady=pady,text="",width=width_frame,height = height_other,bg='SkyBlue1')
frame_2 = LabelFrame(frame_in_canvas,padx=padx,pady=pady,text="",width=width_frame,height = height_mul,bg='SkyBlue2' )
frame_3 = LabelFrame(frame_in_canvas,padx=padx,pady=pady,text="",width=width_frame,height = height_other + 10,bg='SkyBlue3')
frame_4 = LabelFrame(frame_in_canvas,padx=padx,pady=pady,text="",width=width_frame,height = height_other,bg='SkyBlue4')
frame_5 = LabelFrame(frame_in_canvas,padx=padx,pady=pady,text="",width=width_frame,height = height_other + 30,bg='LightSkyBlue1')
frame_btn = LabelFrame(frame_in_canvas,padx=padx,pady=pady,text="",width=width_frame,height=height_mul)
frame_7 = LabelFrame(frame_in_canvas,padx=padx,pady=pady,text="",width=width_frame,height=height_other-20,bg='SkyBlue4')

frame_mul = LabelFrame(frame_2,padx=padx_frame,pady=pady_frame,text='Multipath.')
frame_SamplingRate = LabelFrame(frame_1,padx=padx_frame,pady=pady_frame,text='Sampling Rate.')
frame_CFO = LabelFrame(frame_4,padx=padx_frame,pady=pady_frame,text='Carrier Frequency offset.')
frame_TFO = LabelFrame(frame_5,padx=padx_frame,pady=pady_frame,text='Time Frequency offset.')
frame_IQ = LabelFrame(frame_3,padx=padx_frame,pady=pady_frame,text='IQ imbalance.')
frame_PN = LabelFrame(frame_3,padx=padx_frame,pady=pady_frame,text='Phase Noise.')
frame_IP3 = LabelFrame(frame_5,padx=padx_frame,pady=pady_frame,text='IIP3.')
frame_Doppler = LabelFrame(frame_4,padx=padx_frame,pady=pady_frame,text='Doppler Frequency.')
frame_btn_send = LabelFrame(frame_7,padx=padx_frame,pady=pady_frame,text='Send.')
#pack main_frames
# frame_1.pack(anchor=NW)
# frame_mul.pack(anchor=NW)

#grid main_frames
frame_1.grid(row=0,column=0,sticky=NW,padx=0,pady=0)
frame_2.grid(row=1,column=0,sticky=NW,padx=0,pady=0)
frame_3.grid(row=2,column=0,sticky=NW,padx=0,pady=0)
frame_4.grid(row=3,column=0,sticky=NW,padx=0,pady=0)
frame_5.grid(row=4,column=0,sticky=NW,padx=0,pady=0)
frame_btn.grid(row=5,column=0,sticky=NW,padx=0,pady=0)
frame_7.grid(row=6,column=0,padx=0,pady=0)


frame_1.grid_propagate(False)
frame_2.grid_propagate(False)
frame_3.grid_propagate(False)
frame_4.grid_propagate(False)
frame_5.grid_propagate(False)
frame_btn.grid_propagate(False)
frame_7.grid_propagate(False)

#place main_frames
# frame_1.place(x=5,y=5,anchor=NW)
# frame_2.place(x=15,y=5,anchor=NW)


#define row and column
rs = 0
cs = 0
rmul = 0
cmul = 0
rTFO = 0
cTFO = 0
rIQ = 0
cIQ = 1
rPN = 0
cPN = 0
rCFO = 0
cCFO = 1
rIP3 = 0
cIP3 = 1
rDop = 0
cDop = 0
rsend = 0
csend = 0
width = 10
#frame_Entry.grid(row=0,column=1,padx=padx,pady=pady)
#frame_Entry.pack(side='right',anchor=NE,padx=padx,pady=pady)

frame_SamplingRate.grid(row=rs,column = cs,padx=padx_b_frame,pady=pady_b_frame,sticky = NW)
frame_mul.grid(row=rmul,column = cmul,padx=padx_b_frame,pady=pady_b_frame,sticky = NW)
frame_TFO.grid(row=rTFO,column = cTFO,padx=padx_b_frame,pady=pady_b_frame,sticky = NW)
frame_CFO.grid(row=rCFO,column = cCFO,padx=padx_b_frame,pady=pady_b_frame,sticky = NW)
frame_IQ.grid(row=rIQ,column = cIQ,padx=padx_b_frame,pady=pady_b_frame,sticky = NW)
frame_PN.grid(row=rPN,column = cPN,padx=padx_b_frame,pady=pady_b_frame,sticky = NW)
frame_IP3.grid(row=rIP3,column = cIP3,padx=padx_b_frame,pady=pady_b_frame,sticky = NW)
frame_Doppler.grid(row=rDop,column = cDop,padx=padx_b_frame,pady=pady_b_frame,sticky = NW)
frame_btn_send.grid(row=rsend,column = csend,padx=padx_b_frame,pady=pady_b_frame,sticky = NW)

# frame_mul.pack(anchor=N,padx=padx_b_frame,pady=pady_b_frame)
# frame_SamplingRate.pack(anchor=NW,padx=padx_b_frame,pady=pady_b_frame)
# frame_TFO.pack(anchor=NW,padx=padx_b_frame,pady=pady_b_frame)
# frame_PN.pack(anchor=NW,padx=padx_b_frame,pady=pady_b_frame)
# frame_IP3.pack(anchor=NW,padx=padx_b_frame,pady=pady_b_frame)
# frame_IQ.pack(anchor=NW,padx=padx_b_frame,pady=pady_b_frame)
# frame_CFO.pack(anchor=NW,padx=padx_b_frame,pady=pady_b_frame)
# frame_Doppler.pack(anchor=NW,padx=padx_b_frame,pady=pady_b_frame)



#create btn
btn_show_result_multipath = Button(frame_mul,text = "Show result",relief = "solid",font = "Time 8",width = width_btn,bg='white')
btn_send = Button(frame_btn_send,text = "send",relief = "solid",font = "Time 8",width = width_btn,bg='yellow')



#create label
l_CFO = Label(frame_CFO,text='Enter ratio (default=0) ',relief = 'solid',bg='grey',justify='center',font = "Time 11",width=4*width_Entry,fg='white')
l_TFO_delay = Label(frame_TFO,text='Enter time delay(micro second)(default=0) ',relief = 'solid',bg='grey',justify='center',font = "Time 11",width=4*width_Entry,fg='white')
l_TFO_SamplingRate = Label(frame_SamplingRate,text='Enter SamplingRate (MHz)(default=0) ',relief = 'solid',bg='grey',justify='center',font = "Time 11",width=4*width_Entry,fg='white')
l_IQ_Amplitude = Label(frame_IQ,text='Enter Amplitude(dB) (default=0) ',relief = 'solid',bg='grey',justify='center',font = "Time 11",width=4*width_Entry,fg='white')
l_IQ_Phase = Label(frame_IQ,text='Enter Phase imbalance (degree) (default=0) ',relief = 'solid',bg='grey',justify='center',font = "Time 11",width=4*width_Entry,fg='white')
l_PN_var = Label(frame_PN,text='Enter variance of noise (dB) (default=0) ',relief = 'solid',bg='grey',justify='center',font = "Time 11",width=4*width_Entry,fg='white')
l_PN_offset = Label(frame_PN,text='Enter offset of noise(default=10 Hz) ',relief = 'solid',bg='grey',justify='center',font = "Time 11",width=4*width_Entry,fg='white')
#l_PN_SamplingRate = Label(frame_Entry,text='Enter SamplingRate (MHz) (default=0 Hz) ',relief = 'solid',bg='grey',justify='center',font = "Time 9",width=4*width_Entry,fg='white')
l_mul_delay = Label(frame_mul,text='  ',relief = 'solid',bg='grey',justify='center',font = "Time 11",width=4*width_Entry,fg='white')
l_mul_gain_P = Label(frame_mul,text='  ',relief = 'solid',bg='grey',justify='center',font = "Time 11",width=4*width_Entry,fg='white')
l_mul_gain_A = Label(frame_mul,text='  ',relief = 'solid',bg='grey',justify='center',font = "Time 11",width=6*width_Entry,fg='white')
l_mul_for_gain_P= Label(frame_mul,text='please enter Phase gain: ',relief = 'solid',bg='grey',justify='center',font = "Time 11",width=4*width_Entry,fg='white')
l_mul_for_gain_A = Label(frame_mul,text='Amplitude gain(dB)',relief = 'solid',bg='grey',justify='center',font = "Time 11",width=4*width_Entry,fg='white')
l_mul_for_delay = Label(frame_mul,text='tab delay (Discrete) : ',relief = 'solid',bg='grey',justify='center',font = "Time 11",width=4*width_Entry,fg='white')
#l_mul_samplingrate = Label(frame_mul,text='Enter SamplingRate (MHz)(default=0) ',relief = 'solid',bg='grey',justify='center',font = "Time 9",width=4*width_Entry,fg='white')
l_Doppler = Label(frame_Doppler,text='Enter ratio doppler frequency: ',relief = 'solid',bg='grey',justify='center',font = "Time 11",width=4*width_Entry,fg='white')
l_IIP3 = Label(frame_IP3,text='Enter IIP3 vector: ',relief = 'solid',bg='grey',justify='center',font = "Time 11",width=4*width_Entry,fg='white')

l_fx = Label(frame_btn_send,text='Carrier Frequency (MHz) : ',relief = 'solid',bg='grey',justify='center',font = "Time 11",width=4*width_Entry,fg='white')
#create Entry
e_CFO_carrier = Entry(frame_CFO,textvariable=v_CFO_carrier,relief = 'solid',width =width_Entry,selectbackground = 'grey',justify='center',selectforeground = 'red')
e_TFO_delay = Entry(frame_TFO,textvariable=v_TFO_delay,relief = 'solid',width = width_Entry,selectbackground = 'grey',justify='center',selectforeground = 'red')
e_TFO_SamplingRate = Entry(frame_SamplingRate,textvariable=v_TFO_SamplingRate,relief = 'solid',width = width_Entry,selectbackground = 'grey',justify='center',selectforeground = 'red')
e_IQ_Amplitude = Entry(frame_IQ,textvariable=v_IQ_Ampitude,relief = 'solid',width = width_Entry,selectbackground = 'grey',justify='center',selectforeground = 'red')
e_IQ_Phase = Entry(frame_IQ,textvariable=v_IQ_Phase,relief = 'solid',width = width_Entry,selectbackground = 'grey',justify='center',selectforeground = 'red')
e_PN_var = Entry(frame_PN,textvariable=v_PN_Var,relief = 'solid',width = width_Entry,selectbackground = 'grey',justify='center',selectforeground = 'red')
e_PN_ofsset = Entry(frame_PN,textvariable=v_PN_offset,relief = 'solid',width = width_Entry,selectbackground = 'grey',justify='center',selectforeground = 'red')
e_PN_SamplinRate = Entry(frame_PN,textvariable=v_PN_SamplingRate,relief = 'solid',width = width_Entry,selectbackground = 'grey',justify='center',selectforeground = 'red')
e_mul_SamplingRte = Entry(frame_mul,textvariable=v_mul_SamplingRate,relief = 'solid',width = width_Entry,selectbackground = 'grey',justify='center',selectforeground = 'red')
e_Doppler = Entry(frame_Doppler,textvariable=v_Doppler,relief = 'solid',width = width_Entry,selectbackground = 'grey',justify='center',selectforeground = 'red')
e_IIP3_0 = Entry(frame_IP3,textvariable=v_IIP3_0,relief = 'solid',width = width_Entry,selectbackground = 'grey',justify='center',selectforeground = 'red')
e_IIP3_1 = Entry(frame_IP3,textvariable=v_IIP3_1,relief = 'solid',width = width_Entry,selectbackground = 'grey',justify='center',selectforeground = 'red')
e_IIP3_2 = Entry(frame_IP3,textvariable=v_IIP3_2,relief = 'solid',width = width_Entry,selectbackground = 'grey',justify='center',selectforeground = 'red')
e_IIP3_3 = Entry(frame_IP3,textvariable=v_IIP3_3,relief = 'solid',width = width_Entry,selectbackground = 'grey',justify='center',selectforeground = 'red')

e_fx = Entry(frame_btn_send,textvariable=v_fx,relief = 'solid',width = width_Entry,selectbackground = 'grey',justify='center',selectforeground = 'red')
#enrty multipath delay
e_mul_custom_delay0 = Entry(frame_mul,textvariable=var_mul_custom_delay0,relief = 'solid',width = width_Entry,selectbackground = 'grey',justify='center',selectforeground = 'red')
e_mul_custom_delay1 = Entry(frame_mul,textvariable=var_mul_custom_delay1,relief = 'solid',width = width_Entry,selectbackground = 'grey',justify='center',selectforeground = 'red')
e_mul_custom_delay2 = Entry(frame_mul,textvariable=var_mul_custom_delay2,relief = 'solid',width = width_Entry,selectbackground = 'grey',justify='center',selectforeground = 'red')
e_mul_custom_delay3 = Entry(frame_mul,textvariable=var_mul_custom_delay3,relief = 'solid',width = width_Entry,selectbackground = 'grey',justify='center',selectforeground = 'red')
e_mul_custom_delay4 = Entry(frame_mul,textvariable=var_mul_custom_delay4,relief = 'solid',width = width_Entry,selectbackground = 'grey',justify='center',selectforeground = 'red')
e_mul_custom_delay5 = Entry(frame_mul,textvariable=var_mul_custom_delay5,relief = 'solid',width = width_Entry,selectbackground = 'grey',justify='center',selectforeground = 'red')
e_mul_custom_delay6 = Entry(frame_mul,textvariable=var_mul_custom_delay6,relief = 'solid',width = width_Entry,selectbackground = 'grey',justify='center',selectforeground = 'red')
#enrty multipath gain_A
e_mul_custom_gainA0 = Entry(frame_mul,textvariable=var_mul_custom_gainA0,relief = 'solid',width = width_Entry,selectbackground = 'grey',justify='center',selectforeground = 'red')
e_mul_custom_gainA1 = Entry(frame_mul,textvariable=var_mul_custom_gainA1,relief = 'solid',width = width_Entry,selectbackground = 'grey',justify='center',selectforeground = 'red')
e_mul_custom_gainA2 = Entry(frame_mul,textvariable=var_mul_custom_gainA2,relief = 'solid',width = width_Entry,selectbackground = 'grey',justify='center',selectforeground = 'red')
e_mul_custom_gainA3 = Entry(frame_mul,textvariable=var_mul_custom_gainA3,relief = 'solid',width = width_Entry,selectbackground = 'grey',justify='center',selectforeground = 'red')
e_mul_custom_gainA4 = Entry(frame_mul,textvariable=var_mul_custom_gainA4,relief = 'solid',width = width_Entry,selectbackground = 'grey',justify='center',selectforeground = 'red')
e_mul_custom_gainA5 = Entry(frame_mul,textvariable=var_mul_custom_gainA5,relief = 'solid',width = width_Entry,selectbackground = 'grey',justify='center',selectforeground = 'red')
e_mul_custom_gainA6 = Entry(frame_mul,textvariable=var_mul_custom_gainA6,relief = 'solid',width = width_Entry,selectbackground = 'grey',justify='center',selectforeground = 'red')
#enrty multipath gain_P
e_mul_custom_gainP0 = Entry(frame_mul,textvariable=var_mul_custom_gainP0,relief = 'solid',width = width_Entry,selectbackground = 'grey',justify='center',selectforeground = 'red')
e_mul_custom_gainP1 = Entry(frame_mul,textvariable=var_mul_custom_gainP1,relief = 'solid',width = width_Entry,selectbackground = 'grey',justify='center',selectforeground = 'red')
e_mul_custom_gainP2 = Entry(frame_mul,textvariable=var_mul_custom_gainP2,relief = 'solid',width = width_Entry,selectbackground = 'grey',justify='center',selectforeground = 'red')
e_mul_custom_gainP3 = Entry(frame_mul,textvariable=var_mul_custom_gainP3,relief = 'solid',width = width_Entry,selectbackground = 'grey',justify='center',selectforeground = 'red')
e_mul_custom_gainP4 = Entry(frame_mul,textvariable=var_mul_custom_gainP4,relief = 'solid',width = width_Entry,selectbackground = 'grey',justify='center',selectforeground = 'red')
e_mul_custom_gainP5 = Entry(frame_mul,textvariable=var_mul_custom_gainP5,relief = 'solid',width = width_Entry,selectbackground = 'grey',justify='center',selectforeground = 'red')
e_mul_custom_gainP6 = Entry(frame_mul,textvariable=var_mul_custom_gainP6,relief = 'solid',width = width_Entry,selectbackground = 'grey',justify='center',selectforeground = 'red')

#create multipath menu
list_multipath = {"EPA","EVA","ETU","Custom","Choose multipath model (default = off)"}
menu_multipath = OptionMenu(frame_mul,v_multipath,*list_multipath)
menu_multipath.config(relief = "raised",font = "Time 8",width = width_btn,bg='white')




def grid_mul_custom():
    #grid mul_delay
    e_mul_custom_delay0.grid(row=1,column=2,padx=padx,pady=pady)
    e_mul_custom_delay1.grid(row=1, column=3, padx=padx, pady=pady)
    e_mul_custom_delay2.grid(row=1, column=4, padx=padx, pady=pady)
    e_mul_custom_delay3.grid(row=1, column=5, padx=padx, pady=pady)
    e_mul_custom_delay4.grid(row=1, column=6, padx=padx, pady=pady)
    e_mul_custom_delay5.grid(row=1, column=7, padx=padx, pady=pady)
    e_mul_custom_delay6.grid(row=1, column=8, padx=padx, pady=pady)
    #grid mul_gain_A
    e_mul_custom_gainA0.grid(row=2,column=2,padx=padx,pady=pady)
    e_mul_custom_gainA1.grid(row=2, column=3, padx=padx, pady=pady)
    e_mul_custom_gainA2.grid(row=2, column=4, padx=padx, pady=pady)
    e_mul_custom_gainA3.grid(row=2, column=5, padx=padx, pady=pady)
    e_mul_custom_gainA4.grid(row=2, column=6, padx=padx, pady=pady)
    e_mul_custom_gainA5.grid(row=2, column=7, padx=padx, pady=pady)
    e_mul_custom_gainA6.grid(row=2, column=8, padx=padx, pady=pady)
    # grid mul_gain_Phase
    e_mul_custom_gainP0.grid(row=3,column=2,padx=padx,pady=pady)
    e_mul_custom_gainP1.grid(row=3, column=3, padx=padx, pady=pady)
    e_mul_custom_gainP2.grid(row=3, column=4, padx=padx, pady=pady)
    e_mul_custom_gainP3.grid(row=3, column=5, padx=padx, pady=pady)
    e_mul_custom_gainP4.grid(row=3, column=6, padx=padx, pady=pady)
    e_mul_custom_gainP5.grid(row=3, column=7, padx=padx, pady=pady)
    e_mul_custom_gainP6.grid(row=3, column=8, padx=padx, pady=pady)

def kill_mul_custom():
    #remove delay
    e_mul_custom_delay0.grid_remove()
    e_mul_custom_delay1.grid_remove()
    e_mul_custom_delay2.grid_remove()
    e_mul_custom_delay3.grid_remove()
    e_mul_custom_delay4.grid_remove()
    e_mul_custom_delay5.grid_remove()
    e_mul_custom_delay6.grid_remove()
    #remove gain_A
    e_mul_custom_gainA0.grid_remove()
    e_mul_custom_gainA1.grid_remove()
    e_mul_custom_gainA2.grid_remove()
    e_mul_custom_gainA3.grid_remove()
    e_mul_custom_gainA4.grid_remove()
    e_mul_custom_gainA5.grid_remove()
    e_mul_custom_gainA6.grid_remove()
    #remove gain_Phase
    e_mul_custom_gainP0.grid_remove()
    e_mul_custom_gainP1.grid_remove()
    e_mul_custom_gainP2.grid_remove()
    e_mul_custom_gainP3.grid_remove()
    e_mul_custom_gainP4.grid_remove()
    e_mul_custom_gainP5.grid_remove()
    e_mul_custom_gainP6.grid_remove()


#help
l_help_CFO = Label(frame_CFO,text="""ratio is offset frequency/sampling rate""",fg='black')
l_help_Doppler = Label(frame_Doppler,text="""ratio is Doppler/sampling_rate""",fg='black')



l_help_IP3 = Label(frame_IP3, text="""from left to right [p3,p2,p1,p0]
y = p3*(x^3) + p2*x(^2) + p3*(x^1) + p4*(x^0)""",fg='black')


#grid
#
l_mul_for_delay.grid(row=1, column=1, pady=pady, padx=padx)
l_mul_for_gain_A.grid(row=2, column=1, pady=pady, padx=padx)
btn_show_result_multipath.grid(row=3, column=2, pady=pady, padx=padx)
menu_multipath.grid(row=0, column=0, padx=padx, pady=2 * pady)
#
l_IIP3.grid(row=0, column=0, padx=padx, pady=pady)
e_IIP3_0.grid(row=0, column=1, padx=padx, pady=pady)
e_IIP3_1.grid(row=0, column=2, padx=padx, pady=pady)
e_IIP3_2.grid(row=0, column=3, padx=padx, pady=pady)
e_IIP3_3.grid(row=0, column=4, padx=padx, pady=pady)
l_help_IP3.grid(row=1, column=0, padx=padx, pady=pady)
#
l_Doppler.grid(row=0, column=0, padx=padx, pady=pady)
e_Doppler.grid(row=0, column=1, padx=padx, pady=pady)
l_help_Doppler.grid(row=1, column=0, padx=padx, pady=pady)
#
l_PN_var.grid(row=0, column=0, padx=padx, pady=pady)
l_PN_offset.grid(row=1, column=0, padx=padx, pady=pady)
#l_PN_SamplingRate.grid(row=2, column=0, padx=padx, pady=pady)

e_PN_var.grid(row=0, column=1, pady=pady, padx=padx)
e_PN_ofsset.grid(row=1, column=1, pady=pady, padx=padx)
#e_PN_SamplinRate.grid(row=2, column=1, pady=pady, padx=padx)
#
l_IQ_Amplitude.grid(row=0, column=0, padx=padx, pady=pady)
l_IQ_Phase.grid(row=1, column=0, padx=padx, pady=pady)

e_IQ_Amplitude.grid(row=0, column=1, pady=pady, padx=padx)
e_IQ_Phase.grid(row=1, column=1, pady=pady, padx=padx)
#
l_TFO_delay.grid(row=0, column=0, padx=padx, pady=pady)
l_TFO_SamplingRate.grid(row=1, column=0, padx=padx, pady=pady)

e_TFO_delay.grid(row=0, column=1, pady=pady, padx=padx)
e_TFO_SamplingRate.grid(row=1, column=1, pady=pady, padx=padx)
#
l_CFO.grid(row=0, column=0, padx=padx, pady=pady)
e_CFO_carrier.grid(row=0, column=1, pady=pady, padx=padx)
l_help_CFO.grid(row=1, column=0, padx=padx, pady=pady)



l_fx.grid(row=0, column=0, padx=padx, pady=pady)
e_fx.grid(row=0, column=1, padx=padx, pady=pady)
btn_send.grid(row=0, column=2, padx=padx, pady=pady)
def command_custom_multipath(*args):
    menu_multipath.config(bg='white')
    if (v_multipath.get() == 'Custom'):
        btn_show_result_multipath.grid_remove()
        l_mul_delay.grid_remove()
        l_mul_gain_A.grid_remove()
        l_mul_gain_P.grid_remove()
        grid_mul_custom()
        l_mul_for_delay.config(text = "please enter time delay (micro second): ")
        l_mul_for_gain_A.config(text = "please enter Amplitude gain(dB): ")
        l_mul_for_gain_P.grid(row=3, column=1, pady=pady, padx=padx)
        menu_multipath.config(bg='white')
    else:
        if (v_multipath.get() != 'Choose multipath model (default = off)'):
            kill_mul_custom()
            l_mul_delay.grid_remove()
            l_mul_gain_A.grid_remove()
            l_mul_gain_P.grid_remove()
            l_mul_for_gain_P.grid_remove()
            l_mul_for_delay.config(text = "tab delay is (Discrete): ")
            l_mul_for_gain_A.config(text = "Amplitude gain is (dB) : ")
            btn_show_result_multipath.grid(row=3, column=2, pady=pady, padx=padx)






def valid_CFO(*args):
    global Change_CFO
    if (Change_CFO):
        try:

            read_CFO = float(v_CFO_carrier.get())
            if (read_CFO>=0):

                e_CFO_carrier.config(bg='white')
                if (read_CFO>0.01):
                    messagebox.showwarning('CFO',"CFO is high value >0.01")
                return True
            else:

                e_CFO_carrier.config(bg='red')
                messagebox.showerror('CFO', "input in CFO box is smaller than 0.")



        except:

            e_CFO_carrier.config(bg='red')
            messagebox.showerror('CFO',"input in CFO box is invalid.")
            return False
    else:
        return True

def valid_TFO():
    global Change_TFO
    if (Change_TFO):
        try:
            read_TFO_delay = float(v_TFO_delay.get())
            if (read_TFO_delay>=0):
                e_TFO_delay.config(bg='white')
                st_TFO_delay = True
            else:
                e_TFO_delay.config(bg='red')
                messagebox.showerror('Time_Frequency_offset', "input in delay box is smaller than 0.")
                st_TFO_delay = False


        except:
            e_TFO_delay.config(bg='red')
            messagebox.showerror('Time_Frequency_offset',"input in delay box is invalid.")
            st_TFO_delay = False
        try:

            read_TFO_SamplinRate = float(v_TFO_SamplingRate.get())
            if (read_TFO_SamplinRate>=0):
                e_TFO_SamplingRate.config(bg='white')
                st_TFO_SM = True
            else:
                e_TFO_SamplingRate.config(bg='red')
                messagebox.showerror('Time_Frequency_offset', "input in SamplingRate box is smaller than 0.")
                st_TFO_SM = False

        except:
            e_TFO_SamplingRate.config(bg='red')
            messagebox.showerror('Time_Frequency_offset', "input in SamplingRate box is invalid.")
            st_TFO_SM = False

        if (st_TFO_SM and st_TFO_delay):

            return True
        else:

            return False
    else:

        return True

def valid_fx():

    try:
        read_fx = float(v_fx.get())
        if (read_fx > 0):
            e_fx.config(bg='white')
            st_fx = True
        else:
            e_fx.config(bg='red')
            messagebox.showerror('Carrier Frequency', "input in SamplingRate box is smaller  than 0.")
            st_fx = False

    except:
        e_fx.config(bg='red')
        messagebox.showerror('Carrier Frequency', "input in SamplingRate box is invalid.")
        st_fx = False


    return st_fx






def valid_IQ():

    if (True):
        try:
            read_IQ_A = float(v_IQ_Ampitude.get())
            e_IQ_Amplitude.config(bg='white')
            st_IQ_A = True

        except:
            e_IQ_Amplitude.config(bg='red')
            messagebox.showerror('I\Q Imbalance',"input in Amplitude box is invalid.")
            st_IQ_A = False
        try:
            read_IQ_P = float(v_IQ_Phase.get())
            e_IQ_Phase.config(bg='white')
            st_IQ_P = True
        except:
            e_IQ_Phase.config(bg='red')
            messagebox.showerror('I\Q Imbalance',"input in Phase box is invalid.")
            st_IQ_P = False

        if (st_IQ_P and st_IQ_A):

            return True
        else:

            return False

def valid_PN():

    if (True):
        try:
            read_PN_var = float(v_PN_Var.get())

            e_PN_var.config(bg='white')
            st_PN_var = True


        except:
            e_PN_var.config(bg='red')
            messagebox.showerror('Phase Noise', "input in var box is invalid.")
            st_PN_var = False

        try:
            read_PN_offset= float(v_PN_offset.get())
            if (read_PN_offset>0):
                e_PN_ofsset.config(bg='white')
                st_PN_offset = True
                if (read_PN_offset<=0.1):
                    messagebox.showwarning('Phase Noise','offset is very low, maybe error in C code. SamplingRate/offset is very high.')

            else:
                e_PN_ofsset.config(bg='red')
                st_PN_offset= False
                messagebox.showerror('Phase Noise','offset is smaller than 0.')

        except:
            e_PN_ofsset.config(bg='red')
            st_PN_offset = False
            messagebox.showerror('Phase Noise', 'offset is invalid. (offset > 0 or offset is float number.)')


        try:
            read_PN_SM= float(v_PN_SamplingRate.get())
            if (read_PN_SM>=0):
                e_PN_SamplinRate.config(bg='white')
                st_PN_SM = True
            else:
                e_PN_SamplinRate.config(bg='red')
                st_PN_SM= False
                messagebox.showerror('Phase Noise','SamplingRate is smaller than 0.')

        except:
            e_PN_SamplinRate.config(bg='red')
            st_PN_SM = False
            messagebox.showerror('Phase Noise', 'SamplingRate is invalid.')

        if (st_PN_offset and st_PN_SM and st_PN_var):

            return True
        else:

            return False


def valid_Doppler():
    global Change_Doppler
    if (Change_Doppler):
        try:

            read_Dopller = float(v_Doppler.get())


            e_Doppler.config(bg='white')


            return True





        except:

            e_Doppler.config(bg='red')
            messagebox.showerror('Dopller',"input in Dopller frequency box is invalid.")
            return False
    else:
        return True


def valid_IIP3():

    st_0 = False
    st_1 = False
    st_2 = False
    st_3 = False



    try:

        read_IIP3_0 = float(v_IIP3_0.get())

        #btn_Doppler.config(bg='white')
        e_IIP3_0.config(bg='white')
        st_0 = True
    except:
        e_IIP3_0.config(bg='red')

        st_0 = False

    try:

        read_IIP3_1 = float(v_IIP3_1.get())

        #btn_Doppler.config(bg='white')
        e_IIP3_1.config(bg='white')
        st_1 = True
    except:
        e_IIP3_1.config(bg='red')

        st_1 = False

    try:

        read_IIP3_2 = float(v_IIP3_2.get())


        e_IIP3_2.config(bg='white')
        st_2 = True
    except:
        e_IIP3_2.config(bg='red')

        st_2 = False


    try:

        read_IIP3_3 = float(v_IIP3_3.get())


        e_IIP3_3.config(bg='white')
        st_3 = True
    except:
        e_IIP3_3.config(bg='red')

        st_3 = False

    if (st_0 and st_1 and st_2 and st_3):

        return True


    else:


        messagebox.showerror('Dopller', "input in Dopller frequency box is invalid.")
        return False

def valid_multipath_custom():
    #vlaid delay
    try:
        read_mul_d0 = float(var_mul_custom_delay0.get())
        read_mul_d1 = float(var_mul_custom_delay1.get())
        read_mul_d2 = float(var_mul_custom_delay2.get())
        read_mul_d3 = float(var_mul_custom_delay3.get())
        read_mul_d4 = float(var_mul_custom_delay4.get())
        read_mul_d5 = float(var_mul_custom_delay5.get())
        read_mul_d6 = float(var_mul_custom_delay6.get())
        e_mul_custom_delay0.config(bg='white')
        e_mul_custom_delay1.config(bg='white')
        e_mul_custom_delay2.config(bg='white')
        e_mul_custom_delay3.config(bg='white')
        e_mul_custom_delay4.config(bg='white')
        e_mul_custom_delay5.config(bg='white')
        e_mul_custom_delay6.config(bg='white')
        st_mul_custom_delay = True
    except:
        messagebox.showerror('multipath_custom','input in custom_delay box is invalid.')
        e_mul_custom_delay0.config(bg='red')
        e_mul_custom_delay1.config(bg='red')
        e_mul_custom_delay2.config(bg='red')
        e_mul_custom_delay3.config(bg='red')
        e_mul_custom_delay4.config(bg='red')
        e_mul_custom_delay5.config(bg='red')
        e_mul_custom_delay6.config(bg='red')
        st_mul_custom_delay =False
    #vliad gain_A
    try:
        read_mul_gA0 = float(var_mul_custom_gainA0.get())
        read_mul_gA1 = float(var_mul_custom_gainA1.get())
        read_mul_gA2 = float(var_mul_custom_gainA2.get())
        read_mul_gA3 = float(var_mul_custom_gainA3.get())
        read_mul_gA4 = float(var_mul_custom_gainA4.get())
        read_mul_gA5 = float(var_mul_custom_gainA5.get())
        read_mul_gA6 = float(var_mul_custom_gainA6.get())
        e_mul_custom_gainA0.config(bg='white')
        e_mul_custom_gainA1.config(bg='white')
        e_mul_custom_gainA2.config(bg='white')
        e_mul_custom_gainA3.config(bg='white')
        e_mul_custom_gainA4.config(bg='white')
        e_mul_custom_gainA5.config(bg='white')
        e_mul_custom_gainA6.config(bg='white')
        st_mul_custom_gain_A = True
    except:
        messagebox.showerror('multipath_custom', 'input in custom_gain_Amplitude box is invalid.')
        e_mul_custom_gainA0.config(bg='red')
        e_mul_custom_gainA1.config(bg='red')
        e_mul_custom_gainA2.config(bg='red')
        e_mul_custom_gainA3.config(bg='red')
        e_mul_custom_gainA4.config(bg='red')
        e_mul_custom_gainA5.config(bg='red')
        e_mul_custom_gainA6.config(bg='red')
        st_mul_custom_gain_A = False
    #valid gain_P
    try:
        read_mul_gP0 = float(var_mul_custom_gainP0.get())
        read_mul_gP1 = float(var_mul_custom_gainP1.get())
        read_mul_gP2 = float(var_mul_custom_gainP2.get())
        read_mul_gP3 = float(var_mul_custom_gainP3.get())
        read_mul_gP4 = float(var_mul_custom_gainP4.get())
        read_mul_gP5 = float(var_mul_custom_gainP5.get())
        read_mul_gP6 = float(var_mul_custom_gainP6.get())
        e_mul_custom_gainP0.config(bg='white')
        e_mul_custom_gainP1.config(bg='white')
        e_mul_custom_gainP2.config(bg='white')
        e_mul_custom_gainP3.config(bg='white')
        e_mul_custom_gainP4.config(bg='white')
        e_mul_custom_gainP5.config(bg='white')
        e_mul_custom_gainP6.config(bg='white')
        st_mul_custom_gain_P = True
    except:
        messagebox.showerror('multipath_custom', 'input in custom_gain_Phase box is invalid.')
        e_mul_custom_gainP0.config(bg='red')
        e_mul_custom_gainP1.config(bg='red')
        e_mul_custom_gainP2.config(bg='red')
        e_mul_custom_gainP3.config(bg='red')
        e_mul_custom_gainP4.config(bg='red')
        e_mul_custom_gainP5.config(bg='red')
        e_mul_custom_gainP6.config(bg='red')
        st_mul_custom_gain_P = False

    if (st_mul_custom_delay and st_mul_custom_gain_A and st_mul_custom_gain_P):
        return True
    else:
        return False

def valid_multipath():
    try:
        SamplingRate = float(v_mul_SamplingRate.get())
        SamplingRate = SamplingRate * pow(10, 6)
        if (SamplingRate>=0):
            e_mul_SamplingRte.config(bg='white')
            if (v_multipath.get() == 'Choose multipath model (default = off)'):
                return True
            else:
                if (v_multipath.get() == 'Custom'):
                    st_custom = valid_multipath_custom()
                    if (st_custom):
                        #menu_multipath.config(bg='white')
                        return True
                    else:
                       # menu_multipath.config(bg='red')
                        return False
                else:
                 #   menu_multipath.config(bg='white')
                    return True

        else:
            messagebox.showerror('Multipath', 'SamplinRate in multipath block is smaller than 0.')
            #menu_multipath.config(bg='red')
            e_mul_SamplingRte.config(bg='red')
            return False
    except:
        messagebox.showerror('Multipath','SamplinRate in multipath block is invalid.')
        #menu_multipath.config(bg='red')
        e_mul_SamplingRte.config(bg='red')
        return False


delay_EPA0 = [0,30,70,90,110,190,410]
delay_EVA0 = [0,30,150,310,370,710,1090,1730,2510]
delay_ETU0 = [0,50,120,200,230,500,1600,2300,5000]


delay_EPA = [0,30,70,90,110,190,410]
delay_EVA = [0,30,150,310,370,710,1090,1730,2510]
delay_ETU = [0,50,120,200,230,500,1600,2300,5000]

abs_gain_EPA = [0,-1,-2,-3,-8,-17.2,-20.8]
abs_gain_EVA = [0,-1.5,-1.4,-3.6,-0.6,-9.1,-7,-12,-16.9]
abs_gain_ETU = [-1,-1,-1,0,0,0,-3,-5,-7]




def show_result_multipath():
    try:
        SamplingRate = float(v_TFO_SamplingRate.get())
        SamplingRate = SamplingRate * pow(10, 6)
        if (SamplingRate>0):
            for index in range(len(delay_EPA0)):
                delay_EPA[index] = int(pow(10, -9) * SamplingRate * delay_EPA0[index])
            for index in range(len(delay_EVA0)):
                delay_EVA[index] = int(pow(10, -9) * SamplingRate * delay_EVA0[index])
            for index in range(len(delay_ETU0)):
                delay_ETU[index] = int(pow(10, -9) * SamplingRate * delay_ETU0[index])


            #l_mul_for_gain_P.grid(row=3,column=0,pady=pady,padx=padx)
            if(v_multipath.get() == "EPA"):
                l_mul_delay.config(text =  delay_EPA)
                l_mul_gain_A.config(text=abs_gain_EPA)
                l_mul_delay.grid(row=1,column=2,pady=pady,padx=padx)
                l_mul_gain_A.grid(row=2,column=2,pady=pady,padx=padx)
            if(v_multipath.get() == "EVA"):
                l_mul_delay.config(text =  delay_EVA)
                l_mul_gain_A.config(text=abs_gain_EVA)
                l_mul_delay.grid(row=1,column=2,pady=pady,padx=padx)
                l_mul_gain_A.grid(row=2,column=2,pady=pady,padx=padx)
            if(v_multipath.get() == "ETU"):
                l_mul_delay.config(text =  delay_ETU)
                l_mul_gain_A.config(text=abs_gain_ETU)
                l_mul_delay.grid(row=1,column=2,pady=pady,padx=padx)
                l_mul_gain_A.grid(row=2,column=2,pady=pady,padx=padx)
            #menu_multipath.config(bg='white')
        else:
            messagebox.showerror('Multipath', 'SamplinRate in SamplingRate block is smaller than 0 or equal 0.')
            #menu_multipath.config(bg='red')
    except:
        messagebox.showerror('Multipath','SamplinRate in SamplingRate block is invalid.')
        #menu_multipath.config(bg='red')



def validation_input():
    state_CFO = valid_CFO()
    state_TFO=valid_TFO()
    state_IQ = valid_IQ()
    state_PN = valid_PN()
    state_Doppler = valid_Doppler()
    state_IIP3 = valid_IIP3()

    state_multipath = valid_multipath()

    if (state_CFO and state_IQ and state_PN and state_TFO and state_multipath and state_Doppler and state_IIP3):

        return True
    else:

        return False



def write_state():
    pass_data = []


    global Change_PN
    if (float(v_PN_Var.get()) ==0):
        Change_PN = False
    else:
        Change_PN = True



    try:
        if (Change_CFO):
            pass_data.append(1)
        else:
            pass_data.append(0)
        if (Change_TFO):
            pass_data.append(1)
        else:
            pass_data.append(0)

        if (Change_IQ):
            pass_data.append(1)
        else:
            pass_data.append(0)
        if (Change_PN):
            pass_data.append(1)
        else:
            pass_data.append(0)

        if (Change_Doppler):
            pass_data.append(1)
        else:
            pass_data.append(0)

        if (Change_IIP3):
            pass_data.append(1)
        else:
            pass_data.append(0)
        if (Change_multipath):
            pass_data.append(1)
        else:
            pass_data.append(0)


        read_SamplingRate = max(float(v_mul_SamplingRate.get()), float(v_PN_SamplingRate.get()), float(v_TFO_SamplingRate.get()))

        read_CFO = float(v_CFO_carrier.get())
        read_TFO_delay = float(v_TFO_delay.get())
        read_IQ_A = float(v_IQ_Ampitude.get())
        read_IQ_Phase = float(v_IQ_Phase.get())
        read_PN_var = float(v_PN_Var.get())
        read_PN_offset = float(v_PN_offset.get())
        read_IIP3_0 = float(e_IIP3_0.get())
        read_IIP3_1 = float(e_IIP3_1.get())
        read_IIP3_2 = float(e_IIP3_2.get())
        read_IIP3_3 = float(e_IIP3_3.get())
        read_Doppler_F = float(v_Doppler.get())
        #delay mul
        read_mul_d0 = float(var_mul_custom_delay0.get())
        read_mul_d1 = float(var_mul_custom_delay1.get())
        read_mul_d2 = float(var_mul_custom_delay2.get())
        read_mul_d3 = float(var_mul_custom_delay3.get())
        read_mul_d4 = float(var_mul_custom_delay4.get())
        read_mul_d5 = float(var_mul_custom_delay5.get())
        read_mul_d6 = float(var_mul_custom_delay6.get())
        #gain_A mul
        read_mul_gA0 = float(var_mul_custom_gainA0.get())
        read_mul_gA1 = float(var_mul_custom_gainA1.get())
        read_mul_gA2 = float(var_mul_custom_gainA2.get())
        read_mul_gA3 = float(var_mul_custom_gainA3.get())
        read_mul_gA4 = float(var_mul_custom_gainA4.get())
        read_mul_gA5 = float(var_mul_custom_gainA5.get())
        read_mul_gA6 = float(var_mul_custom_gainA6.get())
        #gain_Phase mul
        read_mul_gP0 = float(var_mul_custom_gainP0.get())
        read_mul_gP1 = float(var_mul_custom_gainP1.get())
        read_mul_gP2 = float(var_mul_custom_gainP2.get())
        read_mul_gP3 = float(var_mul_custom_gainP3.get())
        read_mul_gP4 = float(var_mul_custom_gainP4.get())
        read_mul_gP5 = float(var_mul_custom_gainP5.get())
        read_mul_gP6 = float(var_mul_custom_gainP6.get())




        if (v_multipath.get() == "EPA"):
            read_size_multipath = 7
            mode_multipath = 0


        elif (v_multipath.get() == "EVA"):
            read_size_multipath = 9
            mode_multipath = 1

        elif (v_multipath.get() == "ETU"):
            read_size_multipath = 9
            mode_multipath = 2

        elif (v_multipath.get() == "Custom"):
            read_size_multipath = 7
            mode_multipath = 3
        else:
            read_size_multipath = 0
            mode_multipath = -1


        #append
        pass_data.append(read_SamplingRate)
        pass_data.append(read_CFO)
        pass_data.append(read_TFO_delay)
        pass_data.append(read_IQ_A)
        pass_data.append(read_IQ_Phase)
        pass_data.append(read_PN_var)
        pass_data.append(read_PN_offset)
        pass_data.append(read_IIP3_0)
        pass_data.append(read_IIP3_1)
        pass_data.append(read_IIP3_2)
        pass_data.append(read_IIP3_3)
        pass_data.append(read_Doppler_F)
        pass_data.append(read_size_multipath)
        pass_data.append(mode_multipath)
        #append delay mul custom
        pass_data.append(read_mul_d0)
        pass_data.append(read_mul_d1)
        pass_data.append(read_mul_d2)
        pass_data.append(read_mul_d3)
        pass_data.append(read_mul_d4)
        pass_data.append(read_mul_d5)
        pass_data.append(read_mul_d6)
        #append Amplitude
        pass_data.append(read_mul_gA0)
        pass_data.append(read_mul_gA1)
        pass_data.append(read_mul_gA2)
        pass_data.append(read_mul_gA3)
        pass_data.append(read_mul_gA4)
        pass_data.append(read_mul_gA5)
        pass_data.append(read_mul_gA6)
        #append Phase mul
        pass_data.append(read_mul_gP0)
        pass_data.append(read_mul_gP1)
        pass_data.append(read_mul_gP2)
        pass_data.append(read_mul_gP3)
        pass_data.append(read_mul_gP4)
        pass_data.append(read_mul_gP5)
        pass_data.append(read_mul_gP6)





        #write
        f = open('get.bin', 'wb')
        s = struct.pack('f' * len(pass_data), *pass_data)
        f.write(s)
        f.close()

        #write_input_from_user









        print(pass_data)
        return  True
    except:
        return False




def run_C():
    cwd = os.getcwd()

    try:
        f = open(cwd+"/float_d.bin")
        st_exist_signal_file = True
        f.close()
    except:
        st_exist_signal_file = False
        messagebox.showerror('binary file','binary file signal is not exist. please load it.')


    if (st_exist_signal_file):
        try:

            so_file = cwd+"/my_functions.so"

            my_functions = CDLL(so_file)

            print(type(my_functions))
            messagebox._show('run script', 'C script is running...')

            my_functions.main()

            return True


        except:
            messagebox.showerror('run script', 'run C script was fail.')

            return False

    else:
        messagebox.showerror('run script', 'run C script was fail.')

        return False










def run_script():

    global on_srs
    if (on_srs):
        try:
            os.system(command='sudo killall pdsch_ue')
            time.sleep(2)
        except:
            pass

    st_valid_input = validation_input()
    if(st_valid_input):
        try:
            st_write_data = write_state()
            messagebox.showinfo("pass input",'pass input was successful.')
            if(st_write_data):
                st_run_C = run_C()
                if (st_run_C):
                    messagebox.showinfo('apply unwanted phenomenon','apply unwanted phenomenon was successful.')
                else:
                    messagebox.showerror('apply unwanted phenomenon', 'apply unwanted phenomenon was fail.')



        except:
            messagebox.showerror("pass input",'pass input was fail.')





    else:
        messagebox.showerror('run','code can not run. some inputs are invalid')


    if (on_srs):
        time.sleep(5)
        os.system(command='sudo ./constlation.sh&')



def load_binary_file():
    try:
        dir_binary_file = filedialog.askopenfile(title = 'Select binary file',filetypes = (("binary files","*.bin"),))
        shutil.copy(dir_binary_file.name, 'float_d.bin')

        messagebox.showinfo('load binary file','load binary file was successful.')
    except:
        messagebox.showinfo('load binary file', 'load binary file was fail.')
def Reset_color():
    e_CFO_carrier.config(bg="white")
    e_PN_var.config(bg='white')
    e_PN_ofsset.config(bg='white')
    e_IQ_Amplitude.config(bg='white')
    e_IQ_Phase.config(bg='white')
    e_Doppler.config(bg='white')
    e_TFO_delay.config(bg='white')
    e_TFO_SamplingRate.config(bg='white')
    e_IIP3_0.config(bg='white')
    e_IIP3_1.config(bg='white')
    e_IIP3_2.config(bg='white')
    e_IIP3_3.config(bg='white')
    e_mul_custom_delay0.config(bg='white')
    e_mul_custom_delay1.config(bg='white')
    e_mul_custom_delay2.config(bg='white')
    e_mul_custom_delay3.config(bg='white')
    e_mul_custom_delay4.config(bg='white')
    e_mul_custom_delay5.config(bg='white')
    e_mul_custom_delay6.config(bg='white')
    e_mul_custom_gainP0.config(bg='white')
    e_mul_custom_gainP1.config(bg='white')
    e_mul_custom_gainP2.config(bg='white')
    e_mul_custom_gainP3.config(bg='white')
    e_mul_custom_gainP4.config(bg='white')
    e_mul_custom_gainP5.config(bg='white')
    e_mul_custom_gainP6.config(bg='white')
    e_mul_custom_gainA0.config(bg='white')
    e_mul_custom_gainA1.config(bg='white')
    e_mul_custom_gainA2.config(bg='white')
    e_mul_custom_gainA3.config(bg='white')
    e_mul_custom_gainA4.config(bg='white')
    e_mul_custom_gainA5.config(bg='white')
    e_mul_custom_gainA6.config(bg='white')
    e_fx.config(bg='white')

def Reset():
    set_default_variable()

    Reset_color()






def trace_fx(*args):
    try:
        read_fx = float(v_fx.get())
        if (read_fx > 0):
            e_fx.config(bg='white')

        else:
            e_fx.config(bg='red')




    except:
        e_fx.config(bg='red')





#def trace
def trace_CFO(*args):
    if (Change_CFO):
        try:

            read_CFO = float(v_CFO_carrier.get())
            if (read_CFO>=0):

                e_CFO_carrier.config(bg='white')


                return True
            else:

                e_CFO_carrier.config(bg='red')




        except:

            e_CFO_carrier.config(bg='red')


    else:
        return True

def trace_TFO_delay(*args):
    if (Change_TFO):
        try:
            read_TFO_delay = float(v_TFO_delay.get())
            if (read_TFO_delay>=0):
                e_TFO_delay.config(bg='white')

            else:
                e_TFO_delay.config(bg='red')




        except:
            e_TFO_delay.config(bg='red')

def trace_TFO_SamplingRate(*args):

    if (Change_TFO):

        try:

            read_TFO_SamplinRate = float(v_TFO_SamplingRate.get())
            if (read_TFO_SamplinRate>=0):
                e_TFO_SamplingRate.config(bg='white')

            else:
                e_TFO_SamplingRate.config(bg='red')



        except:
            e_TFO_SamplingRate.config(bg='red')






def trace_IQ_A(*args):
    try:
        read_IQ_A = float(v_IQ_Ampitude.get())
        e_IQ_Amplitude.config(bg='white')


    except:
        e_IQ_Amplitude.config(bg='red')
def trace_IQ_P(*args):
    try:
        read_IQ_P = float(v_IQ_Phase.get())
        e_IQ_Phase.config(bg='white')

    except:
        e_IQ_Phase.config(bg='red')
def trace_PN_var(*args):
    try:
        read_PN_var = float(v_PN_Var.get())

        e_PN_var.config(bg='white')



    except:
        e_PN_var.config(bg='red')
def trace_PN_offset(*args):
    try:
        read_PN_offset = float(v_PN_offset.get())
        if (read_PN_offset > 0):
            e_PN_ofsset.config(bg='white')


        else:
            e_PN_ofsset.config(bg='red')


    except:
        e_PN_ofsset.config(bg='red')


def trace_IP3(*args):
    try:

        read_IIP3_0 = float(v_IIP3_0.get())

        #btn_Doppler.config(bg='white')
        e_IIP3_0.config(bg='white')

    except:
        e_IIP3_0.config(bg='red')



    try:

        read_IIP3_1 = float(v_IIP3_1.get())

        #btn_Doppler.config(bg='white')
        e_IIP3_1.config(bg='white')

    except:
        e_IIP3_1.config(bg='red')


    try:

        read_IIP3_2 = float(v_IIP3_2.get())


        e_IIP3_2.config(bg='white')

    except:
        e_IIP3_2.config(bg='red')



    try:

        read_IIP3_3 = float(v_IIP3_3.get())


        e_IIP3_3.config(bg='white')

    except:
        e_IIP3_3.config(bg='red')





def trace_Doppler(*args):

    try:

        read_Dopller = float(v_Doppler.get())

        e_Doppler.config(bg='white')

    except:

        e_Doppler.config(bg='red')



def trace_multipath_delay(*args):
    try:
        read_mul_d0 = float(var_mul_custom_delay0.get())
        read_mul_d1 = float(var_mul_custom_delay1.get())
        read_mul_d2 = float(var_mul_custom_delay2.get())
        read_mul_d3 = float(var_mul_custom_delay3.get())
        read_mul_d4 = float(var_mul_custom_delay4.get())
        read_mul_d5 = float(var_mul_custom_delay5.get())
        read_mul_d6 = float(var_mul_custom_delay6.get())
        e_mul_custom_delay0.config(bg='white')
        e_mul_custom_delay1.config(bg='white')
        e_mul_custom_delay2.config(bg='white')
        e_mul_custom_delay3.config(bg='white')
        e_mul_custom_delay4.config(bg='white')
        e_mul_custom_delay5.config(bg='white')
        e_mul_custom_delay6.config(bg='white')

    except:

        e_mul_custom_delay0.config(bg='red')
        e_mul_custom_delay1.config(bg='red')
        e_mul_custom_delay2.config(bg='red')
        e_mul_custom_delay3.config(bg='red')
        e_mul_custom_delay4.config(bg='red')
        e_mul_custom_delay5.config(bg='red')
        e_mul_custom_delay6.config(bg='red')

def trace_multipath_A(*args):
    try:
        read_mul_gA0 = float(var_mul_custom_gainA0.get())
        read_mul_gA1 = float(var_mul_custom_gainA1.get())
        read_mul_gA2 = float(var_mul_custom_gainA2.get())
        read_mul_gA3 = float(var_mul_custom_gainA3.get())
        read_mul_gA4 = float(var_mul_custom_gainA4.get())
        read_mul_gA5 = float(var_mul_custom_gainA5.get())
        read_mul_gA6 = float(var_mul_custom_gainA6.get())
        e_mul_custom_gainA0.config(bg='white')
        e_mul_custom_gainA1.config(bg='white')
        e_mul_custom_gainA2.config(bg='white')
        e_mul_custom_gainA3.config(bg='white')
        e_mul_custom_gainA4.config(bg='white')
        e_mul_custom_gainA5.config(bg='white')
        e_mul_custom_gainA6.config(bg='white')

    except:

        e_mul_custom_gainA0.config(bg='red')
        e_mul_custom_gainA1.config(bg='red')
        e_mul_custom_gainA2.config(bg='red')
        e_mul_custom_gainA3.config(bg='red')
        e_mul_custom_gainA4.config(bg='red')
        e_mul_custom_gainA5.config(bg='red')
        e_mul_custom_gainA6.config(bg='red')

def trace_multipath_P(*args):
    try:
        read_mul_gP0 = float(var_mul_custom_gainP0.get())
        read_mul_gP1 = float(var_mul_custom_gainP1.get())
        read_mul_gP2 = float(var_mul_custom_gainP2.get())
        read_mul_gP3 = float(var_mul_custom_gainP3.get())
        read_mul_gP4 = float(var_mul_custom_gainP4.get())
        read_mul_gP5 = float(var_mul_custom_gainP5.get())
        read_mul_gP6 = float(var_mul_custom_gainP6.get())
        e_mul_custom_gainP0.config(bg='white')
        e_mul_custom_gainP1.config(bg='white')
        e_mul_custom_gainP2.config(bg='white')
        e_mul_custom_gainP3.config(bg='white')
        e_mul_custom_gainP4.config(bg='white')
        e_mul_custom_gainP5.config(bg='white')
        e_mul_custom_gainP6.config(bg='white')

    except:

        e_mul_custom_gainP0.config(bg='red')
        e_mul_custom_gainP1.config(bg='red')
        e_mul_custom_gainP2.config(bg='red')
        e_mul_custom_gainP3.config(bg='red')
        e_mul_custom_gainP4.config(bg='red')
        e_mul_custom_gainP5.config(bg='red')
        e_mul_custom_gainP6.config(bg='red')





def command_Time_view():
    try:
        fs = float(v_TFO_SamplingRate.get())
        if (fs<0):
            messagebox.showerror('Plot Time signal.', 'SamplingRate is smaller than 0.')
        elif(fs==0):
            messagebox.showerror('Plot Time signal','PLease fill SamplingRate (for plot PSD, zero is not acceptable)')
        else:
            view.Time_view(fs)


    except:
        messagebox.showerror('Plot Time signal.','SamplingRate is invalid.')






def command_PSD_view():
    try:
        fs = float(v_TFO_SamplingRate.get())
        if (fs<0):
            messagebox.showerror('Plot PSD signal.', 'SamplingRate is smaller than 0.')
        elif(fs==0):
            messagebox.showerror('Plot PSD signal','PLease fill SamplingRate (for plot PSD, zero is not acceptable)')
        else:
            view.PSD_view(fs)


    except:
        messagebox.showerror('Plot PSD signal.','SamplingRate is invalid.')


def command_pass_fx():
    if (valid_fx()):
        return float(e_fx.get())

    fx = float (e_fx.get())
    return fx


def command_pass_fs():

    fs = float(v_TFO_SamplingRate.get())

    return fs



def command_btn_send():
    st_fs = False
    try:
        fs = float(v_TFO_SamplingRate.get())
        if (fs<0):
            messagebox.showerror('send.', 'SamplingRate is invalid.')
            st_fs = False
        elif(fs==0):
            messagebox.showerror('send','PLease fill SamplingRate ( zero samplingrate is not acceptable)')
            st_fs = False
        elif(fs >0):
            st_fs = True


    except:
        messagebox.showerror('send.', 'SamplingRate is invalid.')
        st_fs = False

    st_fx = valid_fx()

    if (st_fx and st_fs):
        fx_fs = []
        fx_fs.append(float(v_fx.get()))
        fx_fs.append(fs)

        f = open('fx_fs.bin', 'wb')
        s = struct.pack('f' * len(fx_fs), *fx_fs)
        f.write(s)
        f.close()



        btn_send.config(state=DISABLED,text="sending...")
        os.system('sudo python top_block.py')
        btn_send.config(state=NORMAL, text="send")
    else:
        messagebox.showerror('send.', 'send process failed.')






btn_send.config(command=command_btn_send)

















#trace


#btn_config
btn_show_result_multipath.config(command = show_result_multipath)
###
v_CFO_carrier.trace('w',trace_CFO)
v_TFO_delay.trace('w',trace_TFO_delay)
v_TFO_SamplingRate.trace('w',trace_TFO_SamplingRate)
v_IQ_Ampitude.trace('w',trace_IQ_A)
v_IQ_Phase.trace('w',trace_IQ_P)
v_PN_Var.trace('w',trace_PN_var)
v_PN_offset.trace('w',trace_PN_offset)
v_Doppler.trace('w',trace_Doppler)
v_IIP3_0.trace('w',trace_IP3)
v_IIP3_1.trace('w',trace_IP3)
v_IIP3_2.trace('w',trace_IP3)
v_IIP3_3.trace('w',trace_IP3)
v_fx.trace('w',trace_fx)
#trace_mul_delay
var_mul_custom_delay0.trace('w',trace_multipath_delay)
var_mul_custom_delay1.trace('w',trace_multipath_delay)
var_mul_custom_delay2.trace('w',trace_multipath_delay)
var_mul_custom_delay3.trace('w',trace_multipath_delay)
var_mul_custom_delay4.trace('w',trace_multipath_delay)
var_mul_custom_delay5.trace('w',trace_multipath_delay)
var_mul_custom_delay6.trace('w',trace_multipath_delay)
#trace_mul_A
var_mul_custom_gainA0.trace('w',trace_multipath_A)
var_mul_custom_gainA1.trace('w',trace_multipath_A)
var_mul_custom_gainA2.trace('w',trace_multipath_A)
var_mul_custom_gainA3.trace('w',trace_multipath_A)
var_mul_custom_gainA4.trace('w',trace_multipath_A)
var_mul_custom_gainA5.trace('w',trace_multipath_A)
var_mul_custom_gainA6.trace('w',trace_multipath_A)
#trace_mul_P
var_mul_custom_gainP0.trace('w',trace_multipath_P)
var_mul_custom_gainP1.trace('w',trace_multipath_P)
var_mul_custom_gainP2.trace('w',trace_multipath_P)
var_mul_custom_gainP3.trace('w',trace_multipath_P)
var_mul_custom_gainP4.trace('w',trace_multipath_P)
var_mul_custom_gainP5.trace('w',trace_multipath_P)
var_mul_custom_gainP6.trace('w',trace_multipath_P)
#trce
v_multipath.trace('w',command_custom_multipath)

#create btn
btn_apply = Button(frame_btn,text="apply to signal",font='Time 11',command=run_script,relief=RAISED,bg='yellow',width=10)
btn_reset = Button(frame_btn,text="Reset",font='Time 11',command=Reset,relief=RAISED,bg='yellow',width=10)

btn_apply.pack(padx=3*padx,pady=pady*3)
btn_reset.pack(padx=3*padx,pady=pady*4)

root.attributes('-zoomed', True)

command_custom_multipath()


#menu
my_menu = Menu(root,activebackground = 'yellow',bg = 'grey',font = "Time 10")

root.config(menu=my_menu)
File = Menu(my_menu,activebackground = 'yellow',bg = 'white',font = "Time 10")
View = Menu(my_menu,activebackground= 'yellow',bg='white',font='Time 10')

my_menu.add_cascade(label = 'File',menu = File)
File.add_command(label='Load binary file',command=load_binary_file,font='Time 9')
File.add_separator()

my_menu.add_cascade(label='View',menu=View)
View.add_command(label= 'Plot signal in time',command=command_Time_view,font= 'Time 9')
View.add_separator()
View.add_command(label='plot PSD signal',command= command_PSD_view,font='Time 9')
View.add_separator()

#srs
def run_srs():
    kill_command = "sudo killall pdsch_ue"
    os.system(command=kill_command)

    create_command = "sudo ./create_signal.sh"
    os.system(command=create_command)

    start_command = "sudo ./constlation.sh&"
    os.system(command=start_command)

def kill_srs():
    kill_command = "sudo killall pdsch_ue"
    os.system(command=kill_command)

def change_SR_start():
    v_TFO_SamplingRate.set('7.68')
    e_TFO_SamplingRate.config(state=DISABLED)

def change_SR_exit():
    v_TFO_SamplingRate.set('0')
    e_TFO_SamplingRate.config(state=NORMAL)
    e_TFO_SamplingRate.config(bg='white')

def start_srs():
    change_SR_start()
    File.entryconfig('Load binary file',state=DISABLED)
    View.entryconfig('Exit open source mode',state=NORMAL)
    run_srs()
    global on_srs
    on_srs=True

def exit_srs():
    change_SR_exit()
    File.entryconfig('Load binary file', state=NORMAL)
    View.entryconfig('Exit open source mode', state=DISABLED)
    kill_srs()
    global on_srs
    on_srs=False
    Reset_color()



View.add_command(label='Reset/Start open source mode',command=start_srs)
View.add_separator()
View.add_command(label='Exit open source mode',command=exit_srs,state=DISABLED)

root.mainloop()









#import shutil

#shutil.copy('/media/root/New Volume/uni/project/C/read_binary_python/read_binary_python/data_c.bin','test.bin')
