//  script that fetches from given URL and displays the value of hello

$('document').ready(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    $('DIV#hello').text(data.hello);
  });
});
