# 1. 请写出求巴塞尔问题近似解的python代码
# （注：巴塞尔问题不了解是什么可以百度，但是请不要试图抄网上的答案）

import math

def TheBaselProblem(N):
    BP_num = 0
    for i in range(1,N+1):
        BP_num+=1/(i*i)
    return BP_num

if __name__ == '__main__':
    N = int(1e6)
    BP_value = TheBaselProblem(N)
    print(
        "巴塞尔问题近似解:%s\n近似解与实值误差:%s"
        %(BP_value,math.pi*math.pi/6-BP_value)
        )



# 2. sqrt(1+2*sqrt(1+3*sqrt(1+4*sqrt(1+...))))的值等于? 
# （提示：第二题可以使用python，也可以手算，给出结果即可）
# 答案为：3