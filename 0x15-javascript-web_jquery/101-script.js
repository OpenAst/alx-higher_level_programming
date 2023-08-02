//  a JavaScript script that adds, removes and clears LI elements from a list when the user clicks:
//  The new element must be: <li>Item</li>
//  When the user clicks on DIV#add_item: a new element is added to the list
// When the user clicks on DIV#add_item: a new element is added to the list

  $('#add_item').click(function () {
    $('ul.my_list').append('<li>Item</li>');
  });

  // When the user clicks on DIV#remove_item: the last element is removed from the list
  $('#remove_item').click(function () {
    $('ul.my_list li:last-child').remove();
  });

  // When the user clicks on DIV#clear_list: all elements of the list are removed
  $('#clear_list').click(function () {
    $('ul.my_list').empty();
  });
});

