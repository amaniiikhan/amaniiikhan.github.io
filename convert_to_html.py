#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 22:20:35 2023

@author: amani
"""

import pdfkit

pdf_file = open('catalog.pdf', 'rb')

html_file = pdfkit.from_pdf(pdf_file, 'catalog.html')

pdf_file.close()

