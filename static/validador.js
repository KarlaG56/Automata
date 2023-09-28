function validarCadena() {
    var cadena = document.getElementById("cadena").value;
    if (cadena.length !== 8) {
        var resultadoElement = document.getElementById("resultado");
        resultadoElement.innerHTML = "La cadena debe tener exactamente 8 caracteres.";
        return;
    }

    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var raw = JSON.stringify({
        "cadena": cadena
    });

    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };

    fetch("http://127.0.0.1:5000/automata", requestOptions)
      .then(response => response.json())
      .then(result => {
          var resultadoElement = document.getElementById("resultado");
          var recorridoElement = document.getElementById("recorrido");

          if (result.estado) {
                resultadoElement.innerHTML = `Cadena válida: ${cadena}`;
                mostrarRecorrido(result.recorrido, recorridoElement);
          } else {
                resultadoElement.innerHTML = "La cadena no es válida según el autómata.";
                mostrarRecorrido(result.recorrido, recorridoElement);
          }
      })
      .catch(error => console.log('error', error));
}

function mostrarRecorrido(recorrido, recorridoElement) {
    var recorridoString = recorrido.join("->");
    recorridoElement.innerHTML = `Recorrido: ${recorridoString}`;
}

