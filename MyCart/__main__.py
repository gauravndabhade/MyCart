import sys
from MyCart.cli import main 
from category.cli import category
from product.cli import product
from user.cli import user

main.add_command(user)
main.add_command(category)
main.add_command(product)

if __name__ == '__main__':
    args = sys.argv
    if "--help" in args or len(args) == 1:
        print("cart")
    main()
