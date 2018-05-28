$(document).ready(function() {
  $("#id_password1").keyup(function() {
    var pass = $("#id_password1").val();
    $("#result").text(check(pass));
  });

  function check(pass) {
    var protect = 0;
    
    if(pass.length < 8) {
      $("#result").removeClass();
      $("#result").addClass('err');
      return 'Очень короткий';
    }
    
    // Английские прописные
    var en_small = "([a-z]+)";
    
    if(pass.match(en_small)) {
      protect++;
    }
    
    //A,B,C,D
    var en_big = "([A-Z]+)";
      
    if(pass.match(en_big)) {
      protect++;
    }

    //1,2,3,4,5 ... 0
    var numb = "([0-9]+)";
    
    if(pass.match(numb)) {
      protect++;
    }

    //!@#$
    var symbols = /\W/;
     
    if(pass.match(symbols)) {
      protect++;
    }
    
    if(protect == 1) {
      $("#result").removeClass();
      $("#result").addClass('err');
      return 'Слабый';
    }

    if(protect == 2) {
      $("#result").removeClass();
      $("#result").addClass('medium-pass');
      return 'Средний';
    }

    if(protect == 3) {
      $("#result").removeClass();
      $("#result").addClass('hard-pass');
      return 'Хороший';
    }

    if((protect == 4) && (pass.length >= 10)) {
      $("#result").removeClass();
      $("#result").addClass('strong-pass');
      return 'Надежный';
    }
    }}
);

// Сравнение паролей
function isConfirm(SignupForm, password1, password2, pass22, submit){
  // Пароль 1
  PASS1 = document.forms[SignupForm].password1.value;
  // Длина пароля
  PASS1count = document.forms[SignupForm].password1.value.length;
  // Пароль 2
  PASS2 = document.forms[SignupForm].password2.value;
  // Индикатор совпадения паролей
  PASS22 = document.getElementById(pass22);
  // Кнопка отправки формы
  SUBMIT = document.forms[SignupForm].submit;

  if(PASS1count < 8) {
    // Деактивация кнопки отправки
    SUBMIT.disabled = 1;
  } 
  
  if ((PASS1 == PASS2) && (PASS1count >= 8)) {
    PASS22.style.color = "green";
    PASS22.innerHTML = "Пароли совпадают";
    SUBMIT.disabled = 0;
  } else {
    if(PASS1count >= 8) {
      PASS22.style.color = "red";
      PASS22.innerHTML = "Пароли не совпадают";
      // Деактивация кнопки отправки
      SUBMIT.disabled = 1;
    }
  }
}