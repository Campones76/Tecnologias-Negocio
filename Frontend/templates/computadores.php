<!DOCTYPE html>
<html lang="pt">

<head>
    <meta charset="UTF-8">
    <title>Main menu</title>

    <link rel="stylesheet" href="/static/styles/main.css">
    <link rel="stylesheet" href="/static/styles/dropdown.css">
    <!-- bootstrap css -->
    <link href="https://fonts.googleapis.com/css?family=Arvo&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.6/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.6/js/bootstrap.min.js"></script>
</head>


<body>
    <div class="container">
        <nav class="main-menu" style="height: 695px; width:250px;">
            <ul>
                <img src="/static/images/LOGO_PROJETO_TEN.png" style="padding-left: 10px; width: 200px; height: 100px;" alt="Logo">
                <span class="nav-text" style="color: #364958; font-family: Inter; font-size: 20px;font-style: normal;font-weight: 700;line-height: normal; width:100%;text-align:center; display: inline-block;">
                    IT on Demand
                </span>
                <div id="linha">
                </div>
                <li style="padding-top: 50px;">
                    <a href="inicio.php">
                        <i class="fa fa-home" ></i>
                        <span class="nav-text">
                            Home Page
                        </span>
                    </a>
                </li>
                <li>
                    <a class="dropdown-btn">
                        <i class="fa fa-boxes-stacked" ></i>
                        <span class="nav-text">
                            Products
                            <i class="fa fa-caret-down" style="position:absolute;top:10%;right:50px"></i>
                        </span>
                    </a>
                </li>
               <div class="dropdown-container">
                 <ul class="nav nav-sidebar">
                  <li>
                    <i class="fa fa-laptop"><a href="computadores.php" class="links-dropdown" style="padding-left:10px;">Computers</a></i><p>
                    <i class="fa fa-keyboard-o" style="padding-left:1px;"><a href="#" class="links-dropdown" style="padding-left:12px;">Keybords</a></i><p>
                    <i class="fa fa-mouse" style="padding-left:3px;"><a href="#" class="links-dropdown" style="padding-left:16px;">Mouses</a></i><p>
                    <i class="fa fa-desktop"><a href="#" class="links-dropdown" style="padding-left:12px;">Screen's</a></i>
                  </li>
                </u>
                </div>
                <li>
                    <a href="utilizadores_inserir.php">
                        <i class="fa fa-shopping-cart"></i>
                        <span class="nav-text">
                            Shopping Cart
                        </span>
                    </a>
                </li>
                <li>
                    <a href="utilizador_eventos.php">
                        <i class="fa fa-user"></i>
                        <span class="nav-text ">
                            Profile
                        </span>
                    </a>
                </li>
                <li>
                    <a href="utilizador_eventos.php">
                        <i class="fa fa-users"></i>
                        <span class="nav-text">
                            About Us
                        </span>
                    </a>
                </li>
            </ul>
                <li style="position: absolute; left: 0; bottom: 0;">
                  <div style="background-color: #CAE4CB; width:90%; height:100px; border-radius: 8px; padding-left:10px;">
                    <h4 style="padding-top:10px;">Contact Us By:</h4>
                      <p>
                        <strong>Email:</strong>
                        <a href="#" style="font-size: 15px; font-weight:500;">itondemand@gmail.com</a>
                      </p>
                      <p>
                        <strong>Phone:</strong>
                        +222 222 222
                      </p>
                  </div>
                  <i style="color: #1E1E1E;font-family: Inter;font-size: 15px;font-style: normal;font-weight: 500;line-height: normal;padding-left:150px;">@TEN2023</i>
                </li>
        </nav>
</div>
<div class="banner">
  <p style="font-size:40px; padding-top:10px; color: #364958;font-family: Jockey One; padding-left:20px;"><i class="fa fa-boxes-stacked" style="font-size:30px;" ></i>Products-Computers<i class="fa fa-laptop" style="font-size:30px;"></i></p>
</div>

<div id="divBusca">
  <input type="text" id="txtBusca" placeholder="Buscar..."/>
  <i class="fa fa-magnifying-glass" style="font-size:30px; padding-top:4px;"></i>
</div>

<div style="display: flex; flex-direction: row; width:100%; margin-top:30px;">
  <div id="containerimg" style="margin-left:300px;">
    <img src="/static/images/COMPUTADOR 1.jpg" style=" width: 320px; height: 300px; padding-top:30px; border-radius: 10px;border: 4px solid #CAE4CB;">
    <p>Lenovo IdeaPad Slim 3 15IAH8 Intel Core i5-12450H/16GB/512GB SSD/15.6</p>
    <p>Price:</p>
    <p style="color: #87BBA2;font-family: Jockey One;font-size: 24px;font-style: normal;font-weight: 400;line-height: normal;">608,60€</p>

  </div>
  <div id="containerimg" style="margin-left:100px;">
    <img src="/static/images/COMPUTADOR 2.jpg" style=" width: 320px; height: 300px; padding-top:30px; border-radius: 10px;border: 4px solid #CAE4CB;">
    <p style="padding-right:20px;">ASUS TUF Gaming F15 Intel Core i5-11400H/16GB/512GB SSD/RTX 2050</p>
    <p>Price:</p>
    <p style="color: #87BBA2;font-family: Jockey One;font-size: 24px;font-style: normal;font-weight: 400;line-height: normal;">635,36€</p>
  </div>
  <div id="containerimg" style="margin-left:100px;">
    <img src="/static/images/COMPUTADOR 3.jpg" style=" width: 320px; height: 300px; padding-top:30px; border-radius: 10px;border: 4px solid #CAE4CB;">
    <p style="padding-right:20px;">Macbook Air APPLE Silver (Apple M1 - RAM: 8 GB - 256 GB SSD - 7-Core GPU)</p>
    <p>Price:</p>
    <p style="color: #87BBA2;font-family: Jockey One;font-size: 24px;font-style: normal;font-weight: 400;line-height: normal;">999,99€</p>

  </div>
</div>

    <div class="container">
        <form action="php/login.php" method="POST">
        </form>
    </div>
    <script>
/* Loop through all dropdown buttons to toggle between hiding and showing its dropdown content - This allows the user to have multiple dropdowns without any conflict */
    var dropdown = document.getElementsByClassName("dropdown-btn");
    var i;

    for (i = 0; i < dropdown.length; i++) {
      dropdown[i].addEventListener("click", function() {

        var dropdownContent =  document.getElementsByClassName("dropdown-container");
        if (dropdownContent[0].style.display === "block") {
          dropdownContent[0].style.display = "none";
        } else {
          dropdownContent[0].style.display = "block";
        }
      });
    }

    $(".nav a").on("click", function() {
      $(".nav").find(".active").removeClass("active");
      $(this).parent().addClass("active");
    });

    </script>

    <!-- bootstrap js -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
        integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
        crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.7/dist/umd/popper.min.js"
        integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1"
        crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/js/bootstrap.min.js"
        integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM"
        crossorigin="anonymous"></script>
</body>

</html>
