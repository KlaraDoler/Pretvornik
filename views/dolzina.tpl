% import model
<!DOCTYPE html>
<html lang="sl">

<head>
  <title>Dolžina</title>
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
</style>
</head>
<body>

  <blockquote>
  <h1>Pretvarjanje dolžine</h1>

  <hr class="solid">
  <br>
    <form action="/pretvori/">
    Pretvori število <input type="text" name="st">
    iz enote  
  <select name="osnovna">
  <option value="km">km</option>
  <option value="m">m</option>
  <option value="dm">dm</option>
  <option value="cm">cm</option>
  <option value="mm">mm</option>
  <option value="milja">milja</option>
  <option value="yd">yd</option>
  <option value="in">in</option>
  <option value="ft">ft</option>
</select>
    v enoto
    <select name="zelena">
  <option value="km">km</option>
  <option value="m">m</option>
  <option value="dm">dm</option>
  <option value="cm">cm</option>
  <option value="mm">mm</option>
  <option value="milja">milja</option>
  <option value="yd">yd</option>
  <option value="in">in</option>
  <option value="ft">ft</option>
</select>
                  
    <button type="submit">PRETVORI</button>
    </form>
  <blockquote>

</body>
</html>