def staff_ranking(cs): 
        """
        Funkcja tworzy ranking pracowników dla każdego miesiąca w którym sklep prowadził działalność.
        """ 
        
        cs.execute("SELECT distinct YEAR(payment_date) as 'Year', MONTH(payment_date) as 'Month' from payment ORDER BY YEAR DESC,MONTH DESC")
        dates=cs.fetchall()
        rank=[]
        for i in dates: 
                wzorzec_daty=f"{i[0]}-{i[1]:02}"
                cs.execute("SELECT staff.staff_id,staff.first_name,staff.last_name,sum(amount) as earn from payment inner join staff on payment.staff_id=staff.staff_id WHERE payment_date LIKE %s GROUP BY staff.staff_id ORDER BY earn DESC LIMIT 1",[wzorzec_daty+ '%'])
                wynik = cs.fetchall()
                rank.append([wzorzec_daty,wynik[0][0],wynik[0][1],wynik[0][2],int(wynik[0][3])])
        
        return rank

def top_10_tournament_players(cs,g_id):
        """
        g_id- id gry
        Funkcja tworzy ranking 10 najlepszych zawodników dla id danej gry.
        Ranking tworzony jest na podstawie liczby wygranych turniejów przez zawodnika.
        """
        cs.execute("SELECT distinct game_id from tournaments")
        g_ids =cs.fetchall()
        g_ids=list(element[0] for element in g_ids)
        if g_id in g_ids:
                cs.execute("SELECT games.title,first_name,last_name,COUNT(list_of_players.customer_id) from list_of_players inner join tournaments on list_of_players.tournament_id=tournaments.tournament_id inner join games on tournaments.game_id=games.game_id inner join customers on list_of_players.customer_id=customers.customer_id WHERE place=1 and games.game_id=%s GROUP BY list_of_players.customer_id ORDER BY COUNT(*) DESC LIMIT 10",[g_id])
                top_10=cs.fetchall()
                return top_10
        else:
                print("Brak turniej dla danej gry.")
                
def best_players(cs):
        """
        Funkcja zwraca graczy którzy wygrali najwiecej turniejów w danej grze.
        """
        cs.execute("SELECT title,first_name,last_name,MAX(won_num) best_player FROM (SELECT games.game_id,games.title,first_name,last_name,COUNT(list_of_players.customer_id) as won_num from list_of_players inner join tournaments on list_of_players.tournament_id=tournaments.tournament_id inner join games on tournaments.game_id=games.game_id inner join customers on list_of_players.customer_id=customers.customer_id WHERE place=1 GROUP BY list_of_players.customer_id ORDER BY COUNT(*) DESC) as sub1 GROUP BY game_id")
        return cs.fetchall()

def top5_selers_AND_rental(cs):
        '''
        Funkcja zwraca 5 najlepszych gier pod względem sumy sprzedaży, 
        oraz 5 najlepszych gier pod względem sumy wynajmu.
        '''
        cs.execute("SELECT games.title as 'Game title',sum(payment.amount) as 'Sum of rental' from payment inner join inventory on payment.rental_id_or_last_rental_id=inventory.inventory_id inner join games on inventory.game_id=games.game_id WHERE rental_id_or_last_rental_id LIKE '___' GROUP BY games.game_id ORDER by sum(payment.amount) DESC LIMIT 5")
        top_5_rental=cs.fetchall()
        
        cs.execute("SELECT games.title as 'Game title',sum(payment.amount) as 'Sum of sold' from payment inner join inventory on substring(payment.rental_id_or_last_rental_id,16)=inventory.inventory_id inner join games on inventory.game_id=games.game_id WHERE rental_id_or_last_rental_id LIKE 'l%' GROUP BY games.game_id ORDER by sum(payment.amount) DESC LIMIT 5")
        top_5_sold=cs.fetchall()
        return  top_5_rental,top_5_sold

def days_rental(cs):
        '''
        Funkcja tworzy wykres punktowy oraz pudełkowy czasów wynajmowania gier. [dni]
        '''
        import itertools
        cs.execute("SELECT DATEDIFF(return_date,rental_date) as 'Liczba dni w wypożyczeniu' FROM rental ")
        X = cs.fetchall()
        X_lista = list(itertools.chain(*X))
        return(X,X_lista)
        

def longest_tournament(cs):
        '''
        Funkcja tworzy tabelę 10 najdluższych turniejów,
        oraz średni czas trwania turnieju danej gry.
        '''

        cs.execute("SELECT games.game_id,games.title,TIMESTAMPDIFF(MINUTE,tournaments.start_date,tournaments.end_date) as 'Czas_trwania_turnieju[min]' from tournaments inner join games on tournaments.game_id=games.game_id ORDER BY TIMESTAMPDIFF(MINUTE,tournaments.start_date,tournaments.end_date) DESC LIMIT 10")
        top_10=cs.fetchall()
        return (top_10)

def longest_tournament_plot(cs):       
        cs.execute("SELECT games.game_id,games.title,sum(TIMESTAMPDIFF(MINUTE,tournaments.start_date,tournaments.end_date)) as 'Czas_trwania_turnieju[min]',count(*) from tournaments inner join games on tournaments.game_id=games.game_id GROUP BY games.title ORDER BY SUM(TIMESTAMPDIFF(MINUTE,tournaments.start_date,tournaments.end_date)) DESC")
        X= cs.fetchall()
        sr=[]
        for i in range(len(X)):
                sr.append((X[i][0],round(X[i][2]/X[i][3],2)))
        kategorie = [sr[i][0] for i in range(len(sr))]
        wartosci = [sr[i][1] for i in range(len(sr))]
        return(kategorie,wartosci)

