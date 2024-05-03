$(document).ready(function() {
  $('#btn_translate').click(function() {
    const languageCode = $('#language_code').val();
    $.get('https://hellosalut.stefanbohacek.dev/', { lang: languageCode }, function(response) {
      $('#hello').text(response.hello);
    });
  });

  $('#language_code').keypress(function(event) {
    if (event.which == 13) { // Check if Enter key is pressed
      const languageCode = $('#language_code').val();
      $.get('https://hellosalut.stefanbohacek.dev/', { lang: languageCode }, function(response) {
        $('#hello').text(response.hello);
      });
    }
  });
});
