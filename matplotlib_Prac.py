import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#https://blog.csdn.net/liuxiao214/article/details/78975792
##三维绘图
#画点
def point():
    x_list = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]]
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    for x in x_list:
        print(x)
        ax.scatter(x[0],x[1],x[2],c='r')
    plt.show()

    print(ax)


def d3_plane():
    x = np.arange(1,10,1)
    y = np.arange(1,10,1)
    x,y = np.meshgrid(x,y) #将坐标向量转成坐标矩阵
    z = 5*x+2*y+30
    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')
    surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=plt.cm.jet, linewidth=0, antialiased=True)

    ax.set_xlabel("x-label", color='r')
    ax.set_ylabel("y-label", color='g')
    ax.set_zlabel("z-label", color='b')

    ax.set_zlim3d(0, 100) # 设置z坐标轴
    fig.colorbar(surf, shrink=0.5, aspect=5) # 图例
    plt.show()

def d3_hookface():
    x = np.arange(-5,5,0.1)
    y = np.arange(-5,5,0.1)
    x,y = np.meshgrid(x,y)
    z = np.sin(np.sqrt(x**2+y**2))
    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')
    # 曲面，x,y,z坐标，横向步长，纵向步长，颜色，线宽，是否渐变
    surf =ax.plot_surface(x,y,z,rstride=1,cstride=1,cmap=plt.cm.coolwarm,linewidth=0,antialiased=True)
    ax.set_zlim(-1.01,1.01)
    ax.set_xlabel('x-label',color='r')
    ax.set_ylabel('y-label',color='g')
    ax.set_zlabel('z_label',color='b')

    ax.zaxis.set_major_locator(Linearl)  # 设置z轴标度
    ax.zaxis.set_major_formatter(FormatStrFormatter('%0.02f'))  # 设置z轴精度
    # shrink颜色条伸缩比例0-1, aspect颜色条宽度（反比例，数值越大宽度越窄）

    fig.colorbar(surf,shrink=1.0,aspect=5)
    plt.show()

d3_hookface()