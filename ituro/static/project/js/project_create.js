$(document).ready(function() {
    var category = getCategory();
    var field = $('[for="id_presentation"]').parent();
    if (category !== 'innovative')
        $(field).addClass('hidden');

    $('#id_category').on('change', function() {
        category = getCategory();
        if (category !== 'innovative')
            $(field).addClass('hidden');
        else
            $(field).removeClass('hidden');
    });
});

function getCategory() {
    return $('#id_category option:selected').attr('value');
}
