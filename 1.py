import time
import subprocess

# 執行指令
def cmd(command):
    subp = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8")
    subp.wait(30)
    if subp.poll() == 0:
        print(subp.communicate()[0])
    else:
        print("失败")

mycmd='conda run -n fastai python modules/fastai/mnist-detection.py \
--model modules/fastai/mnist-detection.pkl \
--input "static/2032.png"'

print(cmd(mycmd))