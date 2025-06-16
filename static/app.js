$('form input[type="file"]').change(event => {
    let archives = event.target.files;
    if (archives.length === 0) {
        console.log('Sem imagem para mostrar')
    } else {
        if (archives[0].type == 'image/jpeg') {
            $('img').remove();
            let image = $('<img class="img-fluid">');
            image.attr('src', window.URL.createObjectURL(archives[0]));
            $('figure').prepend(image);
        } else {
            alert('Formato não Suportado!')
        }
    }
});

