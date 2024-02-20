# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.0.0-0-g0efcecf)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Book Management App", pos = wx.DefaultPosition, size = wx.Size( 1280,800 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel45 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,20 ), wx.TAB_TRAVERSAL )
		self.m_panel45.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		bSizer1.Add( self.m_panel45, 0, wx.EXPAND |wx.ALL, 5 )

		self.btn_add = wx.Button( self, wx.ID_ANY, u"Add New", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.btn_add, 0, wx.ALL, 5 )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,20 ), wx.TAB_TRAVERSAL )
		self.m_panel1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		bSizer1.Add( self.m_panel1, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		comboBox_searchByChoices = [ u"ID", u"ISBN", u"Title", u"Author", u"Quantity" ]
		self.comboBox_searchBy = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBox_searchByChoices, 0 )
		self.comboBox_searchBy.SetSelection( 0 )
		self.comboBox_searchBy.SetToolTip( u"search by" )

		bSizer2.Add( self.comboBox_searchBy, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.txt_searchKey = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_searchKey.SetToolTip( u"key words" )

		bSizer2.Add( self.txt_searchKey, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.btn_search = wx.Button( self, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_search.SetToolTip( u"search" )

		bSizer2.Add( self.btn_search, 0, wx.ALL, 5 )

		self.btn_clear = wx.Button( self, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_clear.SetToolTip( u"clear the filter" )

		bSizer2.Add( self.btn_clear, 0, wx.ALL, 5 )

		self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2.Add( self.m_panel5, 1, wx.EXPAND |wx.ALL, 5 )

		self.btn_edit = wx.Button( self, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_edit.SetToolTip( u"edit the selected item" )

		bSizer2.Add( self.btn_edit, 0, wx.ALL, 5 )

		self.btn_delete = wx.Button( self, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_delete.SetToolTip( u"delete the selected item" )

		bSizer2.Add( self.btn_delete, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )

		self.m_panel11 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,20 ), wx.TAB_TRAVERSAL )
		self.m_panel11.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		bSizer1.Add( self.m_panel11, 0, wx.EXPAND |wx.ALL, 5 )

		self.gridView_books = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.gridView_books.CreateGrid( 0, 5 )
		self.gridView_books.EnableEditing( False )
		self.gridView_books.EnableGridLines( True )
		self.gridView_books.EnableDragGridSize( False )
		self.gridView_books.SetMargins( 0, 0 )

		# Columns
		self.gridView_books.EnableDragColMove( True )
		self.gridView_books.EnableDragColSize( True )
		self.gridView_books.SetColLabelValue( 0, u"ID" )
		self.gridView_books.SetColLabelValue( 1, u"ISBN" )
		self.gridView_books.SetColLabelValue( 2, u"Title" )
		self.gridView_books.SetColLabelValue( 3, u"Author" )
		self.gridView_books.SetColLabelValue( 4, u"Quantity" )
		self.gridView_books.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.gridView_books.AutoSizeRows()
		self.gridView_books.EnableDragRowSize( False )
		self.gridView_books.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.gridView_books.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer1.Add( self.gridView_books, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_add.Bind( wx.EVT_BUTTON, self.showAddDiag )
		self.btn_search.Bind( wx.EVT_BUTTON, self.search )
		self.btn_clear.Bind( wx.EVT_BUTTON, self.clear )
		self.btn_edit.Bind( wx.EVT_BUTTON, self.showEditDiag )
		self.btn_delete.Bind( wx.EVT_BUTTON, self.delete )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def showAddDiag( self, event ):
		event.Skip()

	def search( self, event ):
		event.Skip()

	def clear( self, event ):
		event.Skip()

	def showEditDiag( self, event ):
		event.Skip()

	def delete( self, event ):
		print("del main")
		event.Skip()


###########################################################################
## Class AddBook_Frame
###########################################################################

class AddBook_Frame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 900,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText37 = wx.StaticText( self, wx.ID_ANY, u"   Add New Book", wx.DefaultPosition, wx.Size( -1,60 ), 0 )
		self.m_staticText37.Wrap( -1 )

		self.m_staticText37.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Segoe UI Variable Display" ) )
		self.m_staticText37.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.m_staticText37.SetBackgroundColour( wx.Colour( 0, 128, 192 ) )

		bSizer3.Add( self.m_staticText37, 0, wx.ALL|wx.EXPAND, 0 )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"ID", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText5.Wrap( -1 )

		bSizer5.Add( self.m_staticText5, 0, wx.ALL, 5 )

		self.txt_id = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.txt_id, 0, wx.ALL, 5 )

		self.m_panel8 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5.Add( self.m_panel8, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"ISBN", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText6.Wrap( -1 )

		bSizer5.Add( self.m_staticText6, 0, wx.ALL, 5 )

		self.txt_isbn = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.txt_isbn, 0, wx.ALL, 5 )


		bSizer3.Add( bSizer5, 0, wx.ALL|wx.EXPAND, 20 )

		bSizer51 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, u"Title", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText51.Wrap( -1 )

		bSizer51.Add( self.m_staticText51, 0, wx.ALL, 5 )

		self.txt_title = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer51.Add( self.txt_title, 0, wx.ALL, 5 )

		self.m_panel81 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer51.Add( self.m_panel81, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText61 = wx.StaticText( self, wx.ID_ANY, u"Author", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText61.Wrap( -1 )

		bSizer51.Add( self.m_staticText61, 0, wx.ALL, 5 )

		self.txt_author = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer51.Add( self.txt_author, 0, wx.ALL, 5 )


		bSizer3.Add( bSizer51, 0, wx.ALL|wx.EXPAND, 20 )

		bSizer52 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText52 = wx.StaticText( self, wx.ID_ANY, u"Quantity", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText52.Wrap( -1 )

		bSizer52.Add( self.m_staticText52, 0, wx.ALL, 5 )

		self.txt_quantity = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer52.Add( self.txt_quantity, 0, wx.ALL, 5 )

		self.m_panel82 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer52.Add( self.m_panel82, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer3.Add( bSizer52, 0, wx.ALL|wx.EXPAND, 20 )

		self.m_panel14 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3.Add( self.m_panel14, 1, wx.EXPAND |wx.ALL, 5 )

		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel15 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer14.Add( self.m_panel15, 1, wx.EXPAND |wx.ALL, 5 )

		self.btn_apply = wx.Button( self, wx.ID_ANY, u"Apply", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.btn_apply, 0, wx.ALL|wx.RIGHT, 20 )

		self.btn_cancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.btn_cancel, 0, wx.ALL|wx.LEFT, 20 )


		bSizer3.Add( bSizer14, 0, wx.EXPAND|wx.RIGHT, 20 )

		self.m_panel16 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3.Add( self.m_panel16, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_apply.Bind( wx.EVT_BUTTON, self.add_apply )
		self.btn_cancel.Bind( wx.EVT_BUTTON, self.add_cancel )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def add_apply( self, event ):
		event.Skip()

	def add_cancel( self, event ):
		event.Skip()


###########################################################################
## Class EditBook_Frame
###########################################################################

class EditBook_Frame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Edit A Book", pos = wx.DefaultPosition, size = wx.Size( 900,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText38 = wx.StaticText( self, wx.ID_ANY, u"   Edit Book", wx.DefaultPosition, wx.Size( -1,60 ), 0 )
		self.m_staticText38.Wrap( -1 )

		self.m_staticText38.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Segoe UI Variable Display" ) )
		self.m_staticText38.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.m_staticText38.SetBackgroundColour( wx.Colour( 255, 128, 128 ) )

		bSizer3.Add( self.m_staticText38, 0, wx.EXPAND, 5 )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"ID", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText5.Wrap( -1 )

		bSizer5.Add( self.m_staticText5, 0, wx.ALL, 5 )

		self.txt_id = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_id.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.txt_id.Enable( False )

		bSizer5.Add( self.txt_id, 0, wx.ALL, 5 )

		self.m_panel8 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5.Add( self.m_panel8, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"ISBN", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText6.Wrap( -1 )

		bSizer5.Add( self.m_staticText6, 0, wx.ALL, 5 )

		self.txt_isbn = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.txt_isbn, 0, wx.ALL, 5 )


		bSizer3.Add( bSizer5, 0, wx.ALL|wx.EXPAND, 20 )

		bSizer51 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, u"Title", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText51.Wrap( -1 )

		bSizer51.Add( self.m_staticText51, 0, wx.ALL, 5 )

		self.txt_title = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer51.Add( self.txt_title, 0, wx.ALL, 5 )

		self.m_panel81 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer51.Add( self.m_panel81, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText61 = wx.StaticText( self, wx.ID_ANY, u"Author", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText61.Wrap( -1 )

		bSizer51.Add( self.m_staticText61, 0, wx.ALL, 5 )

		self.txt_author = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer51.Add( self.txt_author, 0, wx.ALL, 5 )


		bSizer3.Add( bSizer51, 0, wx.ALL|wx.EXPAND, 20 )

		bSizer52 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText52 = wx.StaticText( self, wx.ID_ANY, u"Quantity", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText52.Wrap( -1 )

		bSizer52.Add( self.m_staticText52, 0, wx.ALL, 5 )

		self.txt_quantity = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer52.Add( self.txt_quantity, 0, wx.ALL, 5 )

		self.m_panel82 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer52.Add( self.m_panel82, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer3.Add( bSizer52, 0, wx.ALL|wx.EXPAND, 20 )

		self.m_panel14 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3.Add( self.m_panel14, 1, wx.EXPAND |wx.ALL, 5 )

		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel15 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer14.Add( self.m_panel15, 1, wx.EXPAND |wx.ALL, 5 )

		self.btn_apply = wx.Button( self, wx.ID_ANY, u"Apply", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.btn_apply, 0, wx.ALL|wx.RIGHT, 20 )

		self.btn_cancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.btn_cancel, 0, wx.ALL|wx.LEFT, 20 )


		bSizer3.Add( bSizer14, 0, wx.EXPAND|wx.RIGHT, 20 )

		self.m_panel16 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3.Add( self.m_panel16, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_apply.Bind( wx.EVT_BUTTON, self.edit_apply )
		self.btn_cancel.Bind( wx.EVT_BUTTON, self.edit_cancel )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def edit_apply( self, event ):
		event.Skip()

	def edit_cancel( self, event ):
		event.Skip()


