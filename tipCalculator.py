sub_total = total = tip_Amount = each = percent = people = 0
#Some Inputs
sub_total = int(input("Sub Total Amount   : "))
percent =   int(input("Percentage         : "))
people =    int(input("How Many People\'s  : "))
#Tips Calculating Methods
tip_Amount = round(percent / 100 * sub_total)
total_Amount = tip_Amount + sub_total
each = round(total_Amount / people)
print("\n\n------------------------------------")
print('        Estimated Valuation         ')
print("------------------------------------")
print(f"Sub Total Amount : ₹ {sub_total}   ")
print(f"Percentage       : % {percent}     ")
print(f"Tip Amount       : ₹ {tip_Amount}  ")
print(f"Total Amount     : ₹ {total_Amount}")
print(f"People           : 👥 {people}      ")
print(f"Each Amount      : ₹ {each}        ")
print("------------------------------------")
