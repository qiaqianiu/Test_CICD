import os

class RunManager:
    def __init__(self):
        folder_path = '../report/result'
        if len(os.listdir(folder_path)) > 0:
            for file_name in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file_name)
                os.remove(file_path)

    def run_pytest(self):
        cmd = f'python -m pytest ../cases --alluredir=../report/result'
        os.system(cmd)
        os.system('allure generate ../report/result -o ../report/html --clean')




if __name__ == '__main__':
    RunManager().run_pytest()