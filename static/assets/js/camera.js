//
img_tag = "<img src='../../img/profile_default.png' alt='Student Photo' height='240' width='320'>";
Webcam.set({
            width: 320,
            height: 240,
            image_format: 'jpeg',
            jpeg_quality: 90
        });

$('#photo').on('click', function() {
    if(this.val !== 'Cancel'){
        Webcam.attach( '#camera-frame' );
        this.val = 'Cancel'
        this.value = 'Cancel';
        
        $(this).removeClass('btn-outline-success');
        $(this).addClass('btn-outline-danger')
    }else{
        $('#camera-frame').html(img_tag);
        this.val = 'Take a Photo';
        this.value = 'Take a Photo';

        $(this).removeClass('btn-outline-danger');
        $(this).addClass('btn-outline-success')
    }
});

$('#snapper').on('click', function() {
    take();
});  

function take() {
    Webcam.snap( function(data_uri) {
       
        img = document.createElement('img');
        img.setAttribute('src', data_uri);
        

        $('#camera-frame').html(img);
        document.getElementById('snapper').style.display = 'none';
        $('#photo').val = 'Take a Photo';
        $('#photo').value = 'Take a Photo';

        $('#photo').removeClass('btn-outline-danger');
        $('#photo').addClass('btn-outline-success');
        // console.log(blob);

    } );
}

function b64toBlob(b64Data, contentType, sliceSize) {
    contentType = contentType || '';
    sliceSize = sliceSize || 512;

    var byteCharacters = atob(b64Data);
    var byteArrays = [];

    for (var offset = 0; offset < byteCharacters.length; offset += sliceSize) {
        var slice = byteCharacters.slice(offset, offset + sliceSize);

        var byteNumbers = new Array(slice.length);
        for (var i = 0; i < slice.length; i++) {
            byteNumbers[i] = slice.charCodeAt(i);
        }

        var byteArray = new Uint8Array(byteNumbers);

        byteArrays.push(byteArray);
    }

  var blob = new Blob(byteArrays, {type: contentType});
  return blob;
}

function chooseFile() {
    $('#passport').click();
}


$('#passport').on('change', function () {
    $('#choose_btn').html(this.value)
})