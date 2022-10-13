import Game_World
import network_commn_client


def driver_code():
    net=network_commn_client.Network_Commn()

    myid=net.id

    if(myid==1):

        #Wait indefinitely till server response arrived, nd move on once that happens

    #Create Game world

    while True:
        #send ready to server
        #wait for server response OK

        #wait for question
        #Once question arrived
        #Make 2 threads:
        #1 waiting indefinitely for server to announce winner, if winner announced
        #check if winner matching with myid, accordingly update board_state, terminate both threads and repeat
        #1 waiting for user input, if input check if correct, if yes, send to server myid break, if no repeat
