#main

#max tickets
MAX_TICKETS = 3

# loop 4 tickets sold
tickets_sold = 0
while tickets_sold < MAX_TICKETS:
    name = input("Please enter your name or 'xxx' to quit")

    tickets_sold += 1

    if name == 'xxx':
     break

#output number of tickets sold
if tickets_sold == MAX_TICKETS:
    print("Congratulations you have sold out all the tickets")
else:
    print("you have sold {} ticket/s. There is  {} ticket/s"
          "remaining".format(tickets_sold, MAX_TICKETS - tickets_sold))