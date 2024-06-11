$(document).ready(function() {
    // Aggiungi il token CSRF a tutte le richieste AJAX
    if (typeof csrf_token === 'undefined' || !csrf_token) {
        console.error('CSRF token is not defined');
    } else {
        $.ajaxSetup({
            headers: {
                'X-CSRFToken': csrf_token
            }
        });
        console.log('CSRF token configurato per AJAX:', csrf_token);
    }

    $('#tags').change(function() {
        if ($(this).val() === 'new') {
            $('#new_tag_group').show();
        } else {
            $('#new_tag_group').hide();
        }
    });

    $('#add_new_tag').click(function() {
        var newTag = $('#new_tag').val().trim();
        if (newTag !== '') {
            $('#added_tags').append('<span class="badge badge-primary mr-2">' + newTag + '</span>');
            $('<input>').attr({
                type: 'hidden',
                name: 'new_tags[]',
                value: newTag
            }).appendTo('form');
            $('#new_tag').val('');
            $('#new_tag_group').hide();
            $('#tags').val('');  // Reset the tag selection
        }
    });

    $('#add_selected_tag').click(function() {
        var selectedTag = $('#tags').val();
        var selectedTagText = $('#tags option:selected').text();
        if (selectedTag !== 'new' && selectedTag) {
            $('#added_tags').append('<span class="badge badge-primary mr-2">' + selectedTagText + '</span>');
            $('<input>').attr({
                type: 'hidden',
                name: 'tag_ids[]',
                value: selectedTag
            }).appendTo('form');
            $('#tags').val('');
        } else if (selectedTag === 'new') {
            $('#new_tag_group').show();
        }
    });
});
