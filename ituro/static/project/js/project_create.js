$(document).ready(function() {
    var category = getCategory();
    if (category !== 'innovative')
        $('[for="id_presentation"]').parent().toggleClass('hidden');

    $('#id_category').on('change', function() {
        category = getCategory();
        if (category !== 'innovative')
            $('[for="id_presentation"]').parent().toggleClass('hidden');
    });
});

var getCategory = function() {
    return $('#id_category option[selected="selected"]').attr('value');
}
