# Booking Test on makemytrip.com
This is an automation framework to test the booking functionality of makemytrip.com written in python3 using selenium as 
testing tool and unittest library.

Steps to run the test script:
0. Requirements - You must have python3, selenium library and unittest package in your machine.
1. Open terminal 
2. Run command - $git clone https://github.com/swati-goyal/mmt_test_framework.git
3. Run command - $cd mmt_test_framework
4. Run command - $ls
5. Make sure these files are present: extra.txt, mmttest, xpath.json
6. Make sure geckodriver is in the executable path, if not please check this [link](https://stackoverflow.com/questions/40388503/how-to-put-geckodriver-into-path).
7. If you need to run this via "Chrome", please uncomment line#15 and please add '#' before line#16 in mmttest file, change the path to chromedriver executable as available on the machine.
8. Run command - $python3 mmttest
9. Run command - $ls
10. Check the "final_booking_page.png" file to verify the result. 
