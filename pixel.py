import customtkinter

customtkinter.set_appearance_mode("dark")

app = customtkinter.CTk()
app.geometry("500x300")

frame = customtkinter.CTkFrame(master=app, bg_color="black")
frame.pack(pady=20, padx=60, fill="both", expand=True)

btn = customtkinter.CTkButton(master=frame,text="Pixel Stirpe", text_color=("#FB8500"), font=("arial", 35, "bold"), fg_color="transparent", 
                              border_width=2, border_color="#FB8500", corner_radius=24, hover="False", width=280, height=70)
btn.pack(pady=12, padx=10)

label = customtkinter.CTkLabel(master=frame, text="Last Refresh at 10:59 am 18 February 2024", text_color=("#FB8500"), font=("arial" , 15))
label.pack()

all = customtkinter.CTkButton(master=frame, text="All", text_color=("#FB8500"), font=("arial", 15), fg_color="transparent", border_width=1,
                              border_color="#FB8500", corner_radius=10)
all.place(relx=0.3, rely=0.13, anchor="e")

refresh = customtkinter.CTkButton(master=frame, text="REFRESH", text_color=("#FB8500"), font=("arial", 15), fg_color="transparent", border_width=1,
                              border_color="#FB8500", corner_radius=10)
refresh.place(relx=0.7, rely=0.13, anchor="w")

companyName= customtkinter.CTkLabel(master=frame, text="Company Name", text_color=("#fafafa"), font=("arial", 13, "bold"))
companyName.place(relx=0.26, rely=0.18, anchor="e")

symb= customtkinter.CTkLabel(master=frame, text="SYMB", text_color=("#fafafa"), font=("arial", 13, "bold"))
symb.place(relx=0.32, rely=0.18, anchor="e")

price= customtkinter.CTkLabel(master=frame, text="Price(USD)", text_color=("#fafafa"), font=("arial", 13, "bold"))
price.place(relx=0.40, rely=0.18, anchor="e")

change_per= customtkinter.CTkLabel(master=frame, text="Change(%)", text_color=("#fafafa"), font=("arial", 13, "bold"))
change_per.place(relx=0.45, rely=0.18, anchor="center")

change_usd= customtkinter.CTkLabel(master=frame, text="Change(USD)", text_color=("#fafafa"), font=("arial", 13, "bold"))
change_usd.place(relx=0.54, rely=0.18, anchor="center")

sector= customtkinter.CTkLabel(master=frame, text="Industry(sector)", text_color=("#fafafa"), font=("arial", 13, "bold"))
sector.place(relx=0.61, rely=0.18, anchor="w")

stock= customtkinter.CTkLabel(master=frame, text="Stock Progress", text_color=("#fafafa"), font=("arial", 13, "bold"))
stock.place(relx=0.72, rely=0.18, anchor="w")

inc= customtkinter.CTkLabel(master=frame, text="Broadcom Inc", text_color=("#fafafa"), font=("arial", 13))
inc.place(relx=0.25, rely=0.24, anchor="e")

coca= customtkinter.CTkLabel(master=frame, text="Coca-cola consolidated \n"
                             "Inc", text_color=("#fafafa"), justify="left", font=("arial", 13))
coca.place(relx=0.29, rely=0.32, anchor="e")

adobe= customtkinter.CTkLabel(master=frame, text="Adobe Inc", text_color=("#fafafa"), font=("arial", 13))
adobe.place(relx=0.24, rely=0.39, anchor="e")

corp= customtkinter.CTkLabel(master=frame, text="NVIDIA Corp", text_color=("#fafafa"), font=("arial", 13))
corp.place(relx=0.25, rely=0.47, anchor="e")

netflix= customtkinter.CTkLabel(master=frame, text="Netflix Inc", text_color=("#fafafa"), font=("arial", 13))
netflix.place(relx=0.24, rely=0.54, anchor="e")

lululemon= customtkinter.CTkLabel(master=frame, text="Lululemon Athletica", text_color=("#fafafa"), font=("arial", 13))
lululemon.place(relx=0.28, rely=0.61, anchor="e")

