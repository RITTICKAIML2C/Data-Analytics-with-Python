# # 📂 Step 5: Mini Project
# # Sales Data Analyzer
# # Given: sales = [1200, 4500, 800, 3000, 1500, 6000, 900]. Your program should create:
# # High-value sales (> ₹2000), Low-value sales (≤ ₹2000), Sales after adding 18% GST, Sales after applying a 10% discount
# # Labels: "High" if sale > ₹3000, "Low" otherwise
# # Print every result neatly.
sales = [1200, 4500, 800, 3000, 1500, 6000, 900]
high_value = [sale for sale in sales if sale > 2000]
low_value = [sale for sale in sales if sale <= 2000]
gst_sales = [sale * 1.18 for sale in sales]
discount_sales = [sale * 0.90 for sale in sales]
labels = ["High" if sale > 3000 else "Low" for sale in sales]
print("Original Sales:", sales)
print("High-value Sales (> 2000):", high_value)
print("Low-value Sales (≤ 2000):", low_value)
print("Sales after 18% GST:", gst_sales)
print("Sales after 10% Discount:", discount_sales)
print("Labels:", labels)
