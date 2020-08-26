% import model
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
h1 {
  color: rgba(0, 176, 151, 0.7);
  font-family: verdana;
  font-size: 250%;
}
/* Solid border */
hr.solid {
  border-top: 3px solid #bbb;
}
.footer{ 
  position: absolute;
  bottom: 1em;
  right: 1em;
  text-align: right;
} 
  width: 100%;
}  
</style>
</head>
<body>

  <center>
  <h1>Pretvornik enot</h1>

  Izberite, katero mersko enoto želite pretvarjati.

  <hr class="solid">
  <form action="/pretvarjanje_teze/">
    <button type="submit">TEŽA</button>
  </form>
<br>
  <form action="/pretvarjanje_casa/">
    <button type="submit">ČAS</button>
  </form>
<br>
  <form action="/pretvarjanje_dolzine/">
    <button type="submit">DOLŽINA</button>
  </form>
<br>
  <form action="/pretvarjanje_temperature/">
    <button type="submit">TEMPERATURA</button>
  </form>
<br>
  <form action="/pretvarjanje_prostornine/">
    <button type="submit">PROSTORNINA</button>
  </form>
  <hr class="solid">
  </center>
  <div class="footer">Klara Doler, 2020</div>

</body>
</html>