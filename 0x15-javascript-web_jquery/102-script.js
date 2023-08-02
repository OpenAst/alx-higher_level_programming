//a JavaScript script that fetches and prints how to say “Hello” depending on the language
//You should use this API service: https://www.fourtonfish.com/hellosalut/hello/

$('#btn_translate').click(function () {
  const langCode = $('#language_code').val();
  const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/${langCode}`;

  $.get(apiUrl, function (data) {
    $('#hello').text(data.hello);
  });
});

