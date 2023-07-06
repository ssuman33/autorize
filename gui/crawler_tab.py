#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from javax.swing import JLabel
from javax.swing import JComboBox
from javax.swing import JTextArea
from javax.swing import JScrollPane
from javax.swing import DefaultListModel
from javax.swing import JList
from javax.swing import JPanel
from javax.swing import JButton

from java.awt import Color
from javax.swing.border import LineBorder

import re

class Crawler():
    def __init__(self, extender):
        self._extender = extender
    
    def draw(self):  
        """ init the match/replace tab  
        """  
        self._extender.CPnl = JPanel()  
        self._extender.CPnl.setLayout(None)  
        self._extender.CPnl.setBounds(0, 0, 1000, 1000)  
  
        # URLs label and input box  
        urls_label = JLabel("Target URL")  
        urls_label.setBounds(10, 100, 100, 25)  
        self._extender.CPnl.add(urls_label)  
  
        urls_input = JTextArea()  
        urls_scroll = JScrollPane(urls_input)  
        urls_scroll.setBounds(120, 100, 200, 100)  
        self._extender.CPnl.add(urls_scroll)  
        
        # Admin login label, username, and password input  
        admin_login_label = JLabel("Admin Login")  
        admin_login_label.setBounds(10, 210, 120, 25)  
        self._extender.CPnl.add(admin_login_label)  
        
        admin_username_label = JLabel("Username:")  
        admin_username_label.setBounds(120, 240, 60, 25)  
        self._extender.CPnl.add(admin_username_label)  
        
        admin_password_label = JLabel("Password:")  
        admin_password_label.setBounds(120, 270, 60, 25)  
        self._extender.CPnl.add(admin_password_label)  
        
        admin_username = JTextArea()  
        admin_username.setBounds(180, 240, 140, 25)  
        admin_username.setBorder(LineBorder(Color.BLACK))  
        self._extender.CPnl.add(admin_username)  
        
        admin_password = JTextArea()  
        admin_password.setBounds(180, 270, 140, 25)  
        admin_password.setBorder(LineBorder(Color.BLACK))  
        self._extender.CPnl.add(admin_password)  
        
        
        # Standard login label, username, and password input  
        std_login_label = JLabel("Standard Login")  
        std_login_label.setBounds(10, 310, 120, 25)  
        self._extender.CPnl.add(std_login_label)  
        
        std_username_label = JLabel("Username:")  
        std_username_label.setBounds(120, 340, 60, 25)  
        self._extender.CPnl.add(std_username_label)  
        
        std_password_label = JLabel("Password:")  
        std_password_label.setBounds(120, 370, 60, 25)  
        self._extender.CPnl.add(std_password_label)  
        
        std_username = JTextArea()  
        std_username.setBounds(180, 340, 140, 25)  
        std_username.setBorder(LineBorder(Color.BLACK))  
        self._extender.CPnl.add(std_username)  
        
        std_password = JTextArea()  
        std_password.setBounds(180, 370, 140, 25)  
        std_password.setBorder(LineBorder(Color.BLACK))  
        self._extender.CPnl.add(std_password)  


        # Admin Cookies label and input box  
        admin_cookies_label = JLabel("Admin Cookies")  
        admin_cookies_label.setBounds(10, 10, 100, 25)  
        self._extender.CPnl.add(admin_cookies_label)  
  
        admin_cookies_input = JTextArea()  
        admin_cookies_scroll = JScrollPane(admin_cookies_input)  
        admin_cookies_scroll.setBounds(120, 10, 200, 25)  
        self._extender.CPnl.add(admin_cookies_scroll)  
  
        # Standard Cookies label and input box  
        standard_cookies_label = JLabel("Standard Cookies")  
        standard_cookies_label.setBounds(10, 40, 100, 25)  
        self._extender.CPnl.add(standard_cookies_label)  
  
        standard_cookies_input = JTextArea()  
        standard_cookies_scroll = JScrollPane(standard_cookies_input)  
        standard_cookies_scroll.setBounds(120, 40, 200, 25)  
        self._extender.CPnl.add(standard_cookies_scroll)    
    def add_array_item(self, event):  
        # Add your logic to handle adding array items here  
        pass  




    def get_crawler_panel(self):  
        return self._extender.CPnl  

