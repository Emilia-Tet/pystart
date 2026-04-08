# zadanie 1
from random import choice
objects_list = ["mieszek zlota", "miecz", "klucz", "woda", "ksiega", "mapa"]

users_set = set({})

def check_for_object(obj: str, obj_list: set) -> bool:
    if obj in obj_list:
        return True

for _ in range(5):
    random_obj = choice(objects_list)
    print(random_obj)
    users_set.add(random_obj)
    print(users_set)

    if check_for_object("miecz", users_set):
        print("Masz juz miecz!")
    else:
        print(f"Twoje znalezisko to: {random_obj}, ale nadal nie masz miecza.")


# zadanie 2
emails = ["jan@wp.pl", "lego@lego.com", "karol@op.pl", "yoan@yahoo.com", "kukuryku.pl",
          "lelo@polelo.com", "jajajajaj", "fokus@pokus.pl", "aloha", "jan@wp.pl"]
emails_database = []
# wersja z inputem
# for _ in range(11):
#     email = input("Podaj adres mailowy: ")
#     if email.endswith(".com", ".pl")  and "@" in email:
#         emails_database.add(email)
# print(f"The email database contains {len(emails_database)} emails: {emails_database}.")

for email in emails:
    if (email.endswith(".com") or email.endswith(".pl"))  and "@" in email:
        emails_database.append(email)
print(f"The email database contains {len(emails_database)} emails: {emails_database}.")
emails_database = set(emails_database)
print(f"After removing duplicates, "
      f"the database contains {len(emails_database)} emails: {emails_database}.")





