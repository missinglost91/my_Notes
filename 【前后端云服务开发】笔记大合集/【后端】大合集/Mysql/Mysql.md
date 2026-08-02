# Mysql入门到精通
编写:关山难
______

## 下载安装


Mysql社区版不要钱
商业版要钱

下载地址
<https://dev.mysql.com/downloads/>

## 基础概念

![2025-07-23-00-55-43](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-23-00-55-43.png)

![2025-07-23-01-21-08](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-23-01-21-08.png)

![2025-07-23-00-48-19](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-23-00-48-19.png)


![2025-07-23-00-50-16](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-23-00-50-16.png)

root
123456

## 指令入门

要用*管理员权限*打开程序

**操作数据库**

```sql
show databases;
//查询所有数据库

create database itcast;
//创建一个叫itcast的数据库

drop database test;
//删除一个叫test的数据库

use test;
//使用一个叫test的数据库

select database();
//查询当前在哪个数据库
```


**操作表结构**
```SQL
use test;
//使用表

show tables;
//展示该数据库中的表

desc tb_user;
//查看表结构

show create table tb_user;
//查看建表语句

```
做一张如图的表
![2025-07-23-22-01-51](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-23-22-01-51.png)



**数值类型**
![2025-07-23-23-10-29](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-23-23-10-29.png)
sore double(整体长度，小数位数长度)


**字符串类型**
![2025-07-23-23-11-33](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-23-23-11-33.png)
char(最大长度)定长----性能高       性别 gender char(1)
varchar(最大)成都//变长---性能较差     用户名 username varchar(50)

**日期类型**
![2025-07-23-23-11-55](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2025-07-23-23-11-55.png)

```sql
create table emp(
id int comment '编号',
worknum varchar(10) comment '工号',
name varchar(10) comment '姓名',
gender char(1) comment '性别',
age tinyint unsigned comment '年龄',
idcard char(18) comment '身份证号',
entrydate date comment '入职时间'
) comment '员工表';
```

添加新字段

```sql
alter table 表名 add 字段名 类型(长度) [COMMENT 注释][约束];  
//添加新字段

alter table 表名 modify 字段名 新数据类型(长度);
//修改数据类型

alter table 表名 change 旧字段名 新字段名 类型(长度) [COMMENT 注释][约束];      
//修改字段名和字段类型

alter table 表名 drop 字段名;
//删除字段

alter table 表名 rename to 新表名;
//修改表明

drop table[IF EXISTS] 表名;
//删除表

truncate table 表名;
//删除指定表,并重新创建该表(只有表结构，没有表数据)
``` 

```sql
insert into 表名(字段名1,字段名2,...) values(值1,值2,...);
//给指定字段添加数据

insert into 表名(字段名1,字段名2,...) values(值1,值2,...),(值1,值2,...);
//批量添加数据


插入数据时，指定的字段顺序需要与值的顺序一一对应

字符串和日期型数据应该包含在引号中

插入的数据大小，应该在字符的规定范围内
```




