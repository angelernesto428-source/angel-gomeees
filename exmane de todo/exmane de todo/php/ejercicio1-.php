<?php
//ejercicio 1
echo "hola mundo "


//ejercicio2

$nombre = "angel";
$edad = 17;

echo "soy ". $nombre ." y tengo ". $edad ."\n";

//ejercicio 3
$a = 1
$b = 2

echo "Suma: " . ($a + $b ) . "\n";        
echo "Resta: " . ($a - $b) . "\n";        
echo "Multiplicación: " . ($a * $b) . "\n"; 
echo "División: " . ($a / $b) . "\n";       
echo "Módulo: " . ($b % $b) . "\n\n";   

//ejercicio 4

echo "Lista de juegos favo:\n";
$juegos = ["undertale", "kh:birth by sleep", "tekken", "hollow knigth"];

foreach ($juegos as $juego) {
    echo "- " . $juego . "\n";
}

echo "\n";

//ejercico 7

$edad = (int)readline("Ponma su edad: "); 

if ($edad < 10) {
    echo "Eres un niño.\n";
} elseif ($edad < 18) {
  
    echo "Eres un adolescente.\n";
} elseif ($edad < 55) {
   
    echo "Eres un adulto.\n";
} else {

    echo "Eres un adulto mayor.\n";
}

\





?>
