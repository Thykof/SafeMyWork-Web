$(document).ready(function($) {
  if (typeof($('.member').html()) !== 'undefined') {
    dest = $('#s-user').offset().top;
    $('html,body').animate({scrollTop:dest}, 0);
  }
});
