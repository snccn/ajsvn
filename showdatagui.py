# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import time,os,os.path

###########################################################################
## Class MyFrame1
###########################################################################
rootdir='data/'
class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent,title ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = title, pos = wx.DefaultPosition, size = wx.Size( 589,443 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetMaxSize((589,443))
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
		
		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.execute = wx.Button( self.m_panel1, wx.ID_ANY, u"执行", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.execute, wx.GBPosition( 1, 8 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.filename = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.filename.SetMinSize( wx.Size( 300,-1 ) )
		
		gbSizer1.Add( self.filename, wx.GBPosition( 1, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.output = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,60 ), wx.TE_MULTILINE )
		self.output.SetMinSize( wx.Size( 560,320 ) )
		
		gbSizer1.Add( self.output, wx.GBPosition( 2, 0 ), wx.GBSpan( 200, 200 ), wx.ALL, 6 )
		
		self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"json 路径", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		gbSizer1.Add( self.m_staticText1, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		
		self.m_panel1.SetSizer( gbSizer1 )
		self.m_panel1.Layout()
		gbSizer1.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 1 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		# Connect Events
		self.execute.Bind( wx.EVT_BUTTON, self.openandhandlejson )
		self.filenamepool=[]
		for parent ,dirname,filenames in os.walk(rootdir):
			for filename in filenames:
				self.filenamepool.append(parent+'\\'+filename+'\n')		
	def __del__( self ):
		pass
	# Virtual event handlers, overide them in your derived class
	def openandhandlejson( self, event ):
		self.output.Clear()
		print "init complete and hello world"
		fn=self.filename.GetValue()
		print fn
		for i in self.filenamepool:
			if fn==i[6:-1]:
				# print fn
				fileobj=open(i[0:-1],'r')
				print "open file complete!"
				self.output.AppendText('________')

class mainApp(wx.App):
	def OnInit(self):
		frameobj=MyFrame1(None,u'project ZJSVN json数据查看器(单例)')
		frameobj.Show(True)
		return True
if __name__=='__main__':
	app=mainApp(0)
	app.MainLoop()
	
	
	