import wx
import mainUI_frame as mf
import mysql.connector
import wx.grid as gridlib


###########
# Add Book
###########
class AddNewBook(mf.AddBook_Frame):
    def __init__(self, parent):
        mf.AddBook_Frame.__init__(self, parent)
        self.main = parent
        self.Show()

    def add_apply(self, event):
        conn = mysql.connector.connect(**MainUI.db_params)
        if conn.is_connected():
            cursor = conn.cursor()
            sqlQuery = "INSERT INTO books (`id`, `isbn`, `title`, `author`, `quantity`) VALUES(%s, %s,%s, %s, %s)"
            cursor.execute(
                sqlQuery,
                (
                    self.txt_id.Value,
                    self.txt_isbn.Value,
                    self.txt_title.Value,
                    self.txt_author.Value,
                    self.txt_quantity.Value,
                ),
            )
            conn.commit()
            cursor.close()
            self.main.fillGrid("SELECT * FROM books")
            self.Close()
        conn.close()
        event.Skip()

    def add_cancel(self, event):
        self.Close()
        return super().add_cancel(event)


###########
# Edit Book
###########
class EditBook(mf.EditBook_Frame):
    def __init__(
        self, parent, book_id, book_isbn, book_title, book_author, book_quantity
    ):
        mf.EditBook_Frame.__init__(self, parent)
        self.main = parent
        self.id = book_id
        self.txt_id.SetLabelText(book_id)
        self.txt_isbn.SetLabelText(book_isbn)
        self.txt_title.SetLabelText(book_title)
        self.txt_author.SetLabelText(book_author)
        self.txt_quantity.SetLabelText(book_quantity)
        
        self.Show()

    def edit_apply(self, event):
        conn = mysql.connector.connect(**MainUI.db_params)
        if conn.is_connected():
            cursor = conn.cursor()
            sqlQuery = (
                "UPDATE books SET isbn=%s,title=%s,author=%s,quantity=%s WHERE id=%s"
            )
            cursor.execute(
                sqlQuery,
                (
                    self.txt_isbn.Value,
                    self.txt_title.Value,
                    self.txt_author.Value,
                    self.txt_quantity.Value,
                    self.txt_id.Value,
                ),
            )
            conn.commit()
            cursor.close()
            self.main.fillGrid("SELECT * FROM books")
            self.Close()
        conn.close()
        return super().edit_apply(event)

    def edit_cancel(self, event):
        self.Close()
        return super().edit_cancel(event)

    # def test(self):
    #     self.__tt="123"
    #     print("main test")


###########
# Main UI
###########
class MainUI(mf.MainFrame):
    db_params = {  # class attribute, similar to static field
        "host": "localhost",
        "database": "edmond_book_management",
        "user": "root",
        "password": "",
    }

    def __init__(self, parent):
        mf.MainFrame.__init__(self, parent)
        # mf_instance = mf.MainFrame(None)
        # self.txt_feed.SetLabel("cbd")
        # print(self.txt_feed.LabelText)
        self.gridView_books.SetColSize(1, 192)
        self.gridView_books.SetColSize(2, 384)
        self.gridView_books.SetColSize(3, 384)
        self.gridView_books.HideRowLabels()
        self.fillGrid("SELECT * FROM books")

    def fillGrid(self, sqlQuery):
        self.gridView_books.ClearGrid()
        if self.gridView_books.GetNumberRows() > 0:
            self.gridView_books.DeleteRows(
                pos=0, numRows=self.gridView_books.GetNumberRows()
            )
        conn = mysql.connector.connect(**self.db_params)
        if conn.is_connected():
            # print("connected")
            cursor = conn.cursor()
            cursor.execute(sqlQuery)
            rows = cursor.fetchall()
            grid = self.gridView_books
            grid.SetSelectionMode(gridlib.Grid.SelectRows)
            for row_num, row_data in enumerate(rows):
                self.gridView_books.AppendRows(1)
                for col_num, col_data in enumerate(row_data):
                    grid.SetCellValue(row_num, col_num, str(col_data))
            cursor.close()
        conn.close()

    def showAddDiag(self, event):
        add_book_frame = AddNewBook(self)
        add_book_frame.Show()
        event.Skip()

    def search(self, event):
        method = self.comboBox_searchBy.GetStringSelection()
        print(method)
        keyWord = self.txt_searchKey.GetValue()
        print(keyWord)
        sqlQuery = "SELECT * FROM books WHERE " + method + " LIKE '%" + keyWord + "%'"
        self.fillGrid(sqlQuery)
        event.Skip()

    def clear(self, event):
        self.comboBox_searchBy.Clear
        self.txt_searchKey.Clear
        self.fillGrid("SELECT * FROM books")
        event.Skip()

    def showEditDiag(self, event):
        if self.gridView_books.IsSelection():
            selected_row = gridlib.Grid.GetSelectedRows(self.gridView_books)[0]
            id = self.gridView_books.GetCellValue(selected_row, 0)
            isbn = self.gridView_books.GetCellValue(selected_row, 1)
            title = self.gridView_books.GetCellValue(selected_row, 2)
            author = self.gridView_books.GetCellValue(selected_row, 3)
            quantity = self.gridView_books.GetCellValue(selected_row, 4)
            edit_book_frame = EditBook(self, id, isbn, title, author, quantity)
            # edit_book_frame.test()
            # print(edit_book_frame.tt)
            edit_book_frame.Show()
        event.Skip()

    def delete(self, event):
        selected_row = gridlib.Grid.GetSelectedRows(self.gridView_books)[0]
        id = self.gridView_books.GetCellValue(selected_row, 0)
        title = self.gridView_books.GetCellValue(selected_row, 2)
        if bool(id):
            result = wx.MessageBox(
                f"Are you sure to DELETE the book: {title}？",
                "Delete Confirmation",
                wx.OK | wx.CANCEL | wx.ICON_QUESTION,
            )
            if result == wx.OK:
                sqlQuery = "DELETE FROM books WHERE id = " + id
                conn = mysql.connector.connect(**self.db_params)
                if conn.is_connected():
                    print("connected")
                    cursor = conn.cursor()
                    cursor.execute(sqlQuery)
                    conn.commit()
                    self.fillGrid("SELECT * FROM books")
                    cursor.close()
                conn.close()
        event.Skip()


app = wx.App(False)
mff = MainUI(None)
mff.Show(True)
app.MainLoop()


# class MainUI(wx.App):
#     def OnInit(self):
#         # Load all controls:
#         self.frame=mf.MainFrame(None)
#         self.frame.Show()
#         self.SetTopWindow(self.frame)
#         mf_instance = mf.MainFrame(None)
#         mf_instance.txt_feed.SetLabel("cbd")
#         print(mf_instance.txt_feed.LabelText)
#         return True

#     def delete(self, event):
#         print("delete it") #doesn't work

# if __name__ == '__main__':
#     app = MainUI()
#     app.MainLoop()
