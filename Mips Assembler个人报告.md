[TOC]



# Mips Assembler个人报告

假设指令是PC+4

## 一、测试数据

```mips
disp: add $t0,$zero,$zero
For: add $t1,$t0,$a0
 lb $t1,0($t1)
 beq $t1,$zero,Exjt
 addi $sp,$sp,-4
 sw $a0,4($sp)
 add $a0,$t1,$zero
 addi $v0,$zero,11
 syscall
 lw $a0,4($sp)
 addi $sp,$sp,4
 addi $t0,$t0,1
 j For
Exjt: add $v0,$t0,$zero
 jr $ra
```



## 二、测试结果

![](https://koyomi.oss-cn-hangzhou.aliyuncs.com/20200313160342.png)

## 三、指令分类

### i 指令

#### 形如 ORDERNAME  R,IMM(R)

lw sw  lh lhu sh

#### 形如 ORDERNAME  R,IMM

lui bgezal

#### 形如  ORDERNAME R,R,IMM

addi addiu andi ori xori

#### 形如 ORDERNAME R,R,label

beq bne

### R指令

#### 形如 ORDERNAME  R,R,R

add addu sub subu slt sltu  and or xor nor sll srl sra sllv srlv srav

#### 形如ORDERNAME R,R

mult(mul) multu div divu jalr

#### 形如ORDERNAME R

jr

#### 形如ORDERNAME

eret syscall

### J指令

#### 形如ORDERNAME IMM

j

#### 形如ORDERNAME R,R

jal

### 伪指令



## 四、思路

### 1.总体设计

将指令按照以上分类建立三个类：IOrder,ROrder,JOrder

每个类分别负责：

1. 通过指令名和参数表翻译成Hex

   ```java
   public static Integer transformOrder2Binary(String orderName, List<String> paraList);
   ```

2. 通过指令名判断是否属于本类指令

   ```java
   public static Boolean isROrder(String orderName)
   ```

i指令和j指令的transformOrder2Binary由于label和PC的参与有所变化：

i指令：

```java
public static Integer transformOrder2Binary(String orderName, List<String> paraList, int PC,
    Map<String, Integer> map)
```

j指令:

```java
static Integer transformOrder2Binary(String orderName , List<String> paraList,Map<String,Integer> map)
```

IOrder,ROrder,JOrder 均继承自Order类，该类中包含寄存器编号结构。

Util类提供String拆分、String[] 打印和数字转化的工具方法

Program类提供PC，Label表和汇编执行方法，以及执行前的预扫描功能

### 2.数据结构

寄存器编号保存在HashMap中；

orderName 保存在HashSet中；

Label 与 address的对应关系保存在HashMap中；

### 3.算法

算法大致按照ZPC资料中给出的汇编算法，如beq:

```java
return (4 << 26) | (registersMap.get(rs) << 21) | (registersMap.get(rt) << 16) | (
    ((address - PC - 2) >> 1) & 0xFFFF);
```

## 五、未完成部分

* 放松格式要求，能通过正则智能匹配
* 目前只支持简单mips指令，不支持data段等

* 寄存器编号匹配  :ok_hand:
* 输出格式[bin] origin order(without label) :ok_hand:
* 伪指令、表达式、格式指令
* 细化报错  :ok_hand:
* 日志记录
* 大小写转化 展示的时候要显示原始的  :ok_hand:

* 立即数范围检查 溢出
* 立即数支持其他进制
