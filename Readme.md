# Visual Transmission

## Communication Systems Lab Project(2023)

___
[Report](/documents/report.pdf) -  [Demo-video](https://www.youtube.com/)

* This repository contains codes and demonstrations for the transmission of reception of images over visible electromagnetic spectrum

___

## Demo video

 [![yt](/documents/thumbnail.png)](https://www.youtube.com/)

___

## Installing requirements with conda

* Run the following commands in the master root to create a new virtual env to run the files in local:

```shell
conda create -n <ENV NAME> python=3.9
conda activate <ENV NAME>
conda install -r requirements.txt
```

___

## Instructions

* Open two different terminal
* Ensure that the ENV is activated
* Navigate to the /python folder
* Enter the respective commands

```shell
python compression.py
```

```shell
python retrieval.py
```

___

## Structure

* /python consists of files compression.py and retrieval.py which are used for communicating with arduino
* /arduino has files for signal reception and trnsmisson with the help of serial port
* For more comprehensive analysis and comparison, refer to [report](/documents/report.pdf).

___

### Contributors

> Aaditya Baranwal baranwal.1@iitj.ac.in ;  Github: [eternal-f1ame](https://github.com/aeternum) <br>
> Aayush Gautam gautam.7@iitj.ac.in ; Github: [ArixCrest](https://github.com/ArixCrest)
