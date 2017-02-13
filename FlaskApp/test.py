from dbconnect import connection

def tst():
    try:
        c, conn = connection()
        print("okay")
    except Exception as e:
        print(str(e))
if __name__ == '__main__':
    tst()
