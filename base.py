from sqlite3 import connect, Error



def Kino_Delete(id):
    try:
        con = connect("kino.db")
        cursor = con.cursor()
        cursor.execute(f"delete from kinolar where KINO_ID = {id};")
        con.commit()
        cursor.close()
    except (Error, Exception) as eror:
        print("Eror", eror)
    finally:
        if con:
            con.close()

















def Kinolar_Read():
    try:
        con = connect("kino.db")
        cursor = con.cursor()
        cursor.execute(f"select *
                       
                       from KINOLAR")
        a = cursor.fetchall()
        cursor.close()
        return a
    except (Error, Exception) as eror:
        print("Eror", eror)
    finally:
        if con:
            con.close()











def Kino_add(kino_nomi, kino_des, kino_url):
    try:
        con = connect("kino.db")
        cursor = con.cursor()
        cursor.execute("INSERT INTO KINOLAR(KINO_NAME, KINO_DESCRIPTION, KINO_URL) VALUES(?, ?, ?)", (kino_nomi, kino_des, kino_url))
        con.commit()
        cursor.close()
    except (Error, Exception) as eror:
        print("Eror", eror)
    finally:
        if con:
            con.close()
        

def Kino_Read(id):
    try:
        con = connect("kino.db")
        cursor = con.cursor()
        cursor.execute(f"select * from KINOLAR where KINO_ID={id}")
        a = cursor.fetchone()
        cursor.close()
        return a
    except (Error, Exception) as eror:
        print("Eror", eror)
    finally:
        if con:
            con.close()


# try:
#     con = connect("kino.db")
#     cursor = con.cursor()
#     cursor.execute("""
#                    CREATE TABLE KINOLAR(
#                        KINO_ID INTeger PRIMARY KEY NOT NULL,
#                        KINO_NAME TEXT NOT NULL,
#                        KINO_DESCRIPTION TEXT NOT NULL,
#                        KINO_URL TEXT NOT NULL
#                        );
#                    """)
#     con.commit()
#     cursor.close()
# except (Error, Exception) as eror:
#     print("Eror", eror)
# finally:
#     if con:
#         con.close()
        
    