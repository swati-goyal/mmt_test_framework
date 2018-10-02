# Booking Test on makemytrip.com
This is an automation framework to test the booking functionality of makemytrip.com written in python3 using selenium as 
testing tool and unittest library.

Steps to run the test script:
1. Requirements - You must have python3, selenium library and unittest package in your machine.
2. Open terminal 
3. Run command - $git clone https://github.com/swati-goyal/mmt_test_framework.git
4. Run command - $cd mmt_test_framework
5. Run command - $ls
6. Make sure these files are present: extra.txt, mmttest, xpath.json
7. Make sure geckodriver is in the executable path, if not please check this [link](https://stackoverflow.com/questions/40388503/how-to-put-geckodriver-into-path).
8. If you need to run this via "Chrome", please uncomment line#15 and please add '#' before line#16 in mmttest file, change the path to chromedriver executable as available on the machine.
9. Run command - $python3 mmttest
10. Run command - $ls
11. Check the "final_booking_page.png" file to verify the result. 
