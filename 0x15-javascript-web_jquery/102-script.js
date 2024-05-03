$(document).ready(function() {
  $('#btn_translate').click(function() {
    const languageCode = $('#language_code').val();
    $.get('https://hellosalut.stefanbohacek.dev/', { lang: languageCode }, function(response) {
      $('#hello').text(response.hello);
    });
  });
});
