import tkinter
from tkinter import *
import datetime
from fontTools.ttLib import TTFont
import calendar
from random import randrange
from tkinter import ttk
import PIL
from PIL import Image
from PIL import ImageTk


font = TTFont('TechnaSans-Regular.otf')
font.save('TechnaSans-Regular.otf')

fontt = TTFont('Louis George Cafe Bold.ttf')
fontt.save('Louis George Cafe Bold.ttf')

fonttt = TTFont('Louis George Cafe.ttf')
fonttt.save('Louis George Cafe.ttf')



class SleepMoreIdiot:


   def __init__(self, master):


       self.master = master
       self.version = "Beta Version 0.1"

       master.title("Sleep More, Idiot")
       master.resizable(False, False)


       #self.width = 1024
       #self.height = 576

       #self.width = 1600
       #self.height = 900

       self.width = 1920
       self.height = 1080

       self.height_input_window = 0.75 * self.height #actually the width and height JUST FOR THE BUTTONS BECAUSE THEY HAVE TO BE SCALED
       self.width_input_window = 0.75 * self.width

       self.true_height_input_window = round(0.52083333333*self.height)
       self.true_width_input_window = round(0.87890625*self.width)

       self.edit_width = self.width * 0.75
       self.edit_height = self.height * 0.75

       self.main_text_color = "#a6a6a6"
       self.left_background_color = "#1d222e"
       self.background_color = "#191d26"
       self.highlighted_text_color = "#f6ff94"
       self.dull_highlight = "#62663b"
       self.edge_color = "#2d3548"
       self.secondary_background_color = "#232938"
       self.credit_color = "#384259"
       self.clock_color = "#61b3da"
       self.cancel_color = "#da3452"
       self.dull_cancel = "#643343"
       self.meter_color = "#7a91da"
       self.dull_clock_color = "#3c6079"
       self.overlap_bar = "#9785a3"
       self.dull_bar_color = "#49667e"
       self.dull_graph_color = "#75767a"

       self.data_file = "dataaa.txt"

       self.font_a = "TechnaSans-Regular"
       self.font_b = 'Louis George Cafe Bold'
       self.font_c = 'Louis George Cafe'



       self.master_data_storage = self.process_data(self.data_file)
       self.update_data()
       self.save_data(self.data_file)










       self.dashboard_frame = Canvas(master, width = self.width, height = self.height, bg = self.background_color, highlightthickness=0)


       # Place Everything Down _______________________________________





       self.graph_section(master)
       self.bottom_section(master)
       self.right_section(master)
       self.left_sidebar(master)

       self.lock_bottom()

       self.dashboard_frame.pack(expand = True)


   # Left section thigny

   def left_sidebar(self, master):


       self.left_sidebar = Canvas(master, bg=self.left_background_color, highlightthickness=0)

       self.left_sidebar.place(x=0, y=0, relwidth=0.15, relheight=1)


       self.title = Label(text = "Sleep", font = (self.font_a,int(0.033*self.width)), fg = self.main_text_color, bg = self.left_background_color)
       self.titlee = Label(text="More,", font=(self.font_a, int(0.033*self.width)), fg=self.main_text_color, bg=self.left_background_color)
       self.titleee = Label(text="Idiot", font = (self.font_a, int(0.033*self.width)), fg = self.highlighted_text_color, bg=self.left_background_color)
       self.bar1 = Canvas(master, bg = self.main_text_color, highlightthickness=0)
       self.bar2 = Canvas(master, bg=self.main_text_color, highlightthickness=0)
       self.ego = Label(text = "Hacker Pengwin \n2019", font = (self.font_b,int(0.0185546875*self.width)), fg = self.credit_color, bg = self.left_background_color)
       self.date = Label(text="", font=(self.font_b, int(0.0166*self.width)), fg=self.main_text_color, bg=self.left_background_color)
       self.clock = Label(text = "", font = (self.font_b,int(0.0224609375*self.width)), fg = self.clock_color, bg = self.left_background_color)
       #self.apm = Label(text="", font=(self.font_b, 15), fg="#61b3da", bg="#1d222e")
       self.version_display = Label(text=self.version, font=(self.font_b, round(0.01302083333*self.width)),
                        fg=self.credit_color, bg=self.left_background_color, anchor = "w")


       self.moving_clock()

       self.title.place(relx = 0.003, rely = 0.01, relwidth = 0.14, relheight = 0.085)
       self.titlee.place(relx=0.003, rely=0.1, relwidth=0.14, relheight=0.085)
       self.titleee.place(relx=-0.008, rely=0.19, relwidth=0.14, relheight=0.085)
       self.bar1.place(relx=0.01, rely = 0.33, relwidth = 0.13, relheight = 0.005)
       self.bar2.place(relx=0.01, rely=0.7, relwidth=0.13, relheight=0.005)
       self.ego.place(relx = 0.005, rely = 0.9, relwidth = 0.14, relheight = 0.1)
       self.clock.place(relx = 0.005, rely = 0.79, relwidth = 0.14, relheight = 0.05)
       #self.apm.place(relx=0.12, rely=0.8, relwidth=0.03, relheight=0.05)
       self.date.place(relx = 0.005, rely = 0.72, relwidth = 0.14, relheight = 0.1)
       self.version_display.place(relx=0.012, rely=0.28, relwidth=0.14, relheight=0.045)

       self.time_to_sleep()

   def time_to_sleep(self):

       self.left_sidebar.create_text(round(0.078125*self.width),round(0.22916666666*self.width), text = "Tonight, go \n to bed at", font = (self.font_b, round(0.02083333333*self.width)), fill = self.main_text_color)
       self.time_display = self.left_sidebar.create_text(0,0,text = "")
       self.update_sleep()
       self.left_sidebar.create_text(round(0.078125*self.width), round(0.33854166666*self.width), text="because you \n  need sleep",
                                     font=(self.font_b, round(0.02083333333 * self.width)), fill=self.main_text_color)
       #self.left_sidebar.create_text(text="Tonight, go to bed at")

   def update_sleep(self):

       self.left_sidebar.delete(self.time_display)

       sleep_at = 9.5

       prev = self.master_data_storage[-1][3]



       if prev > -1:

           adjustment = (9.5 - prev) * 0.5

           if adjustment >= 0:
               sleep_at -= adjustment

           self.time_display = self.left_sidebar.create_text(round(0.078125*self.width), round(0.28125*self.width), text=self.format_time_numbers_rounded(sleep_at),
                                                             font=(
                                                             self.font_b, round(0.02083333333 / 0.5 * self.width)),
                                                             fill=self.highlighted_text_color)

       else:

           self.time_display = self.left_sidebar.create_text(round(0.078125*self.width), round(0.27864583333*self.width), text="--:--",
                                                             font=(
                                                             self.font_b, round(0.02083333333 / 0.5 * self.width)),
                                                             fill=self.highlighted_text_color)

   def moving_clock(self):


       now = datetime.datetime.now()
       dat = now.strftime("%a, %b %d, %Y")
       time = now.strftime("%I:%M:%S %p")

       if int(time[0:2]) < 10:

           time = time[1:2] + time[2:]

       #apm = now.strftime("%p")
       self.clock.configure(text = time)
       self.date.configure(text = dat)
       #self.apm.configure(text=apm)
       self.master.after(1000, self.moving_clock)

   # graph section

   def graph_section(self, master):




       self.time_period_width = round(0.15625*self.width)
       self.time_period_height = round(0.3125*self.width)



       self.graph_section = Canvas(master, bg=self.secondary_background_color, highlightthickness=0)
       self.graph_section_underbar = Canvas(master, bg=self.edge_color, highlightthickness=0)


       corner_nw = self.dashboard_frame.create_oval(0.16 * self.width, 0.01 * self.height, 0.205 * self.width, 0.09 * self.height, fill=self.secondary_background_color, outline=self.secondary_background_color)

       corner_sw = self.dashboard_frame.create_oval(0.16 * self.width, 0.56 * self.height, 0.205 * self.width,  0.64 * self.height, fill=self.edge_color, outline=self.edge_color)

       corner_ne = self.dashboard_frame.create_oval(0.795 * self.width, 0.01 * self.height, 0.839 * self.width,  0.09 * self.height, fill=self.secondary_background_color, outline=self.secondary_background_color)

       corner_se = self.dashboard_frame.create_oval(0.795 * self.width, 0.56 * self.height, 0.839 * self.width, 0.64 * self.height, fill=self.edge_color, outline=self.edge_color)

       edge = self.dashboard_frame.create_rectangle(0.1825 * self.width, 0.01 * self.height, 0.8175 * self.width,   0.64 * self.height, fill=self.secondary_background_color, outline=self.secondary_background_color)

       south_edge = self.dashboard_frame.create_rectangle(0.1825 * self.width, 0.6 * self.height, 0.8175 * self.width, 0.64 * self.height, fill=self.edge_color, outline=self.edge_color)

       south_bar = self.graph_section.create_rectangle(0.16 * self.width, 0.55 * self.height, 0.84 * self.width,  0.6 * self.height, fill=self.edge_color, outline=self.edge_color)






















       self.time_period = 7

       self.graph = Canvas(master, bg=self.secondary_background_color, highlightthickness=0)
       self.graph.place(relx=0.165, rely=0.027, relwidth=0.666, relheight=0.51)

       self.graph_width = 0.666 * self.width
       self.graph_height = 0.51 * self.height



       self.graph_section.place(relx=0.16, rely=0.05, relwidth=0.68, relheight=0.55)
       self.graph_section_underbar.place(relx=0.16, rely=0.54, relheight=0.06, relwidth=0.68)





       '''

       self.tp_width = 1440
       self.tp_height = 810



       self.time_period_button_frame = Canvas(master, bg=self.secondary_background_color, highlightthickness=0)

       b1_left = self.time_period_button_frame.create_oval(int(0.00347222222 * self.tp_height),
                                                           int(0.00347222222 * self.tp_height),
                                                           0.92 * 0.1 * self.tp_height, 0.92 * 0.1 * self.tp_height,
                                                           fill=self.secondary_background_color,
                                                           outline=self.main_text_color,
                                                           width=int(0.003125 * self.tp_width))

       b1_right = self.time_period_button_frame.create_oval(int(0.25 * self.tp_width - 0.92 * 0.1 * self.tp_height),
                                                            int(0.00347222222 * self.tp_height),
                                                            0.993 * 0.25 * self.tp_width, 0.92 * 0.1 * self.tp_height,
                                                            fill=self.secondary_background_color,
                                                            outline=self.main_text_color,
                                                            width=int(0.003125 * self.tp_width))

       b1_connector = self.time_period_button_frame.create_rectangle(int(0.92 * 0.1 * self.tp_height / 2),
                                                                     int(0.00347222222 * self.tp_height),
                                                                     0.25 * self.tp_width - int(
                                                                         0.92 * 0.1 * self.tp_height / 2),
                                                                     0.92 * 0.1 * self.tp_height,
                                                                     outline=self.main_text_color,
                                                                     width=int(0.003125 * self.tp_width))

       b1_fill = self.time_period_button_frame.create_rectangle(
           int(0.92 * 0.1 * self.tp_height / 2) - round(0.00173611111 * self.tp_height + 1),
           int(0.00347222222 * self.tp_height) + round(0.00347222222 * self.tp_height),
           0.25 * self.tp_width - int(0.92 * 0.1 * self.tp_height / 2) + round(0.00173611111 * self.tp_height),
           0.92 * 0.1 * self.tp_height - round(0.00347222222 * self.tp_height), outline=self.secondary_background_color,
           fill=self.secondary_background_color)

       self.time_period_button_frame.place(relx=0.2, rely=0.5, relwidth=0.25, relheight=0.1)

       self.time_period_button = Button(self.master, text="a;wdgh",
                                        highlightbackground=self.secondary_background_color,
                                        highlightthickness=round(0.05208333333 * self.tp_height),
                                        fg=self.highlighted_text_color,
                                        font=(self.font_c, round(0.03298611111 * self.tp_height)),
                                        activeforeground=self.dull_highlight, command=lambda: self.input(-1))

       self.time_period_button.place(relx=0.225, rely=0.5055, relwidth=0.199, relheight=0.081)

       '''

       self.okay_button = Canvas(master, bg=self.edge_color, highlightthickness=0)


       self.real_okay_button = Button(master, text="Edit Sleep Data",
                                      highlightbackground=self.edge_color,
                                      highlightthickness=round(0.05208333333 * self.height_input_window),
                                      fg=self.cancel_color, font=(self.font_c, round(0.015625 * self.width)),
                                      activeforeground=self.dull_highlight, command=lambda: self.edit_data())



       b1_left = self.okay_button.create_oval(int(0.00347222222 * self.height_input_window),
                                              int(0.00347222222 * self.height_input_window),
                                              0.92 * 0.1 * self.height_input_window,
                                              0.92 * 0.1 * self.height_input_window,
                                              fill=self.edge_color, outline=self.main_text_color,
                                              width=int(0.003125 * self.width_input_window))

       b1_right = self.okay_button.create_oval(
           int(0.25 * self.width_input_window - 0.92 * 0.1 * self.height_input_window),
           int(0.00347222222 * self.height_input_window),
           0.993 * 0.25 * self.width_input_window, 0.92 * 0.1 * self.height_input_window,
           fill=self.edge_color,
           outline=self.main_text_color, width=int(0.003125 * self.width_input_window))

       b1_connector = self.okay_button.create_rectangle(int(0.92 * 0.1 * self.height_input_window / 2),
                                                        int(0.00347222222 * self.height_input_window),
                                                        0.25 * self.width_input_window - int(
                                                            0.92 * 0.1 * self.height_input_window / 2),
                                                        0.92 * 0.1 * self.height_input_window,
                                                        outline=self.main_text_color,
                                                        width=int(0.003125 * self.width_input_window))

       b1_fill = self.okay_button.create_rectangle(
           int(0.92 * 0.1 * self.height_input_window / 2) - round(0.00173611111 * self.height_input_window + 1),
           int(0.00347222222 * self.height_input_window) + round(0.00347222222 * self.height_input_window),
           0.25 * self.width_input_window - int(0.92 * 0.1 * self.height_input_window / 2) + round(
               0.00173611111 * self.height_input_window),
           0.92 * 0.1 * self.height_input_window - round(0.00347222222 * self.height_input_window),
           outline=self.edge_color,
           fill=self.edge_color)


       self.okay_button.place(relx=0.63, rely=0.555, width=0.25 * self.width_input_window,
                              height=0.1 * self.height_input_window)

       self.real_okay_button.place(relx=0.65, rely=0.558, width=0.199 * self.width_input_window,
                                   height=0.081 * self.height_input_window)


























       self.update_graph()

   def update_graph(self):

       self.graph.delete("all")

       x_zero = 0.05

       x_axis = self.graph.create_line(round(x_zero * self.graph_width),
                                                round(0.9 * self.graph_height),
                                                round(0.99 * self.graph_width),
                                                round(0.9 * self.graph_height), width=3,
                                                fill=self.main_text_color)

       y_axis = self.graph.create_line(round(x_zero * self.graph_width),
                                       round(0.01 * self.graph_height),
                                       round(x_zero * self.graph_width),
                                       round(0.903 * self.graph_height), width=3,
                                       fill=self.main_text_color)








       self.hours = self.graph.create_text(round(0.001 * self.graph_width), round( x_zero * self.graph_height),
                                                     text="Hours \n Slept", fill=self.main_text_color,
                                                     font=(self.font_c, round(0.01197916666 * self.width)),
                                                     anchor="w")

       self.graph.create_text(round(0.03 * self.graph_width), round((0.9 - 0.004) * self.graph_height),
                              text="0", fill=self.main_text_color,
                              font=(self.font_c, round(0.00885416666 * self.width)),
                              anchor="w")

       #self.graph.create_oval(300,300,310,310, fill = "red")
       #self.graph.create_oval(500, 500, 505, 505, fill="red")


       self.date_range = []

       i = self.time_period
       high = 10

       while i > 0:

           self.date_range.append(self.master_data_storage[i * -1][3])

           if self.date_range[-1] > high:

               high = self.date_range[-1]

           i -= 1

       high = int(high+2) - (int(high) % 2)

       y_increment = 0.75/(high/2 )
       x_increment = 0.92/(len(self.date_range))
       buffer = x_increment/2

       p = 0


       while p < high/2:

           y_value = 0.15 + p * y_increment

           self.graph.create_line(round((x_zero + 0.002) * self.graph_width),
                                  round(y_value * self.graph_height),
                                  round(0.99 * self.graph_width),
                                  round(y_value * self.graph_height), width=2,
                                  fill=self.dull_graph_color)

           self.graph.create_text(round(0.03 * self.graph_width), round((y_value - 0.004) * self.graph_height),
                                  text=high - p*2, fill=self.main_text_color,
                                  font=(self.font_c, round(0.00885416666 * self.width)),
                                  anchor="w")

           p+= 1


       print(y_increment)

       y_increment = y_increment/2

       print(y_increment)


       q = 1
       diff = round(0.00260416666 * self.width)

       for point in self.date_range:

           print(point)

           if point >= 0:
               xpoint = round(((q-1) * x_increment + x_zero + buffer) * self.graph_width)
               ypoint = round((0.75 - (point * y_increment) + 0.15) * self.graph_height)

               #self.graph.create_text(round(xpoint * self.graph_width),round(ypoint * self.graph_height), text = "UWU", fill = "red")
               self.graph.create_oval(xpoint - diff, ypoint - diff, xpoint + diff, ypoint + diff,
                                      fill=self.cancel_color, width = 0)

               if q < len(self.date_range):

                   if self.date_range[q] >= 0:
                       x2point = round(((q) * x_increment + x_zero + buffer) * self.graph_width)
                       y2point = round((0.75 - (self.date_range[q] * y_increment) + 0.15) * self.graph_height)

                       self.graph.create_line(xpoint, ypoint, x2point, y2point,
                                              fill=self.cancel_color, width=round(0.0015625 * self.width))



           q += 1




       #7 displays days of the week, 14 displays days of the week and of the month, 28 displays just dates? try it out, 84 displays just the first day of every week, 182 displays months, 365 displays months

       g = 0

       if self.time_period == 7 or g == self.time_period - 1:



           while g < self.time_period:



               date = self.master_data_storage[-1 *(self.time_period-g)]

               day_of_the_week = self.number_into_day_of_the_week_generator_thingy(
                   datetime.datetime(date[0], date[1], date[2]).weekday())


               self.graph.create_text(round((x_increment * (g) + x_zero + buffer) * self.graph_width),
                                      round(0.94 * self.graph_height),
                                      text=day_of_the_week, fill=self.main_text_color, font=(self.font_c, round(0.01041666666*self.width)))

               g += 1

       elif self.time_period == 14 or g == self.time_period - 1:



           while g < self.time_period:

               date = self.master_data_storage[-1 * (self.time_period - g)]



               day_of_the_week = self.number_into_day_of_the_week_generator_thingy(
                   datetime.datetime(date[0], date[1], date[2]).weekday())

               day_of_the_week = day_of_the_week[0:3] + "\n" + str(date[2]) + self.ordinal_indicator_wow_look_fancy_title(date[2])

               self.graph.create_text(round((x_increment * (g) + x_zero + buffer) * self.graph_width),
                                      round(0.95 * self.graph_height),
                                      text=day_of_the_week, fill=self.main_text_color, font=(self.font_c, round(0.00989583333*self.width)))

               g += 1

       elif self.time_period == 28:



           while g < self.time_period or g == self.time_period - 1:

               if g % 2 == 1:
                   date = self.master_data_storage[-1 * (self.time_period - g)]

                   dote = str(date[1]) + "/" + str(date[2])

                   self.graph.create_text(round((x_increment * (g) + x_zero + buffer) * self.graph_width),
                                          round(0.95 * self.graph_height),
                                          text=dote, fill=self.main_text_color, font=(self.font_c, round(0.00989583333*self.width)))



               g += 1

       elif self.time_period == 84:



           while g < self.time_period or g == self.time_period - 1:

               if g % 7 == 5:
                   date = self.master_data_storage[-1 * (self.time_period - g)]

                   dote = self.number_into_month_of_the_year_generator_thingy(date[1])

                   self.graph.create_text(round((x_increment * (g) + x_zero + buffer) * self.graph_width),
                                          round(0.95 * self.graph_height),
                                          text=dote, fill=self.main_text_color, font=(self.font_c, round(0.00989583333*self.width)))



               g += 1

       elif self.time_period == 182:



           while g < self.time_period:

               if g % 14 == 0 or g == self.time_period - 1:
                   date = self.master_data_storage[-1 * (self.time_period - g)]

                   dote = self.number_into_month_of_the_year_generator_thingy(date[1])

                   self.graph.create_text(round((x_increment * (g) + x_zero + buffer) * self.graph_width),
                                          round(0.95 * self.graph_height),
                                          text=dote, fill=self.main_text_color, font=(self.font_c, round(0.00989583333*self.width)))



               g += 1

       elif self.time_period == 365:



           while g < self.time_period:

               if g % 30 == 0:
                   date = self.master_data_storage[-1 * (self.time_period - g)]

                   dote = self.number_into_month_of_the_year_generator_thingy(date[1])

                   self.graph.create_text(round((x_increment * (g) + x_zero + buffer) * self.graph_width),
                                          round(0.95 * self.graph_height),
                                          text=dote, fill=self.main_text_color, font=(self.font_c, round(0.00989583333*self.width)))



               g += 1

       if self.time_period == 7:

           self.words = "Past Week"

       elif self.time_period  == 14:

           self.words = "Past 2 weeks"


       elif self.time_period  == 28:

           self.words = "Past month"

       elif self.time_period  == 84:

           self.words = "Past 3 months"

       elif self.time_period  == 182:

           self.words = "Past 6 months"

       elif self.time_period  == 365:

           self.words = "Past year"

       self.rokay_button = Canvas(self.master, bg=self.secondary_background_color, highlightthickness=0)

       self.rreal_okay_button = Button(self.master, text=self.words,
                                       highlightbackground=self.left_background_color,
                                       highlightthickness=round(0.05208333333 * self.height_input_window),
                                       fg=self.main_text_color, font=(self.font_c, round(0.03703703703*self.height)),
                                       activeforeground=self.dull_highlight, command=lambda: self.select_time())

       '''
       b1_left = self.rokay_button.create_oval(int(0.00347222222 * self.height_input_window),
                                              int(0.00347222222 * self.height_input_window),
                                              0.92 * 0.1 * self.height_input_window,
                                              0.92 * 0.1 * self.height_input_window,
                                              fill=self.secondary_background_color, outline=self.main_text_color,
                                              width=int(0.003125 * self.width_input_window))

       b1_right = self.rokay_button.create_oval(
           int(0.25 * self.width_input_window - 0.92 * 0.1 * self.height_input_window),
           int(0.00347222222 * self.height_input_window),
           0.993 * 0.25 * self.width_input_window, 0.92 * 0.1 * self.height_input_window,
           fill=self.secondary_background_color,
           outline=self.main_text_color, width=int(0.003125 * self.width_input_window))'''

       b1_connector = self.rokay_button.create_rectangle(int(0.92 * 0.1 * self.height_input_window / 2),
                                                         int(0.00347222222 * self.height_input_window),
                                                         0.25 * self.width_input_window - int(
                                                             0.92 * 0.1 * self.height_input_window / 2),
                                                         0.92 * 0.1 * self.height_input_window,
                                                         outline=self.main_text_color,
                                                         width=int(0.003125 * self.width_input_window))
       '''
       b1_fill = self.rokay_button.create_rectangle(
           int(0.92 * 0.1 * self.height_input_window / 2) - round(0.00173611111 * self.height_input_window + 1),
           int(0.00347222222 * self.height_input_window) + round(0.00347222222 * self.height_input_window),
           0.25 * self.width_input_window - int(0.92 * 0.1 * self.height_input_window / 2) + round(
               0.00173611111 * self.height_input_window),
           0.92 * 0.1 * self.height_input_window - round(0.00347222222 * self.height_input_window),
           outline=self.secondary_background_color,
           fill=self.secondary_background_color)'''

       self.rokay_button.place(relx=0.63, rely=0.017, width=0.25 * self.width_input_window,
                               height=0.1 * self.height_input_window)

       self.rreal_okay_button.place(relx=0.65, rely=0.02, width=0.197 * self.width_input_window,
                                    height=0.081 * self.height_input_window)

       self.time_chosen = Label(self.master, text="Show data over:", font=(self.font_c, round(0.0234375 * self.width)),
                                background=self.secondary_background_color,
                                fg=self.main_text_color)
       self.time_chosen.place(relx=0.475, rely=0.019, relwidth=0.17, relheight=0.07)




       self.graph_title = Label(self.master, text="Sleep per night over the " + self.words.lower(), font=(self.font_a, round(0.02604166666*self.width)),
                                background=self.edge_color,
                                fg=self.main_text_color)
       self.graph_title.place(relx=0.17, rely=0.55, relwidth=0.46, relheight=0.07)

   def select_time(self):

       x = self.master.winfo_x()
       y = self.master.winfo_y()


       time_window = Toplevel(self.master, width=self.time_period_width, height=self.time_period_height,
                               bg=self.secondary_background_color)

       time_window.geometry("%dx%d+%d+%d" % (self.time_period_width, self.time_period_height,  x + round(0.64583333333 * self.width), y))


       s = 0

       def weekly():


           self.time_period = 7
           self.update_graph()

           time_window.destroy()
           self.update_stats()

       def biweekly():


           self.time_period = 14
           self.update_graph()

           time_window.destroy()
           self.update_stats()


       def monthly():


           self.time_period = 28
           self.update_graph()

           time_window.destroy()
           self.update_stats()

       def quarterly():


           self.time_period = 84
           self.update_graph()

           time_window.destroy()
           self.update_stats()

       def halfyearly():


           self.time_period = 182
           self.update_graph()

           time_window.destroy()
           self.update_stats()

       def yearly():


           self.time_period = 365
           self.update_graph()

           time_window.destroy()
           self.update_stats()




       self.weekly_frame = Canvas(time_window, bg=self.secondary_background_color, highlightthickness=0)

       self.weekly_button = Button(time_window, text="Past Week",
                                 highlightbackground=self.left_background_color,
                                 highlightthickness=round(0.05208333333 * self.height_input_window),
                                 fg=self.main_text_color, font=(self.font_c, round(0.03703703703*self.height)),
                                 activeforeground=self.dull_highlight, command=lambda: weekly())

       b1_connector = self.weekly_frame.create_rectangle(int(0.92 * 0.1 * self.height_input_window / 2),
                                                       int(0.00347222222 * self.height_input_window),
                                                       0.25 * self.width_input_window - int(
                                                           0.92 * 0.1 * self.height_input_window / 2),
                                                       0.92 * 0.1 * self.height_input_window,
                                                       outline=self.main_text_color,
                                                       width=int(0.003125 * self.width_input_window))

       self.weekly_frame.place(relx=-0.095, rely=0.023, width=0.25 * self.width_input_window,
                             height=0.1 * self.height_input_window)

       self.weekly_button.place(relx=0.03, rely=0.026, width=0.197 * self.width_input_window,
                              height=0.081 * self.height_input_window)

       self.biweekly_frame = Canvas(time_window, bg=self.secondary_background_color, highlightthickness=0)

       self.biweekly_button = Button(time_window, text="Past 2 weeks",
                                 highlightbackground=self.left_background_color,
                                 highlightthickness=round(0.05208333333 * self.height_input_window),
                                 fg=self.main_text_color, font=(self.font_c, round(0.03703703703*self.height)),
                                 activeforeground=self.dull_highlight, command=lambda: biweekly())

       b1_connector = self.biweekly_frame.create_rectangle(int(0.92 * 0.1 * self.height_input_window / 2),
                                                       int(0.00347222222 * self.height_input_window),
                                                       0.25 * self.width_input_window - int(
                                                           0.92 * 0.1 * self.height_input_window / 2),
                                                       0.92 * 0.1 * self.height_input_window,
                                                       outline=self.main_text_color,
                                                       width=int(0.003125 * self.width_input_window))

       self.biweekly_frame.place(relx=-0.095, rely=0.023 + 0.16 , width=0.25 * self.width_input_window,
                             height=0.1 * self.height_input_window)

       self.biweekly_button.place(relx=0.03, rely=0.026 + 0.16, width=0.197 * self.width_input_window,
                              height=0.081 * self.height_input_window)

       self.monthly_frame = Canvas(time_window, bg=self.secondary_background_color, highlightthickness=0)

       self.monthly_button = Button(time_window, text= "Past month",
                                 highlightbackground=self.left_background_color,
                                 highlightthickness=round(0.05208333333 * self.height_input_window),
                                 fg=self.main_text_color, font=(self.font_c, round(0.03703703703*self.height)),
                                 activeforeground=self.dull_highlight, command=lambda: monthly())

       b1_connector = self.monthly_frame.create_rectangle(int(0.92 * 0.1 * self.height_input_window / 2),
                                                       int(0.00347222222 * self.height_input_window),
                                                       0.25 * self.width_input_window - int(
                                                           0.92 * 0.1 * self.height_input_window / 2),
                                                       0.92 * 0.1 * self.height_input_window,
                                                       outline=self.main_text_color,
                                                       width=int(0.003125 * self.width_input_window))

       self.monthly_frame.place(relx=-0.095, rely=0.023 + 0.16 * 2, width=0.25 * self.width_input_window,
                             height=0.1 * self.height_input_window)

       self.monthly_button.place(relx=0.03, rely=0.026 + 0.16 * 2, width=0.197 * self.width_input_window,
                              height=0.081 * self.height_input_window)

       self.quarterly_frame = Canvas(time_window, bg=self.secondary_background_color, highlightthickness=0)

       self.quarterly_button = Button(time_window, text="Past 3 months",
                                 highlightbackground=self.left_background_color,
                                 highlightthickness=round(0.05208333333 * self.height_input_window),
                                 fg=self.main_text_color, font=(self.font_c, round(0.03703703703*self.height)),
                                 activeforeground=self.dull_highlight, command=lambda: quarterly())

       b1_connector = self.quarterly_frame.create_rectangle(int(0.92 * 0.1 * self.height_input_window / 2),
                                                       int(0.00347222222 * self.height_input_window),
                                                       0.25 * self.width_input_window - int(
                                                           0.92 * 0.1 * self.height_input_window / 2),
                                                       0.92 * 0.1 * self.height_input_window,
                                                       outline=self.main_text_color,
                                                       width=int(0.003125 * self.width_input_window))

       self.quarterly_frame.place(relx=-0.095, rely=0.023 + 0.16 * 3, width=0.25 * self.width_input_window,
                             height=0.1 * self.height_input_window)

       self.quarterly_button.place(relx=0.03, rely=0.026 + 0.16 * 3, width=0.197 * self.width_input_window,
                              height=0.081 * self.height_input_window)

       self.halfyearly_frame = Canvas(time_window, bg=self.secondary_background_color, highlightthickness=0)

       self.halfyearly_button = Button(time_window, text="Past 6 months",
                                 highlightbackground=self.left_background_color,
                                 highlightthickness=round(0.05208333333 * self.height_input_window),
                                 fg=self.main_text_color, font=(self.font_c, round(0.03703703703*self.height)),
                                 activeforeground=self.dull_highlight, command=lambda: halfyearly())

       b1_connector = self.halfyearly_frame.create_rectangle(int(0.92 * 0.1 * self.height_input_window / 2),
                                                       int(0.00347222222 * self.height_input_window),
                                                       0.25 * self.width_input_window - int(
                                                           0.92 * 0.1 * self.height_input_window / 2),
                                                       0.92 * 0.1 * self.height_input_window,
                                                       outline=self.main_text_color,
                                                       width=int(0.003125 * self.width_input_window))

       self.halfyearly_frame.place(relx=-0.095, rely=0.023 + 0.16 * 4, width=0.25 * self.width_input_window,
                             height=0.1 * self.height_input_window)

       self.halfyearly_button.place(relx=0.03, rely=0.026 + 0.16 * 4, width=0.197 * self.width_input_window,
                              height=0.081 * self.height_input_window)

       self.yearly_frame = Canvas(time_window, bg=self.secondary_background_color, highlightthickness=0)

       self.yearly_button = Button(time_window, text= "Past year",
                                 highlightbackground=self.left_background_color,
                                 highlightthickness=round(0.05208333333 * self.height_input_window),
                                 fg=self.main_text_color, font=(self.font_c, round(0.03703703703*self.height)),
                                 activeforeground=self.dull_highlight, command=lambda: yearly())

       b1_connector = self.yearly_frame.create_rectangle(int(0.92 * 0.1 * self.height_input_window / 2),
                                                       int(0.00347222222 * self.height_input_window),
                                                       0.25 * self.width_input_window - int(
                                                           0.92 * 0.1 * self.height_input_window / 2),
                                                       0.92 * 0.1 * self.height_input_window,
                                                       outline=self.main_text_color,
                                                       width=int(0.003125 * self.width_input_window))

       self.yearly_frame.place(relx=-0.095, rely=0.023 + 0.16 * 5, width=0.25 * self.width_input_window,
                             height=0.1 * self.height_input_window)

       self.yearly_button.place(relx=0.03, rely=0.026 + 0.16 * 5, width=0.197 * self.width_input_window,
                              height=0.081 * self.height_input_window)

   # right section

   def right_section(self, master):

       self.right_sidebar = Canvas(master, bg=self.secondary_background_color, highlightthickness=0)

       self.r_topbar = Canvas(master, bg=self.edge_color, highlightthickness=0)


       r_corner_nw = self.dashboard_frame.create_oval(0.85 * self.width, 0.01 * self.height, 0.895 * self.width, 0.09 * self.height, fill=self.edge_color, outline=self.edge_color)

       r_corner_ne = self.dashboard_frame.create_oval(0.945 * self.width, 0.01 * self.height, 0.989 * self.width, 0.09 * self.height, fill=self.edge_color, outline=self.edge_color)

       r_corner_se = self.dashboard_frame.create_oval(0.945 * self.width, 0.91 * self.height, 0.989 * self.width, 0.99 * self.height, fill=self.secondary_background_color, outline=self.secondary_background_color)

       r_corner_sw = self.dashboard_frame.create_oval(0.85 * self.width, 0.91 * self.height, 0.895 * self.width, 0.99 * self.height, fill=self.secondary_background_color, outline=self.secondary_background_color)

       r_edge = self.dashboard_frame.create_rectangle(0.8725 * self.width, 0.01 * self.height, 0.9665 * self.width, 0.99 * self.height, fill=self.secondary_background_color, outline=self.secondary_background_color)

       r_topedge = self.dashboard_frame.create_rectangle(0.8725 * self.width, 0.01 * self.height, 0.9665 * self.width, 0.05 * self.height, fill=self.edge_color, outline=self.edge_color)


       self.right_sidebar.place(relx=0.85, rely=0.05, relwidth=0.14, relheight=0.9)

       self.r_topbar.place(relx=0.85, rely=0.05, relwidth=0.14, relheight=0.035)

       self.header = Label(master, text = "Stats", font = (self.font_a, round(0.03645833333*self.width)), fg = self.main_text_color, bg = self.edge_color)
       self.header.place(relx=0.87,rely=0.01,relwidth=0.1,relheight=0.07)

       self.update_stats()

   def update_stats(self):


       if self.time_period == 7:

           period = "over the past week:"

       if self.time_period == 14:
           period = "over the past 2 weeks:"

       if self.time_period == 28:
           period = "over the past month:"

       if self.time_period == 84:
           period = "over the past 3 months:"

       if self.time_period == 182:
           period = "over the past 6 months:"

       if self.time_period == 365:
           period = "over the past year:"





       self.right_sidebar.delete("all")

       self.right_sidebar.create_text(round(0.0703125*self.width),round(0.0390625*self.width), font = (self.font_b, round(0.015625*self.width)), text = "Total time slept", fill = self.main_text_color)
       self.right_sidebar.create_text(round(0.0703125 * self.width), round(0.05729166666*self.width),
                                      font=(self.font_b, round(0.01197916666 * self.width)), text=period,
                                      fill=self.main_text_color)

       self.right_sidebar.create_text(round(0.0703125 * self.width), round(0.08333333333*self.width),
                                      font=(self.font_b, round(0.02083333333*self.width)), text=self.calculate_total(),
                                      fill=self.highlighted_text_color)

       self.right_sidebar.create_line(round(0.01041666666*self.width),round(0.11458333333*self.width),round(0.13020833333*self.width),round(0.11458333333*self.width), width = round(0.0015625*self.width), fill = self.main_text_color)





       self.right_sidebar.create_text(round(0.0703125 * self.width), round(0.14583333333*self.width),
                                      font=(self.font_b, round(0.015625 * self.width)), text="Average amount \nof sleep per night",
                                      fill=self.main_text_color)
       self.right_sidebar.create_text(round(0.0703125 * self.width), round(0.171875*self.width),
                                      font=(self.font_b, round(0.01197916666 * self.width)), text=period,
                                      fill=self.main_text_color)

       self.right_sidebar.create_text(round(0.0703125 * self.width), round(0.19791666666*self.width),
                                      font=(self.font_b, round(0.02083333333*self.width)), text=self.calculate_average(),
                                      fill=self.highlighted_text_color)

       self.right_sidebar.create_line(round(0.01041666666*self.width), round(0.22916666666*self.width), round(0.13020833333*self.width), round(0.22916666666*self.width), width=round(0.0015625*self.width), fill=self.main_text_color)




       self.right_sidebar.create_text(round(0.0703125 * self.width), round(0.25520833333*self.width),
                                      font=(self.font_b, round(0.015625/1.2 * self.width)), text="Average interruptions \n           per night",
                                      fill=self.main_text_color)
       self.right_sidebar.create_text(round(0.0703125 * self.width), round(0.28125*self.width),
                                      font=(self.font_b, round(0.015625/1.2 * self.width)), text=period,
                                      fill=self.main_text_color)

       self.right_sidebar.create_text(round(0.0703125 * self.width), round(0.3046875*self.width),
                                      font=(self.font_b, round(0.02083333333*self.width)), text=self.calculate_average_interruptions(),
                                      fill=self.highlighted_text_color)

       self.right_sidebar.create_line(round(0.01041666666*self.width), round(0.3359375*self.width), round(0.13020833333*self.width), round(0.3359375*self.width), width=round(0.0015625*self.width), fill=self.main_text_color)






       self.right_sidebar.create_text(round(0.0703125 * self.width), round(0.38020833333*self.width),
                                      font=(self.font_b, round(0.015625/0.7 * self.width)),
                                      text="Healthy \n  Sleep \n Streak",
                                      fill=self.main_text_color)
       self.right_sidebar.create_text(round(0.0703125 * self.width), round(0.43229166666*self.width),
                                      font=(self.font_b, round(0.015625 / 1.7 * self.width)),
                                      text="(9 or more hours per night)",
                                      fill=self.main_text_color)

       self.right_sidebar.create_text(round(0.0703125 * self.width), round(0.453125*self.width),
                                      font=(self.font_b, round(0.02083333333*self.width)), text=self.calculate_streak(),
                                      fill=self.highlighted_text_color)
       '''
       self.right_sidebar.create_text(round(0.0703125 * self.width), 920,
                                      font=(self.font_b, round(0.015625 / 1.5 * self.width)),
                                      text="How pifitully low",
                                      fill=self.main_text_color)'''

   def calculate_total(self):

       count = self.time_period
       total = 0

       while count > 0:

           alsuhdf = self.master_data_storage[-1 * count][3]

           if alsuhdf > 0:

               total += alsuhdf


           count-=1

           print(total)

       return str(round(total,2)) + " hours"

   def calculate_average(self):

       count = self.time_period
       total = 0
       self.active_days = 0

       while count > 0:

           alsuhdf = self.master_data_storage[-1 * count][3]

           if alsuhdf > 0:
               total += alsuhdf
               self.active_days += 1

           count -= 1

       if self.active_days > 0:
           return str(round((total / self.active_days), 2)) + " hours"

       else:

           return "0 hours"

   def calculate_average_interruptions(self):

       count = self.time_period
       total = 0
       self.active_days = 0

       while count > 0:

           alsuhdf = self.master_data_storage[-1 * count][3]

           if alsuhdf > 0:
               total += len(self.master_data_storage[-1 * count])-5
               self.active_days += 1
           count-=1

       if self.active_days > 0:
           return round(total/self.active_days)

       else:

           return 0

   def calculate_streak(self):

       days = 0

       while self.master_data_storage[-1 * (days+1)][3] >= 9:

           days += 1

       return str(days) + " days"

   # data interaction

   def process_data(self, file):

       data_table = []

       with open(file, "r") as data:


           datalines = []
           datalines = data.readlines()


           if len(datalines) > 0:

               for line in datalines:

                   # put try catch exceptions in front of EVERYTHING

                   entry = []
                   entry.append(int(line[0:(line.find("."))]))
                   entry.append(int(line[(line.find(".") + 1):(line.find(","))]))
                   entry.append(int(line[(line.find(",") + 1):(line.find("["))]))
                   entry.append(float(line[(line.find("[") + 1):(line.find("]"))]))

                   sleeps = 0

                   for e in line:

                       if e == "(":
                           sleeps += 1

                   while sleeps > 0:

                       reeeee_variable_name = []

                       reeeee_variable_name.append(line[(line.find("(") + 1):(line.find("-"))])
                       reeeee_variable_name.append(line[(line.find("-") + 1):(line.find(")"))])


                       entry.append(reeeee_variable_name)
                       line = line[(line.find(")") + 1):]
                       sleeps -= 1

                   data_table.append(entry)

               return data_table

           else:

               starter = []
               starter.append(18)
               starter.append(1)
               starter.append(1)
               starter.append(-1)

               data_table.append(starter)

               return data_table

   def update_data(self):

       now = datetime.datetime.now()

       current_year = int(now.strftime("%y"))
       current_month = int(now.strftime("%m"))
       current_day = int(now.strftime("%d"))

       print(len(self.master_data_storage))
       last_known_date = self.master_data_storage[-1]


       last_known_year = int(last_known_date[0])
       last_known_month = int(last_known_date[1])
       last_known_day = int(last_known_date[2]) + 1

       while last_known_year < current_year:

           while last_known_month < 13:

               day_limit = self.days_in_a_month(last_known_month, last_known_year)

               while last_known_day <= day_limit:
                   missing_date = []
                   missing_date.append(last_known_year)
                   missing_date.append(last_known_month)
                   missing_date.append(last_known_day)
                   missing_date.append(-1)

                   self.master_data_storage.append(missing_date)

                   last_known_day += 1

               last_known_day = 1
               last_known_month += 1

           last_known_month = 1
           last_known_year += 1

       while last_known_month < current_month:

           day_limit = self.days_in_a_month(last_known_month, last_known_year)

           while last_known_day <= day_limit:
               missing_date = []
               missing_date.append(last_known_year)
               missing_date.append(last_known_month)
               missing_date.append(last_known_day)
               missing_date.append(-1)

               self.master_data_storage.append(missing_date)

               last_known_day += 1

           last_known_day = 1
           last_known_month += 1

       while last_known_day <= current_day:
           missing_date = []
           missing_date.append(last_known_year)
           missing_date.append(last_known_month)
           missing_date.append(last_known_day)
           missing_date.append(-1)

           self.master_data_storage.append(missing_date)

           last_known_day += 1

   def save_data(self, file):

       stringed_data = []

       for day in self.master_data_storage:

           string_day = str(day[0]) + "." + str(day[1]) + "," + str(day[2]) + "["

           if len(day) == 4:

               string_day += str(day[3]) + "]"

           else:

               string_day += str(day[3]) + "]"

               count = 4

               while count < len(day):

                   string_day = string_day + "(" + str((day[count])[0]) + "-" + str((day[count])[1]) + ")"
                   count += 1

           stringed_data.append(string_day)

       open(file, 'w').close()

       with open(file, "a") as data:

           data.truncate()

           for line in stringed_data:

               data.write(line + "\n")

   def store_data(self, date_index, data, hours_slept):

       the_day = []

       the_day.append((self.master_data_storage[date_index])[0])
       the_day.append((self.master_data_storage[date_index])[1])
       the_day.append((self.master_data_storage[date_index])[2])
       the_day.append(hours_slept)


       if hours_slept > 0:

           for period in data:
               im_too_tired_to_come_up_with_variable_names = []

               im_too_tired_to_come_up_with_variable_names.append(period[0])
               im_too_tired_to_come_up_with_variable_names.append(period[1])
               the_day.append(im_too_tired_to_come_up_with_variable_names)

       self.master_data_storage[date_index] = the_day





       #rint(self.master_data_storage[date_index])
       self.save_data(self.data_file)

       self.update_sleep()
       self.update_calendar()
       self.update_graph()
       self.update_stats()

   def input(self, date_index, today):

       self.sleep_periods = []

       self.starting_points = []












       date = self.master_data_storage[date_index]

       day_of_the_week = self.number_into_day_of_the_week_generator_thingy(datetime.datetime(date[0], date[1], date[2]).weekday())
       month_of_the_year = self.number_into_month_of_the_year_generator_thingy(date[1])
       year_of_time = "20" + str(date[0])

       dat = day_of_the_week + ", " + month_of_the_year + " " + str(date[2]) + ", " + year_of_time



       input_window = Toplevel(self.master, width = self.true_width_input_window, height = self.true_height_input_window, bg = self.secondary_background_color)

       '''

       if today == 1:

           if self.clicks == 0:
               self.input_button.config(state='disable')

           else:
               self.input_button2.config(state='disable')'''







       main_canvas = Canvas(input_window, bg=self.secondary_background_color, highlightthickness=0)
       main_canvas.place(relx=0, rely=0, relwidth = 1, relheight = 1)

       topbar = Canvas(input_window, bg = self.edge_color, highlightthickness = 0)
       topbar.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.25)






       prompt = Label(input_window, text="Sleep Data - " + dat, font=(self.font_a, round(0.0390625*self.width)), fg=self.main_text_color,
                          bg=self.edge_color, anchor = 'w')
       prompt.place(relx = 0.02, rely = 0, relwidth = 1, relheight = 0.25)


       yesterdate = self.master_data_storage[date_index-1]
       yestermonth_of_the_year = self.number_into_month_of_the_year_generator_thingy(yesterdate[1])







       today_underbar = main_canvas.create_line(round(0.88 * self.true_width_input_window),
                                                round(0.41 * self.true_height_input_window),
                                                round(0.98 * self.true_width_input_window),
                                                round(0.41 * self.true_height_input_window), width=round(0.00104166666*self.width),
                                                fill=self.main_text_color)

       yesterday_underbar = main_canvas.create_line(round(0.02 * self.true_width_input_window),
                                                round(0.41 * self.true_height_input_window),
                                                round(0.12 * self.true_width_input_window),
                                                round(0.41 * self.true_height_input_window), width = round(0.00104166666*self.width),
                                                fill=self.main_text_color)



       today_label = Label(input_window, text=month_of_the_year + " " + str(date[2]),
                           font=(self.font_b, round(0.015625 * self.width)), bg=self.secondary_background_color,
                           fg=self.main_text_color)
       today_label.place(relx=0.88, rely=0.3, relwidth=0.1, relheight=0.1)

       yesterday_label = Label(input_window, text = yestermonth_of_the_year + " " + str(yesterdate[2]), font = (self.font_b, round(0.015625*self.width)), bg = self.secondary_background_color, fg = self.main_text_color)
       yesterday_label.place(relx=0.02, rely=0.3, relwidth=0.1, relheight=0.1)

       progress_frame = main_canvas.create_rectangle(round(0.05 * self.true_width_input_window),
                                                     round(0.5 * self.true_height_input_window),
                                                     round(0.95 * self.true_width_input_window),
                                                     round(0.56 * self.true_height_input_window),
                                                     outline=self.main_text_color, width=round(0.0015625 * self.width))

       progress_left_end = main_canvas.create_oval(
           round(0.05 * self.true_width_input_window) - round(0.03 * self.true_height_input_window),
           round(0.5 * self.true_height_input_window),
           round(0.05 * self.true_width_input_window) + round(0.03 * self.true_height_input_window),
           round(0.56 * self.true_height_input_window), outline=self.main_text_color,
           width=round(0.0015625 * self.width))

       progress_right_end = main_canvas.create_oval(
           round(0.95*self.true_width_input_window) - round(0.03 * self.true_height_input_window),
           round(0.5 * self.true_height_input_window),
           round(0.95*self.true_width_input_window) + round(0.03 * self.true_height_input_window),
           round(0.56 * self.true_height_input_window), outline=self.main_text_color,
           width=round(0.0015625 * self.width))


       progress_fill = main_canvas.create_rectangle(round(0.049 * self.true_width_input_window),
                                                     round(0.503 * self.true_height_input_window),
                                                     round(0.951 * self.true_width_input_window),
                                                     round(0.557 * self.true_height_input_window),
                                                     fill=self.secondary_background_color, outline = self.secondary_background_color)






       self.okay_button = Canvas(input_window, bg=self.secondary_background_color, highlightthickness=0)
       self.okay_button.place(relx = 0.75, rely = 0.8, width = 0.25*self.width_input_window, height = 0.1*self.height_input_window)

       self.real_okay_button = Button(input_window, text="Okay, I'm done",
                                      highlightbackground=self.secondary_background_color,
                                      highlightthickness=round(0.05208333333 * self.height_input_window),
                                      fg=self.highlighted_text_color, font=(self.font_c, round(0.015625 * self.width)),
                                      activeforeground=self.dull_highlight, command=lambda: save_and_leave())

       self.real_okay_button.place(relx=0.772, rely=0.807, width=0.199*self.width_input_window, height=0.081*self.height_input_window)

       b1_left = self.okay_button.create_oval(int(0.00347222222 * self.height_input_window), int(0.00347222222 * self.height_input_window),
                                                0.92 * 0.1 * self.height_input_window, 0.92 * 0.1 * self.height_input_window,
                                                fill=self.secondary_background_color, outline=self.main_text_color,
                                                width=int(0.003125 * self.width_input_window))

       b1_right = self.okay_button.create_oval(int(0.25 * self.width_input_window - 0.92 * 0.1 * self.height_input_window),
                                                 int(0.00347222222 * self.height_input_window),
                                                 0.993 * 0.25 * self.width_input_window, 0.92 * 0.1 * self.height_input_window,
                                                 fill=self.secondary_background_color,
                                                 outline=self.main_text_color, width=int(0.003125 * self.width_input_window))

       b1_connector = self.okay_button.create_rectangle(int(0.92 * 0.1 * self.height_input_window / 2),
                                                          int(0.00347222222 * self.height_input_window),
                                                          0.25 * self.width_input_window - int(0.92 * 0.1 * self.height_input_window / 2),
                                                          0.92 * 0.1 * self.height_input_window, outline=self.main_text_color,
                                                          width=int(0.003125 * self.width_input_window))

       b1_fill = self.okay_button.create_rectangle(
           int(0.92 * 0.1 * self.height_input_window / 2) - round(0.00173611111 * self.height_input_window + 1),
           int(0.00347222222 * self.height_input_window) + round(0.00347222222 * self.height_input_window),
           0.25 * self.width_input_window - int(0.92 * 0.1 * self.height_input_window / 2) + round(0.00173611111 * self.height_input_window),
           0.92 * 0.1 * self.height_input_window - round(0.00347222222 * self.height_input_window), outline=self.secondary_background_color,
           fill=self.secondary_background_color)















       self.cancel_button = Canvas(input_window, bg=self.secondary_background_color, highlightthickness=0)
       self.cancel_button.place(relx=0.03, rely=0.8, width=0.25 * self.width_input_window, height=0.1 * self.height_input_window)

       self.real_cancel_button = Button(input_window, text="Delete this crap (clear)",
                                      highlightbackground=self.secondary_background_color,
                                      highlightthickness=round(0.05208333333 * self.height_input_window),
                                      fg=self.cancel_color, font=(self.font_c, round(0.03086419753*self.height_input_window)),
                                      activeforeground=self.dull_highlight, command=lambda: clearall())

       self.real_cancel_button.place(relx=0.052, rely=0.807, width=0.199 * self.width_input_window,
                                   height=0.081 * self.height_input_window)

       b1_left = self.cancel_button.create_oval(int(0.00347222222 * self.height_input_window),
                                              int(0.00347222222 * self.height_input_window),
                                              0.92 * 0.1 * self.height_input_window, 0.92 * 0.1 * self.height_input_window,
                                              fill=self.secondary_background_color, outline=self.main_text_color,
                                              width=int(0.003125 * self.width_input_window))

       b1_right = self.cancel_button.create_oval(int(0.25 * self.width_input_window - 0.92 * 0.1 * self.height_input_window),
                                               int(0.00347222222 * self.height_input_window),
                                               0.993 * 0.25 * self.width_input_window, 0.92 * 0.1 * self.height_input_window,
                                               fill=self.secondary_background_color,
                                               outline=self.main_text_color, width=int(0.003125 * self.width_input_window))

       b1_connector = self.cancel_button.create_rectangle(int(0.92 * 0.1 * self.height_input_window / 2),
                                                        int(0.00347222222 * self.height_input_window),
                                                        0.25 * self.width_input_window - int(
                                                            0.92 * 0.1 * self.height_input_window / 2),
                                                        0.92 * 0.1 * self.height_input_window, outline=self.main_text_color,
                                                        width=int(0.003125 * self.width_input_window))

       b1_fill = self.cancel_button.create_rectangle(
           int(0.92 * 0.1 * self.height_input_window / 2) - round(0.00173611111 * self.height_input_window + 1),
           int(0.00347222222 * self.height_input_window) + round(0.00347222222 * self.height_input_window),
           0.25 * self.width_input_window - int(0.92 * 0.1 * self.height_input_window / 2) + round(
               0.00173611111 * self.height_input_window),
           0.92 * 0.1 * self.height_input_window - round(0.00347222222 * self.height_input_window),
           outline=self.secondary_background_color,
           fill=self.secondary_background_color)








       xframe = Canvas(input_window, background = self.main_text_color, highlightthickness = 0)
       xframe.place(relx = 0.9481, rely = 0.034, width = round(0.034 * self.width), height = round(0.034 * self.width))

       self.exit_button = Button(input_window, text="X", highlightbackground=self.secondary_background_color,
                                 highlightthickness=round(0.05208333333 * self.height_input_window),
                                 fg=self.cancel_color,
                                 font=(self.font_c, round(0.03086419753 * self.height_input_window)),
                                 activeforeground=self.dull_highlight, command=lambda: leave())
       self.exit_button.place(relx=0.95, rely=0.04, width=round(0.03 * self.width), height=round(0.03 * self.width))











           # effective range is from ~0.04 to ~0.96 for x, and 0.5 to 0.56 for y



       self.movement_state = 0


       dummy = main_canvas.create_rectangle(0, 0, 1, 1)



       red_dot_list = []
       red_dot_list.append(dummy)
       red_dot_list.append(dummy)

       print(len(red_dot_list))


       main_slider = []
       main_slider.append(dummy)





       translated_width = self.true_width_input_window
       translated_height = self.true_height_input_window

       dot_color = self.dull_cancel



       self.relx = 0
       self.rely = 0

       self.limit = 0

       self.time_slept = 0
       time_slept_label = main_canvas.create_text(round(0.45 * self.true_width_input_window),
                                                   round(0.86 * self.true_height_input_window),
                                                   text="Time Slept:", fill=self.main_text_color,
                                                   font=(self.font_b, round(0.02083333333*self.width)))

       time_slept_display = main_canvas.create_text(round(0.55 * self.true_width_input_window),
                                                  round(0.86 * self.true_height_input_window),
                                                  text="--:--", fill=self.clock_color,
                                                  font=(self.font_b, round(0.02083333333*self.width)))




       def movement(event):



           x, y = input_window.winfo_pointerx() - input_window.winfo_rootx(), input_window.winfo_pointery() - input_window.winfo_rooty()

           self.relx = round(x/translated_width,8)
           self.rely = round(y/translated_height,8)



           print('{}, {}'.format(self.relx, self.rely) )
           '''

           print("next limit is . .. ")
           print(self.limit)



           print(len(self.starting_points))'''


           main_canvas.itemconfig(time_slept_display, text = total_time_slept())


           if 0.05 < self.relx < 0.95 and 0.5 < self.rely < 0.56 and self.movement_state == 0:


               if check_placed(self.relx) == True:

                   label_color = self.dull_bar_color
                   ddot_color = self.overlap_bar

                   circle_difference = 0.018
                   circley1 = 0.513
                   circley2 = 0.547

               else:

                   label_color = self.dull_cancel
                   ddot_color = self.dull_cancel
                   circle_difference = 0.022
                   circley1 = 0.509
                   circley2 = 0.553



               last_dot = red_dot_list[0]
               last_label = red_dot_list[1]

               main_canvas.delete(last_dot)
               main_canvas.delete(last_label)

               red_dot_list.clear()

               red_dot = main_canvas.create_oval(
                   round(self.relx * translated_width) - round(circle_difference * translated_height),
                   round(circley1 * translated_height),
                   round(self.relx * translated_width) + round(circle_difference * translated_height),
                   round(circley2 * translated_height), fill=ddot_color, width=0)

               new_label = main_canvas.create_text(round(self.relx * self.true_width_input_window),
                                                   round(0.45 * self.true_height_input_window),
                                                   text=time(self.relx), fill=label_color,
                                                   font=(self.font_c, round(0.015625 * self.width)))

               red_dot_list.append(red_dot)
               red_dot_list.append(new_label)


           elif self.movement_state == 0:



               last_dot = red_dot_list[0]
               last_label = red_dot_list[1]

               main_canvas.delete(last_dot)
               main_canvas.delete(last_label)

               red_dot_list.clear()

               dummy = main_canvas.create_rectangle(0, 0, 1, 1)
               red_dot_list.append(dummy)
               red_dot_list.append(dummy)





           elif self.movement_state == 1 and self.relx > self.starting_points[-1] and 0.05 < self.relx < self.limit:



               last_circle = main_slider[0]
               last_bar = main_slider[1]
               last_label = main_slider[2]

               main_canvas.delete(last_circle)
               main_canvas.delete(last_bar)
               main_canvas.delete(last_label)

               main_slider.clear()

               new_bar = main_canvas.create_rectangle(
                   round(self.starting_points[-1] * self.true_width_input_window),
                   round(0.512 * self.true_height_input_window),
                   round(self.relx * self.true_width_input_window),
                   round(0.548 * self.true_height_input_window),
                   fill=self.cancel_color,
                   outline=self.secondary_background_color, width=0)

               new_circle = main_canvas.create_oval(
                   round(self.relx * self.true_width_input_window) - round(0.035 * self.true_height_input_window),
                   round(0.495 * self.true_height_input_window),
                   round(self.relx * self.true_width_input_window) + round(0.035 * self.true_height_input_window),
                   round(0.565 * self.true_height_input_window), fill=self.cancel_color, width=0)

               new_label = main_canvas.create_text(round(self.relx * self.true_width_input_window),
                                                   round(0.45 * self.true_height_input_window),
                                                   text=time(self.relx), fill=self.cancel_color,
                                                   font=(self.font_c, round(0.015625 * self.width)))

               main_slider.append(new_circle)
               main_slider.append(new_bar)
               main_slider.append(new_label)
























       def click(event):








           if self.movement_state == 0 and 0.05 < self.relx < 0.95 and 0.5 < self.rely < 0.56 and check_placed(self.relx) == False:



               self.movement_state = 1


               last_dot = red_dot_list[0]
               last_label = red_dot_list[1]

               main_canvas.delete(last_dot)
               main_canvas.delete(last_label)
               red_dot_list.clear()
               red_dot_list.append(dummy)
               red_dot_list.append(dummy)
               self.starting_points.append((self.relx))

               new_circle = main_canvas.create_oval(
                   round(self.relx * self.true_width_input_window) - round(0.035 * self.true_height_input_window),
                   round(0.495 * self.true_height_input_window),
                   round(self.relx * self.true_width_input_window) + round(0.035 * self.true_height_input_window),
                   round(0.565 * self.true_height_input_window), fill=self.cancel_color, width=0)

               main_slider.append(new_circle)

               new_label = main_canvas.create_text(round(self.relx * self.true_width_input_window),
                                                   round(0.45 * self.true_height_input_window),
                                                   text=time(self.relx), fill=self.cancel_color,
                                                   font=(self.font_c, round(0.015625 * self.width)))

               main_slider.append(new_label)

               self.limit = next_limit(self.relx)







           elif self.starting_points[-1] < self.relx:

               #if total_time_slept_int() > 0:
                   #self.okay_button.config(state='normal')

               last_circle = main_slider[0]
               last_bar = main_slider[1]
               last_label = main_slider[2]

               main_canvas.delete(last_circle)
               main_canvas.delete(last_bar)
               main_canvas.delete(last_label)

               main_slider.clear()
               main_slider.append(dummy)

               period = []

               period.append(self.starting_points[-1])
               period.append(self.relx)

               self.movement_state = 0



               new_bar = main_canvas.create_rectangle(round(self.starting_points[-1] * self.true_width_input_window),
                                                      round(0.512 * self.true_height_input_window),
                                                      round(self.relx * self.true_width_input_window),
                                                      round(0.548 * self.true_height_input_window),
                                                      fill=self.clock_color,
                                                      outline=self.secondary_background_color, width=0)

               period.append(new_bar)

               self.sleep_periods.append(period)

















       def right_click(event):

           if self.movement_state == 0 and 0.05 < self.relx < 0.95 and 0.5 < self.rely < 0.56:

               death_value = 0

               for range in self.sleep_periods:

                   if range[0] < self.relx < range[1]:

                       main_canvas.delete(range[2])
                       self.sleep_periods.remove(range)
                       death_value = range[0]

               for starter in self.starting_points:

                   if starter == death_value:

                       self.starting_points.remove(starter)








           elif self.movement_state == 1 and 0.05 < self.relx < 0.95 and 0.5 < self.rely < 0.56:

               #if total_time_slept_int() > 0:
                   #self.okay_button.config(state='normal')

               last_circle = main_slider[0]
               last_bar = main_slider[1]
               last_label = main_slider[2]

               main_canvas.delete(last_circle)
               main_canvas.delete(last_bar)
               main_canvas.delete(last_label)

               main_slider.clear()
               main_slider.append(dummy)


               '''
               period = []

               period.append(self.starting_points[-1])
               period.append(self.relx)'''

               self.starting_points.pop(-1)

               self.movement_state = 0





       def check_placed(point):

           acceptable_point = 0

           for range in self.sleep_periods:

               if range[0] < point < range[1]:
                   acceptable_point = 1

           if acceptable_point == 0:

               return False

           else:

               return True


       def next_limit(point):

           difference = 1
           limit = 0.95

           if len(self.starting_points) > 1:



               for start in self.starting_points:

                   if point < start:



                       if start - point < difference:
                           difference = start - point
                           limit = start














           return limit




       def clearall():

           for instance in self.sleep_periods:

               main_canvas.delete(instance[2])

           self.sleep_periods.clear()
           self.starting_points.clear()



       def time(point):



           total_minutes = point_to_minute(point)
           hours = int(total_minutes / 60)
           minutes = format_minutes(int(total_minutes % 60))


           if hours == 0:

               return "12:{} pm".format(minutes)

           elif hours < 12:

               return "{}:{} pm".format(hours, minutes)

           elif hours == 12:

               return "12:{} am".format(minutes)

           elif 24 > hours > 12:

               hours -= 12
               return "{}:{} am".format(hours, minutes)

           elif hours == 24:

               return "12:{} pm".format(minutes)


           '''
           selected_unformatted_time = (((point - 0.05) / 0.9) * 1440) / 60
           selected_hour = int(selected_unformatted_time)

           selected_real_hour = selected_hour
           selected_apm = "pm"

           if selected_hour == 0:

               selected_real_hour = 12


           elif selected_hour == 12:

               selected_apm = "am"

           elif 12 < selected_hour < 24:

               selected_real_hour -= 12
               selected_apm = "am"

           elif selected_hour >= 24:

               selected_real_hour -= 12
               selected_apm = "pm"

           selected_minute = round((selected_unformatted_time - selected_hour) * 60)
           selected_minute = selected_minute - selected_minute % 5

           if selected_minute < 10:
               selected_minute = "0" + str(selected_minute)

           elif selected_minute == 60:
               selected_minute = "00"
               selected_real_hour += 1

           selected_formatted_time = "{}:{} {}".format(selected_real_hour, selected_minute, selected_apm)

           return selected_formatted_time
           '''









       def time_raw(point):


           total_minutes = point_to_minute(point)
           hours = int(total_minutes / 60)
           minutes = format_minutes(int(total_minutes % 60))

           return "{}:{}".format(hours, minutes)





           '''
           selected_unformatted_time = (((point - 0.05) / 0.9) * 1440) / 60
           selected_hour = int(selected_unformatted_time)

           selected_minute = round((selected_unformatted_time - selected_hour) * 60)
           selected_minute = selected_minute - selected_minute % 5

           if selected_minute < 10:
               selected_minute = "0" + str(selected_minute)

           elif selected_minute == 60:
               selected_minute = "00"
               selected_hour += 1

           selected_formatted_time = "{}:{}".format(selected_hour, selected_minute)

           return selected_formatted_time
           '''


       def point_to_minute(point):

           minutes = ((point - 0.05) / 0.9) * 1440
           minutes = minutes - minutes % 5

           return minutes

       def format_minutes(minute):

           if minute == 0:

               return "00"

           elif minute < 10:

               return "0" + str(minute)

           else:

               return str(minute)















       def total_time_slept():

           if len(self.sleep_periods) > 0:


               total = total_time_slept_int() * 60

               hours = int(total / 60)
               minutes = format_minutes(int(total % 60))

               return "{}:{}".format(hours, minutes)


           else:

               return "--:--"


       def total_time_slept_int():

           if len(self.sleep_periods) > 0:

               total = 0

               for period in self.sleep_periods:
                   start = time_raw(period[0])
                   end = time_raw(period[1])

                   starting_minute = int(start[0:(start.find(":"))]) * 60 + int(start[(start.find(":")) + 1:])
                   ending_minute = int(end[0:(end.find(":"))]) * 60 + int(end[(end.find(":")) + 1:])

                   print(starting_minute)
                   print(ending_minute)

                   total += ending_minute - starting_minute

               return total/60

           else:

               return 0









       input_window.bind('<Motion>', movement)
       input_window.bind('<Button-1>', click)
       input_window.bind('<Button-2>', right_click)




















       new_label = main_canvas.create_text(round(0.27665877 * self.true_width_input_window),
                                           round(0.61 * self.true_height_input_window),
                                           text=time(0.27665877), fill=self.main_text_color,
                                           font=(self.font_c, round(0.015625 * self.width)))

       new_label = main_canvas.create_text(round(0.5 * self.true_width_input_window),
                                           round(0.61 * self.true_height_input_window),
                                           text=time(0.5), fill=self.main_text_color,
                                           font=(self.font_c, round(0.015625 * self.width)))

       new_label = main_canvas.create_text(round(0.72630332 * self.true_width_input_window),
                                           round(0.61 * self.true_height_input_window),
                                           text=time(0.72630332), fill=self.main_text_color,
                                           font=(self.font_c, round(0.015625 * self.width)))









       def save_and_leave():

           if total_time_slept_int() > 0:
               input_window.destroy()






               self.store_data(date_index, self.sleep_periods, total_time_slept_int())

               if today == 1:

                   #if self.clicks == 0:
                       #self.input_button.config(state='normal')

                   #else:

                       #self.input_button2.config(state='normal')

                   self.update_bottom()

                   self.yes_sleep()



               else:



                   self.update_calendar()

           else:

               input_window.destroy()

               if today == 1:
                   self.dialogue_path_nosleep()

               else:

                   self.store_data(date_index, self.sleep_periods, total_time_slept_int())
                   self.update_calendar()



















       def leave():


               input_window.destroy()

               #if today == 1:
                   #self.input_button.config(state='normal')








       input_window.protocol("WM_DELETE_WINDOW", lambda: leave())

   def edit_data(self):

       x = self.master.winfo_x()
       y = self.master.winfo_y()

       self.edit_window = Toplevel(self.master, width=self.edit_width, height=self.edit_height,
                              bg=self.secondary_background_color)

       self.edit_window.geometry(
           "%dx%d+%d+%d" % (self.edit_width, self.edit_height, x + round(0.125*self.width), y))

       self.displaybar = Canvas(self.edit_window, background = self.edge_color, highlightthickness = 0)
       self.displaybar.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.2)

       self.calendar = Canvas(self.edit_window, background = self.secondary_background_color, highlightthickness =0)
       self.calendar.place(relx = 0,rely=0.2,relwidth=1,relheight=0.8)



       def exit():


               self.edit_window.destroy()


       xframe = Canvas(self.edit_window, background=self.main_text_color, highlightthickness=0)
       xframe.place(relx=0.9481, rely=0.034, width=round(0.034 * self.width), height=round(0.034 * self.width))

       self.exit_button = Button(self.edit_window, text="X", highlightbackground=self.secondary_background_color,
                                 highlightthickness=round(0.05208333333 * self.height_input_window),
                                 fg=self.cancel_color,
                                 font=(self.font_c, round(0.03086419753 * self.height_input_window)),
                                 activeforeground=self.dull_highlight, command=lambda: exit())
       self.exit_button.place(relx=0.95, rely=0.04, width=round(0.03 * self.width), height=round(0.03 * self.width))



       print('this is the last recorded date:' + str(self.master_data_storage[-1][0]) + ' ' + str(self.master_data_storage[-1][1]) + ' ' + str(self.master_data_storage[-1][2]))


       self.selected_month = []
       self.selected_month.append(self.master_data_storage[-1][0])
       self.selected_month.append(self.master_data_storage[-1][1])



       self.box_width = int(self.edit_width / 7)
       self.box_height = int(self.edit_height * 0.799 / 5)


       self.update_calendar()

       self.moving_box = []
       self.dummy = self.calendar.create_rectangle(0,0,0,0)
       self.moving_box.append(self.dummy)
       self.moving_box.append(self.dummy)
       self.moving_box.append(self.dummy)
       self.moving_box.append(self.dummy)

       def movement(event):





           x, y = self.edit_window.winfo_pointerx() - self.edit_window.winfo_rootx(), self.edit_window.winfo_pointery() - self.edit_window.winfo_rooty()
           q = int(x/self.box_width )
           i = int(y/self.box_height-0.2) -1

           day = i * 7 + q + 1

           print('{}, {}'.format(x, y))

           if day <= len(self.month):

               last_box = self.moving_box[0]
               last_text = self.moving_box[1]
               last_highlight = self.moving_box[2]
               last_highlight2 = self.moving_box[3]

               self.calendar.delete(last_box)
               self.calendar.delete(last_text)
               self.calendar.delete(last_highlight)
               self.calendar.delete(last_highlight2)

               self.moving_box.clear()

               new_box = self.calendar.create_rectangle(q * self.box_width, i * self.box_height,
                                                        (q + 1) * self.box_width, (i + 1) * self.box_height,
                                                        outline=self.highlighted_text_color,
                                                        width=round(0.00260416666 * self.width))

               new_text = self.calendar.create_text(round(0.01041666666 * self.width) + q * self.box_width,
                                                    round(0.01041666666 * self.width) + i * self.box_height,
                                                    text=day,
                                                    font=(self.font_b, round(0.01041666666 * self.width)),
                                                    fill=self.highlighted_text_color)

               if self.month[day - 1][3] < 0:
                   new_hl = self.calendar.create_text(round(0.04947916666 * self.width) + q * self.box_width,
                                             round(0.03645833333 * self.width) + i * self.box_height,
                                             text="   Click to \n  add data",
                                             font=(self.font_c, round(0.01302083333 * self.width)),
                                             fill=self.highlighted_text_color)

                   new_hl2 = self.dummy

               else:

                   new_hl =self.calendar.create_text(
                       round(0.04947916666 * self.width) + q * self.box_width,
                       round(0.02604166666*self.width) + i * self.box_height,
                       text=self.format_time_numbers(self.month[day - 1][3]),
                       font=(self.font_c, round(0.015625*self.width)),
                       fill=self.highlighted_text_color)

                   new_hl2 = self.calendar.create_text(
                       round(0.04947916666 * self.width) + q * self.box_width,
                       round(0.04427083333 * self.width) + i * self.box_height,
                       text="(click to edit)",
                       font=(self.font_c, round(0.01041666666 * self.width)),
                       fill=self.highlighted_text_color)

               self.moving_box.append(new_box)
               self.moving_box.append(new_text)
               self.moving_box.append(new_hl)
               self.moving_box.append(new_hl2)


       def click(event):

           x, y = self.edit_window.winfo_pointerx() - self.edit_window.winfo_rootx(), self.edit_window.winfo_pointery() - self.edit_window.winfo_rooty()

           if y > 0.2 * self.height:

               q = int(x / self.box_width)
               i = int(y / self.box_height - 0.2) - 1

               day = i * 7 + q + 1

               date_index = (self.first_month_id + day - 1) - len(self.master_data_storage)

               print(date_index)

               if date_index != -1:
                   self.input(date_index, 0)

               else:
                   self.input(date_index, 1)





























       self.edit_window.bind('<Motion>', movement)
       self.edit_window.bind('<Button-1>', click)
       self.edit_window.bind('<Button-2>', click)

   def update_calendar(self):

       self.calendar.delete("all")
       self.displaybar.delete("all")


       self.displaybar.create_text(round(0.02083333333*self.width),round(0.0390625*self.width),text = "Sleep data for:                   ,", font = (self.font_b, round(0.0390625*self.width)), fill = self.main_text_color, anchor = "w")



       monthframe = Canvas(self.edit_window, background=self.main_text_color, highlightthickness=0)
       monthframe.place(relx=0.395, rely=0.021, relwidth = 0.21, relheight = 0.14)

       self.month_selector = Button(self.edit_window, text=self.number_into_month_of_the_year_generator_thingy(self.selected_month[1]), highlightbackground=self.secondary_background_color,
                                 highlightthickness=round(0.05208333333*self.width),
                                 fg=self.main_text_color,
                                 font=(self.font_c, round(0.03125*self.width)),
                                 activeforeground=self.dull_highlight, command=lambda: self.set_month())
       self.month_selector.place(relx=0.4, rely=0.025, relwidth = 0.2, relheight = 0.13)

       yearframe = Canvas(self.edit_window, background=self.main_text_color, highlightthickness=0)
       yearframe.place(relx=0.645, rely=0.021, relwidth=0.21, relheight=0.14)

       self.year_selector = Button(self.edit_window,
                                    text=self.selected_month[0] + 2000,
                                    highlightbackground=self.secondary_background_color,
                                    highlightthickness=round(0.05208333333*self.width),
                                    fg=self.main_text_color,
                                    font=(self.font_c, round(0.03125*self.width)),
                                    activeforeground=self.dull_highlight, command=lambda: self.set_year())
       self.year_selector.place(relx=0.65, rely=0.025, relwidth=0.2, relheight=0.13)



       chosen_year = 18
       chosen_month = 1

       self.month_id = 0


       while chosen_year < self.selected_month[0]:
           print("month id is " + str(self.month_id))

           self.month_id += 365
           chosen_year += 1



       while chosen_month < self.selected_month[1]:
           print("month id is " + str(self.month_id))

           self.month_id += self.days_in_a_month(chosen_month, chosen_year + 2000)
           chosen_month += 1

       print("month id is " + str(self.month_id))
       print(len(self.master_data_storage))



       self.month = []

       self.first_month_id = self.month_id



       lim = self.month_id + self.days_in_a_month(self.selected_month[1], chosen_year + 2000)



       if self.selected_month[1] != self.master_data_storage[-1][1] or self.selected_month[0] != self.master_data_storage[-1][0]:

           while self.month_id < lim:

               self.month.append(self.master_data_storage[self.month_id])

               self.month_id += 1

       else:

           while self.month_id < len(self.master_data_storage):
               self.month.append(self.master_data_storage[self.month_id])

               self.month_id += 1



       for h in self.month:

           print(h)







       i = 4

       while i >= 0:

           q = 6

           while q >= 0:

               day = i * 7 + q + 1

               if day > len(self.month):

                   color = self.edge_color

               else:

                   color = self.main_text_color

                   self.calendar.create_text(round(0.01041666666 * self.width) + q * self.box_width,
                                             round(0.01041666666 * self.width) + i * self.box_height, text=day,
                                             font=(self.font_b, round(0.01041666666 * self.width)),
                                             fill=self.main_text_color)

                   if self.month[day-1][3] < 0:

                       self.calendar.create_text(round(0.04947916666*self.width) + q * self.box_width,
                                                 round(0.03645833333*self.width) + i * self.box_height, text="   Click to \n  add data",
                                                 font=(self.font_c, round(0.01302083333*self.width)),
                                                 fill=self.main_text_color)

                   else:

                       self.calendar.create_text(
                           round(0.04947916666 * self.width) + q * self.box_width,
                           round(0.02604166666 * self.width) + i * self.box_height,
                           text=self.format_time_numbers(self.month[day - 1][3]),
                           font=(self.font_c, round(0.015625*self.width)),
                           fill=self.cancel_color)



                       self.calendar.create_text(
                           round(0.04947916666 * self.width) + q * self.box_width,
                           round(0.04427083333*self.width) + i * self.box_height,
                           text="(click to edit)",
                           font=(self.font_c, round(0.01041666666*self.width)),
                           fill=self.dull_cancel)









               self.calendar.create_rectangle(q * self.box_width, i * self.box_height, (q + 1) * self.box_width,
                                              (i + 1) * self.box_height,
                                              outline=color, width= round(0.00260416666*self.width))


               q -= 1

           i -= 1

   def set_month(self):

       x = self.edit_window.winfo_x()
       y = self.edit_window.winfo_y()



       self.set_month_width = round(0.32291666666*self.width) #620
       self.set_month_height = round(0.75 * self.height) #810

       self.set_month_window = Toplevel(self.edit_window, width=self.set_month_width, height=self.edit_height,
                                   bg=self.secondary_background_color)

       self.set_month_window.geometry(
           "%dx%d+%d+%d" % (self.set_month_width, self.edit_height, x + round(0.29 * self.width), y))


       month_width = round(0.99 *self.set_month_width / 2)
       month_height = round(0.99 * self.set_month_height / 6)

       month_menu = Canvas(self.set_month_window, background = self.secondary_background_color, highlightthickness = 0)
       month_menu.place(relx = 0,rely = 0.005,relwidth = 1, relheight = 1)


       c = 0

       while c < 6:

           r = 0

           while r < 2:

               month_menu.create_rectangle(r * month_width, c * month_height, (r+1) * month_width,
                                              (c+1) * month_height,
                                              outline=self.main_text_color, width=round(0.00260416666 * self.width))


               month_menu.create_text(r * month_width + round(0.078125*self.width), c * month_height + round(0.03385416666*self.width), text = self.number_into_month_of_the_year_generator_thingy(r + 1 + c * 2), font = (self.font_c, round(0.03125*self.width)), fill = self.main_text_color)

               r+=1
           c+=1




       select_a_month = []

       dummy = month_menu.create_rectangle(0,0,0,0)

       select_a_month.append(dummy)
       select_a_month.append(dummy)

       def movement(event):

           x, y = self.set_month_window.winfo_pointerx() - self.set_month_window.winfo_rootx(), self.set_month_window.winfo_pointery() - self.set_month_window.winfo_rooty()
           r = int(x / month_width)
           c = int(y / month_height)

           self.monthhhhh = c * 2 + r + 1



           last_box = select_a_month[0]
           last_text = select_a_month[1]

           month_menu.delete(last_box)
           month_menu.delete(last_text)

           select_a_month.clear()

           new_box = month_menu.create_rectangle(r * month_width, c * month_height, (r + 1) * month_width,
                                       (c + 1) * month_height,
                                       outline=self.highlighted_text_color, width=round(0.00260416666 * self.width))

           new_text = month_menu.create_text(r * month_width + round(0.078125*self.width), c * month_height + round(0.03385416666*self.width), text = self.number_into_month_of_the_year_generator_thingy(r + 1 + c * 2), font = (self.font_c, round(0.03125*self.width)), fill=self.highlighted_text_color)

           select_a_month.append(new_box)
           select_a_month.append(new_text)

       def click(event):

           self.set_month_window.destroy()
           self.selected_month[1] = self.monthhhhh
           self.update_calendar()










       self.set_month_window.bind('<Motion>', movement)
       self.set_month_window.bind('<Button-1>', click)
       self.set_month_window.bind('<Button-2>', click)













       '''



       i = 4

       while i >= 0:

           q = 6

           while q >= 0:

               color = self.main_text_color

               self.calendar.create_text(round(0.01041666666 * self.width) + q * self.box_width,
                                         round(0.01041666666 * self.width) + i * self.box_height, text=,
                                         font=(self.font_b, round(0.01041666666 * self.width)),
                                         fill=self.main_text_color)

               if self.month[day - 1][3] < 0:

                   self.calendar.create_text(round(0.04947916666 * self.width) + q * self.box_width,
                                             round(0.03645833333 * self.width) + i * self.box_height,
                                             text="   Click to \n  add data",
                                             font=(self.font_c, round(0.01302083333 * self.width)),
                                             fill=self.main_text_color)

               else:

                   self.calendar.create_text(
                       round(0.04947916666 * self.width) + q * self.box_width,
                       50 + i * self.box_height,
                       text=self.format_time_numbers(self.month[day - 1][3]),
                       font=(self.font_c, 30),
                       fill=self.cancel_color)

                   self.calendar.create_text(
                       round(0.04947916666 * self.width) + q * self.box_width,
                       round(0.04427083333 * self.width) + i * self.box_height,
                       text="(click to edit)",
                       font=(self.font_c, round(0.01041666666 * self.width)),
                       fill=self.dull_cancel)

           self.calendar.create_rectangle(q * self.box_width, i * self.box_height, (q + 1) * self.box_width,
                                          (i + 1) * self.box_height,
                                          outline=color, width=round(0.00260416666 * self.width))







               q -= 1

           i -= 1'''

   def set_year(self):

       x = self.edit_window.winfo_x()
       y = self.edit_window.winfo_y()

       self.set_year_width = round(0.18229166666*self.width)
       self.set_year_height = round(0.18518518518*self.height)

       self.set_year_window = Toplevel(self.edit_window, width=self.set_year_width, height=self.edit_height,
                                        bg=self.secondary_background_color)

       self.set_year_window.geometry(
           "%dx%d+%d+%d" % (self.set_year_width, self.set_year_height, x + round(0.48 * self.width), y))

       self.year_display = Canvas(self.set_year_window, background = self.secondary_background_color, highlightthickness = 0)
       self.year_display.place(relx=0,rely=0,relwidth=1,relheight=1)


       def update_display(increment):


           year = self.selected_month[0] + 2000 + increment

           if year < 2018:

               year = 2018

           self.year_display.delete("all")

           self.year_display.create_text(round(0.1 * self.set_year_width), round(0.5 * self.set_year_height), text = year, font = (self.font_b, round(0.06944444444*self.height)), fill = self.main_text_color, anchor = "w")

           self.selected_month[0] = year - 2000

       def chosen():
           self.set_year_window.destroy()
           self.update_calendar()

       up_button_frame = Canvas(self.set_year_window, background=self.main_text_color, highlightthickness=0)
       up_button_frame.place(relx=0.67, rely=0.032, width=round(0.03 * self.width), height=round(0.03 * self.width))

       self.up_button = Button(self.set_year_window, text="⇧", highlightbackground=self.secondary_background_color,
                                 highlightthickness=round(0.05208333333 * self.height_input_window),
                                 fg=self.main_text_color,
                                 font=(self.font_c, round(0.03086419753 * self.height_input_window)),
                                 activeforeground=self.dull_highlight, command=lambda: update_display(1))
       self.up_button.place(relx=0.679, rely=0.04, width=round(0.027 * self.width), height=round(0.027 * self.width))



       check_button_frame = Canvas(self.set_year_window, background=self.main_text_color, highlightthickness=0)
       check_button_frame.place(relx=0.67, rely=0.362, width=round(0.03 * self.width), height=round(0.03 * self.width))

       self.check_button = Button(self.set_year_window, text="✓", highlightbackground=self.secondary_background_color,
                               highlightthickness=round(0.05208333333 * self.height_input_window),
                               fg=self.clock_color,
                               font=(self.font_c, round(0.03086419753 * self.height_input_window)),
                               activeforeground=self.dull_highlight, command=lambda: chosen())
       self.check_button.place(relx=0.679, rely=0.37, width=round(0.027 * self.width), height=round(0.027 * self.width))



       down_button_frame = Canvas(self.set_year_window, background=self.main_text_color, highlightthickness=0)
       down_button_frame.place(relx=0.67, rely=0.692, width=round(0.03 * self.width), height=round(0.03 * self.width))

       self.down_button = Button(self.set_year_window, text="⇩", highlightbackground=self.secondary_background_color,
                               highlightthickness=round(0.05208333333 * self.height_input_window),
                               fg=self.main_text_color,
                               font=(self.font_c, round(0.03086419753 * self.height_input_window)),
                               activeforeground=self.dull_highlight, command=lambda: update_display(-1))
       self.down_button.place(relx=0.679, rely=0.7, width=round(0.027 * self.width), height=round(0.027 * self.width))








       update_display(0)

   # daily sleep input section

   def bottom_section(self, master):

       self.bottom_section = Canvas(master, bg=self.secondary_background_color, highlightthickness=0)

       self.button1_frame = Canvas(master, bg=self.secondary_background_color , highlightthickness=0)
       self.button2_frame = Canvas(master, bg=self.secondary_background_color, highlightthickness=0)

       b_corner_nw = self.dashboard_frame.create_oval(0.16 * self.width, 0.66 * self.height, 0.205 * self.width,  0.74 * self.height, fill=self.secondary_background_color, outline=self.secondary_background_color)

       b_corner_sw = self.dashboard_frame.create_oval(0.16 * self.width, 0.91 * self.height, 0.205 * self.width, 0.99 * self.height, fill=self.secondary_background_color, outline=self.secondary_background_color)

       b_corner_ne = self.dashboard_frame.create_oval(0.795 * self.width, 0.66 * self.height, 0.839 * self.width, 0.74 * self.height, fill=self.secondary_background_color, outline=self.secondary_background_color)

       b_corner_se = self.dashboard_frame.create_oval(0.795 * self.width, 0.91 * self.height, 0.839 * self.width, 0.99 * self.height, fill=self.secondary_background_color, outline=self.secondary_background_color)

       b_edge = self.dashboard_frame.create_rectangle(0.1825 * self.width, 0.66 * self.height, 0.8175 * self.width, 0.99 * self.height, fill=self.secondary_background_color, outline=self.secondary_background_color)


       b1_left = self.button1_frame.create_oval(int(0.00347222222*self.height),int(0.00347222222*self.height),0.92*0.1*self.height,0.92*0.1*self.height, fill = self.secondary_background_color, outline = self.main_text_color, width = int(0.003125*self.width))

       b1_right = self.button1_frame.create_oval(int(0.25*self.width-0.92*0.1*self.height), int(0.00347222222 * self.height),
                                      0.993*0.25*self.width, 0.92 * 0.1 * self.height, fill=self.secondary_background_color,
                                      outline=self.main_text_color, width=int(0.003125 * self.width))

       b1_connector = self.button1_frame.create_rectangle(int(0.92*0.1*self.height/2), int(0.00347222222*self.height), 0.25*self.width-int(0.92*0.1*self.height/2), 0.92*0.1*self.height, outline = self.main_text_color, width = int(0.003125*self.width))

       b1_fill = self.button1_frame.create_rectangle(int(0.92 * 0.1 * self.height / 2) - round(0.00173611111*self.height+1),
                                                     int(0.00347222222 * self.height)+ round(0.00347222222*self.height),
                                                     0.25 * self.width - int(0.92 * 0.1 * self.height / 2)+ round(0.00173611111*self.height),
                                                     0.92 * 0.1 * self.height- round(0.00347222222*self.height), outline=self.secondary_background_color,
                                                     fill=self.secondary_background_color)






       b2_left = self.button2_frame.create_oval(int(0.00347222222 * self.height), int(0.00347222222 * self.height),
                                                0.92 * 0.1 * self.height, 0.92 * 0.1 * self.height,
                                                fill=self.secondary_background_color, outline=self.main_text_color,
                                                width=int(0.003125 * self.width))
       b2_right = self.button2_frame.create_oval(int(0.25 * self.width - 0.92 * 0.1 * self.height),
                                                 int(0.00347222222 * self.height),
                                                 0.993 * 0.25 * self.width, 0.92 * 0.1 * self.height,
                                                 fill=self.secondary_background_color,
                                                 outline=self.main_text_color, width=int(0.003125 * self.width))
       b2_connector = self.button2_frame.create_rectangle(int(0.92 * 0.1 * self.height / 2),
                                                          int(0.00347222222 * self.height),
                                                          0.25 * self.width - int(0.92 * 0.1 * self.height / 2),
                                                          0.92 * 0.1 * self.height, outline=self.main_text_color,
                                                          width=int(0.003125 * self.width))

       b2_fill = self.button2_frame.create_rectangle(
           int(0.92 * 0.1 * self.height / 2) - round(0.00173611111 * self.height),
           int(0.00347222222 * self.height) + round(0.00347222222 * self.height),
           0.25 * self.width - int(0.92 * 0.1 * self.height / 2) + round(0.00173611111 * self.height),
           0.92 * 0.1 * self.height - round(0.00347222222 * self.height), outline=self.secondary_background_color,
           fill=self.secondary_background_color)







       self.input_button = Button(self.master, text = "Input Today's Sleep Data", highlightbackground=self.secondary_background_color, highlightthickness=round(0.05208333333*self.height), fg = self.highlighted_text_color, font = (self.font_c, round(0.03298611111*self.height)), activeforeground = self.dull_highlight, command = lambda: self.input(-1, 1))
       self.sleepless_button = Button(self.master, text=self.flavor_text("no sleep"), highlightbackground=self.secondary_background_color,
                                  highlightthickness=round(0.05208333333*self.height), fg=self.clock_color,
                                  font=(self.font_c, round(0.02604166666*self.height)), command = lambda: self.dialogue_path_nosleep())



       self.button2_frame.place(relx = 0.55, rely = 0.81, relwidth = 0.25, relheight = 0.1)
       self.button1_frame.place(relx = 0.2, rely = 0.81, relwidth = 0.25, relheight = 0.1)
       self.input_button.place(relx = 0.225, rely = 0.8155, relwidth = 0.199, relheight = 0.081)
       self.sleepless_button.place(relx=0.572, rely=0.816, relwidth=0.199, relheight=0.081)
       self.bottom_section.place(relx=0.16, rely=0.7, relwidth=0.68, relheight=0.25)



       date = self.master_data_storage[-1]

       month_of_the_year = self.number_into_month_of_the_year_generator_thingy(date[1])
       year_of_time = "20" + str(date[0])

       dat = month_of_the_year + " " + str(date[2]) + ", " + year_of_time + " - "



       #day = self.bottom_section.create_text(round(0.68 * 0.04 * self.width),round(0.25*0.08*self.height), text = dat, fill = self.main_text_color, font = (self.font_b, round(0.04629629629*self.height)), anchor = "w")
       self.prompt = self.bottom_section.create_text(round(0.68 * 0.04 * self.width), round(0.25 * 0.08 * self.height),
                                                text=self.flavor_text("bottom prompt"), fill=self.main_text_color,
                                                font=(self.font_c, round(0.04629629629 * self.height)), anchor="w")

       self.clicks = 0

   def dialogue_path_nosleep(self):

       self.update_bottom()

       self.clicks += 1

       self.button1_frame.destroy()
       self.button2_frame.destroy()
       self.input_button.destroy()
       self.sleepless_button.destroy()
       self.bottom_section.delete(self.prompt)

       self.button3_frame = Canvas(self.master, bg=self.secondary_background_color, highlightthickness=0)
       self.button4_frame = Canvas(self.master, bg=self.secondary_background_color, highlightthickness=0)

       b_corner_nw = self.dashboard_frame.create_oval(0.16 * self.width, 0.66 * self.height, 0.205 * self.width,
                                                      0.74 * self.height, fill=self.secondary_background_color,
                                                      outline=self.secondary_background_color)

       b_corner_sw = self.dashboard_frame.create_oval(0.16 * self.width, 0.91 * self.height, 0.205 * self.width,
                                                      0.99 * self.height, fill=self.secondary_background_color,
                                                      outline=self.secondary_background_color)

       b_corner_ne = self.dashboard_frame.create_oval(0.795 * self.width, 0.66 * self.height, 0.839 * self.width,
                                                      0.74 * self.height, fill=self.secondary_background_color,
                                                      outline=self.secondary_background_color)

       b_corner_se = self.dashboard_frame.create_oval(0.795 * self.width, 0.91 * self.height, 0.839 * self.width,
                                                      0.99 * self.height, fill=self.secondary_background_color,
                                                      outline=self.secondary_background_color)

       b_edge = self.dashboard_frame.create_rectangle(0.1825 * self.width, 0.66 * self.height, 0.8175 * self.width,
                                                      0.99 * self.height, fill=self.secondary_background_color,
                                                      outline=self.secondary_background_color)

       b1_left = self.button3_frame.create_oval(int(0.00347222222 * self.height), int(0.00347222222 * self.height),
                                                0.92 * 0.1 * self.height, 0.92 * 0.1 * self.height,
                                                fill=self.secondary_background_color, outline=self.main_text_color,
                                                width=int(0.003125 * self.width))

       b1_right = self.button3_frame.create_oval(int(0.25 * self.width - 0.92 * 0.1 * self.height),
                                                 int(0.00347222222 * self.height),
                                                 0.993 * 0.25 * self.width, 0.92 * 0.1 * self.height,
                                                 fill=self.secondary_background_color,
                                                 outline=self.main_text_color, width=int(0.003125 * self.width))

       b1_connector = self.button3_frame.create_rectangle(int(0.92 * 0.1 * self.height / 2),
                                                          int(0.00347222222 * self.height),
                                                          0.25 * self.width - int(0.92 * 0.1 * self.height / 2),
                                                          0.92 * 0.1 * self.height, outline=self.main_text_color,
                                                          width=int(0.003125 * self.width))

       b1_fill = self.button3_frame.create_rectangle(
           int(0.92 * 0.1 * self.height / 2) - round(0.00173611111 * self.height + 1),
           int(0.00347222222 * self.height) + round(0.00347222222 * self.height),
           0.25 * self.width - int(0.92 * 0.1 * self.height / 2) + round(0.00173611111 * self.height),
           0.92 * 0.1 * self.height - round(0.00347222222 * self.height), outline=self.secondary_background_color,
           fill=self.secondary_background_color)

       b2_left = self.button4_frame.create_oval(int(0.00347222222 * self.height), int(0.00347222222 * self.height),
                                                0.92 * 0.1 * self.height, 0.92 * 0.1 * self.height,
                                                fill=self.secondary_background_color, outline=self.main_text_color,
                                                width=int(0.003125 * self.width))
       b2_right = self.button4_frame.create_oval(int(0.25 * self.width - 0.92 * 0.1 * self.height),
                                                 int(0.00347222222 * self.height),
                                                 0.993 * 0.25 * self.width, 0.92 * 0.1 * self.height,
                                                 fill=self.secondary_background_color,
                                                 outline=self.main_text_color, width=int(0.003125 * self.width))
       b2_connector = self.button4_frame.create_rectangle(int(0.92 * 0.1 * self.height / 2),
                                                          int(0.00347222222 * self.height),
                                                          0.25 * self.width - int(0.92 * 0.1 * self.height / 2),
                                                          0.92 * 0.1 * self.height, outline=self.main_text_color,
                                                          width=int(0.003125 * self.width))

       b2_fill = self.button4_frame.create_rectangle(
           int(0.92 * 0.1 * self.height / 2) - round(0.00173611111 * self.height),
           int(0.00347222222 * self.height) + round(0.00347222222 * self.height),
           0.25 * self.width - int(0.92 * 0.1 * self.height / 2) + round(0.00173611111 * self.height),
           0.92 * 0.1 * self.height - round(0.00347222222 * self.height), outline=self.secondary_background_color,
           fill=self.secondary_background_color)

       self.input_button2 = Button(self.master, text=self.flavor_text("sleep button"),
                                  highlightbackground=self.secondary_background_color,
                                  highlightthickness=round(0.05208333333 * self.height),
                                  fg=self.highlighted_text_color,font=(self.font_c, round(0.02604166666 * self.height)
                                  ),
                                  activeforeground=self.dull_highlight, command=lambda: self.input(-1))

       self.sleepless_button2 = Button(self.master, text="I did not sleep at all",
                                      highlightbackground=self.secondary_background_color,
                                      highlightthickness=round(0.05208333333 * self.height), fg=self.clock_color,
                                      font=(self.font_c, round(0.03298611111 * self.height)),
                                      command=lambda: self.no_sleep())

       self.button4_frame.place(relx=0.55, rely=0.81, relwidth=0.25, relheight=0.1)
       self.button3_frame.place(relx=0.2, rely=0.81, relwidth=0.25, relheight=0.1)
       self.input_button2.place(relx=0.225, rely=0.8155, relwidth=0.199, relheight=0.081)
       self.sleepless_button2.place(relx=0.572, rely=0.816, relwidth=0.199, relheight=0.081)
       self.bottom_section.place(relx=0.16, rely=0.7, relwidth=0.68, relheight=0.25)

       date = self.master_data_storage[-1]

       month_of_the_year = self.number_into_month_of_the_year_generator_thingy(date[1])
       year_of_time = "20" + str(date[0])

       dat = month_of_the_year + " " + str(date[2]) + ", " + year_of_time + " - "

       # day = self.bottom_section.create_text(round(0.68 * 0.04 * self.width),round(0.25*0.08*self.height), text = dat, fill = self.main_text_color, font = (self.font_b, round(0.04629629629*self.height)), anchor = "w")
       self.prompt2 = self.bottom_section.create_text(round(0.68 * 0.04 * self.width), round(0.25 * 0.08 * self.height),
                                                     text=self.flavor_text("bottom prompt 2"), fill=self.main_text_color,
                                                     font=(self.font_c, round(0.04629629629 * self.height)),
                                                     anchor="w")

   def no_sleep(self):



       self.update_bottom()

       null = []

       self.store_data(-1, null, 0)


       self.daily_results = self.bottom_section.create_text(round(0.68 * 0.5 * self.width), round(0.25 * 0.2 * self.height),
                                                     text=self.flavor_text("congrats"),
                                                     fill=self.cancel_color,
                                                     font=(self.font_c, round(0.04166666666 * self.width)))

       self.daily2 = self.bottom_section.create_text(round(0.68 * 0.5 * self.width),
                                                      round(0.25 * 0.5 * self.height),
                                                      text=self.flavor_text("sleepless"),
                                                      fill=self.main_text_color,
                                                      font=(self.font_c, round(0.04629629629 * self.height)))

       self.daily2 = self.bottom_section.create_text(round(0.68 * 0.5 * self.width),
                                                     round(0.25 * 0.75 * self.height),
                                                     text=self.flavor_text("sleepless2"),
                                                     fill=self.main_text_color,
                                                     font=(self.font_c, round(0.02777777777 * self.height)))

   def yes_sleep(self):

       self.update_bottom()
       self.bottom_section.delete("all")

       null = []

       sleeptime = self.master_data_storage[-1][3]

       sleepmessage = self.format_time_words(sleeptime)

       flavoured_text = ""
       bottom_text = ""

       if sleeptime >= 24:

           flavoured_text = self.flavor_text(">24")

       elif sleeptime >= 16:

           flavoured_text = self.flavor_text(">16")

       elif sleeptime >= 12:

           flavoured_text = self.flavor_text(">12")

       elif sleeptime >= 10:

           flavoured_text = self.flavor_text(">10")

       elif sleeptime >= 9:

           flavoured_text = self.flavor_text(">9")

       elif sleeptime >= 8:

           flavoured_text = self.flavor_text(">8")

       elif sleeptime >= 7:

           flavoured_text = self.flavor_text(">7")

       elif sleeptime >= 5:

           flavoured_text = self.flavor_text(">5")

       elif sleeptime >= 3:

           flavoured_text = self.flavor_text(">3")

       elif sleeptime >= 1:

           flavoured_text = self.flavor_text(">1")

       elif sleeptime > 0:

           flavoured_text = self.flavor_text(">0")







       if flavoured_text.find("\n") > 0:

           bottom_text = flavoured_text[flavoured_text.find("\n") + 1:]
           flavoured_text = flavoured_text[0:flavoured_text.find("\n")]





       self.daily_results = self.bottom_section.create_text(round(0.68 * 0.5 * self.width),
                                                            round(0.25 * 0.2 * self.height),
                                                            text="You slept " + sleepmessage,
                                                            fill=self.cancel_color,
                                                            font=(self.font_c, round(0.03125 * self.width)))







       self.daily2 = self.bottom_section.create_text(round(0.68 * 0.5 * self.width),
                                                      round(0.25 * 0.45 * self.height),
                                                      text=flavoured_text,
                                                      fill=self.main_text_color,
                                                      font=(self.font_c, round(0.03703703703 * self.height)))

       self.daily2 = self.bottom_section.create_text(round(0.68 * 0.5 * self.width),
                                                     round(0.25 * 0.625 * self.height),
                                                     text=bottom_text,
                                                     fill=self.main_text_color,
                                                     font=(self.font_c, round(0.02777777777 * self.height)))

   def update_bottom(self):

       if self.clicks == 0:

           self.button1_frame.destroy()
           self.button2_frame.destroy()
           self.input_button.destroy()
           self.sleepless_button.destroy()
           self.bottom_section.delete(self.prompt)

       else:

           self.button3_frame.destroy()
           self.button4_frame.destroy()
           self.input_button2.destroy()
           self.sleepless_button2.destroy()
           self.bottom_section.delete(self.prompt2)


   # misc functions

   def flavor_text(self, type):


       messages = []


       if type == "no sleep":


           messages.append("Bold of you to assume\n I slept at all")
           messages.append("What is this sleep\n you speak of")
           messages.append("Sleep is for the weak")
           messages.append("I'll sleep when I'm dead")

           messages.append("Sleep is irrelevant")



       elif type == "bottom prompt":


           messages.append("Alright kid, how much did you sleep?")
           messages.append("Hey man how much did you bother to sleep last night?")
           messages.append("Did you get a healthy 10 hours of sleep?")
           messages.append("Just tell me you didn't destroy your sleep schedule.")
           messages.append("Please tell me you didn't do another sleepless night.")
           messages.append("If you didn't sleep I'm gonna slap you.")




       elif type == "bottom prompt 2":

           messages.append("You're joking. You didn't sleep at all?")
           messages.append("Really? Not even 5 minutes of sleep?")
           messages.append("Did you actually pull an all nighter?")




       elif type == "sleep button":

           messages.append("Just kidding, I slept \n(input sleep data)")
           messages.append("I actually did sleep \n(input sleep data)")
           messages.append("Chill, I slept \n(input sleep data)")




       elif type == "congrats":

           messages.append("Congratulations!")
           messages.append("Great job!")
           messages.append("Amazing!")







       elif type == "sleepless":

           messages.append("You slept an astounding 0 hours")
           messages.append("You didn't sleep a single bit")
           messages.append("You had absolutely zero sleep")



       elif type == "sleepless2":

           messages.append("Hopefully it was for a good reason.")
           messages.append("It was for a good reason, right?")
           messages.append("Let's hope you didn't waste all that time.")




       elif type == ">24":

           messages.append("Congratulations! You found a bug! \n (This typically doesn't bother people so just ignore it)")
           messages.append("I'm not sure how this happened \n(It's a bug okay ignore it)")



       elif type == ">16":

           messages.append("Either you're trying to break the system or you need to see a doctor")
           messages.append("Okay sleep is good but maybe not that much")
           messages.append("Legend has it those who sleep this much gain godlike powers \n (feeling anything yet?)")



       elif type == ">12":

           messages.append("Well then. You recovering from an all nighter?")
           messages.append("That's a long time. Maybe too long.")
           messages.append("More than enough for someone like you. \n (Don't do it too too often.)")
           messages.append("They say those who achieve this much sleep gain enlightenment \n (How does it feel?)")





       elif type == ">10":

           messages.append("A good amount of sleep \n Sleeping this much every so often ain't so bad")
           messages.append("Definitely enough sleep. \n Don't be too lazy tho.")
           messages.append("As long as you're well rested take as much time as you need I guess.")
           messages.append("You've slept more in one night than I have in the past month ")




       elif type == ">9":

           messages.append("You hit the sweet spot. \n Try to sleep this much every day")
           messages.append("Perfect. That's the right amount. ")
           messages.append("That's solid. Sleep like this as often as you can.")
           messages.append("Beautiful. Hopefully you're well rested.")
           messages.append("9 Hours? N-no, I thought it was a MYTH \n (For real good on you)")
           messages.append("Modern physics doesn't allow for it, but somehow you've done it \n (Hope you're well rested!)")



       elif type == ">8":

           messages.append("A tad bit low, but still pretty good")
           messages.append("Not bad kid. Not bad at all.")
           messages.append("Pretty decent amount if you ask me.")




       elif type == ">7":

           messages.append("That's a bit low, but still fine overall")
           messages.append("Seven hours ... lucky number! \n (Aim for more though) ")
           messages.append("THAT ... is about average, to be honest. \n (Go for 9 if you can)")



       elif type == ">5":

           messages.append("You have to be a bit tired, right? \n (Get more sleep tonight if you can)")
           messages.append("Not great, but not terrible either \n (Sleep more if you can)")
           messages.append("Ehhhhhhhhhh, it's okay i guess. ")
           messages.append("I'd give that a C \n (at least it's a pass)")




       elif type == ">3":

           messages.append("That's awfully short \n (were you procrastinating again?)")
           messages.append("How pitifully short \n (like your lifespan if you keep sleeping like this)")
           messages.append("I would say unbelievable, but it's exactly what I'd expect \n (get more sleeeep)")
           messages.append("You utter fool. \n Sleep more. Nothin else to say")

       elif type == ">1":

           messages.append("bro why are you on the computer \n (go to bed kid)")
           messages.append("how are you not dead \n (you should be asleep rn)")
           messages.append("are you even sentient right now. \n (sleep immediately fool)")
           messages.append("you fooool \n (you better have been saving babies from fires or something)")

       elif type == ">0":

           messages.append("I've seen junkies on caffine with more than sleep than you")
           messages.append("That is completely and utterly laughable, you idiot")
           messages.append("Ugh. Look at the title of this program.")

       message = messages[randrange(0, len(messages))]
       return message

   def number_into_day_of_the_week_generator_thingy(self, num):

       if num == 0:

           return "Monday"

       elif num == 1:

           return "Tuesday"

       elif num == 2:

           return "Wednesday"

       elif num == 3:

           return "Thursday"

       elif num == 4:

           return "Friday"

       elif num == 5:

           return "Saturday"

       elif num == 6:

           return "Sunday"

   def number_into_month_of_the_year_generator_thingy(self, num):


       if num == 1:

           return "January"

       elif num == 2:

           return "February"

       elif num == 3:

           return "March"

       elif num == 4:

           return "April"

       elif num == 5:

           return "May"

       elif num == 6:

           return "June"

       elif num == 7:

           return "July"

       elif num == 8:

           return "August"

       elif num == 9:

           return "September"

       elif num == 10:

           return "October"

       elif num == 11:

           return "November"

       elif num == 12:

           return "December"

   def days_in_a_month(self, month, year):

       if month == 2 and calendar.isleap(year):

           return 29

       elif month == 2:

           return 28

       elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:

           return 31

       else:

           return 30

   def ordinal_indicator_wow_look_fancy_title(self, num):

       aksjdklj = num % 10

       if aksjdklj == 1:

           return "st"

       if aksjdklj == 2:

           return  "nd"

       if aksjdklj == 3:

           return "rd"

       return "th"

   def format_time_words(self, sleeptime):

       mint = sleeptime - int(sleeptime)

       minute = round(mint * 60)

       if sleeptime - int(sleeptime) == 0 and sleeptime >= 2:

           sleepmessage = str(int(sleeptime)) + " hours"

       elif sleeptime - int(sleeptime) == 0 and sleeptime >= 1:

           sleepmessage = str(int(sleeptime)) + " hour"

       elif sleeptime - int(sleeptime) == 0 and sleeptime >= 1:

           sleepmessage = str(int(sleeptime)) + " hour"

       elif sleeptime - int(sleeptime) != 0 and sleeptime >= 2:

           sleepmessage = str(int(sleeptime)) + " hours and " + str(minute) + " minutes"

       elif sleeptime - int(sleeptime) != 0 and sleeptime >= 1:

           sleepmessage = str(int(sleeptime)) + " hour and " + str(minute) + " minutes"

       elif sleeptime < 1:

           sleepmessage = str(minute) + " minutes"

       else:

           print("you fool")

       return sleepmessage

   def format_time_numbers(self, time):

       hours = int(time)
       minutes = round((time - hours) * 60)

       if minutes < 10:

           minutes = "0" + str(minutes)

       return "{}:{}".format(hours, minutes)

   def format_time_numbers_rounded(self, time):

       hours = int(time)
       minutes = round((time - hours) * 60)

       minutes = minutes - (minutes % 5)

       if minutes < 10:

           minutes = "0" + str(minutes)

       return "{}:{}".format(hours, minutes)

   def lock_bottom(self):



       if self.master_data_storage[-1][3] == 0:

           self.no_sleep()

       if self.master_data_storage[-1][3] > 0:

           self.yes_sleep()
























































def ree(event):
   '''
   x, y = root.winfo_pointerx() - root.winfo_rootx(), root.winfo_pointery() - root.winfo_rooty()
   relx = round(x/1024.0,3)
   rely = round(y/576.0,3)


   print('{}, {}'.format(relx, rely))
   '''

   x, y = root.winfo_rootx(), root.winfo_rooty()



   print('{}, {}'.format(x, y))



root = Tk()
instance = SleepMoreIdiot(root)
#root.bind('<Motion>', ree)
root.mainloop()

