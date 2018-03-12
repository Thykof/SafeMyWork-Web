$(document).ready(function($) {
  if ($('#a-account').html() == 'Account'){
    dest = $('#s-user').offset().top;
    $('html,body').animate({scrollTop:dest}, 0);
  }
});
