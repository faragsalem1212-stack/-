print("Your Library .")
The_Library = []
ist_book = input("Enter the name of a book you own: ")
The_Library.append(ist_book)
sec_book = input("Enter the name of another book you own (or press 'Enter' to skip): ")
if sec_book:
  The_Library.append(sec_book)
  print(f"\nYour Library: {The_Library}\n")
else:
  print(f"\nYour Library: {The_Library}\n")
Wishlist = []
wish_book = input("Enter the name of a book you wish to have in the future: ")
Wishlist.append(wish_book)
sec_wish_book = input("Enter the name of another book you wish to have (or priss 'Enter' to skip): ")
if sec_wish_book:
  Wishlist.append(sec_wish_book)
  print(f"\nYour Wishlist: {Wishlist}\n")
else:
  print(f"\nYour Wishlist: {Wishlist}\n")

gotten_book = input("Enter the name of a book from your wishlist that you've acquire (or press 'Enter' to skip): ")
if gotten_book in Wishlist:
  Wishlist.remove(gotten_book)
  The_Library.append(gotten_book)
  print(f"\nUpdated Library: {The_Library}")
  print(f"Updated Wishlist: {Wishlist}\n")

don_book = input("Enter the name of a book from your library you wish to donate (or press 'Enter' to skip): ")

if don_book in The_Library:
   The_Library.remove(don_book)
   print(f"\nFinal Library after donation: {The_Library}")
else:
   print(f"\nYour final library : {The_Library}")
