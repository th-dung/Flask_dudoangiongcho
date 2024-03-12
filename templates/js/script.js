// When the user scrolls down 20px from the top of the document, slide down the navbar
window.onscroll = function () { scrollFunction() };

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    document.getElementById("navbar").style.top = "0";
  } else {
    document.getElementById("navbar").style.top = "-50px";
  }
}


/* upload hình ảnh */
function readURL(input) {
  if (input.files && input.files[0]) {

    var reader = new FileReader();

    reader.onload = function (e) {
      $('.image-upload-wrap').hide();

      $('.file-upload-image').attr('src', e.target.result);
      $('.file-upload-content').show();

      $('.image-title').html(input.files[0].name);
    };

    reader.readAsDataURL(input.files[0]);

  } else {
    removeUpload();
  }
}

function removeUpload() {
  $('.file-upload-input').replaceWith($('.file-upload-input').clone());
  $('.file-upload-content').hide();
  $('.image-upload-wrap').show();
}
$('.image-upload-wrap').bind('dragover', function () {
  $('.image-upload-wrap').addClass('image-dropping');
});
$('.image-upload-wrap').bind('dragleave', function () {
  $('.image-upload-wrap').removeClass('image-dropping');
});
