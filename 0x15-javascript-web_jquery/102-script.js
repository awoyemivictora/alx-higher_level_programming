$('document').ready(() => {
  const url = 'https://www.fourtonfish.com/hellosalut/?';
  $('INPUT#htn_translate').click(() => {
    $.get(url + $.param({ lang: $('INPUT#language_code').val() }), (data) => {
      $('DIV#hello').html(data.hello);
    });
  });
});
