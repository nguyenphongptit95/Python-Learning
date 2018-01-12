listBig = ["Phong", 4, 7.0, "Van", 3.0];
listTiny = [123, "Tran"];

print(listBig);
print(listBig[0]);
print(listBig[1:3]);
print(listBig[2:]);
print(listTiny * 4);
print(listTiny + listBig);

listBig[0] = "Phonggggg";
print(listBig);