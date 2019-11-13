
$('input[type="file"]').change(function(e){
        var fileName = e.target.files[0].name;
        $('.custom-file-label').html(fileName);
    });

$('#but_upload').click(function (event) {
    event.preventDefault();

    var fd = new FormData();
    var files = $('#file')[0].files[0];
    fd.append('file',files);
   debugger;
  $.post({
    type: "POST",
    url: "http://127.0.0.1:5000/uploadinputimage",
    data: fd,
      contentType: false,
      processData: false,
    success: function(response){
       if(response != 0){
                    $("#resultedimage").attr("src",'static/images/' + response);
                }else{
                    alert('file not uploaded');
                }
    },
  });
    return false;
});

