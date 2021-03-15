# -*- coding: utf-8 -*-
"""
    jpg_to_pdf.py
        選択したフォルダに入ってるJPGファイルをまとめてPDFに変換する
"""
# ------
# Import
# ------
import wx.xrc
import wx
import os
import img2pdf
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

# ------
# Function
# ------


# convert function
def Func_convert(name, path):
    # desktop_path = os.getenv("HOMEDRIVE") + os.getenv("HOMEPATH") + "\\Desktop"
    desktop_path = "D:\\iriwa\\デスクトップ\\pdf\\"
    pdf_FileName = desktop_path + name+".pdf"
    jpg_Folder = path + "\\"
    extension1 = ".jpg"  # 拡張子がPNGのものを対象
    extension2 = ".png"

    # 画像フォルダの中にあるPNGファイルを取得し配列に追加、バイナリ形式でファイルに書き込む
    data = [Image.open(jpg_Folder+j).convert('RGB') for j in os.listdir(jpg_Folder)
            if j.endswith(extension1) or j.endswith(extension2)]
    # data[0].save(pdf_FileName, save_all=True, append_images=data[1:])
    hsize = 842
    num = len(data)
    resize_data = [data[i].resize(
        (int(data[i].width * hsize / data[i].height), hsize)) for i in range(num)]
    resize_data[0].save(pdf_FileName, save_all=True, dpi=(72, 72),
                        append_images=resize_data[1:])

    # re_data = []
    # for i in range(num):
    #    wsize = int(data[i].width * hsize / data[i].height)
    #    re_data[i] = data[i].resize((wsize, hsize))
    #    print(wsize)
    #    print(re_data[i])
    # rate = hsize / data[10].height
    # wsize = data[10].width * rate
    # data.resize((wsize, int(hsize)))
    # f.write(img2pdf.convert(resize_data))


# ------
# Class
# ------


