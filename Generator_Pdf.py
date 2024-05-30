import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
import os
from matplotlib.backends.backend_pdf import PdfPages
from Analiza_danych import *
from datetime import date
current_path = os.path.dirname(os.path.abspath(__file__))

con = mysql.connector.connect(
                host = "127.0.0.1",
                user = "root",
                password = "password",
                database = "clients_base",
                )
if not con:
                raise Exception("connection error")
cs = con.cursor()

output_path = os.path.join(current_path, 'Analiza.pdf')
pp = PdfPages(output_path)
today = date.today()
plt.figure(figsize=(5, 0.5))
plt.suptitle(f"Raport {today}",fontsize=26)
pp.savefig()

df = pd.DataFrame(staff_ranking(cs),columns=["Date","Staff_id","First_name","Last_Name","Earn"])
fig, ax =plt.subplots(figsize=(12,12))
plt.title("Pracownicy miesiąca")
ax.axis('tight')
ax.axis('off')
the_table = ax.table(cellText=df.values,colLabels=df.columns,loc='center')
pp.savefig()

g_id=1
df = pd.DataFrame(top_10_tournament_players(cs,g_id=1),columns=["Game_title","First_name","Last_name","Num_of_wins"])
fig, ax =plt.subplots(figsize=(12,12))
ax.axis('tight')
ax.axis('off')
plt.title(f"Top 10 graczy turniejowych dla gry o id = {g_id}")
the_table = ax.table(cellText=df.values,colLabels=df.columns,loc='center')
pp.savefig()

df = pd.DataFrame(top5_selers_AND_rental(cs)[0],columns=["Game Title", "Sum of rental amount"])
fig, ax =plt.subplots(figsize=(12,4))
ax.axis('tight')
ax.axis('off')
plt.title("Top5 zarabiających gier na wynajmie")
the_table = ax.table(cellText=df.values,colLabels=df.columns,loc='center')
pp.savefig()

df = pd.DataFrame(top5_selers_AND_rental(cs)[1],columns=["Game Title", "Sum of rental amount"])
fig, ax =plt.subplots(figsize=(12,4))
ax.axis('tight')
ax.axis('off')
plt.title("Top5 zarabiających gier na sprzedaży")
the_table = ax.table(cellText=df.values,colLabels=df.columns,loc='center')
pp.savefig()

df=pd.DataFrame(longest_tournament(cs),columns=["id_gry","Tytuł","czas trwania turnieju[min]"])
fig, ax =plt.subplots(figsize=(12,4))
ax.axis('tight')
ax.axis('off')
plt.title("Najdłuższe turnieje")
the_table = ax.table(cellText=df.values,colLabels=df.columns,loc='center')
pp.savefig()

plt.figure()
plt.clf()
plt.bar(longest_tournament_plot(cs)[0],longest_tournament_plot(cs)[1])
plt.title("Wykres słupkowy średniego czasu turniejów")
plt.xlabel('Id gry')
plt.ylabel('Minuty')
pp.savefig()

plt.figure()
plt.clf()
plt.plot(days_rental(cs)[0],'o')
plt.title("Wykres punktowy czasu wynajmu gry.")
plt.xlabel("ID_gry")
plt.ylabel("Czas wynajmu [dni].")
pp.savefig()

plt.figure()
plt.clf()
plt.boxplot(days_rental(cs)[1],vert=False)
plt.xlabel("Czas wynajmu [dni]")
plt.title("Wykres pudełkowy wynajmu gier.")
pp.savefig()

df=pd.DataFrame(longest_tournament(cs),columns=["id_gry","Tytuł","czas trwania turnieju[min]"])
fig, ax =plt.subplots(figsize=(12,4))
ax.axis('tight')
ax.axis('off')
plt.title("Najdłuższe turnieje- Top10")
the_table = ax.table(cellText=df.values,colLabels=df.columns,loc='center')
pp.savefig()

df=pd.DataFrame(top_10_clients(cs)[0],columns=["Id_klienta","Imię","Nazwisko","Suma","Ilość płatności"])
fig, ax =plt.subplots(figsize=(12,4))
ax.axis('tight')
ax.axis('off')
plt.title("Najwięcej wydający klienci.")
the_table = ax.table(cellText=df.values,colLabels=df.columns,loc='center')
pp.savefig()

plt.figure()
plt.clf()
plt.bar(top_10_clients(cs)[1],top_10_clients(cs)[2])
plt.title("Średnia wartość transakcji klienta")
plt.xlabel("Id klietna")
plt.ylabel("Kwota")
pp.savefig()

pp.close()