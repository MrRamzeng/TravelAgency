window.setInterval(
      function Time(){
            var time = new Date();
            document.getElementById("clock").innerHTML = time.toLocaleTimeString();
      }, 0, 1);