# GUI class
class GUI (wx.Frame):
    def __init__(self, parent, ID, title):
        wx.Frame.__init__(self, parent, title=title,
                          pos=(0, 0), size=wx.Size(500, 300))
        self.__widget(parent, ID)
        self.__layout(parent, ID)
        self.__event(parent, ID)
        """
        self frame
          ├main panel
          │  ├path panel
          │  │  ├path static text
          │  │  └path text ctrl
          │  ├name panel
          │  │  ├name static text
          │  │  └name text ctrl
          │  └list panel
          │     └list list box
          ├button panel
          │  ├browse button
          │  ├add button
          │  ├delete button
          │  ├space panel
          │  └convert button
          └footer status bar
        """

    # Widget function
    def __widget(self, parent, ID):
        # "main"     Panel
        self.P_main = wx.Panel(self, ID)
        # "path"     Panel
        self.P_path = wx.Panel(self.P_main, ID)
        # "path"     StaticText
        self.ST_path = wx.StaticText(self.P_path, ID, label="出力ファイル元")
        # "path"     TextCtrl
        self.TC_path = wx.TextCtrl(self.P_path, ID)
        self.TC_path.Disable()
        # "name"     Path
        self.P_name = wx.Panel(self.P_main, ID)
        # "name"     StaticText
        self.ST_name = wx.StaticText(self.P_name, ID, label="出力ファイル名")
        # "name"     TextCtrl
        self.TC_name = wx.TextCtrl(self.P_name, ID)
        # "list"     Panel
        self.P_list = wx.Panel(self.P_main, ID)
        # "list"     ListBox
        self.LB_list = wx.ListBox(self.P_list, ID, style=wx.LB_SINGLE)
        # "button"     Panel
        self.P_button = wx.Panel(self, ID)
        # "browse"     Button
        self.B_browse = wx.Button(self.P_button, ID, label="参照")
        # "delete"     Button
        self.B_delete = wx.Button(self.P_button, ID, label="削除")
        # "add"     Button
        self.B_add = wx.Button(self.P_button, ID, label="追加")
        # "space"     Panel
        self.P_space = wx.Panel(self.P_button, ID)
        # "convert"    Button
        self.B_convert = wx.Button(self.P_button, ID, label="変換")
        # Footer
        self.SB_status = self.CreateStatusBar(1, wx.STB_SIZEGRIP, ID)

    # Layout function
    def __layout(self, parent, ID):
        # ------ Sizer ------
        # frame     Sizer
        S_frame = wx.FlexGridSizer(1, 2, 0, 0)
        S_frame.AddGrowableCol(0)
        S_frame.AddGrowableRow(0)
        S_frame.SetFlexibleDirection(wx.BOTH)
        S_frame.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        # main         Sizer
        S_main = wx.FlexGridSizer(3, 1, 0, 0)
        S_main.AddGrowableCol(0)
        S_main.AddGrowableRow(2)
        S_main.SetFlexibleDirection(wx.BOTH)
        S_main.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        # path         Sizer
        S_path = wx.FlexGridSizer(1, 2, 0, 0)
        S_path.AddGrowableCol(1)
        S_path.SetFlexibleDirection(wx.BOTH)
        S_path.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        # name        Sizer
        S_name = wx.FlexGridSizer(1, 2, 0, 0)
        S_name.AddGrowableCol(1)
        S_name.SetFlexibleDirection(wx.BOTH)
        S_name.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        # list        Sizer
        S_list = wx.BoxSizer(wx.VERTICAL)
        # button    Sizer
        S_button = wx.BoxSizer(wx.VERTICAL)

        # ------ Adding ------
        # path add
        S_path.Add(self.ST_path, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)
        S_path.Add(self.TC_path, 0, wx.ALL | wx.EXPAND, 5)
        # main add
        S_main.Add(self.P_path,  1, wx.ALL | wx.EXPAND,  5)
        S_main.Add(self.P_name,  1, wx.ALL | wx.EXPAND,  5)
        S_main.Add(self.P_list,  1, wx.ALL | wx.EXPAND,  5)
        # name add
        S_name.Add(self.ST_name, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)
        S_name.Add(self.TC_name, 0, wx.ALL | wx.EXPAND, 5)
        # list add
        S_list.Add(self.LB_list, 1, wx.ALL | wx.EXPAND, 5)
        # frame add
        S_frame.Add(self.P_main,   1, wx.EXPAND | wx.ALL, 5)
        S_frame.Add(self.P_button, 1, wx.EXPAND | wx.ALL, 5)
        # button add
        S_button.Add(self.B_browse,  0, wx.ALL, 5)
        S_button.Add(self.B_add,     0, wx.ALL, 5)
        S_button.Add(self.B_delete,  0, wx.ALL, 5)
        S_button.Add(self.P_space,   1, wx.ALL, 5)
        S_button.Add(self.B_convert, 0, wx.ALL, 5)

        # ------ Set Sizer ------
        # path set sizer
        self.P_path.SetSizer(S_path)
        self.P_path.Layout()
        S_path.Fit(self.P_path)
        # name set sizer
        self.P_name.SetSizer(S_name)
        self.P_name.Layout()
        S_name.Fit(self.P_name)
        # list set sizer
        self.P_list.SetSizer(S_list)
        self.P_list.Layout()
        S_list.Fit(self.P_list)
        # main set sizer
        self.P_main.SetSizer(S_main)
        self.P_main.Layout()
        S_main.Fit(self.P_main)
        # button set sizer
        self.P_button.SetSizer(S_button)
        self.P_button.Layout()
        S_button.Fit(self.P_button)
        # frame set sizer
        self.SetSizer(S_frame)
        self.Layout()

    # event function
    def __event(self, parent, ID):
        # ------ Connect Events ------
        self.B_browse.Bind(wx.EVT_BUTTON,  self.OnBrowse)
        self.B_add.Bind(wx.EVT_BUTTON,     self.OnAdd)
        self.B_delete.Bind(wx.EVT_BUTTON,  self.OnDelete)
        self.B_convert.Bind(wx.EVT_BUTTON, self.OnConvert)

    # browse Button event
    def OnBrowse(self, event):
        Folder_dialog = wx.DirDialog(self, u"出力先を指定してください",
                                     u"D:\\iriwa\\デスクトップ\\book")
        Folder_dialog.ShowModal()
        Folder_path = Folder_dialog.GetPath()
        Folder_name = Folder_path[Folder_path.rfind("\\")+1:]
        self.TC_path.SetValue(Folder_path)
        self.TC_name.SetValue("【】"+Folder_name)

    # add Button event
    def OnAdd(self, event):
        if self.TC_name.GetValue():
            self.LB_list.Append(self.TC_name.GetValue(),
                                self.TC_path.GetValue())
            self.TC_path.SetValue("")
            self.TC_name.SetValue("")
        else:
            event.Skip()

    # delete button event
    def OnDelete(self, event):
        self.LB_list.Delete(self.LB_list.GetSelection())

    # convert button event
    def OnConvert(self, event):
        n = len(self.LB_list.GetItems())
        for i in range(n):
            name = self.LB_list.GetItems()
            path = self.LB_list.GetClientData(i)
            self.SB_status.SetStatusText("converting:"+str(i)+"/"+str(n))
            Func_convert(name[i], path)
        self.SB_status.SetStatusText("")
        self.LB_list.Clear()


# Application class
class Application(wx.App):
    # Class initialization
    def OnInit(self):
        # Frame object creation
        frame = GUI(None, wx.ID_ANY, "PDF変換")
        # Set to main frame
        self.SetTopWindow(frame)
        # Frame display
        frame.Show(True)
        return True


# ------
# Main
# ------
if __name__ == "__main__":
    # Application object creation
    app = Application()
    # Main loop
    app.MainLoop()
