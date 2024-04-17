import mysql.connector

def connect_to_db():

    # trying to connect
    try:
        conn = mysql.connector.connect(
            database = "library_system_db",
            user ="root",
            password = "751996Jl",
            host = "localhost"
        )

        # return conn if its good to go
        return conn
    
    # connection failed shows error
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        