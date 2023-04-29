"""Question 1 - 

Description - Create a small command-line program in Python to calculate the total invoice amount for the below purchases - 

Book - Introduction to Python Programming : Rs 499.00

Book - Python Libraries Cookbook : Rs. 855.00

Book - Data Science in Python : Rs. 645.00


Taxes and additional charges are described as details - 

GST : 12%

Delivery Charges : Rs. 250.00"""

book1=int(input("how many copies of 'Introduction to Python Programming(Rs. 499.00)' do you want : "))
book2=int(input("how many copies of 'Python Libraries Cookbook(Rs. 855.00)' do you want : "))
book3=int(input("how many copies of 'Data Science in Python(Rs.645.00)' do you want : "))
c1=499.00
c2=855.00
c3=645.00
dc=250.00
three_books_total=c1*book1+c2*book2+c3*book3
print("-------------------------------------------------------------------------")
print("Amount for {} books of 'Introduction to Python Programming' = {}".format(book1,c1*book1))
print("Amount for {} books of ' Python Libraries Cookbook' = {}".format(book2,c2*book2))
print("Amount for {} books of ' Data Science in Python' = {}".format(book3,c3*book3))

print("Delivery Charges : ", dc)

gst = (three_books_total/100)*12
print("Amount for 12% of GST = ", gst)

total_amount = dc+three_books_total+gst
print("TOTAL AMOUNT = ", total_amount)


'''
         OUTPUT 1

how many copies of 'Introduction to Python Programming(Rs. 499.00)' do you want : 2
how many copies of 'Python Libraries Cookbook(Rs. 855.00)' do you want : 3
how many copies of 'Data Science in Python(Rs.645.00)' do you want : 2
-------------------------------------------------------------------------
Amount for 2 books of 'Introduction to Python Programming' = 998.0
Amount for 3 books of ' Python Libraries Cookbook' = 2565.0
Amount for 2 books of ' Data Science in Python' = 1290.0
Delivery Charges :  250.0
Amount for 12% of GST =  582.36
TOTAL AMOUNT =  5685.36


        OUTPUT 2
show many copies of 'Introduction to Python Programming(Rs. 499.00)' do you want : 4
how many copies of 'Python Libraries Cookbook(Rs. 855.00)' do you want : 5
how many copies of 'Data Science in Python(Rs.645.00)' do you want : 2
-------------------------------------------------------------------------
Amount for 4 books of 'Introduction to Python Programming' = 1996.0
Amount for 5 books of ' Python Libraries Cookbook' = 4275.0
Amount for 2 books of ' Data Science in Python' = 1290.0
Delivery Charges :  250.0
Amount for 12% of GST =  907.3199999999999
TOTAL AMOUNT =  8718.32
'''