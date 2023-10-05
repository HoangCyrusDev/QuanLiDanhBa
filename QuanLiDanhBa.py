#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def welcome():
    entry = int(input("""
                        ------------Project Quản lý Danh Bạ--------------
                        1. Hiển thị
                        2. Thêm liên lạc
                        3, Kiểm tra danh bạ
                        4. Xóa liên lạc
                        5. Thoát
                        Enter your number: """))
    return entry

def phonebook():
    contacts = [] # Khơi tạo một ds trống để lưu các liên lạc
    while True:   # Bắt đầu vòng lặp vô hạn cho phép người dùng thực hiện chức năng của danh bạ
        entry = welcome() # Gọi hàm welcome
        if entry == 1: # nếu lựa chọn nhập vào bằng 1 thì thực hiện
            f = open("Contact.txt", "r") # mở file Contact để đọc ds ở chế độ đọc "r"
            contacts = f.readlines() #đọc nd của file và gán vào contacts
            f.close() # đóng file khi đọc xog để giải phóng tài nguyên hệ thống
            if not contacts: # Kiểm tra xem ds có rỗng hay không
                print("Danh sách liên lạc trống!")
            else:
                for i in contacts: # dùng vòng lặp for để in ra từng dòng
                    print(i)
        elif entry == 2: #thêm liên lạc
            checked = False # khởi tạo biến checked với gtri ban đầu là False
            phone_number = input("Số điện thoại:")
            contact_name = input("Tên liên lạc?")
            f = open("Contact.txt", "r")
            contacts = f.readlines()
            f.close()
            for i in contacts: # duyệt qua từng dòng
                if i.find(name) != -1: # nếu tìm thấy
                    print("Liên lạc đã tồn tại!")
                    checked = True
                    break
            if checked == False: # giá trị vẫn là False tức là chưa tìm thấy
                f = open("Contact.txt", "a") # Mở file, mở chế độ ghi
                contacts.append(contact_name + ": " + phone_number + "\n")
                contacts = f.write(contacts[-1]) # ghi nd mới vào file txt
                f.close()
                print("Liên lạc đã được lưu")
        elif entry == 3: #kiểm tra danh bạ
            checked = False
            f = open("Contact.txt", "r")
            contacts = f.readlines() #  đọc nd của file và gán vào
            f.close()
            name = input("Nhập tên liên lạc:")
            for i in contacts: # dùng vòng lặp để duyệt từng dòng, nếu tìm thấy sẽ in ra dòng đó
                if i.find(name) != -1:
                    print(i)
                    checked = True
                    break
            if checked == False:# nếu check vẫn là false tức là k tìm thấy
                print("Liên lạc không tồn tại")
        elif entry == 4: # xóa liên lạc
            checked = False
            delete_var = 0 #tạo để lát gán vào vị trí thấy cho nó
            f = open("Contact.txt", "r")
            contacts = f.readlines()
            f.close()
            name = input("Nhập tên liên lạc:")
            for i in contacts:
                if i.find(name) != -1:
                    print(i)
                    delete_var = contacts.index(i) #tìm thấy và gán vị trí cho nó
                    checked = True
                    confirm = input("Bạn có chắc chắn xóa? Y/N:")
                    if confirm.capitalize() == "Y":
                        contacts.pop(delete_var)
                        f = open("Contact.txt", "w") # ghi lại ds xóa vào file
                        print("Bạn đã xóa tên liên lạc {0} khỏi danh sách!".format(name))
                        for i in contacts:
                            f.write(i) #chạy và hiển thị ra cái tên đó
                        f.close()
                    else:
                        print("Quay trở lại menu!")
                    break
            if checked == False: # nếu checked bằng False có nghĩa là vẫn chưa tìm thấy
                print("Liên lạc không tồn tại")
        elif entry == 5: #thoát
            print("Xin cảm ơn!")
            break
        else:
            print("Mời bạn nhập lại!")

phonebook()


# In[ ]:





# #### 
