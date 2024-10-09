from tkinter import *
from speedtest import Speedtest  # Import the Speedtest class explicitly

def speedcheck():
    sp = Speedtest()  # Directly use Speedtest
    sp.get_best_server()  
    down = str(round(sp.download() / (10 ** 6), 3)) + " Mbps"
    up = str(round(sp.upload() / (10 ** 6), 3)) + " Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)

sp = Tk()
sp.title("WiFi Speed Checker")
sp.geometry("500x500")
sp.config(bg="#C1D8C3")

# Center labels and button
lab = Label(sp, text="Internet Speed Test", font=("Times New Roman", 30, "bold"), bg="blue", fg="white")
lab.place(relx=0.5, y=60, height=50, width=380, anchor="center")

lab_download = Label(sp, text="Download speed", font=("Times New Roman", 22, "bold"), bg="black", fg="white")
lab_download.place(relx=0.5, y=120, height=50, width=380, anchor="center")

lab_down = Label(sp, text="00", font=("Times New Roman", 22, "bold"), bg="black", fg="white")
lab_down.place(relx=0.5, y=180, height=50, width=380, anchor="center")

lab_upload = Label(sp, text="Upload speed", font=("Times New Roman", 22, "bold"), bg="black", fg="white")
lab_upload.place(relx=0.5, y=240, height=50, width=380, anchor="center")

lab_up = Label(sp, text="00", font=("Times New Roman", 22, "bold"), bg="black", fg="white")
lab_up.place(relx=0.5, y=300, height=50, width=380, anchor="center")

button = Button(sp, text="Check speed", font=("Times New Roman", 22, "bold"), relief="raised", bg="#00a400", command=speedcheck)
button.place(relx=0.5, y=360, height=50, width=380, anchor="center")

sp.mainloop()
