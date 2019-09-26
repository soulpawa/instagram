from diego_util import login
import datetime
import time
import random
import winsound
import csv


inicio = datetime.datetime.now()
print("...Start unfollowing at " + inicio.strftime("%c"))
api = login()
line_count = 0

with open('followed_TEST.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    for row in csv_reader:
        try:
            print(line_count, ":", datetime.datetime.now().strftime("%c"))
            with open('followings.csv') as csv_white_list:
                white_list = csv.reader(csv_white_list, delimiter=';')
                unfollow = True
                for white_list_row in white_list:
                    try:
                        pk = white_list_row[0]
                        pk2 = row[2]
                        if row[2] == pk:
                            unfollow = False
                            print("Not unfollowing, true follow")
                            break
                    except Exception as err:
                        print("exception: ", err)
                if unfollow:
                    # api.unfollow(row[2])
                    print(f'\t{row[0]} >UNFOLLOWED: {row[1]} >ID:{row[2]}.')
            line_count += 1

        except Exception as err:
            print("exception: ", err)

        finally:
            t = datetime.datetime.now()
            print(f'\t Sleeping................................... ', end="")

            time.sleep(random.randint(60, 70))
            t2 = datetime.datetime.now() - t
            print("Slept for: " + str(t2))


print(f'Processed {line_count} lines.')
print("...End working.... " + str(line_count) + " users unfollowed! " + str(datetime.datetime.now()-inicio))
winsound.Beep(2500, 250)