avgo= customtkinter.CTkLabel(master=frame, text="AVGO", text_color=("#fafafa"), font=("arial", 13))
avgo.place(relx=0.32, rely=0.24, anchor="e")

cola= customtkinter.CTkLabel(master=frame, text="COKE", text_color=("#fafafa"), font=("arial", 13))
cola.place(relx=0.32, rely=0.32, anchor="e")

adbe= customtkinter.CTkLabel(master=frame, text="ADBE", text_color=("#fafafa"), font=("arial", 13))
adbe.place(relx=0.32, rely=0.39, anchor="e")

nvda= customtkinter.CTkLabel(master=frame, text="NVDA", text_color=("#fafafa"), font=("arial", 13))
nvda.place(relx=0.32, rely=0.47, anchor="e")

nflx= customtkinter.CTkLabel(master=frame, text="NFLX", text_color=("#fafafa"), font=("arial", 13))
nflx.place(relx=0.32, rely=0.54, anchor="e")

lulu= customtkinter.CTkLabel(master=frame, text="LULU", text_color=("#fafafa"), font=("arial", 13))
lulu.place(relx=0.32, rely=0.61, anchor="e")

avgo_price= customtkinter.CTkLabel(master=frame, text="1245.48", text_color=("#fafafa"), font=("arial", 13))
avgo_price.place(relx=0.39, rely=0.24, anchor="e")

cola_price= customtkinter.CTkLabel(master=frame, text="846.07", text_color=("#fafafa"), font=("arial", 13))
cola_price.place(relx=0.39, rely=0.32, anchor="e")

adbe_price= customtkinter.CTkLabel(master=frame, text="546.66", text_color=("#fafafa"), font=("arial", 13))
adbe_price.place(relx=0.39, rely=0.39, anchor="e")

nvda_price= customtkinter.CTkLabel(master=frame, text="726.13", text_color=("#fafafa"), font=("arial", 13))
nvda_price.place(relx=0.39, rely=0.47, anchor="e")

nflx_price= customtkinter.CTkLabel(master=frame, text="583.95", text_color=("#fafafa"), font=("arial", 13))
nflx_price.place(relx=0.39, rely=0.54, anchor="e")

lulu_price= customtkinter.CTkLabel(master=frame, text="449.60", text_color=("#fafafa"), font=("arial", 13))
lulu_price.place(relx=0.39, rely=0.61, anchor="e")

avgo_per= customtkinter.CTkLabel(master=frame, text="-1.55", text_color=("#fafafa"), font=("arial", 13))
avgo_per.place(relx=0.45, rely=0.24, anchor="center")

cola_per= customtkinter.CTkLabel(master=frame, text="-2.14", text_color=("#fafafa"), font=("arial", 13))
cola_per.place(relx=0.45, rely=0.32, anchor="center")

adbe_per= customtkinter.CTkLabel(master=frame, text="-7.14", text_color=("#fafafa"), font=("arial", 13))
adbe_per.place(relx=0.45, rely=0.39, anchor="center")

nvda_per= customtkinter.CTkLabel(master=frame, text="-0.06", text_color=("#fafafa"), font=("arial", 13))
nvda_per.place(relx=0.45, rely=0.47, anchor="center")

nflx_per= customtkinter.CTkLabel(master=frame, text="-1.60", text_color=("#fafafa"), font=("arial", 13))
nflx_per.place(relx=0.45, rely=0.54, anchor="center")

lulu_per= customtkinter.CTkLabel(master=frame, text="-2.04", text_color=("#fafafa"), font=("arial", 13))
lulu_per.place(relx=0.45, rely=0.61, anchor="center")

avgo_change= customtkinter.CTkLabel(master=frame, text="-19.59", text_color=("#fafafa"), font=("arial", 13))
avgo_change.place(relx=0.54, rely=0.24, anchor="center")

