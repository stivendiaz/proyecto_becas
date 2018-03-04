<!DOCTYPE html>
<html lang="en">
<head>
  <title>Prototipo</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
  <style>
    /* Remove the navbar's default rounded borders and increase the bottom margin */ 
    .navbar {
      margin-bottom: 50px;
      border-radius: 0;
      background-color: #000099;
    }
    
    /* Remove the jumbotron's default bottom margin */ 
     .jumbotron {
      margin-bottom: 0;
    }
   
    /* Add a gray background color and some padding to the footer */
    footer {
      background-color: #f2f2f2;
      padding: 25px;
    }
  </style>
</head>
<body>
<!--Estilo Inicio de la página-->
<div class="jumbotron">
  <div class="container-fluid">
        <div class="row">
            <div class="col-sm-2">
                <img src="./itm.png" style="width: 55%;">
            </div>
            <div class="col-sm-2">
                <img src="./campus.jpg" style="width: 120%; ">
            </div>
        </div>
      </div>
</div>
<!-- Barra de navegación-->
<nav class="navbar navbar-inverse">
  <div class="container-fluid">
    <div class="navbar-header">
      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>                        
      </button>
      <a class="navbar-brand" href="#">Inicio</a>
    </div>
    <div class="collapse navbar-collapse" id="myNavbar">
      <ul class="nav navbar-nav">
        <li><a href="#">Becas en el Extranjero</a></li>
        <li><a href="#">Becas a nivel Nacional</a></li>
        <li><a href="#">Contacto</a></li>
      </ul>
    </div>
  </div>
</nav>
<!-- Espacio para el buscador-->
<div class="container">
  <div class="row">
    <div class="col-sm-4">
      <h3 style="color: red;">Próximamente el buscador...</h3><br>
    </div>
  </div>
</div>
<!-- Resultados-->
<div class="container">    
  <div class="row">
    <h3>Resultados</h3>
    <!-- Ejemplo de que puede llenarse con "x" resultados que arroje la consulta -->
   <?php 
for($i=0;$i<4;$i++){;
   ?>
    <div class="col-sm-4">
      <div class="panel panel-primary">
        <div class="panel-heading">NOMBRE BECA<?php echo " ".($i+1); ?></div>
        <div class="panel-body"><img src="https://placehold.it/150x80?text=IMAGE" class="img-responsive" style="width:100%" alt="Image"></div>
        <div class="panel-footer">
        <p>ENTIDAD</p>
        <p>VIGENCA</p>
        <p>VALOR</p>  
        </div>
      </div>
    </div>
<?php
}
?>    
  </div><br>
</div><br><br>

<footer class="container-fluid text-center">
  <p>Derechos Reservados</p>  
  <p>Semillero de BI & Analítica de Datos</p>  
  </form>
</footer>

</body>
</html>