var urlExtract;

$(".viewDictionary").click(function () {
   
    urlExtract = $(this).attr("href");
});    

// Used to launch the modal dialog via ajax
$('#modal').on('show.bs.modal', function (event) {

  var modal = $(this);  
  $.ajax({
    url: urlExtract,
    context: document.body
  }).done(function(response) {
    modal.html(response);
  });
})

$('body').on('hidden.bs.modal', '.modal', function () {
  $(this).removeData('bs.modal');
});