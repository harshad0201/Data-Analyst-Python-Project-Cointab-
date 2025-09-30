import pandas as pd
import math
import tkinter as tk
from tkinter import messagebox

# importing files
courier_invoice = pd.read_excel("D:\Edu\cointab\Cointab-DataAnalyst-Assignment-main\Courier Company - Invoice.xlsx")
x_order_rpt = pd.read_excel("D:\Edu\cointab\Cointab-DataAnalyst-Assignment-main\Company X - Order Report.xlsx")
x_pin_zone = pd.read_excel("D:\Edu\cointab\Cointab-DataAnalyst-Assignment-main\Company X - Pincode Zones.xlsx")
x_sku = pd.read_excel("D:\Edu\cointab\Cointab-DataAnalyst-Assignment-main\Company X - SKU Master.xlsx")
courier_charges = pd.read_excel("D:\Edu\cointab\Cointab-DataAnalyst-Assignment-main\Courier Company - Rates.xlsx")


a = pd.merge(x_order_rpt,x_sku,on ="SKU")
a["Total Weight as per X"] = ((a["Order Qty"]*a["Weight (g)"])/1000)

b = pd.pivot_table(a,index = "ExternOrderNo",aggfunc = "sum")
b= b.reset_index()
b.drop(["Weight (g)","Order Qty"],axis =1, inplace = True)
b.columns = ["Order ID","Total Weight as per X (KG)"]

courier_invoice = pd.merge(courier_invoice,b, on="Order ID" )


def calculate_weight_slab(weight):
    return ((math.ceil(weight/0.5))/2)

courier_invoice["Weight_X"] = courier_invoice["Total Weight as per X (KG)"].apply(calculate_weight_slab)

courier_invoice["Weight slab charged by Courier Company (KG)"] = courier_invoice["Charged Weight"].apply(calculate_weight_slab)


courier_invoice.rename(columns = {'Zone':'Delivery Zone charged by Courier Company'}, inplace = True)
courier_invoice = pd.merge(courier_invoice,x_pin_zone,on ="Customer Pincode"	)


def charges(Zone, Type_of_Shipment, Weight_X):

  if Type_of_Shipment == "Forward charges":
    if Zone  == "a":
        if Weight_X / 0.5 == 0.5:
          return 29.5 
        else: 
          a = Weight_X /0.5   
          return (29.5 + (23.6*(a-1)))

    elif Zone  == "b":
        if Weight_X / 0.5 == 0.5:
          return 33.0
        else: 
          a = Weight_X /0.5   
          return (33+ (28.3*(a-1)))

    elif Zone  == "c":
        if Weight_X / 0.5 == 0.5:
          return 40.1
        else: 
          a = Weight_X /0.5   
          return (40.1+ (38.9*(a-1)))

    elif Zone  == "d":
        if Weight_X / 0.5 == 0.5:
          return 45.4
        else: 
          a = Weight_X /0.5   
          return (45.4+ (44.8*(a-1)))

    elif Zone  == "e":
        if Weight_X / 0.5 == 0.5:
          return 56.6
        else: 
          a = Weight_X /0.5   
          return (56.6+ (55.5*(a-1)))

  elif Type_of_Shipment == "Forward and RTO charges":
    if Zone  == "a":
        if Weight_X / 0.5 == 0.5:
          return (29.5 + 13.6)
        else: 
          a = Weight_X /0.5   
          return (29.5 + 13.6 + ((23.6*(a-1)*2)))

    elif Zone  == "b":
        if Weight_X / 0.5 == 0.5:
          return (29.5 + 20.5)
        else: 
          a = Weight_X /0.5   
          return (29.5 + 20.5 + ((23.6*(a-1)*2)))

    if Zone  == "c":
        if Weight_X / 0.5 == 0.5:
          return (29.5 + 31.9)
        else: 
          a = Weight_X /0.5   
          return (29.5 + 31.9 + ((23.6*(a-1)*2)))

    if Zone  == "d":
        if Weight_X / 0.5 == 0.5:
          return (29.5 + 41.3)
        else: 
          a = Weight_X /0.5   
          return (29.5 + 41.3 + ((23.6*(a-1)*2)))

    if Zone  == "e":
        if Weight_X / 0.5 == 0.5:
          return (29.5 + 55.5)
        else: 
          a = Weight_X /0.5   
          return (29.5 + 55.5 + ((23.6*(a-1)*2)))



courier_invoice['Expected Charge as per X (Rs)'] = courier_invoice.apply(lambda row: charges(row['Zone'], row['Type of Shipment'], row['Weight_X']), axis=1)

courier_invoice["Difference Between Expected Charges and Billed Charges (Rs.)"]=courier_invoice["Expected Charge as per X (Rs)"]-courier_invoice["Billing Amount (Rs.)"]

courier_invoice.rename(columns={"AWB Code":"AWB Number","Charged Weight":"Total weight as per Courier Company (KG)","Billing Amount (Rs.)":"Charges Billed by Courier Company (Rs.) " ,"Zone":"Delivery Zone as per X","Weight_X":"Weight slab as per X (KG)"},inplace=True)


courier_invoice.drop(columns=["Warehouse Pincode_y","Type of Shipment","Customer Pincode","Warehouse Pincode_x"],axis=1,inplace=True)

# courier_invoice.reindex(columns=["Order ID","AWB Number","Total weight as per X (KG)","Weight slab as per X (KG)","Total weight as per Courier Company (KG)","Weight slab charged by Courier Company (KG)","Delivery Zone as per X","Delivery Zone charged by Courier Company","Expected Charge as per X (Rs.)","Charges Billed by Courier Company (Rs.)"])
courier_invoice = courier_invoice.drop_duplicates()


courier_invoice.to_excel("Result.xlsx", index=False)

courier_invoice

print(courier_invoice)

# Show a pop-up message
root = tk.Tk()
root.withdraw()
messagebox.showinfo("Success", "Excel file has been generated successfully!")
