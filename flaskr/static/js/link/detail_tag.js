document.addEventListener('DOMContentLoaded', function() {
    var container = document.getElementById('variable-container');
    var variable = container ? container.getAttribute('data-variable') : null;
    var csrfToken = container ? container.getAttribute('data-csrf') : null;

    $(document).ready(function() {
        // Verifica che csrfToken sia definito
        if (typeof csrfToken === 'undefined' || !csrfToken) {
            console.error('CSRF token is not defined');
        } else {
            $.ajaxSetup({
                headers: {
                    'X-CSRFToken': csrfToken
                }
            });
            console.log('CSRF token configurato per AJAX:', csrfToken);
        }

        $('#tags').change(function() {
            if ($(this).val() === 'new') {
                $('#new-tag-group').show();
            } else {
                $('#new-tag-group').hide();
            }
        });

        $('#add-new-tag').click(function() {
            var newTag = $('#new-tag').val().trim();
            if (newTag !== '') {
                $.ajax({
                    url: "/link/add_tag/" + variable,
                    type: 'POST',
                    data: { new_tag: newTag, link_id: variable },
                    success: function(response) {
                        if(response.success) {
                            $('#tag-list').append('<li class="list-group-item d-flex justify-content-between align-items-center">'
                                + response.tag.name +
                                '<button type="button" class="btn btn-danger btn-sm remove-tag" data-tag-id="' + response.tag.id + '">Remove</button></li>');
                            $('#new-tag').val('');
                            $('#new-tag-group').hide();
                            $('#tags').val('').trigger('change');
                        } else {
                            alert(response.message);
                        }
                    }
                });
            } else {
                alert('Please enter a tag name.');
            }
        });

        $('#add-selected-tag').click(function() {
            var selectedTag = $('#tags').val();
            var selectedTagName = $('#tags option:selected').text();
            if (selectedTag && selectedTag !== 'new') {
                $.ajax({
                    url: "/link/add_tag/" + variable,
                    type: 'POST',
                    data: { tag_id: selectedTag, link_id: variable },
                    success: function(response) {
                        if(response.success) {
                            $('#tag-list').append('<li class="list-group-item d-flex justify-content-between align-items-center">'
                                + selectedTagName +
                                '<button type="button" class="btn btn-danger btn-sm remove-tag" data-tag-id="' + selectedTag + '">Remove</button></li>');
                            $('#tags').val('').trigger('change');
                        } else {
                            alert(response.message);
                        }
                    }
                });
            } else {
                alert('Please select a tag to add.');
            }
        });

        $(document).on('click', '.remove-tag', function() {
            var button = $(this);
            var tagId = button.data('tag-id');
            $.ajax({
                url: "/link/remove_tag/" + variable,
                type: 'POST',
                data: { tag_id: tagId, link_id: variable },
                success: function(response) {
                    if(response.success) {
                        button.closest('li').remove();
                    } else {
                        alert(response.message);
                    }
                }
            });
        });
    });
});
