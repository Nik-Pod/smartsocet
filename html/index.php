<html>
<head>
     <style>input.knopka {
  color: #fff; /* цвет текста */
  text-decoration: none; /* убирать подчёркивание у ссылок */
  user-select: none; /* убирать выделение текста */
  background: rgb(212,75,56); /* фон кнопки */
  padding: .7em 1.5em; /* отступ от текста */
  outline: none; /* убирать контур в Mozilla */
  border: 0px;
} 
a.knopka:hover { background: rgb(232,95,76); } /* при наведении курсора мышки */
a.knopka:active { background: rgb(152,15,0); } </style>
     <!--index.php-->
</head>
<body>
<form action="" method="post">
<table>
	<tr>
		<td>Port 1&nbsp;</td>
		<td align="center"><input type="submit" name="on1" value="on" class="knopka"></td>
		<td align="center"><input type="submit" name="off1" value="off" class="knopka"></td>
	</tr>
        <tr>
                <td>Port 2&nbsp;</td>
                <td align="center"><input type="submit" name="on2" value="on" class="knopka"></td>
                <td align="center"><input type="submit" name="off2" value="off" class="knopka"></td>
        </tr>
        <tr>
                <td>Port 3&nbsp;</td>
                <td align="center"><input type="submit" name="on3" value="on" class="knopka"></td>
                <td align="center"><input type="submit" name="off3" value="off" class="knopka"></td>
        </tr>
        <tr>
                <td>Port 4&nbsp;</td>
                <td align="center"><input type="submit" name="on4" value="on" class="knopka"></td>
                <td align="center"><input type="submit" name="off4" value="off" class="knopka"></td>
        </tr>
<tr><td>&nbsp;</td></tr>
        <tr>
                <td>Cam&nbsp;</td>
                <td><input type="submit" name="camon" value="Cam-on" class="knopka"></td>
                <td><input type="submit" name="camoff" value="Cam-off" class="knopka"></td>
        </tr>

</table>
</form>
	<?php
  if (!empty($_POST['on1'])) {
   echo exec("sudo python3 /var/www/html/relay/1/on1.py");
  }
  if (!empty($_POST['off1'])) {
   echo exec("sudo python3 /var/www/html/relay/1/off1.py");
  }
  if (!empty($_POST['on2'])) {
   echo exec("sudo python3 /var/www/html/relay/2/on2.py");
  }
  if (!empty($_POST['off2'])) {
   echo exec("sudo python3 /var/www/html/relay/2/off2.py");
  }
  if (!empty($_POST['on3'])) {
   echo exec("sudo python3 /var/www/html/relay/3/on3.py");
  }
  if (!empty($_POST['off3'])) {
   echo exec("sudo python3 /var/www/html/relay/3/off3.py");
  }
  if (!empty($_POST['on4'])) {
   echo exec("sudo python3 /var/www/html/relay/4/on4.py");
  }
  if (!empty($_POST['off4'])) {
   echo exec("sudo python3 /var/www/html/relay/4/off4.py");
  }
  if (!empty($_POST['camon'])){
   echo exec("sudo bash /home/pi/Desktop/mc/oncam.sh");
  }
  if (!empty($_POST['camoff'])){
   echo exec("sudo bash /home/pi/Desktop/mc/killcam.sh");	  
  }
?>
</body>
</html>

