% import model
<!DOCTYPE html>
<html lang="sl">

<head>
  <title>Čas</title>
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
  <h1>Pretvarjanje časa</h1>

  <hr class="solid">
  <br>
    <form action="/pretvori/">
    Pretvori število <input type="text" name="st">
    iz enote  
  <select name="osnovna">
  <option value="leto">leto</option>
  <option value="dan">dan</option>
  <option value="h">h</option>
  <option value="min">min</option>
  <option value="s">s</option>
</select>
    v enoto
    <select name="zelena">
  <option value="leto">leto</option>
  <option value="dan">dan</option>
  <option value="h">h</option>
  <option value="min">min</option>
  <option value="s">s</option>
</select>
                  
    <button type="submit">PRETVORI</button>
    </form>
  <blockquote>

</body>
</html>