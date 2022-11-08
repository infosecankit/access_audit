# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

#HR Sheet
df1 = pd.read_csv("HR.csv")
#print(df1)

#IT sheet
df2 = pd.read_csv("IT.csv")
#print(df2)

#see if the data is not found in the HR/legal sheet but is present in the IT sheet then spit it out which might mean they do not have a account with the HR or legal but have an Active onelogin account
not_matching_emails = df2[~ df2["Email"].isin(df1["Email"])]
print(not_matching_emails.shape)
print(not_matching_emails)
not_matching_emails.to_csv('update.csv')
