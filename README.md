<div align="center">
  <h1 align = "center">Python Tkinter Upload Files to Sqlite</h1>
</div>

[![License: MIT](https://cdn.prod.website-files.com/5e0f1144930a8bc8aace526c/65dd9eb5aaca434fac4f1c34_License-MIT-blue.svg)](/LICENSE)

This is an open-source GUI desktop software designed to upload files to sqlite on our desktop.

When you are using the Windows system environment, you can download python file and run this script below on your terminal.

<p align="center">
  <img src="screenshot/output_windows_exe.JPG" width="850" alt="accessibility text">
</p>

```shell
pyinstaller --onefile --name huizhou-grocery -i logo.jpg --windowed huizhouGrocery_Tkinter.py
```


After that, you will get an exe file in your working directory.


<p align="center">
  <img src="screenshot/window_exe.JPG" width="150" title="hover text">
</p>

We could test our software in a Windows environment.

<p align="center">
  <img src="screenshot/windows_exe_intro.JPG" width="360" title="hover text">
</p>

<p align="center">
  <img src="screenshot/windows_huizhou_grocery.JPG" width="360" title="hover text">
</p>

Once you input dates or some words and click upload, you will start to select your files that will be uploaded to your local sqlite database(not remote server). Your selected files(images, xlsx) will be converted to BLOB data and stored in sqlite.

<p align="center">
  <img src="screenshot/insertDateTo_Sqlite.JPG" width="360" title="hover text">
</p>

We are developing some software programs to support our POS (point of sale) system. This is our open-source project. Python code could be cross-platform for many users (like Linux environment).


