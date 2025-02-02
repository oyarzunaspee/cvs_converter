# CVSer

###### Works with link and path !

A script that converts a .xlsx into a .cvs file
_________________

#### How to use:

* Build container

`docker build -t cvser .`

* Run the container

`docker run -it -v ${PWD}/output:/output cvser + [link or path to .xlsx file]`

* You can provide a link

`https://www.myurl.com/GET/xlsx`

* Or a path

`/User/Folder/my_file.xlsx`

* You will be asked to name each file

* And it's done! You'll find the new .cvs file or files inside /output

____

#### License

MIT License
