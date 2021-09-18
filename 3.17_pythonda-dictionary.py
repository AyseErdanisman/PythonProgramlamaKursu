"""
dictionary liste tipi key - value şeklinde çalışır
41 => kocaeliyi temsil ediyor
34 => istanbulu temsil ediyor gibi
"""

# peki dictionary olmadan bu işlem nasıl tanımlanabilir? 
sehirler = ["kocaeli", "istanbul"]
plakalar = [41, 34]

print(plakalar[sehirler.index("kocaeli")])
print(plakalar[sehirler.index("istanbul")])

# dictionary kullansaydık
# plaka = {"key": value}
plaka = {"kocaeli": 41, "istanbul": 34}
print(plaka["istanbul"])

plaka["ankara"] = 6
# ankara lisyeye eklenir
print(plaka)
plaka["kocaeli"] = "new value"
#dersek kocaeli için 41 yerine new value ifadesi atanmış olur
print(plaka)

users = {
    "sadikturan": {
        "age": 36,
        "roles":["user"],
        "email": "sadik@gmail.com",
        "address":"kocaeli",
        "phone": "12123123"
    },

    "cihanturan": {
        "age": 24,
        "roles": ["admin", "user"],
        "email": "cihan@gmail.com",
        "address":"istanbul",
        "phone": "12123123"
    }
}

print(users["sadikturan"])
print(users["cihanturan"]["age"])
print(users["cihanturan"]["roles"][0])