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

    def get_crawler_panel(self):  
        return self._extender.CPnl  

