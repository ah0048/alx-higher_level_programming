$('DIV#toggle_header').on('click', function () {
  if ($('header').hasClass('red') && $('header').hasClass('green')) {
    $('header').removeClass('green');
  } else if ($('header').hasClass('red')) {
    $('header').removeClass('red');
    $('header').addClass('green');
  } else {
    $('header').removeClass('green');
    $('header').addClass('red');
  }
});
