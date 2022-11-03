# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

df1 = pd.read_csv("HR_Employee_Report_Global.csv")
#print(df1)

df2 = pd.read_csv("user_details_report_4.csv")
#print(df2)

#matching_emails = df2[df2["Email"].isin(df1["Email"])]
#print(matching_emails.shape)
#print(matching_emails)

not_matching_emails = df2[~ df2["Email"].isin(df1["Email"])]
print(not_matching_emails.shape)
print(not_matching_emails)
not_matching_emails.to_csv('update.csv')
