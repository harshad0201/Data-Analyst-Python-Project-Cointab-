# 👓 Cointab Data Analyst Assignment

## 📌 Overview  
This project verifies courier charges for an Indian e-commerce company (**X**).  
The goal is to compare **expected delivery charges** (calculated from X’s internal data) with the **charges billed by courier companies**, and highlight mismatches.  

---

## 📂 Input Data  
- **Order Report** – Order IDs with SKUs  
- **Pincode Mapping** – Warehouse → Delivery pincode zones  
- **SKU Master** – Product weights  
- **Courier Invoice (CSV)** – AWB, Order ID, courier weight, zone, billed charges, etc.  
- **Rate Card** – Charges by zone & weight slab (forward / RTO)  

---

## ⚙️ Processing Steps  
1. Calculate order weight and applicable weight slab (based on zones).  
2. Map warehouse & delivery pincodes to delivery zones.  
3. Compute expected courier charges using the rate card logic.  
4. Compare expected vs billed charges for each order.  

---

## 📊 Output  
- **Order-level Report (Excel/CSV)**  
  Contains order details, weights, zones, expected vs billed charges, and differences.  

- **Summary Report**  
  Shows counts and amounts of correctly charged, overcharged, and undercharged orders.  

---

## 📦 Deliverables  
- 📑 Excel file with two sheets (order-level report + summary).  
- 💻 Source code (Python / R / Java / JavaScript).  
