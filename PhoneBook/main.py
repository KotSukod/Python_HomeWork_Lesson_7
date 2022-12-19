import view
import controller

print("Телефонный справочник v 1.0")

view.head()
controller.choice_action(view.get_value())
