# -*- coding = uft-8 -*-
# @File: transaction.py.py
# @Software: PyCharm
from db_helper import *
from datetime import datetime


# 3.Document return
def document_return(title, card_number):
    borrow_info_str = f''' SELECT
                            copy_id,
                            b_datetime 
                        FROM
                            borrow 
                        WHERE
	                        reader_id = {card_number} 
	                        AND r_datetime IS NULL 
	                        AND copy_id IN (
	                            SELECT
		                            copy_id 
	                            FROM
		                            copy
		                        NATURAL JOIN document 
                        WHERE
	                        title = '{title}')'''
    borrow_info_info = dbhelper_singleton.query_data(borrow_info_str)
    while len(borrow_info_info) == 0:
        title = input("input wrong, please enter the right title:")
        borrow_info_info = dbhelper_singleton.query_data(borrow_info_str)
    copy_id, borrow_time = borrow_info_info[0][0], borrow_info_info[0][1]
    days = (datetime.now() - borrow_time).days
    fine = 0 if days <= 20 else (days - 20) * 0.2
    document_return_sql = f'''UPDATE borrow SET r_datetime=CURRENT_TIMESTAMP, 
                            fine={fine} WHERE reader_id={card_number} and 
                            copy_id={copy_id} and r_datetime is NULL '''
    dbhelper_singleton.update_data(document_return_sql)
    print("successfully returned")


# 4.Document reserve
def document_reserve(title, card_number):
    pass


# 6.Print the list of documents reserved by a reader and their status
def list_reserved_documents_by_reader(card_number):
    pass


# 9.Search document copy and check its status
def search_and_check_copy():
    pass


# 14.Print the 10 most popular books of the year
def popular_books_by_year():
    pass


if __name__ == '__main__':
    document_return("何以笙箫默", 67)