cola_change= customtkinter.CTkLabel(master=frame, text="-18.52", text_color=("#fafafa"), font=("arial", 13))
cola_change.place(relx=0.54, rely=0.32, anchor="center")

adbe_change= customtkinter.CTkLabel(master=frame, text="-43.78", text_color=("#fafafa"), font=("arial", 13))
adbe_change.place(relx=0.54, rely=0.39, anchor="center")

nvda_change= customtkinter.CTkLabel(master=frame, text="-0.45", text_color=("#fafafa"), font=("arial", 13))
nvda_change.place(relx=0.54, rely=0.47, anchor="center")

nflx_change= customtkinter.CTkLabel(master=frame, text="-19.51", text_color=("#fafafa"), font=("arial", 13))
nflx_change.place(relx=0.54, rely=0.54, anchor="center")

lulu_change= customtkinter.CTkLabel(master=frame, text="-9.38", text_color=("#fafafa"), font=("arial", 13))
lulu_change.place(relx=0.54, rely=0.61, anchor="center")

avgo_sector= customtkinter.CTkLabel(master=frame, text="Semi-conductors \n"
                                    "and semi-conductor \n"
                                    "equipment \n"
                                    "(Technology)", text_color=("#fafafa"),justify="left", font=("arial", 13))
avgo_sector.place(relx=0.61, rely=0.24, anchor="w")

cola_sector= customtkinter.CTkLabel(master=frame, text="Beverages \n"
                                    "(Consumer Non- \n"
                                      "Cyclicals)", text_color=("#fafafa"), justify="left", font=("arial", 13))
cola_sector.place(relx=0.61, rely=0.32, anchor="w")

adbe_sector= customtkinter.CTkLabel(master=frame, text="Software & IT services \n"
                                    "(Technology)", text_color=("#fafafa"), justify="left", font=("arial", 13))
adbe_sector.place(relx=0.61, rely=0.39, anchor="w")

nvda_sector= customtkinter.CTkLabel(master=frame, text="Semi-conductors \n"
                                    "and semi-conductor \n"
                                    "equipment \n"
                                    "(Technology)", text_color=("#fafafa"), justify="left", font=("arial", 13))
nvda_sector.place(relx=0.61, rely=0.47, anchor="w")

nflx_sector= customtkinter.CTkLabel(master=frame, text="Software & IT services \n"
                                    "(Technology)", text_color=("#fafafa"), justify="left", font=("arial", 13))
nflx_sector.place(relx=0.61, rely=0.54, anchor="w")

lulu_sector= customtkinter.CTkLabel(master=frame, text="Textiles & apparel \n"
                                    "(Consoumer Cyclicals)", text_color=("#fafafa"), justify="left", font=("arial", 13))
lulu_sector.place(relx=0.61, rely=0.61, anchor="w")

avgo_stock= customtkinter.CTkLabel(master=frame, text="Progressive", text_color=("#fafafa"), font=("arial", 13))
avgo_stock.place(relx=0.73, rely=0.24, anchor="w")

cola_stock= customtkinter.CTkLabel(master=frame, text="Regressive", text_color=("#fafafa"), font=("arial", 13))
cola_stock.place(relx=0.73, rely=0.32, anchor="w")

adbe_stock= customtkinter.CTkLabel(master=frame, text="Stagnant", text_color=("#fafafa"), font=("arial", 13))
adbe_stock.place(relx=0.73, rely=0.39, anchor="w")

nvda_stock= customtkinter.CTkLabel(master=frame, text="Prograssive", text_color=("#fafafa"), font=("arial", 13))
nvda_stock.place(relx=0.73, rely=0.47, anchor="w")

nflx_stock= customtkinter.CTkLabel(master=frame, text="Regressive", text_color=("#fafafa"), font=("arial", 13))
nflx_stock.place(relx=0.73, rely=0.54, anchor="w")

lulu_stock= customtkinter.CTkLabel(master=frame, text="Stagnant", text_color=("#fafafa"), font=("arial", 13))
lulu_stock.place(relx=0.73, rely=0.61, anchor="w")

app.mainloop()