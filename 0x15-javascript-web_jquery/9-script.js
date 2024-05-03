$(document).ready(function() {
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    success: function(response) {
      $('#hello').text(response.hello);
    }
  });
});
