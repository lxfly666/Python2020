from student import *

class StudentManager(object):
    def __init__(self):
        self.student_list = []

    def run(self):
        self.load_student()
        while True:
            self.show_menu()
            menu_num = int(input("请输入您需要的功能序号："))
            if menu_num == 1:
                self.add_student()
            elif menu_num == 2:
                self.del_student()
            elif menu_num ==3:
                self.modify_student()
            elif menu_num == 4:
                # 查询学员信息
                self.search_student()
            elif menu_num == 5:
                # 显示所有学员信息
                self.show_student()
            elif menu_num == 6:
                # 保存学员信息
                self.save_student()
            elif menu_num == 7:
                break
    @staticmethod
    def show_menu():
        print('请选择如下功能：')
        print('1:添加学员')
        print('2:删除学员')
        print('3:修改学员信息')
        print('4:查询学员信息')
        print('5:显示所有学员信息')
        print('6:保存学员信息')
        print('7:退出系统')

    def add_student(self):
        name = input('请输入您的姓名：')
        gender = input('请输入您的性别：')
        tel = input('请输入您的手机号：')

        student = Student(name, gender, tel)
        self.student_list.append(student)

        print(self.student_list)
        print(student)

    def del_student(self):
        del_name = input('请输入要删除的学员姓名：')
        for i in self.student_list:
            if del_name==i.name:
                self.student_list.remove(i)
                break
            else:
                print('查无此人！')
        print(self.student_list)

    # 2.4 修改学员信息
    def modify_student(self):
        # 1. 用户输入目标学员姓名
        modify_name = input('请输入要修改的学员姓名：')

        # 2. 遍历列表数据，如果学员存在修改姓名性别手机号，否则提示学员不存在
        for i in self.student_list:
            if modify_name == i.name:
                i.name = input('姓名：')
                i.gender = input('性别：')
                i.tel = input('手机号：')
                print(f'修改学员信息成功，姓名{i.name}, 性别{i.gender}, 手机号{i.tel}')
                break
        else:
            print('查无此人！')

    # 2.5 查询学员信息
    def search_student(self):
        # 1. 用户输入目标学员姓名
        search_name = input('请输入您要搜索的学员姓名：')

        # 2. 遍历列表。如果学员存在打印学员信息，否则提示学员不存在
        for i in self.student_list:
            if search_name == i.name:
                print(f'姓名是{i.name}, 性别是{i.gender}, 手机号是{i.tel}')
                break
        else:
            print('查无此人！')

    # 2.6 显示所有学员信息
    def show_student(self):
        # 1. 打印表头
        print('姓名\t性别\t手机号')

        # 2. 打印学员数据
        for i in self.student_list:
            print(f'{i.name}\t{i.gender}\t{i.tel}')

    def save_student(self):
        f = open('student.data','w')
        new_list = [i.__dict__ for i in self.student_list]
        f.write(str(new_list))
        f.close()

    def load_student(self):
        try:
            f = open("student.data",'r')
        except:
            f = open("student.data",'w')
        else:
            data = f.read()
            new_list = eval(data)
            self.student_list = [Student(i['name'],i['gender'],i['tel']) for i in new_list]
        finally:
            f.close()