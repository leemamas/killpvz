# killpvz
植物大战僵尸自动收集阳光，修改阳光

 最终效果：
![Image text](images/1.png)
1.找call大法

掏出我们的神器Cheat Enginge
![Image text](images/2.png)
![Image text](images/3.png)
![Image text](images/4.png)
![Image text](images/5.png)

回到游戏，收集一个阳光，改变数值，然后
![Image text](images/6.png)

出现只配到到一个结果
![Image text](images/7.png)

可以尝试修改地址的value，改变阳光
![Image text](images/8.png)

双击地址就添加到下面区域，修改下面地址的数值就可以改变阳光
![Image text](images/9.png)

找到这个地址，只是临时的偏移量，每局重开，就会变化，不满足使用

我们要找到最终的基址和偏移
![Image text](images/10.png)

回到游戏，随便操作收集或者消耗阳光，使数值变动，ce就会看到偏移地址
记录5578，和2E6C7C00,继续走。。！~~
![Image text](images/11.png)

找到868 ，02879D30
![Image text](images/12.png)

绿色的是基址
![Image text](images/13.png)
![Image text](images/15.png)

明显00755E0C是我们要找~~~！！

---
接下来我们找自动收集的call
同理
![Image text](images/16.png)
点击阳光搜1，不点击搜0 ，
![Image text](images/17.png)
找到jne改jmp测试，成功！

使用python代码，修改相关的基址就可以使用！