def top_10_clients(cs):
        cs.execute("select payment.customer_id,customers.first_name,customers.last_name,sum(amount),count(*) from payment inner join customers on payment.customer_id=customers.customer_id GROUP by payment.customer_id ORDER by sum(amount) DESC")
        X = cs.fetchall()
        top10=X[:10]
        sr=[]
        for i in range(len(X)):
                sr.append((X[i][0],round(X[i][3]/X[i][4],2)))
        kategorie = [sr[i][0] for i in range(len(sr))]
        wartosci = [sr[i][1] for i in range(len(sr))]

        return top10,kategorie,wartosci

def sells_VS_rental_num(cs):
        cs.execute("""
SELECT num_of_rental,CASE WHEN sold.inventory_id is null then 0 ELSE 1 END
FROM (
    SELECT inventory_id
    FROM payment 
    INNER JOIN rental ON substring(payment.rental_id_or_last_rental_id, 16) = rental.rental_id
    WHERE payment.rental_id_or_last_rental_id LIKE 'l%' 
    GROUP BY inventory_id
) AS sold
RIGHT JOIN (
    SELECT inventory_id, COUNT(*) AS num_of_rental
    FROM payment
    LEFT JOIN rental ON payment.rental_id_or_last_rental_id = rental.rental_id
    WHERE payment.rental_id_or_last_rental_id LIKE '___' 
    GROUP BY inventory_id
) AS wyp
ON sold.inventory_id = wyp.inventory_id;
""")
        X=cs.fetchall()
        return X
        

if __name__ == "__main__":
        import itertools
        import mysql.connector
        import pandas as pd
        import matplotlib.pyplot as plt

        con = mysql.connector.connect(
                host = "127.0.0.1",
                user = "root",
                password = "password",
                database = "clients_base",
                )
        if not con:
                raise Exception("connection error")
        cs = con.cursor()
        sells_rental_num=sells_VS_rental_num(cs)
        print(sells_rental_num)
        X=[]
        Y=[]
        for i in sells_rental_num:
                X.append(int(i[1]))
                Y.append(i[0])
        print(X,Y)
        
        X= [0, 9, 0, 11, 10, 9, 8, 11, 9, 8, 7, 5, 3, 3, 1, 1, 0, 0, 0, 0, 0, 0, 3, 2, 2, 2, 1] 
        plt.hist(X)
        plt.show()
        
        # plt.plot(X,Y,'o')
        # plt.show()


        # df = pd.DataFrame(staff_ranking(cs),columns=["Date","Staff_id","First_name","Last_Name","Earn"])
        # print("\n                 Employee of the month ")
        # print(df,"\n")

        # df = pd.DataFrame(top_10_tournament_players(cs,g_id=1),columns=["Game_title","First_name","Last_name","Num_of_wins"])
        # print("\n                 Top10 players")
        # print(df,"\n")
        
        # df_rental = pd.DataFrame(top5_selers_AND_rental(cs)[0],columns=["Game Title", "Sum of rental amount"])
        # print("\n                  Top5 games earning by rental")
        # print(df_rental,"\n")
        
        # df_sold = pd.DataFrame(top5_selers_AND_rental(cs)[1],columns=["Game Title", "Sum of solds amount"])
        # print("\n                 Top 5 best-selling games")
        # print(df_sold,"\n")

        # #Najdluższy czas wynajmowania
        # plt.plot(days_rental(cs)[0],'o')
        # plt.title("Wykres punktowy czasu wynajmu gry.")
        # plt.xlabel("ID_gry")
        # plt.ylabel("Czas wynajmu [dni].")
        # plt.show()
        # plt.boxplot(days_rental(cs)[1],vert=False)
        # plt.xlabel("Czas wynajmu [dni]")
        # plt.title("Wykres pudełkowy wynajmu gier.")
        # plt.show()
        # #Najdłuższy czas turnieju
        # df=pd.DataFrame(longest_tournament(cs),columns=["id_gry","Tytuł","czas trwania turnieju[min]"])
        # print(df,"\n")
        # #Wykres średnich czasu trwania turnieju
        
        # plt.bar(longest_tournament_plot(cs)[0],longest_tournament_plot(cs)[1])
        # plt.title("Wykres słupkowy średniego czasu turniejów")
        # plt.xlabel('Id gry')
        # plt.ylabel('Minuty')
        # plt.show()

        # #Top_10 najwięcej wydających klientów, oraz wykres średniej wszystkich transakcji.
        
        # tabela=pd.DataFrame(top_10_clients(cs)[0],columns=["Id_klienta","Imię","Nazwisko","Suma","Ilość płatności"])
        # print(tabela)
        # plt.bar(top_10_clients(cs)[1],top_10_clients(cs)[2])
        # plt.title("Średnia wartość transakcji klienta")
        # plt.xlabel("Id klietna")
        # plt.ylabel("Kwota")
        # plt.show()
        # x=pd.DataFrame(best_players(cs),columns=["Game_title","First_name","Last_name","Num_of_wins"])
        # print(x)
        # con.close()