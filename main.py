import ttkbootstrap as ttb
from ttkbootstrap import Style
import tkinter as ttk
import tkinter.font as tk_font

def sign_in():
    pass


# window
window=ttb.Window()
window.geometry('790x400')
window.resizable(False, False)
window.title("Tephdy Tech")
style=Style(theme="cyborg")

# custom_font
custom_font=tk_font.Font(family="Bahnschrift", weight="bold", size=12)
# custom_font

# main_frame_contents

# main_frame
main_frame=ttb.Frame(window)
main_frame.pack(fill='x',padx=10)
# main_frame

# left_content_frame
left_content=ttb.Frame(main_frame)
# left_content.grid(row=0, column=0)
left_content.pack(side="left")
# left_content_frame

# left_content
side_pic=ttk.PhotoImage(file="icons_images/27.png")

side_pic_width=400
side_pic_height=300

side_pic=side_pic.subsample(int(side_pic.width()/side_pic_width), int(side_pic.height()/ side_pic_height))

side_label=ttb.Label(left_content, image=side_pic)
side_label.grid(row=0, column=0)
# left_content end
# ####################################################################################################################

# right_content
right_content_frame=ttb.Frame(main_frame)
# right_content_frame.grid(row=0, column=1, sticky="news")
right_content_frame.pack(side="right", fill='both', padx=15, pady=15, expand=True)

# register_frame
register_frame=ttb.Frame(right_content_frame)
register_frame.grid(row=0, column=0, sticky="ew")

# register_label
register_label=ttb.Label(register_frame, text="Create an account")
register_label.grid(row=0, column=0)
# register_label

# register_btn
register_btn=ttb.Button(register_frame, text="Sign in", style="secondary-link", command=sign_in)
register_btn.grid(row=0, column=1, ipadx=15)
# register_btn

for widget in register_frame.winfo_children():
    widget.grid_configure(padx=5)

# register_frame end

# right_label_group
right_label_group=ttb.Frame(right_content_frame)
right_label_group.grid(row=1, column=0)
# right_label_group

# right_label
right_label=ttb.Label(right_label_group, text="Welcome to Tephdy Tech", font=custom_font)
right_label.grid(row=0, column=0, sticky="news", pady=5)
# right_label

# right_sub_label
right_sub_label=ttb.Label(right_label_group, text="The leader in Tech Solution", font="Calibre 9")
right_sub_label.grid(row=1, column=0, sticky="news")
# right_sub_label

# right_form
right_form=ttb.Frame(right_content_frame)
right_form.grid(row=2, column=0, sticky="news", pady=25)
right_form.columnconfigure(0, weight=2)

# user_name_label
user_name_label=ttb.Label(right_form, text="Username", font="Calibre 7")
user_name_label.grid(row=0, column=0, sticky="ew")
# user_name_label

# user_text_entry
user_text_entry=ttb.Entry(right_form, font="bold")
user_text_entry.grid(row=1, column=0, sticky="ew")
# user_text_entry

# # user_email_label
# user_email_label=ttb.Label(right_form, text="Email", font="Calibre 7")
# user_email_label.grid(row=2, column=0, sticky="ew")
# # user_name_label
#
# # user_email_entry
# user_email_entry=ttb.Entry(right_form, font="bold")
# user_email_entry.grid(row=3, column=0, sticky="ew")
# # user_email_entry

# user_password_label
user_password_label=ttb.Label(right_form, text="Password", font="Calibre 7")
user_password_label.grid(row=4, column=0, sticky="ew")
# user_password_label

# user_password_entry
user_password_entry=ttb.Entry(right_form, show="*", font="bold")
user_password_entry.grid(row=5, column=0, sticky="ew")
# user_password_entry

# login_btn
login_btn=ttb.Button(right_form, text="Login", style="info")
login_btn.grid(row=6, column=0, sticky="ew")
# login_btn

for widget in right_form.winfo_children():
    widget.grid_configure(pady=5)

# other_way
# other_way=ttb.Frame(right_form)
# other_way.grid(row=7, column=0, pady=15)
# other_way

# # other_way_label
# other_way_label=ttb.Label(other_way, text="Create account using:")
# other_way_label.grid(row=0, column=0)
# # other_way_label
#
# # fb_icon
# fb_icon=ttk.PhotoImage(file="icons_images/facebook.png")
# fb_label=ttb.Label(other_way, image=fb_icon)
# fb_label.grid(row=0, column=1)
# # fb_icon
#
# # linkedin_icon
# linkedin_icon=ttk.PhotoImage(file="icons_images/linkedin.png")
# linkedin_label=ttb.Label(other_way, image=linkedin_icon)
# linkedin_label.grid(row=0, column=2)
# # linkedin_icon
#
# # google_icon
# google_icon=ttk.PhotoImage(file="icons_images/google.png")
# google_label=ttb.Label(other_way, image=google_icon)
# google_label.grid(row=0, column=3)
# # google_icon
#
# for widget in other_way.winfo_children():
#     widget.grid_configure(padx=5)


# right_form

# right_content

# main_frame_contents

# run
window.mainloop()