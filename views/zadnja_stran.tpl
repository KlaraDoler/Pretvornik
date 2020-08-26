<!DOCTYPE html>
<html lang="sl">
<head>
  <title>Pretvornik enot</title>
<style>
body {
  background-color: rgba(0, 185, 0, 0.2);
  color: black;
  font-family: verdana;
  font-size: 140%;
}
/* Solid border */
hr.solid {
  border-top: 3px solid #bbb;
}
</style>
</head>
<body>

  <br>
  <hr class="solid">
  <center>
  {{st}} {{osnovna}} = <b>{{round(result, 5)}}</b> {{zelena}}
  </font>
  <hr class="solid">

  <p align="right">
  (Rezultat je zaokrožen na pet decimalnih mest.)
  </p>
  <form action="/nazaj/">
    <button type="submit">NOVA PRETVORBA</button>
    </center>

</body>
</html>