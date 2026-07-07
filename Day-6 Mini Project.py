# # Mini Project
# # Customer Purchase Analyzer
# # Given: purchases = [1200, 4500, 800, 6000, 3500, 1500, 7200]
# # Create a program that:
# # Uses filter() to find purchases above ₹3000. Uses map() to apply a 10% discount, Uses map() to add 18% GST.
# # Uses sorted() to display purchases from highest to lowest, Uses a lambda function to classify purchases:
# # "Premium" if purchase > ₹5000, "Standard" otherwise
# # Display all results neatly.

purchases = [1200, 4500, 800, 6000, 3500, 1500, 7200]
high_purchases = list(filter(lambda purchase: purchase > 3000, purchases))
print("Purchase above 3000:", high_purchases)
discount_purchases = list(map(lambda purchase: purchase * 0.90, purchases))
print("After 10% discount:", discount_purchases)
gst_purchases = list(map(lambda purchase: purchase * 1.18, purchases))
print("After 18% GST:", gst_purchases)
sorted_purchases = sorted(purchases, reverse = True)
print("Sorted:", sorted_purchases)
classification = list(map(lambda purchase: "Premium" if purchase > 5000 else "Standard", purchases))
print("Classification:", classification)
print("END")
