# Created on Mon Dec  3 12:40:13 2018
# author: elvis


import mysql.connector


class task():
    
    cnx = mysql.connector.connect(user='root', password='El.db.mysql12', host='localhost', database='db_todo')
    cursor = cnx.cursor(buffered=True)
    
    def __init__(self, start_date, start_time, end_date, end_time, task_description, group):
        self.start_date = start_date
        self.start_time = start_time
        self.end_date = end_date
        self.end_time = end_time
        self.task_description = task_description
        self.group = group
        
        try:
            self.sql_insert_query = "INSERT INTO `task` (`start_date`, `start_time`, `end_date`, `end_time`, `task_description`, `group`) VALUES (%s, %s, %s, %s, %s, %s)"
            self.cursor.execute(self.sql_insert_query, (self.start_date, self.start_time, self.end_date, self.end_time, self.task_description, self.group))
            self.cnx.commit()
            self.id = self.cursor.lastrowid
            print("\nNew task successfully inserted into the task table")
            print("\nThe id of the newly added record is {}".format(self.id))
        except mysql.connector.Error as error_msg:
            self.cnx.rollback() #rollback if any error occured
            print("\nFailed to insert new task into the task table {}".format(error_msg))
        
    @classmethod
    def open_conn(cls):
        try:
            cls.cnx
            print("Success!\nConnected to database")
        except mysql.connector.Error as error_msg:
            print("An error occured while connecting to the database", error_msg)
            
    @classmethod
    def close_conn(cls):
        cls.cursor.close()
        cls.cnx.close()
        print("\nThe connection to the database has been closed.")
        
    # def add_task(self):
    #     try:
    #         self.sql_insert_query = "INSERT INTO `task` (`start`, `end`, `task_description`) VALUES (%s, %s, %s)"
    #         self.cursor.execute(self.sql_insert_query, (self.start, self.end, self.task_description))
    #         self.cnx.commit()
    #         self.id = self.cursor.lastrowid
    #         print("\nNew task successfully inserted into the task table")
    #     except mysql.connector.Error as error_msg:
    #         self.cnx.rollback() #rollback if any error occured
    #         print("\nFailed to insert new task into the task table {}".format(error_msg))
            
    def delete_task(self):
        try:
            self.sql_delete_query = "DELETE FROM `task` WHERE ID = %s"
            self.cursor.execute(self.sql_delete_query, (self.id,))
            self.cnx.commit()
            print("\nThe record with id {} has been successfully deleted.".format(self.id))
        except mysql.connector.Error as error_msg:
            self.cnx.rollback()
            print("\nSorry\nFailed to deleted task with id {}".format(self.id), error_msg)

    def show_task(self):
        try:
           self.sql_select_query = "SELECT * FROM `task`"
           self.cursor.execute(self.sql_select_query)
           self.rows = self.cursor.fetchall()
           
           self.cnx.commit()
        except mysql.connector.Error as error_msg:
           self.cnx.rollback()
           print("\nSorry, an error occured: ", error_msg)

    def update_task(self):
        try:
            self.sql_update_query = "UPDATE task SET task_description = 'Write Python Code' WHERE id = %s"
            self.cursor.execute(self.sql_update_query, (self.id,))
            self.cnx.commit()
            print("\nUpdate successful at record with id {}".format(self.id))
        except mysql.connector.Error as error_msg:
            self.cnx.rollback()
            print("\nFailed to update record with id {}: ".format(self.id), error_msg)
            
            
# task_2 = task('2018-12-04', '2018-12-05', 'Go to campus')
# task_2.add_task()
# task_2.delete_task()
# task_2.show_task()
# task_2.update_task()
# task_2.close_conn()
