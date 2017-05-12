# -*- coding: utf-8 -*-
"""
Created on Thu May 11 20:07:01 2017

@author: Administrator
"""




#post_pre = [2.5, 5, 7.5, 10, 12.5, 15]
#post_out = [3.2, 4.0, 5.8, 3.8, 2.8, 1.0]
#
#hr = [30, 40, 50, 60]
#hr_out = [12.2, 10.0,  8.0,  7.6]
def smooth_plot(x, y, xlabel=u'x 轴', ylabel=u'y 轴', title=u'光滑拟合曲线', fig='', p1=1, p2=1, pn =1): 
    import matplotlib.pyplot as plt
    from scipy.interpolate import spline
    import numpy as np
    x = np.array(x)
    y = np.array(y)
    data_range = x.max()-x.min()
    data_range2 = y.max()-y.min()
    if not fig:
        fig = plt.figure(2)
    fig.patch.set_facecolor('w')
    ax = fig.add_subplot(p1,p2,pn)#add_axes([0.2,0.2,0.6,0.6])#[0.2,0.2,0.5,0.6])
    ax.set_xlim([x.min()-data_range/10,x.max()+data_range/10])
    ax.set_ylim([y.min()-data_range2/10,y.max()+data_range2/10])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    ax.get_xaxis().set_tick_params(direction='out')
    ax.get_yaxis().set_tick_params(direction='out')
    ax.spines['left'].set_position(('outward', 10))
    ax.spines['bottom'].set_position(('outward', 10))
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_xticks(np.linspace(x.min()-data_range/10,x.max()+data_range/10,5))
    ax.set_yticks(np.linspace(y.min()-data_range/10,y.max()+data_range/10,5))
    ax.set_xticklabels([round(i, 1) for i in np.linspace(x.min()-data_range/10,x.max()+data_range/10,5)])
    ax.set_yticklabels([round(i, 1) for i in np.linspace(y.min()-data_range/10,y.max()+data_range/10,5)])
    
    xnew = np.linspace(x.min(),x.max(),600) #300 represents number of points to make between T.min and T.max
    y_smooth = spline(x,y,xnew)
    plt.title(title)
    plt.plot(xnew,y_smooth, 'b-', linewidth=2.0)
    plt.plot(x, y, 'ko',  linewidth=3)
    for i in range(len(x)):
        plt.text(x[i]+data_range/30, y[i], '('+str(x[i])+', '+ str(y[i]) +')',fontsize= 9)
    fig.tight_layout()
    plt.savefig(u'光滑拟合曲线.pdf')
    plt.show()


#title=u' ploy-fit'smooth_plot(post_pre, post_out, xlabel=u'后负荷(cmH2O)', ylabel=u'心输出量(mL)', title=u'后负荷对心输出量的影响')

# coding: utf-8
def plot_fit(x, y, n=1, xlabel=u'', ylabel=u'', title=u' 次拟合曲线', fig='', p1=1, p2=1, pn =1): 
    import matplotlib.pyplot as plt
    import numpy as np
    result={}
    x = np.array(x)
    y = np.array(y)
    data_range = x.max()-x.min()
    data_range2 = y.max()-y.min()
    if not fig:
        fig = plt.figure(1)
    fig.patch.set_facecolor('w')
    ax = fig.add_subplot(p1,p2,pn)#add_axes([0.2,0.2,0.6,0.6])#[0.2,0.2,0.5,0.6])
    ax.set_xlim([x.min()-data_range/10,x.max()+data_range/10])
    ax.set_ylim([y.min()-data_range2/10,y.max()+data_range2/10])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    ax.get_xaxis().set_tick_params(direction='out')
    ax.get_yaxis().set_tick_params(direction='out')
    ax.spines['left'].set_position(('outward', 10))
    ax.spines['bottom'].set_position(('outward', 10))
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_xticks(np.linspace(x.min()-data_range/10,x.max()+data_range/10,5))
    ax.set_yticks(np.linspace(y.min()-data_range/10,y.max()+data_range/10,5))
    ax.set_xticklabels([round(i, 1) for i in np.linspace(x.min()-data_range/10,x.max()+data_range/10,5)])
    ax.set_yticklabels([round(i, 1) for i in np.linspace(y.min()-data_range/10,y.max()+data_range/10,5)])
    
    z1 = np.polyfit(x, y, n)#多项式拟合
    p1 = np.poly1d(z1)
    result['polynominal']=z1.tolist()
    yhat=p1(x)
    ybar=y.mean()
    ssreg=np.sum((yhat-ybar)**2)
    sstot=np.sum((y-ybar)**2)
    result['determination']=ssreg/sstot
    #print(p1) #在屏幕上打印拟合多项式
    x1=np.linspace(x.min(),x.max(),500)
    yvals=p1(x1)#也可以使用yvals=np.polyval(z1,x)
    plt.plot(x1, yvals, 'b-')
    plt.plot(x, y, 'ko')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(str(n)+title)
    for i in range(len(x)):
        plt.text(x[i]+data_range/30, y[i], '('+str(x[i])+', '+ str(y[i]) +')', color='black', fontsize= 7)
    plt.text(x.min()+data_range/4, y.min()+data_range2/4, 'y = '+str(p1).split('\n')[-1]+'\n'+'R2 = '+str(result['determination']), color='blue', fontsize= 7)
    #ax.set_aspect('equal')
    fig.tight_layout()
    #fig.subplots_adjust(left=0.1,bottom=0.1,right=.9,top=.9)
    plt.savefig(u'多次拟合曲线.pdf')
    if pn == 4:
    	plt.show()
    return(result)

if __name__ == '__main__':
    import matplotlib as mpl
    mpl.rcParams['font.sans-serif']=['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    pre_pre = input(u'请输入横坐标的自变量值, 用逗号或空格分隔:\n')#[2.5, 5.0, 7.5, 10.0,12.5, 15.0]
    pre_out = input(u'请输入纵坐标的因变量值, 用逗号或空格分隔:\n')#[3.8, 5.4, 6.0, 7.0, 7.0, 5.6]
    if ',' in pre_pre:
        pre_pre = [float(i.strip()) for i in pre_pre.split(',')]
        pre_out = [float(i.strip()) for i in pre_out.split(',')]
    else:
        pre_pre = [float(i.strip()) for i in pre_pre.split()]
        pre_out = [float(i.strip()) for i in pre_out.split()]
    if not pre_pre:
        pre_pre = [2.5, 5.0, 7.5, 10.0,12.5, 15.0]
        pre_out = [3.8, 5.4, 6.0, 7.0, 7.0, 5.6]
#post_pre = [2.5, 5, 7.5, 10, 12.5, 15]
#post_out = [3.2, 4.0, 5.8, 3.8, 2.8, 1.0]
#
#hr = [30, 40, 50, 60]
#hr_out = [12.2, 10.0,  8.0,  7.6]

    for i in range(1,5):
        plot_fit(pre_pre,pre_out,n=i,p1=2,p2=2, pn=i)
    smooth_plot(pre_pre, pre_out)
    
