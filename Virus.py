virus_kill = ('This program will kill covid-19.....type selection(quarintine/go-out)')


if virus_kill.lower().strip()== 'quarintine':

    print('Good choice; you will be safe while we work on a vaccine.')

    

if virus_kill.lower().strip()== 'go-out':

    print('Stay safe, please wash your hands, avoid large groups and avoid touching your face....')


vaccination_options = ('Lets select the best vaccination, to kill covid-19')

vacine = 100

vacine_one = 1

vacine_two = 2

vacine_three = 3

vacine_four = 4

vacine_five = 5


while vaccination_options == "Count between 1 and 5":

    vacine = float(input('Please select a vaccine option betwenn 1 and 5: '))

    if vacine.float().strip() == '1':

         print('vacine one is not the best option')

    if vacine.float().strip() == '2':

         print('vaccine two is strong but not killing the virus')

    if vacine.float().strip() == '3':

         print('This is it; this vaccine will kill the virus')

    if vacine.float().strip() == '4':

         print('This option is too strong; it kills the virus and cells')

    if vacine.float().strip() == '5':

         print('This option is working well; but the virus returns after a few hours')

        



