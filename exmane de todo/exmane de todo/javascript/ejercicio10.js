   
const limite = prompt("ponle un numero limite al conteo:");
  



let contador = 1


while (contador <= limite) {
        
        
   if (contador === 5) {
           contador++; 
           continue;
        }

        console.log(`Contador actual: ${contador}`);
        contador++;
    }

    console.log("Conteo finalizado.");