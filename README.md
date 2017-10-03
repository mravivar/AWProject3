# AWProject3

Database:
1. To install mongodb
$ brew install mongodb

2. To install brew services 
$ brew tap homebrew/services

3. Start mongodb service:
$ brew services start mongodb

4. Load data to mongodb:
$ cd awproject3/db
$ mongoimport --db awproject3 --collection table1 --file 01_01_2014-12_31_2014[1].json --jsonArray

Database:awproject3 and Collection:table1 is created in mongodb

Flask server:
1. To install the needed python packages
$ cd awproject3
$ pip install -r requirements.txt

2. To start flask server
$ cd awproject3
$ python server.app

3. In browser, goto: http://localhost:5000/ . 
You will the following output:
/**************************************
This is your index page

Data:

answer Get Weekday from int <p>You can use Map and then create a method like <code>getByCode</code> where you will pass the day number as the argument and it will return you the enum. E.g.</p>\n\n<pre><code>import java.util.HashMap;\nimport java.util.Map;\n\nenum Weekday {\n Sunday(0) Monday(1) Tuesday(2) Wednesday(3) Thursday(4) Friday(5) Saturday(6);\n private int value;\n\n Weekday(int c){\n this.value =c;\n }\n\n\n static Map&lt;Integer Weekday&gt; map = new HashMap&lt;&gt;();\n\n static {\n for (Weekday catalog : Weekday.values()) {\n map.put(catalog.value catalog);\n }\n }\n\n public static Weekday getByCode(int code) {\n return map.get(code);\n }\n }\n</code></pre>\n\n<p>You can call the above method like <code>Weekday.getByCode(2)</code> and it will return you <code>Tuesday</code></p>\n you can use map and then create a method like where you will pass the day number as the argument and it will return you the enum. e.g. you can call the above method like and it will return you getbycode import java.util.hashmap; import java.util.map; enum weekday { sunday(0) monday(1) tuesday(2) wednesday(3) thursday(4) friday(5) saturday(6); private int value; weekday(int c){ this.value =c; } static map&lt;integer weekday&gt; map = new hashmap&lt;&gt;(); static { for (weekday catalog : weekday.values()) { map.put(catalog.value catalog); } } public static weekday getbycode(int code) { return map.get(code); } } weekday.getbycode(2) tuesday 1707520 1419984103 4 6873 100 java enums
*****************************************/

