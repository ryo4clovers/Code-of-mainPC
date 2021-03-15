# -*- coding: utf-8 -*-
import pandas as pd
import wx
import os


# テキスト→CSV変換関数
# def text_to_csv(datas):
#    file = pd.read_csv(datas, encoding="utf-8", sep="\t")
#    file.to_csv('D:/iriwa/デスクトップ/Code/Project_Python/test.csv')

# 視覚パラメータ解析
class Eye_analyze():
    def __init__(self):
        super().__init__()


# 脳波解析
class EEG_analyze():
    def __init__(self):
        super().__init__()


# GUI関連クラス
class GUI (wx.Frame):
    # レイアウト
    def __init__(self):
        wx.Frame.__init__(self, None, title=u"研究用解析ソフト", pos=wx.DefaultPosition, size=wx.Size(
            400, 200), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        Sizer0 = wx.FlexGridSizer(3, 3, 0, 0)
        Sizer0.AddGrowableCol(1)
        Sizer0.SetFlexibleDirection(wx.BOTH)
        Sizer0.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_ALL)

        self.Label1 = wx.StaticText(self, wx.ID_ANY, u"input file",
                                    wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL)
        self.Label1.Wrap(-1)

        Sizer0.Add(self.Label1, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.Text1 = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        Sizer0.Add(self.Text1, 0, wx.ALIGN_CENTER | wx.ALL | wx.EXPAND, 5)

        self.Button1 = wx.Button(
            self, wx.ID_ANY, u"browse", wx.DefaultPosition, wx.DefaultSize, 0)
        Sizer0.Add(self.Button1, 0, wx.ALIGN_RIGHT |
                   wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.Label2 = wx.StaticText(self, wx.ID_ANY, u"output folder",
                                    wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL)
        self.Label2.Wrap(-1)

        Sizer0.Add(self.Label2, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.Text2 = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        Sizer0.Add(self.Text2, 0, wx.ALIGN_CENTER | wx.ALL | wx.EXPAND, 5)

        self.Button2 = wx.Button(
            self, wx.ID_ANY, u"browse", wx.DefaultPosition, wx.DefaultSize, 0)
        Sizer0.Add(self.Button2, 0, wx.ALIGN_CENTER_VERTICAL |
                   wx.ALIGN_RIGHT | wx.ALL, 5)

        self.RButton1 = wx.RadioButton(
            self, wx.ID_ANY, u"Eye parameters", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP)
        Sizer0.Add(self.RButton1, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.RButton2 = wx.RadioButton(
            self, wx.ID_ANY, u"EEG parameter", wx.DefaultPosition, wx.DefaultSize, 0)
        Sizer0.Add(self.RButton2, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.Button3 = wx.Button(
            self, wx.ID_ANY, u"run", wx.DefaultPosition, wx.DefaultSize, 0)
        Sizer0.Add(self.Button3, 0, wx.ALIGN_CENTER_VERTICAL |
                   wx.ALIGN_RIGHT | wx.ALL, 5)

        self.SetSizer(Sizer0)
        self.Layout()
        self.Centre(wx.BOTH)

        self.CreateStatusBar()  # フッター
        self.SetStatusText("©2020 ryo4clovers")
        self.Show(True)

        # イベント紐づけ
        self.Button1.Bind(wx.EVT_BUTTON, self.Button1_Click)
        self.Button2.Bind(wx.EVT_BUTTON, self.Button2_Click)
#        self.RButton1.Bind(wx.EVT_RADIOBUTTON, self.RButton1_select)
#        self.RButton2.Bind(wx.EVT_RADIOBUTTON, self.RButton2_select)
        self.Button3.Bind(wx.EVT_BUTTON, self.Button3_Click)

    def __del__(self):
        pass

    # イベント
    def Button1_Click(self, event):
        File_dialog = wx.FileDialog(self, u"txtファイルを選択してください",
                                    "", "", "*.txt*", wx.FD_MULTIPLE)
        File_dialog.ShowModal()
        File_Path = File_dialog.GetPaths()
        for file in File_Path:
            self.Text1.SetValue(file)
        return True

    def Button2_Click(self, event):
        Folder_dialog = wx.DirDialog(self, u"出力先を指定してください")
        Folder_dialog.ShowModal()
        Folder_Path = Folder_dialog.GetPath()
        self.Text2.SetValue(Folder_Path)

#    def RButton1_select(self, event):
#        event.Skip()

#    def RButton2_select(self, event):
#        event.Skip()

    def Button3_Click(self, event):
        event.Skip()


# メイン関数
if __name__ == '__main__':
    app = wx.App()
    GUI()
    app.MainLoop()
#    filename = "D:/iriwa/デスクトップ/Code/Project_Python/test.txt"  # フルパス推奨
#    text_to_csv(filename)
