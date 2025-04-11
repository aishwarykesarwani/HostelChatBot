from fpdf import FPDF

# Safe plain text version of the hostel info
text = """
Hostel Information Sheet

Name: Green Valley Boys' Hostel
Location: Near Central College Road, Sector 5, Indore, India
Capacity: 60 Residents
Warden: Mr. Rajeev Sharma (+91-9876543210)
Email: greenvalleyhostel@gmail.com

Facilities Provided
- Fully furnished single & double occupancy rooms
- 24x7 electricity and water supply
- High-speed Wi-Fi access in all rooms
- Air-coolers installed in each room
- Study table, chair, and personal wardrobe
- Common lounge area with TV and indoor games
- Fully automated laundry service
- In-house mess offering 3 meals + snacks daily

Rules & Regulations
1. Entry permitted only before 9:30 PM. Late entries require prior warden approval.
2. Visitors allowed only on weekends from 9 AM to 6 PM.
3. Consumption of alcohol, tobacco, or drugs is strictly prohibited.
4. Noise levels must be minimized after 10 PM.
5. Hostel property should be used responsibly. Any damages must be reported.
6. Students must maintain hygiene in rooms and shared spaces.

Fee Structure (per month)
Room Type        | Charges (INR)
-----------------|--------------
Single Occupancy | INR 8000
Double Sharing   | INR 6000
Security Deposit | INR 5000 (One-Time, Refundable)

Current Availability
Single room-5
Double room-10
triple room-0
*Fees include accommodation, Wi-Fi, and mess services.*

Mess Menu (Sample Weekly)

Monday-Friday:
- Breakfast: Poha/Upma + Tea
- Lunch: Roti, Dal, Rice, Seasonal Veg
- Dinner: Paneer/Chole + Rice + Dessert on Wednesdays

Saturday-Sunday:
- Breakfast: Stuffed Paratha + Curd
- Lunch: Fried Rice + Manchurian
- Dinner: Biryani/Noodles + Ice Cream

Emergency Contacts
- Warden: Mr. Rajeev Sharma - +91-9876543210
- Assistant Warden: Ms. Kavita Menon - +91-9123456780
- Nearest Hospital: City Care Hospital (1.2 km away)
"""

pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font("Arial", size=12)

# Add each line to the PDF
for line in text.split('\n'):
    pdf.multi_cell(0, 10, line)

# Save the PDF
pdf.output("Hostel_Information.pdf")
