# scan2PDF
Merge files to PDF using single side scanner.

##Requirement
You need ```Python3``` and ```PyPDF2``` installed in your computer.
You can install ```PyPDF2``` by running ```pip3 install PyPDF2``` in your terminal. (macOS)

##Usage

(On scanner)
1. Scanning the documents in regular order. (Page 1,3,5, ..., n-1.)
2. Scanning the documents in reverse order. (Page n, n-2, n-4, ..., 2.)
3. Getting the PDF document reday in your USB flash drive or your computer.

(On your computer)
1. Changing the file path of scanned document in this Python program.
2. Run it! 

```Python3 mergePDF.py```

You will get the merged PDF file. Remember to rename the ```output.PDF```, or it will be replaced after your next running. XD

# 扫描并生成PDF
此程序将帮助使用单面扫描仪扫描大量文件的您生成合并后的PDF文档。

##所需工具
请确保您的电脑上安装了```Python3``` 以及 ```PyPDF2```。
你可以通过执行```pip3 install PyPDF2```来安装```PyPDF2```。 （macOS）

##用法

（在扫描仪端）
1. 请将您的文件按正常顺序扫描。（第1、3、5、……、最后一张的正面）
2. 请将您的文件翻过来按倒序扫描。（最后一张的反面、倒数第二张的反面、倒数第三章张的反面、……、第一张的反面）
3. 确保您将扫描好的PDF文档存入了您的U盘或者您的电脑。


（在计算机端）
1. 请将```mergePDF.py```中的```input1```和```input2```改为您文件的地址。
2. 运行它！

```Python3 mergePDF.py```

您将会得到合并好的PDF文件。请记得更改默认的输出文件名```output.PDF```，否则它将会在下一次运行中被替换。 XD

