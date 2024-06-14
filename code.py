from lib.light import Light
from lib.body import Body
from lib.engine import Engine

def main_menu():
    while True:
         print("===============MAIN MENU==============")
         print("1. Light Parts Operations")
         print("2. Body Parts Operations")
         print("3. Engine Parts Operations")
         print("0. Exit")

         choice = input("\nEnter your choice: ")
         if choice == "1":
             return light_operations()
         elif choice == "2":
             return body_operations()
         elif choice == "3":
             return engine_operations()
         elif choice == "0":
             exit()
         else:
             print("Invalid choice")


def light_operations():
         while True:
             print("\n***Light Part Menu***")
             print("1. Create Light Part")
             print("2. Get Light Part by id")
             print("3. Update Light Part by id")
             print("4. Delete Light Part")
             print("5. Count all Light Parts")
             print("6. Fetch all Light Parts")
             print("7. Return to main menu")

             choice = input("\n Enter your choice: ")
             light = Light()
             if choice == "1":
                 id = input("Enter id: ")
                 name = input("Enter name: ")
                 price = input("Enter price: ")
                 part_no = input("Enter part no: ")
                 part_description = input("Enter part description: ")

                 create_light_id = light.create_light_part(name, price, part_no, part_description)
                 print(f"Light Part {create_light_id} created successfully")

             elif choice == "2":
                 id = input("Enter id: ")
                 get_light_part_by_id = light.get_light_part_by_id(id)
                 print(get_light_part_by_id)

             elif choice == "3":
                 id = input("Enter id: ")
                 name = input("Enter name: ")
                 price = input("Enter price: ")
                 part_no = input("Enter part no: ")
                 part_description = input("Enter part description: ")

                 update_light_part_by_id = light.update_light_part_by_id(id, name, price, part_no, part_description)
                 print(update_light_part_by_id)

             elif choice == "4":
                 id = input("Enter id: ")
                 delete_light_part = light.delete_light_part_by_id(id)
                 print(delete_light_part)

             elif choice == "5":
                 count = light.count_all_light_parts()
                 print(count)

             elif choice == "6":
                 get_all_light_parts = light.get_all_light_parts()
                 print(get_all_light_parts)

             elif choice == "7":
                 main_menu()

def body_operations():
         while True:
             print("\n***Body Part Menu***")
             print("1. Create Body Part")
             print("2. Get Body Part by id")
             print("3. Update Body Part by id")
             print("4. Delete Body Part")
             print("5. Count all Body Parts")
             print("6. Fetch all Body Parts")
             print("7. Return to main menu")

             choice = input("\n Enter your choice: ")
             body = Body()
             if choice == "1":
                 id = input("Enter id: ")
                 name = input("Enter name: ")
                 price = input("Enter price: ")
                 part_no = input("Enter part no: ")
                 part_description = input("Enter part description: ")

                 create_body_id = body.create_body_part(name, price, part_no, part_description)
                 print(f"Body Part {create_body_id} created successfully")

             elif choice == "2":
                 id = input("Enter id: ")
                 get_body_part_by_id = body.get_body_part_by_id(id)
                 print(get_body_part_by_id)

             elif choice == "3":
                 id = input("Enter id: ")
                 name = input("Enter name: ")
                 price = input("Enter price: ")
                 part_no = input("Enter part no: ")
                 part_description = input("Enter part description: ")

                 update_body_part_by_id = body.update_body_part_by_id(id, name, price, part_no, part_description)
                 print(update_body_part_by_id)

             elif choice == "4":
                 id = input("Enter id: ")
                 delete_body_part = body.delete_body_part_by_id(id)
                 print(delete_body_part)

             elif choice == "5":
                 count = body.count_all_body_parts()
                 print(count)
                
             elif choice == "6":
                 get_all_body_parts = body.get_all_body_parts()
                 print(get_all_body_parts)

             elif choice == "7":
                 main_menu()


def engine_operations():
         while True:
             print("\n***Engine Part Menu***")
             print("1. Create Engine Part")
             print("2. Get Engine Part by id")
             print("3. Update Engine Part by id")
             print("4. Delete Engine Part")
             print("5. Count all Engine Parts")
             print("6. Fetch all Engine Parts")
             print("7. Return to main menu")

             choice = input("\n Enter your choice: ")
             engine = Engine()
             if choice == "1":
                 name = input("Enter name: ")
                 price = input("Enter price: ")
                 part_no = input("Enter part no: ")
                 part_description = input("Enter part description: ")

                 create_engine_id = engine.create_engine(name, price, part_no, part_description)
                 print(f"Engine Part {create_engine_id} created successfully")

             elif choice == "2":
                 id = input("Enter id: ")
                 get_engine_part_by_id = engine.get_engine_part_by_id(id)
                 print(get_engine_part_by_id)

             elif choice == "3":
                 id = input("Enter id: ")
                 name = input("Enter name: ")
                 price = input("Enter price: ")
                 part_no = input("Enter part no: ")
                 part_description = input("Enter part description: ")

                 update_engine_part_by_id = engine.update_engine_part_by_id(id, name, price, part_no, part_description)
                 print(update_engine_part_by_id)

             elif choice == "4":
                 id = input("Enter id: ")
                 delete_engine_part = engine.delete_engine_part_by_id(id)
                 print(delete_engine_part)

             elif choice == "5":
                 count = engine.count_all_engine_parts()
                 print(count)

             elif choice == "6":
                 get_all_engine_parts = engine.get_all_engine_parts()
                 print(get_all_engine_parts)

             elif choice == "7":
                 main_menu()


main_menu()