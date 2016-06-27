while True:
    try:
        number = int(input("whats your fav number?\n"))
        print(18/number)
        break
    except ValueError:
        print("Make sure and enter a number")
    except ZeroDivisionError:
        print("Dont't pick zero!")
    except:
        break
    finally:
        print("-----------------------")

