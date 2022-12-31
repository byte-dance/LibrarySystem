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



#  11
def print_branch_information():
    sql = 'select name,location from branch'
    data = dbhelper_singleton.query_data(sql)
    print('{0:<20}{1:<20}'.format('name','location'))
    for d in data:
        print("%-*s %-20s" % (20 + len(d[0]) - len(d[0].encode("gbk")), d[0], d[1]))

#  7
def print_documents_of_publisher(publisher_id):
    sql = f'''select document_id,title from document where publisher_id= '{publisher_id}' '''
    data = dbhelper_singleton.query_data(sql)
    print('{0:<21}{1:<20}'.format('document_id', 'title'))
    for d in data:
        print("%-*s %-20s" % (20 + len(str(d[0])) - len(str(d[0]).encode("gbk")), d[0], d[1]))

#  15
def find_the_average_fine_paid_per_reader():
    sql = 'select reader_id,avg(fine) from borrow where r_datetime is not null group by reader_id'
    data = dbhelper_singleton.query_data(sql)
    print('{0:<20}{1:<20}'.format('reader_id', 'average fine'))
    for d in data:
        print(f'''读者reader_id为{d[0]},平均罚款为{d[1]}''')

#  5
def compute_fine_for_a_document_copy_borrowed_by_a_reader_based_on_the_current_date(reader_id, copy_id, b_datetime):
    should_r_datetime = b_datetime + datetime.timedelta(days=20)
    now = datetime.datetime.now()
    if now <= should_r_datetime:
        return 0
    days = (now - should_r_datetime).days
    if should_r_datetime + datetime.timedelta(days=days) < now:
        days += 1
    print(f'欠款{days}天，应还{days * 20}cents')

#  13
def print_top_10_most_borrowed_books_in_a_library(library_id):
    sql =f'''select t1.title, t1.document_id, t2.t \
    from \
    (select title, document_id from book WHERE document_id in (SELECT DISTINCT(document_id) \
    from branch_doc where \
    branch_id in (SELECT branch_id FROM branch WHERE lib_id='{library_id}'))) as t1 \
    left JOIN(select document_id, count(*) as t \
    from borrow LEFT JOIN copy on borrow.copy_id = copy.copy_id GROUP BY document_id ORDER BY t DESC) as t2 \
    on t1.document_id = t2.document_id \
    where t2.t is NOT NULL LIMIT 10 '''
    data=dbhelper_singleton.query_data(sql)
    for i in range(1,len(data)+1):
        print(f'''借书次数排名第{i}的书名为{data[i-1][0]},document_id为{data[i-1][1]},一共借出{data[i-1][2]}本''')



if __name__ == '__main__':
    document_return("何以笙箫默", 67)
