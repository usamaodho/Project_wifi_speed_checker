from tkinter import *
import speedtest 


def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_best_server()  # Use get_best_server() instead of get_servers()
    down = str(round(sp.download() / (10 ** 6), 3)) + " Mbps"
    up = str(round(sp.upload() / (10 ** 6), 3)) + " Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)

sp = Tk()
sp.title("WiFi Speed Checker")
sp.geometry("500x500")
sp.config(bg="#C1D8C3")

lab = Label(sp, text="Internet Speed Test", font=("Times New Roman", 30, "bold"), bg="blue", fg="white")
lab.place(x=50, y=60, height=50, width=380)

lab = Label(sp, text="Download speed", font=("Times New Roman", 22, "bold"), bg="black", fg="white")
lab.place(x=50, y=120, height=50, width=380)

lab_down = Label(sp, text="00", font=("Times New Roman", 22, "bold"), bg="black", fg="white")
lab_down.place(x=50, y=180, height=50, width=380)

lab = Label(sp, text="Upload speed", font=("Times New Roman", 22, "bold"), bg="black", fg="white")
lab.place(x=50, y=240, height=50, width=380)

lab_up = Label(sp, text="00", font=("Times New Roman", 22, "bold"), bg="black", fg="white")
lab_up.place(x=50, y=300, height=50, width=380)

button = Button(sp, text="Check speed", font=("Times New Roman", 22, "bold"), relief="raised", bg="#00a400", command=speedcheck)
button.place(x=50, y=360, height=50, width=380)

sp.mainloop()

