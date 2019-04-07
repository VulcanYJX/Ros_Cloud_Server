# ROS_Cloud_Server
Use Cloud server and VPN to deploy Distributed ROS Online;

通过公网部署分布式ROS
====

## 云服务器创建ROS master服务，本地联网设备的node实现对远程服务器的订阅

   * 在网络中有很多关于ros的分布式部署的，但是只能通过一个局域网进行部署，需要在网络中的两台机器互相ping通，才可以进行分布式通信。<br>
   * 为了能够将远程的Server和本地的设备构建成一个虚拟局域网，这里使用了[蒲公英](https://pgy.oray.com/)进行快速搭建。云服务器使用了[阿里云学生机](https://promotion.aliyun.com/ntms/act/campus2018.html)。

* ### 配置虚拟组网后可以查看到本地设备在虚拟组网中的ip

* ### 服务器部署Ros服务及网络配置

  在云主机上安装[ros](http://wiki.ros.org/kinetic/Installation)服务；
  ```Bash
  vi /etc/hosts   #将虚拟组网中的两台设备以 ip hostname 的格式写入；
  ```
  将两个虚拟组网中的`ip  hostname`都写入到hosts文件中，并注释掉服务器ipv6的服务器ip（如果存在）
 
  ```Bash
  echo "export ROS_MASTER_URI=http://运行roscore主机的hostname:11311" >> ~/.bashrc
  echo "export ROS_HOSTNAME=运行roscore主机的hostname" >> ~/.bashrc
  source ~/.bashrc
  ```
  
* ### 本地设备部署Ros服务及网络设备

  在本地设备上安装[ros](http://wiki.ros.org/kinetic/Installation)服务；
  ```Bash
  vi /etc/hosts   #将虚拟组网中的两台设备以 ip hostname 的格式写入；
  ```
  同样将虚拟组网中的数据写入本地设备的hosts中，下面的部分稍有不同；
  
  ```Bash
  echo "export ROS_MASTER_URI=http://运行roscore主机的hostname:11311" >> ~/.bashrc
  echo "export ROS_HOSTNAME=本地机器的hostname" >> ~/.bashrc
  source ~/.bashrc
  ```
  
* ### 配置完成后进行测试
  ```Bash
  ping 运行roscore主机的hostname   #在本地主机
  ping 本地机器的hostname          #在云服务器
  ```
  如果可以ping通则已经部署完成，如果无法ping通请检查上述步骤；
  
* ### 测试
  ```Bash
  roscore                         #在云服务器
  rosnode list                    #在本地主机
  ```
  
  
